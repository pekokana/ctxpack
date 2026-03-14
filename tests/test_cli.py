import sys
import pytest
from ctxpack.cli import main

def create_file(path, content="print('hello')"):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)

@pytest.fixture
def base_args(tmp_path):
    """共通の基本引数を用意するフィクスチャ"""
    f = tmp_path / "src" / "a.py"
    create_file(f)
    out = tmp_path / "out.md"
    return [str(tmp_path / "src"), "-o", str(out), out]

def test_cli_basic(base_args, monkeypatch, capsys):
    src, _, out_str, out_path = base_args
    monkeypatch.setattr(sys, "argv", ["ctxpack", src, "-o", out_str])
    
    main()
    
    assert out_path.exists()
    captured = capsys.readouterr()
    assert "Packed files: 1" in captured.out

def test_cli_tree(base_args, monkeypatch):
    src, _, out_str, out_path = base_args
    monkeypatch.setattr(sys, "argv", ["ctxpack", src, "-o", out_str, "--tree"])
    
    main()
    
    assert "Project Structure" in out_path.read_text()

def test_cli_llm_format(base_args, monkeypatch):
    src, _, out_str, out_path = base_args
    monkeypatch.setattr(sys, "argv", ["ctxpack", src, "-o", out_str, "--llm-format"])
    
    main()
    
    assert "FILE:" in out_path.read_text()

def test_cli_extension_filter(tmp_path, monkeypatch):
    src = tmp_path / "src"
    create_file(src / "a.py")
    create_file(src / "b.txt")
    out = tmp_path / "out.md"
    
    monkeypatch.setattr(sys, "argv", ["ctxpack", str(src), "-o", str(out), "-e", "py"])
    main()
    
    text = out.read_text()
    assert "a.py" in text
    assert "b.txt" not in text

def test_cli_max_size(tmp_path, monkeypatch, capsys):
    src = tmp_path / "src"
    f = src / "large.py"
    create_file(f, "x" * 2000) # 約2KB
    out = tmp_path / "out.md"
    
    # 1KB制限をかける
    monkeypatch.setattr(sys, "argv", ["ctxpack", str(src), "-o", str(out), "--max-size", "1"])
    main()
    
    captured = capsys.readouterr()
    assert "Packed files: 0" in captured.out

def test_cli_max_files(tmp_path, monkeypatch, capsys):
    src = tmp_path / "src"
    create_file(src / "a.py")
    create_file(src / "b.py")
    out = tmp_path / "out.md"
    
    monkeypatch.setattr(sys, "argv", ["ctxpack", str(src), "-o", str(out), "--max-files", "1"])
    main()
    
    captured = capsys.readouterr()
    assert "Packed files: 1" in captured.out

def test_cli_estimate_tokens(base_args, monkeypatch, capsys):
    src, _, out_str, _ = base_args
    monkeypatch.setattr(sys, "argv", ["ctxpack", src, "-o", out_str, "--estimate-tokens"])
    
    main()
    
    captured = capsys.readouterr()
    assert "Estimated tokens:" in captured.out

def test_cli_missing_output(tmp_path, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["ctxpack", str(tmp_path)])
    with pytest.raises(SystemExit):
        main()


def test_cli_gitignore(tmp_path, monkeypatch, capsys):
    # ルートディレクトリを作成
    root = tmp_path / "project"
    root.mkdir()
    
    # ファイルを作成
    f = root / "a.py"
    create_file(f, "print('hello')")
    
    # .gitignore には、root から見た相対パス（またはパターン）を書く
    # ここでは確実にヒットするようにパターン "*.py" を使います
    create_file(root / ".gitignore", "*.py\n.gitignore")
    
    out = tmp_path / "out.md"

    # ターゲットを root に設定
    monkeypatch.setattr(sys, "argv", ["ctxpack", str(root), "-o", str(out), "--gitignore"])
    main()

    captured = capsys.readouterr()
    assert "Packed files: 0" in captured.out

def test_cli_token_output(base_args, monkeypatch):
    src, _, out_str, out_path = base_args
    monkeypatch.setattr(sys, "argv", ["ctxpack", src, "-o", out_str, "--token-output"])

    main()
    
    # writer.py の実装に合わせて "Estimated tokens" に修正
    assert "Estimated tokens:" in out_path.read_text()