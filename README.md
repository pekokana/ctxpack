# pyctxpack

**pyctxpack** is a command-line tool that consolidates source files from a local repository into a single text file, making it easy to provide context to LLMs such as ChatGPT, Claude, or Gemini.

It scans a project directory, collects relevant source files, and outputs them in a structured format optimized for AI analysis and prompting.

This tool helps developers quickly prepare project context when asking questions about their code.

---

🇯🇵 Japanese README is available below.  
日本語の説明はこのREADMEの後半にあります。

---

# Features

- **Smart File Collection**  
  Recursively scans directories and gathers source files.

- **Flexible Filtering**  
  Limit files by extension, file size, or total file count.

- **.gitignore Support**  
  Respects `.gitignore` rules and excludes unnecessary files (e.g., node_modules).

- **Project Structure Visualization**  
  Automatically inserts a directory tree at the top of the output.

- **Robust Encoding Detection**  
  Automatically detects UTF-8, UTF-16, and CP932 (Shift_JIS).  
  Binary files are automatically skipped.

- **Token Estimation**  
  Estimate the approximate number of tokens before sending to an LLM.



# Installation

Using pip:

```bash
pip install pyctxpack
````

Using **uv**:

```bash
uv tool install pyctxpack
```



# Usage

Basic command:

```bash
pyctxpack src/ -o context.md
```



# Common Options

### Limit file extensions

```bash
pyctxpack . -o out.md -e py,js,ts
```

### Include project structure and respect `.gitignore`

```bash
pyctxpack . -o out.md --tree --gitignore
```

### Estimate tokens and record them in the output file

```bash
pyctxpack . -o out.md --estimate-tokens --token-output
```

### Use LLM-optimized formatting

```bash
pyctxpack . -o out.md --llm-format
```



# Command Line Arguments

| Argument            | Description                                                |
| ------------------- | ---------------------------------------------------------- |
| `target`            | Target directory or file                                   |
| `-o, --output`      | **[Required]** Output file path                            |
| `-e, --ext`         | File extensions to include (comma separated, e.g. `py,ts`) |
| `--max-size`        | Maximum file size in KB                                    |
| `--max-files`       | Maximum number of files to collect                         |
| `--tree`            | Include project structure tree at the beginning            |
| `--gitignore`       | Respect `.gitignore` rules                                 |
| `--estimate-tokens` | Print estimated token count                                |
| `--token-output`    | Append estimated token count to the output file            |
| `--llm-format`      | Use formatting optimized for LLM parsing                   |



# License

[MIT License](https://github.com/pekokana/ctxpack/blob/main/LICENSE)



# Contributing

Contributions are welcome!

```bash
git clone https://github.com/pekokana/ctxpack.git
cd ctxpack
uv sync
uv run pytest
```

---


# 日本語README

# pyctxpack

**pyctxpack** は、ローカルリポジトリのソースコードを1つのテキストファイルにまとめ、LLM（ChatGPT, Claude, Gemini等）に渡すコンテキストを瞬時に作成するためのコマンドラインツールです。

多くのファイルを扱うプロジェクトでも、適切なフィルタリングとフォーマットによって、AIへの依頼をスムーズにします。


## 主な特徴

* **スマートなファイル収集**: ディレクトリを再帰的にスキャンし、ソースファイルを統合。
* **柔軟なフィルタリング**: 拡張子、最大ファイルサイズ、最大ファイル数による制限。
* **.gitignore 対応**: プロジェクトの無視設定を尊重し、不要なファイル（node_modules等）を除外。
* **プロジェクト構造の可視化**: ファイルリストの冒頭にディレクトリツリーを自動挿入。
* **堅牢な文字コード判定**: UTF-8, UTF-16, CP932(Shift_JIS) を自動判別。バイナリファイルは自動でスキップ。
* **トークン数見積もり**: LLMに渡す前に、おおよそのトークン数を確認可能。



## インストール

```bash
pip install pyctxpack

```

または **uv** を使用している場合:

```bash
uv tool install pyctxpack

```


## 使い方

基本コマンド:

```bash
pyctxpack src/ -o context.md

```

### よく使うオプション

**拡張子を限定する:**

```bash
pyctxpack . -o out.md -e py,js,ts

```

**プロジェクト構造を含め、.gitignoreを反映させる:**

```bash
pyctxpack . -o out.md --tree --gitignore

```

**トークン数を見積もり、ファイルにも記録する:**

```bash
pyctxpack . -o out.md --estimate-tokens --token-output

```

**LLMに最適化されたフォーマット（セパレーターを強化）を使用:**

```bash
pyctxpack . -o out.md --llm-format

```


## コマンドライン引数詳細

| 引数 | 説明 |
| --- | --- |
| `target` | 対象となるディレクトリまたはファイル |
| `-o, --output` | **[必須]** 出力先のファイル名 |
| `-e, --ext` | 対象とする拡張子（カンマ区切り。例: `py,ts`） |
| `--max-size` | 収集するファイルの最大サイズ (KB) |
| `--max-files` | 収集する最大ファイル数 |
| `--tree` | 出力の冒頭にプロジェクト構造（ツリー）を含める |
| `--gitignore` | `.gitignore` の設定に従ってファイルを無視する |
| `--estimate-tokens` | 実行時に推定トークン数を表示 |
| `--token-output` | ファイルの末尾に推定トークン数を書き込む |
| `--llm-format` | LLMがファイルを識別しやすいフォーマットを使用する |



## ライセンス

[MIT License](https://github.com/pekokana/ctxpack/blob/main/LICENSE)



## 貢献

Issue や Pull Request は大歓迎です。
開発環境のセットアップ:

```bash
git clone https://github.com/pekokana/ctxpack.git
cd ctxpack
uv sync
uv run pytest  # 全テストの実行
```
