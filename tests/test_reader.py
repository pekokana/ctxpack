from ctxpack.reader import read_file
import pytest

def test_read_utf8(tmp_path):

    f = tmp_path / "a.txt"
    f.write_text("hello", encoding="utf-8")

    assert read_file(f) == "hello"


def test_read_cp932(tmp_path):

    f = tmp_path / "a.txt"
    f.write_text("hello", encoding="cp932")

    assert read_file(f) == "hello"


def test_read_utf16(tmp_path):

    f = tmp_path / "a.txt"
    f.write_text("hello", encoding="utf-16")

    assert read_file(f) == "hello"

def test_read_nonexistent(tmp_path):
    f = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        read_file(f)

def test_read_unreadable(tmp_path):
    f = tmp_path / "a.bin"
    f.write_bytes(b"\x00\x01\x02\x03")

    assert read_file(f) is None

def test_read_utf16_invalid(tmp_path):
    # UTF-16のBOMはあるが、中身が奇数バイトで不正なケース
    f = tmp_path / "invalid_utf16.txt"
    f.write_bytes(b"\xff\xfe\x61")  # BOM + 'a' の半分だけ
    
    # 1. UTF-16デコードに失敗し
    # 2. ヌルバイトがないので次に進み
    # 3. UTF-8でもCP932でもない(不正バイト)ので最終的にNone
    assert read_file(f) is None

def test_read_utf8_invalid_fallback_cp932(tmp_path):
    # UTF-8として不正だが、CP932として正しいケース
    # 「あ」のCP932は b"\x82\xa0"
    f = tmp_path / "japanese_cp932.txt"
    f.write_bytes(b"\x82\xa0")
    
    assert read_file(f) == "あ"

def test_read_completely_invalid(tmp_path):
    f = tmp_path / "garbage.bin"
    # 0x81 は CP932 で2バイト文字の開始を意味しますが、
    # その後に続く 0x00-0x3F, 0x7F, 0xFD-0xFF は2バイト目として不正かな？
    # ここでは 0x81 の後に 0x30 (数字の0) を置くことで、
    # 強制的に UnicodeDecodeError を発生をもくろむ。
    f.write_bytes(b"\x81\x30")
    
    assert read_file(f) is None