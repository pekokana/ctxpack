# ctxpack テスト仕様書 (Testing Guide)

## 1. 概要

本ドキュメントは `ctxpack` プロジェクトにおけるテスト戦略を定義します。

本プロジェクトでは **pytest** を使用して自動テストを行い、以下の内容を保証します：

* 各モジュールのユニットテスト（単体テスト）
* CLIの振る舞いに関する統合テスト
* 異常系およびエッジケースのエラーハンドリング

### テスト実行コマンド

以下のコマンドで、HTMLレポートの生成、カバレッジの計測、および未通過行の確認を同時に行います。

```bash
uv run pytest -v --html=docs/report.html --self-contained-html --cov=src --cov-report=html:docs/coverage --cov-report=term-missing

```



## 2. テスト構造

各モジュールに対して、専用のテストファイルが `tests` ディレクトリ配下に配置されています。

```text
tests
 ┣ test_collector.py  # ファイル収集ロジック
 ┣ test_gitignore.py  # Gitignoreによるフィルタリング
 ┣ test_reader.py     # エンコーディング検知と読み込み
 ┣ test_token.py      # トークン数見積もり
 ┣ test_tree.py       # ディレクトリ構造の可視化
 ┣ test_writer.py     # ファイル出力とフォーマット
 ┗ test_cli.py        # コマンドライン引数と統合動作

```



## 3. テスト環境と機能

テストでは pytest の以下の機能を活用しています：

* `tmp_path` : 動的な一時ディレクトリの作成（固定ファイルに依存しないテスト）
* `fixture` : 引数や環境の共通セットアップ（`base_args` など）
* `monkeypatch` : `sys.argv` の書き換えによる CLI 擬似実行
* `capsys` : 標準出力・標準エラー出力のキャプチャと検証



## 4. テストカテゴリ詳細

### 5. Collector (ファイル収集) テスト

`collector.py` のファイル探索ロジックを検証します。

| テストケース | 内容 |
| --- | --- |
| `test_collect_directory` | ディレクトリ内の全ファイルを収集できるか |
| `test_collect_single_file` | 単一ファイル指定時にそのファイルのみを収集するか |
| `test_extension_filter` | 拡張子指定（`-e`）によるフィルタリングが動作するか |
| `test_max_size` | 指定サイズ（KB）を超えるファイルをスキップするか |
| `test_max_files` | 最大ファイル数制限を超えた場合に収集を止めるか |
| `test_empty_directory` | 空のディレクトリでエラーにならず空リストを返すか |
| `test_nested_directories` | サブディレクトリ内のファイルを再帰的に収集するか |

### 6. Gitignore テスト

`gitignore.py` による無視パターンの適用を検証します。

| テストケース | 内容 |
| --- | --- |
| `test_load_gitignore` | `.gitignore` ファイルを正常にロードできるか |
| `test_gitignore_match` | 指定したパターン（`*.log` 等）が正しくマッチするか |
| `test_gitignore_directory` | ディレクトリ指定の無視設定が配下のファイルに適用されるか |
| `test_is_ignored_no_spec` | `spec` が `None`（ファイルなし）の時に全て `False` を返すか |
| `test_is_ignored_outside_root` | ルートディレクトリ外のパスが渡された時に安全に `False` を返すか |

### 7. Reader (読み込み・文字コード) テスト

`reader.py` の多言語・多エンコーディング対応を検証します。

| テストケース | 内容 |
| --- | --- |
| `test_read_utf8` / `utf16` | 主要なエンコーディングを正しく認識しデコードできるか |
| `test_read_cp932` | 日本語環境特有の CP932 (Shift_JIS) をデコードできるか |
| `test_read_utf8_invalid_fallback` | UTF-8で失敗した際に CP932 へ正常にフォールバックするか |
| `test_read_unreadable` / `binary` | ヌルバイトを含むバイナリや不正なバイト列を `None` としてスキップするか |
| `test_read_utf16_invalid` | BOMはあるが中身が不完全な UTF-16 をエラーにせず処理するか |
| `test_read_nonexistent` | 存在しないファイルに対して `FileNotFoundError` を投げるか |

### 8. Token & Tree テスト

トークン計算とディレクトリ木構造の生成を検証します。

| モジュール | テストケース | 内容 |
| --- | --- | --- |
| **Token** | `test_token_small` / `large` | 文字数に応じたトークン見積もり計算の正確性 |
| **Tree** | `test_tree_nested` | ネストした構造が正しく視覚化されるか |
| **Tree** | `test_tree_empty` | ファイルがない場合に空文字列を返すか |

### 9. Writer (出力) テスト

`writer.py` による最終的な Markdown 出力フォーマットを検証します。

| テストケース | 内容 |
| --- | --- |
| `test_writer_llm_format` | `--llm-format` 指定時に区切り線が `=== FILE: ===` になるか |
| `test_writer_language_detection` | 拡張子（`.py` 等）から Markdown のシンタックスハイライトを付与するか |
| `test_writer_token_output` | ファイル末尾にトークン見積もり情報が出力されるか |
| `test_writer_skip_binary_file` | 読み込み不能（`None`）なファイルが含まれる場合にスキップして継続するか |

### 10. CLI 統合テスト

`cli.py` を通じた全オプションの組み合わせ動作を検証します。

| テストケース | 内容 |
| --- | --- |
| `test_cli_basic` | 最小限の引数で正常にファイルが生成されるか |
| `test_cli_max_size` / `max_files` | コマンドライン引数からの制限値が収集ロジックに伝わっているか |
| `test_cli_gitignore` | `--gitignore` 有効時に自身（`.gitignore`）や指定ファイルが除外されるか |
| `test_cli_missing_output` | 必須引数（`-o`）がない場合に `SystemExit` で終了するか |
| `test_cli_estimate_tokens` | `--estimate-tokens` 指定時に標準出力にトークン数が表示されるか |



## 11. テスト結果の期待値

* **総テスト数**: 49 ケース
* **目標カバレッジ**: 100% (全ライン通過を確認済み)
* **対応 Python バージョン**: 3.13.x 以降



## 12. 今後の改善案

* **出力の自動検証 (Snapshot Testing)**: 生成された Markdown が期待通りの構造か、スナップショット比較を導入する。
* **大規模リポジトリの負荷テスト**: 数千ファイルあるディレクトリでのパフォーマンス計測。
* **OS依存パスの検証**: Windows 形式のパス（`\`）における挙動のさらなる強化。

