from pathlib import Path
import pathspec


def load_gitignore(root):

    gitignore = Path(root) / ".gitignore"

    if not gitignore.exists():
        return None

    with open(gitignore) as f:
        spec = pathspec.PathSpec.from_lines("gitignore", f)

    return spec


def is_ignored(path, root, spec):

    if spec is None:
        return False

    try:
        rel = str(path.relative_to(root))
    except ValueError:
        return False

    return spec.match_file(rel)