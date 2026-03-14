from pathlib import Path
from .gitignore import load_gitignore, is_ignored


def collect_files(
    target,
    extensions=None,
    max_size=None,
    max_files=None,
    use_gitignore=False
):

    target = Path(target)

    files = []

    spec = load_gitignore(target) if use_gitignore else None

    if target.is_file():
        return [target]

    for path in target.rglob("*"):

        if not path.is_file():
            continue

        if use_gitignore and is_ignored(path, target, spec):
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