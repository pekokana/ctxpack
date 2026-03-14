# ctxpack

**ctxpack** は、ローカルリポジトリのソースコードを1つのテキストファイルにまとめ、LLM（ChatGPT, Claude, Gemini等）に渡すコンテキストを瞬時に作成するためのコマンドラインツールです。

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
pip install ctxpack

```

または **uv** を使用している場合:

```bash
uv tool install ctxpack

```


## 使い方

基本コマンド:

```bash
ctxpack src/ -o context.md

```

### よく使うオプション

**拡張子を限定する:**

```bash
ctxpack . -o out.md -e py,js,ts

```

**プロジェクト構造を含め、.gitignoreを反映させる:**

```bash
ctxpack . -o out.md --tree --gitignore

```

**トークン数を見積もり、ファイルにも記録する:**

```bash
ctxpack . -o out.md --estimate-tokens --token-output

```

**LLMに最適化されたフォーマット（セパレーターを強化）を使用:**

```bash
ctxpack . -o out.md --llm-format

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

[MIT License](https://www.google.com/search?q=LICENSE)



## 貢献

Issue や Pull Request は大歓迎です。
開発環境のセットアップ:

```bash
git clone https://github.com/pekokana/ctxpack.git
cd ctxpack
uv sync
uv run pytest  # 全テストの実行

