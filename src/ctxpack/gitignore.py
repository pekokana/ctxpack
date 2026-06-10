from pathlib import Path
import pathspec


def load_gitignore(root):
    gitignore = Path(root) / ".gitignore"

    if not gitignore.exists():
        return None

    # 念のため UTF-8 指定で開くのが安全です
    with open(gitignore, "r", encoding="utf-8") as f:
        spec = pathspec.PathSpec.from_lines("gitignore", f)

    return spec


def is_ignored(path, root, spec):
    """ファイル、またはディレクトリが無視対象かを判定する"""
    if spec is None:
        return False

    try:
        rel_path = path.relative_to(root)
    except ValueError:
        return False

    # pathspec に渡す相対パスを文字列形式にする
    # Windows環境のバックスラッシュ(\)を、Git標準のフォワードスラッシュ(/)に統一
    rel_str = rel_path.as_posix()

    # 対象がディレクトリの場合、末尾に '/' をつけないと
    # gitignoreの「dir/」という記述に正しくマッチしない
    if path.is_dir() and not rel_str.endswith("/"):
        rel_str += "/"

    return spec.match_file(rel_str)
