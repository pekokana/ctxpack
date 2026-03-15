import os

def create_test_project():
    base_dir = "demo_project"
    # ディレクトリ作成
    os.makedirs(f"{base_dir}/src/utils", exist_ok=True)
    os.makedirs(f"{base_dir}/docs", exist_ok=True)
    os.makedirs(f"{base_dir}/node_modules", exist_ok=True)

    # 1. .gitignore
    with open(f"{base_dir}/.gitignore", "w", encoding="utf-8") as f:
        f.write("node_modules/\n*.log\n")

    # 2. Pythonファイル (通常)
    with open(f"{base_dir}/src/main.py", "w", encoding="utf-8") as f:
        f.write("def main():\n    print('Hello World')\n")

    # 3. テキストファイル (拡張子テスト用)
    with open(f"{base_dir}/docs/info.txt", "w", encoding="utf-8") as f:
        f.write("This is a text file.\n")

    # 4. 巨大なファイル (1MB以上: --max-size テスト用)
    with open(f"{base_dir}/src/large_file.py", "w", encoding="utf-8") as f:
        f.write("# Large file content\n" + "x = 1\n" * 50000)

    # 5. 大量のファイル (--max-files テスト用)
    for i in range(15):
        with open(f"{base_dir}/docs/file_{i}.txt", "w", encoding="utf-8") as f:
            f.write(f"content {i}")

    # 6. Shift_JISファイル (文字コード判定用)
    with open(f"{base_dir}/sjis_doc.txt", "w", encoding="cp932") as f:
        f.write("Shift_JISの日本語テキストです。")

    print(f"Test project '{base_dir}' has been created with various conditions.")

if __name__ == "__main__":
    create_test_project()