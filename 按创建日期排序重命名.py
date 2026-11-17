from __future__ import annotations

import itertools
import os
import sys
import uuid
from pathlib import Path


def creation_time(path: Path) -> float:
    stat_result = path.stat()
    birth_time = getattr(stat_result, "st_birthtime", None)
    if birth_time is None:
        raise RuntimeError(f"系统未提供文件创建时间，无法排序：{path.name}")
    return birth_time


def free_name_with_dashes(path: Path, reserved_names: set[str]) -> Path:
    for dashes in itertools.count(1):
        candidate = path.with_name(f"{path.stem}{'-' * dashes}{path.suffix}")
        if not os.path.lexists(candidate) and candidate.name.casefold() not in reserved_names:
            return candidate


def rename_by_creation_date(folder: Path) -> int:
    if not folder.is_dir():
        raise ValueError(f"文件夹不存在或不是文件夹：{folder}")

    entries = list(folder.iterdir())
    files = [path for path in entries if path.is_file() and path.name != ".DS_Store"]
    subfolders = [path for path in entries if path.is_dir()]
    if subfolders:
        print(f"检测到 {len(subfolders)} 个子文件夹，文件夹不参与重命名，已跳过。")
    if not files:
        print("该文件夹中没有可重命名的文件。")
        return 0

    ordered = sorted(
        files,
        key=lambda path: (creation_time(path), path.name.casefold(), path.name),
    )
    targets = [
        folder / f"{index}{path.suffix}"
        for index, path in enumerate(ordered, start=1)
    ]

    source_names = {path.name.casefold() for path in ordered}
    occupied_renames: list[tuple[Path, Path]] = []
    for target in targets:
        if not os.path.lexists(target):
            continue
        if target.name.casefold() in source_names and target.is_file():
            continue  # 占用者只是大小写不同的待重命名文件，由临时名机制安全处理
        if target.is_dir():
            raise FileExistsError(
                f"目标名称 {target.name} 已被文件夹占用；文件夹不参与重命名，"
                "请先移走或删除该文件夹"
            )
        freed = free_name_with_dashes(target, source_names)
        occupied_renames.append((target, freed))

    if occupied_renames:
        print("\n目标名称被占用，将先把占用文件改名（在文件名后加“-”）释放名称：")
        for original, freed in occupied_renames:
            print(f"  {original.name}  ->  {freed.name}")

    print("\n按创建时间排序的重命名预览：")
    for index, (source, target) in enumerate(zip(ordered, targets), start=1):
        created = creation_time(source)
        print(f"{index:>3}. {source.name}  ->  {target.name}  (创建时间 {created:.3f})")

    if input("\n确认重命名？输入 Y 继续，其他输入取消：").strip().casefold() != "y":
        print("已取消，文件未更改。")
        return 0

    staged: list[tuple[Path, Path, Path]] = []
    try:
        for original, freed in occupied_renames:
            original.rename(freed)

        for source, target in zip(ordered, targets):
            temporary = folder / f".rename_tmp_{uuid.uuid4().hex}"
            source.rename(temporary)
            staged.append((source, temporary, target))

        for _, temporary, target in staged:
            temporary.rename(target)
    except OSError as error:
        recovery_errors = []
        for source, temporary, target in reversed(staged):
            current = temporary if os.path.lexists(temporary) else target
            if os.path.lexists(current) and not os.path.lexists(source):
                try:
                    current.rename(source)
                except OSError as recovery_error:
                    recovery_errors.append(f"{current.name} -> {source.name}: {recovery_error}")
        for original, freed in reversed(occupied_renames):
            if os.path.lexists(freed) and not os.path.lexists(original):
                try:
                    freed.rename(original)
                except OSError as recovery_error:
                    recovery_errors.append(f"{freed.name} -> {original.name}: {recovery_error}")
        if recovery_errors:
            raise RuntimeError(
                f"重命名失败：{error}；回滚也未能完全完成："
                + "; ".join(recovery_errors)
            ) from error
        raise RuntimeError(f"重命名失败，已尝试恢复原文件名：{error}") from error

    summary = f"完成：已按创建时间将 {len(ordered)} 个文件重命名。"
    if occupied_renames:
        summary += f" 另有 {len(occupied_renames)} 个占用名称的文件已改名（加“-”）释放名称。"
    print(summary)
    return len(ordered)


def main() -> int:
    raw_path = input("请输入文件夹地址：").strip()
    if len(raw_path) >= 2 and raw_path[0] == raw_path[-1] and raw_path[0] in {"'", '"'}:
        raw_path = raw_path[1:-1]
    if not raw_path:
        print("未输入文件夹地址。", file=sys.stderr)
        return 1

    try:
        rename_by_creation_date(Path(raw_path).expanduser())
    except (OSError, RuntimeError, ValueError) as error:
        print(f"错误：{error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
