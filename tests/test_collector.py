from ctxpack.collector import collect_files


def create_file(path, content="data"):
    path.write_text(content)


def test_collect_directory(tmp_path):

    f1 = tmp_path / "a.py"
    f2 = tmp_path / "b.py"

    create_file(f1)
    create_file(f2)

    files = collect_files(tmp_path)

    assert len(files) == 2


def test_collect_single_file(tmp_path):

    f = tmp_path / "a.py"
    create_file(f)

    files = collect_files(f)

    assert len(files) == 1
    assert files[0] == f


def test_extension_filter(tmp_path):

    f1 = tmp_path / "a.py"
    f2 = tmp_path / "b.txt"

    create_file(f1)
    create_file(f2)

    files = collect_files(tmp_path, extensions=["py"])

    assert len(files) == 1


def test_max_size(tmp_path):

    f = tmp_path / "big.py"
    create_file(f, "a" * 5000)

    files = collect_files(tmp_path, max_size=1)

    assert len(files) == 0


def test_max_files(tmp_path):

    for i in range(5):
        create_file(tmp_path / f"a{i}.py")

    files = collect_files(tmp_path, max_files=2)

    assert len(files) == 2


def test_empty_directory(tmp_path):

    files = collect_files(tmp_path)

    assert files == []


def test_extension_not_match(tmp_path):

    create_file(tmp_path / "a.txt")

    files = collect_files(tmp_path, extensions=["py"])

    assert files == []


def test_nested_directories(tmp_path):

    sub = tmp_path / "sub"
    sub.mkdir()

    create_file(sub / "a.py")

    files = collect_files(tmp_path)

    assert len(files) == 1