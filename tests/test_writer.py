from ctxpack.writer import write_output


def create_file(path):

    path.write_text("print('hello')")


def test_writer_basic(tmp_path):

    f = tmp_path / "a.py"
    create_file(f)

    out = tmp_path / "out.md"

    write_output([f], out)

    assert out.exists()


def test_writer_llm_format(tmp_path):

    f = tmp_path / "a.py"
    create_file(f)

    out = tmp_path / "out.md"

    write_output([f], out, llm_format=True)

    text = out.read_text()

    assert "=== FILE:" in text


def test_writer_tree(tmp_path):

    f = tmp_path / "a.py"
    create_file(f)

    out = tmp_path / "out.md"

    write_output([f], out, root=tmp_path, show_tree=True)

    text = out.read_text()

    assert "Project Structure" in text


def test_writer_token_output(tmp_path):

    f = tmp_path / "a.py"
    create_file(f)

    out = tmp_path / "out.md"

    write_output([f], out, include_tokens=True)

    text = out.read_text()

    assert "Estimated tokens" in text


def test_writer_multiple_files(tmp_path):

    f1 = tmp_path / "a.py"
    f2 = tmp_path / "b.py"

    create_file(f1)
    create_file(f2)

    out = tmp_path / "out.md"

    write_output([f1, f2], out)

    text = out.read_text()

    assert "a.py" in text
    assert "b.py" in text


def test_writer_skip_unreadable(tmp_path):

    f = tmp_path / "a.py"
    create_file(f)

    out = tmp_path / "out.md"

    write_output([f], out)

    assert out.exists()


def test_writer_empty_files(tmp_path):

    out = tmp_path / "out.md"

    write_output([], out)

    assert out.exists()


def test_writer_language_detection(tmp_path):

    f = tmp_path / "a.py"
    create_file(f)

    out = tmp_path / "out.md"

    write_output([f], out)

    text = out.read_text()

    assert "```python" in text

def test_writer_skip_binary_file(tmp_path):
    from ctxpack.writer import write_output
    
    src = tmp_path / "src"
    src.mkdir()
    
    # 正常なファイル
    f1 = src / "a.py"
    f1.write_text("print('ok')")
    
    # バイナリファイル (reader.py が None を返すもの)
    f2 = src / "b.bin"
    f2.write_bytes(b"\x00\xff") 
    
    out = tmp_path / "out.md"
    
    # 実行
    files = [f1, f2]
    write_output(files, out, root=src)
    
    # 結果確認
    text = out.read_text()
    assert "a.py" in text
    assert "b.bin" not in text  # None なのでスキップされているはず