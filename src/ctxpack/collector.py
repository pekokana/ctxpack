from pathlib import Path
from .gitignore import load_gitignore, is_ignored


def collect_files(
    target, extensions=None, max_size=None, max_files=None, use_gitignore=False
):

    target = Path(target)

    files = []

    spec = load_gitignore(target) if use_gitignore else None

    if target.is_file():
        return [target]

    for path in sorted(target.rglob("*")):
        is_parent_ignored = False
        if use_gitignore and spec:
            # 自分自身、または親ディレクトリのいずれかが ignore 対象かチェック
            for parent in [path] + list(path.parents):
                if parent == target:
                    break
                if is_ignored(parent, target, spec):
                    is_parent_ignored = True
                    break

        if use_gitignore and is_parent_ignored:
            continue

        if not path.is_file():
            continue

        if extensions:
            if path.suffix.lstrip(".") not in extensions:
                continue

        if max_size:
            size_kb = path.stat().st_size / 1024
            if size_kb > max_size:
                continue

        files.append(path)

        if max_files and len(files) >= max_files:
            break

    return sorted(files)
