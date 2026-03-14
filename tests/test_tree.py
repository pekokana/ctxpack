from ctxpack.tree import build_tree


def test_tree_simple(tmp_path):

    f = tmp_path / "a.py"
    f.write_text("x")

    tree = build_tree([f], tmp_path)

    assert "a.py" in tree


def test_tree_nested(tmp_path):

    sub = tmp_path / "dir"
    sub.mkdir()

    f = sub / "a.py"
    f.write_text("x")

    tree = build_tree([f], tmp_path)

    assert "a.py" in tree


def test_tree_empty():

    tree = build_tree([], ".")

    assert tree == ""


def test_tree_indent(tmp_path):

    sub = tmp_path / "d"
    sub.mkdir()

    f = sub / "a.py"
    f.write_text("x")

    tree = build_tree([f], tmp_path)

    assert "a.py" in tree