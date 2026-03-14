from pathlib import Path
from ctxpack.gitignore import load_gitignore, is_ignored


def test_load_gitignore(tmp_path):

    gi = tmp_path / ".gitignore"
    gi.write_text("*.log\n")

    spec = load_gitignore(tmp_path)

    assert spec is not None


def test_gitignore_match(tmp_path):

    gi = tmp_path / ".gitignore"
    gi.write_text("*.log\n")

    spec = load_gitignore(tmp_path)

    f = tmp_path / "test.log"
    f.write_text("x")

    assert is_ignored(f, tmp_path, spec)


def test_gitignore_not_match(tmp_path):

    gi = tmp_path / ".gitignore"
    gi.write_text("*.log\n")

    spec = load_gitignore(tmp_path)

    f = tmp_path / "main.py"
    f.write_text("x")

    assert not is_ignored(f, tmp_path, spec)


def test_gitignore_directory(tmp_path):

    gi = tmp_path / ".gitignore"
    gi.write_text("build/\n")

    build = tmp_path / "build"
    build.mkdir()

    f = build / "a.py"
    f.write_text("x")

    spec = load_gitignore(tmp_path)

    assert is_ignored(f, tmp_path, spec)


def test_gitignore_missing(tmp_path):

    spec = load_gitignore(tmp_path)

    assert spec is None


def test_is_ignored_no_spec():
    # spec が None の場合、どんなファイルも無視されない (False を返す)
    # これで if spec is None: return False のルートをカバー
    assert is_ignored(Path("a.py"), Path("."), None) is False

def test_is_ignored_outside_root(tmp_path):
    # root ディレクトリの外にあるファイルを判定しようとした場合
    # Path.relative_to が ValueError を投げるので、その処理を確認
    root = tmp_path / "project"
    root.mkdir()
    
    outside_file = tmp_path / "outside.txt"
    outside_file.write_text("outside")
    
    # 読み込まれた spec を用意
    gi = root / ".gitignore"
    gi.write_text("*.txt")
    spec = load_gitignore(root)
    
    # ルート外のファイルは無視判定せず False を返すことを確認
    # これで except ValueError: return False のルートをカバー
    assert is_ignored(outside_file, root, spec) is False