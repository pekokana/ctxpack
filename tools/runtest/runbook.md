# pyctxpack 動作確認ランブック

このディレクトリにあるツールを使用して、`pyctxpack` の全機能を検証します。

## 1. 環境準備

```bash
# プロジェクトのルート(ctxpack/)から tools/runtest/ へ移動
cd tools/runtest/

# 検証用仮想環境の作成
python3 -m venv venv_test
source venv_test/bin/activate

# TestPyPI から最新版(0.1.1)をインストール
pip install --no-cache-dir \
  --index-url [https://test.pypi.org/simple/](https://test.pypi.org/simple/) \
  --extra-index-url [https://pypi.org/simple/](https://pypi.org/simple/) \
  pyctxpack==0.1.1

# テストデータの生成
python3 gen_test_data.py

```

## 2. 全オプション一括検証

以下のコマンドを順に実行し、各テスト結果が個別のファイルに出力されることを確認します。

| テスト内容 | 実行コマンド | 確認ポイント |
| --- | --- | --- |
| **1. 基本統合** | `pyctxpack demo_project -o test1_basic.md` | 全ファイルが統合されているか |
| **2. .gitignore** | `pyctxpack demo_project -o test2_ignore.md --gitignore` | node_modules等が除外されているか |
| **3. 拡張子制限** | `pyctxpack demo_project -o test3_ext.md -e py` | .pyファイルのみか |
| **4. ツリー表示** | `pyctxpack demo_project -o test4_tree.md --tree` | 冒頭にディレクトリ構造があるか |
| **5. サイズ制限** | `pyctxpack demo_project -o test5_size.md --max-size 10` | 巨大なファイルが除外されているか |
| **6. 数制限** | `pyctxpack demo_project -o test6_files.md --max-files 5` | 収録数が5つ以内か |
| **7. トークン計測** | `pyctxpack demo_project -o test7_token.md --estimate-tokens --token-output` | 端末と末尾にトークン数が出るか |
| **8. LLM書式** | `pyctxpack demo_project -o test8_llm.md --llm-format` | セパレーターが強化されているか |

## 3. クリーンアップ

```bash
rm -rf demo_project test*.md venv_test

```
