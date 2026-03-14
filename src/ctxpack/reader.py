from pathlib import Path


def read_file(path: Path) -> str | None:
    if not path.exists():
        raise FileNotFoundError(path)

    raw = path.read_bytes()


    # UTF-16 BOM 判定
    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        try:
            return raw.decode("utf-16")
        except UnicodeDecodeError:
            # BOMがあるのにUTF-16として壊れているなら、
            # 他のエンコーディングを試さずバイナリ（None）とみなす
            return None



    # Binary file check
    if b"\x00" in raw:
        return None

    # UTF-8
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        pass

    # CP932
    try:
        return raw.decode("cp932", errors="strict")
    except UnicodeDecodeError:
        pass

    return None