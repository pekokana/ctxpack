
# PyPI公開チェックリスト

## 基礎情報
① コード品質
✅ テスト
 pytest が 100%成功
 --cov=src で カバレッジ90%以上（理想95%）
 主要モジュール（例：reader）は ほぼ100%
 境界ケーステストあり（空、None、異常値など）
実行例：

uv run pytest -v --cov=src --cov-report=term-missing
✅ 型安全
 mypy 導入
 全コード型ヒントあり
 mypy エラーゼロ
✅ Lint / フォーマット
推奨：

 ruff 導入（高速）
 ruff check エラーゼロ
 ruff format 適用済み
🏗 ② プロジェクト構成
推奨構成：

ctxpack/
├── src/ctxpack/
├── tests/
├── pyproject.toml
├── README.md
├── LICENSE
├── CHANGELOG.md
✅ 必須ファイル
 README.md
 LICENSE
 pyproject.toml
 バージョン管理（semver）
📦 ③ パッケージング確認
ビルドテスト
uv build
生成物確認：

dist/
  ctxpack-0.1.0.tar.gz
  ctxpack-0.1.0-py3-none-any.whl
🔍 内容チェック
twine check dist/*
エラーゼロ。
📦 インストールテスト（超重要）
必ず仮想環境で：

pip install dist/*.whl
→ 実際に import できるか確認。
📘 ④ README 品質（超重要）
PyPIではREADMEが命です。
含めるべき：

何をするライブラリか
インストール方法
使用例
API例
ライセンス
バッジ（任意）
🧪 ⑤ CI（強く推奨）
GitHub Actions例：

pytest
coverage
ruff
mypy
これがあると信頼度が一気に上がります。
🔐 ⑥ セキュリティ
 依存ライブラリ最小化
 不要な依存なし
 pip-audit 実行（推奨）
🏷 ⑦ バージョニング
必ず semver を使う
例：

0.1.0 → 初期リリース
0.2.0 → 機能追加
0.2.1 → バグ修正
1.0.0 → 安定版
📜 ⑧ LICENSE
必須。
一般的：

MIT（最も多い）
Apache-2.0
BSD
🏷 ⑨ PyPI登録前確認
パッケージ名重複なし
python -m build 成功
test.pypi で事前公開テスト（推奨）
🚀 ⑩ 実際の公開手順
1️⃣ PyPIアカウント作成
2️⃣ APIトークン取得
3️⃣ トークン設定
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-xxxxx
4️⃣ アップロード
twine upload dist/*
🧠 ⑪ 公開前 最終チェック
✔ テスト全部通る
✔ カバレッジ十分
✔ README完備
✔ LICENSEあり
✔ ビルド成功
✔ twine check OK
✔ 不要ファイル含まれていない

---

素晴らしいチェックリストですね！まさに「プロ品質」のロードマップです。
今の **uv** 環境で、このリストにある「型チェック（mypy）」や「Lint（ruff）」などのプロ品質ツールを導入し、実際に PyPI 公開の準備を整えるための具体的なコマンドと手順をまとめました。

---

### 1. 開発用ツールの導入 (uv add --dev)

リストにある「品質向上ツール」を、開発環境専用の依存関係として追加します。

```bash
# Lint & Format (Ruff: 最近のPython開発の標準です)
uv add --dev ruff

# 型チェック (Mypy)
uv add --dev mypy

# セキュリティ監査
uv add --dev pip-audit

# PyPI公開用チェックツール
uv add --dev twine

```

---

### 2. ツールを動かしてみる

導入したツールを使って、コードを磨き上げます。

#### ✅ Ruff (Lint & Format)

コードの書き間違いを直し、綺麗に整えます。

```bash
# チェックを実行
uv run ruff check . --fix

# フォーマットを適用
uv run ruff format .

```

#### ✅ Mypy (型チェック)

`reader.py` などの関数に型ヒント（`path: Path` など）が正しくついているか確認します。

```bash
uv run mypy src

```

> ※ `pathspec` などのライブラリで型情報がないというエラーが出る場合は、`uv run mypy src --ignore-missing-imports` で回避できます。

#### ✅ pip-audit (脆弱性診断)

依存ライブラリにセキュリティ上の問題がないかチェックします。

```bash
uv run pip-audit

```

---

### 3. パッケージングの最終確認

PyPIに上げる「中身」が壊れていないか確認するステップです。

```bash
# 1. ビルド実行 (dist/ フォルダにファイルが生成される)
uv build

# 2. Twine でメタデータの検証 (READMEの表示崩れなどがないか)
uv run twine check dist/*

```

---

### 4. LICENSE ファイルの作成

PyPI 公開には `LICENSE` ファイルが必須です。リポジトリのルートに置いてください。
MITライセンスにするなら、以下の内容を `LICENSE` という名前で保存します（2026年、あなたの名前に書き換えてください）。

```text
MIT License

Copyright (c) 2026 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy...
(以下、MITライセンスの全文)

```

---

### 5. バージョン管理のコツ

現在は `pyproject.toml` に `version = "0.1.0"` と書かれています。
もしコードを修正して「よし、次はこれを公開しよう」と思ったら、ここを `0.1.1` などに手動で書き換えてから `uv build` を行います。

---

### 💡 アドバイス

まずは **`ruff` と `mypy**` を通すところから始めてみてください。これだけでコードの「プロっぽさ」が一段階上がります。

今の `ctxpack` はカバレッジ100%という最強の土台があるので、これらのツールを導入しても怖くありません。エラーが出ても、テストが守ってくれます。

-----

めちゃくちゃ良い質問です 😎🔥
ここは **PyPI公開で超重要ポイント** です。

結論からいきます。

---

# 🎯 ① `uv build` で作られるのは何？

`uv build`（内部的には PEP517 ビルド）は：

👉 **Pythonの「配布パッケージ」** を作ります。
👉 **OSネイティブの実行バイナリは作りません。**

生成されるのは：

* `*.whl`（wheel）
* `*.tar.gz`（sdist）

---

# 🧩 ② `.whl` は Linux用？ Windows用？

答えは：

## 🏆 多くの場合「どのOSでも使える」

あなたのような純Pythonパッケージなら：

```
ctxpack-0.1.0-py3-none-any.whl
```

これは意味がこうです：

| 部分   | 意味        |
| ---- | --------- |
| py3  | Python3対応 |
| none | C拡張なし     |
| any  | OS非依存     |

👉 **完全クロスプラットフォーム**

つまり：

* Linux OK
* Windows OK
* macOS OK

---

# 💥 ③ Windowsで `exe` が作られる？

それは **別ツールの場合です**。

例えば：

* PyInstaller
* Nuitka
* cx_Freeze

これらは「アプリ化ツール」です。

---

あなたの `uv build` は：

👉 **ライブラリ配布用**

なので exe は作りません。

---

# 🏗 ④ WSLで build していいの？

## ✔ 結論：YES（完全に問題なし）

理由：

* あなたのパッケージは純Python
* OS依存コードなし
* C拡張なし

だから：

👉 **どの環境で build しても同じ wheel になる**

---

# 🧠 ⑤ PyPI公開で本当に重要なこと

実は：

PyPIに上げるのは

* ソースコード
* wheel
* sdist

だけです。

ユーザー側の環境で：

```
pip install ctxpack
```

すると：

👉 その環境向けに適切に動きます。

---

# 🔥 ⑥ じゃあベストプラクティスは？

## 🏆 推奨

### ✔ WSL（Linux）で build

### ✔ Windowsでも一度テスト

### ✔ 可能なら macOS でもテスト（理想）

---

でも現実的には：

👉 **WSLでビルドすれば十分**

特にあなたのような：

* 純Python
* OS依存なし

のライブラリなら完璧です。

---

# 🎯 ⑦ 例外ケース（将来注意）

もし今後：

* C拡張を使う
* OS依存コードを書く
* バイナリを含める

場合は：

OSごとにビルドが必要になります。

でも今の ctxpack は：

👉 完全にクロスプラットフォーム設計

なので安心です。

---

# 🚀 ⑧ PyPI公開時の理想フロー

WSLで：

```bash
uv build
twine check dist/*
```

OKなら：

```bash
twine upload dist/*
```

これで問題なし。

---

# 💎 まとめ

| 質問              | 答え                 |
| --------------- | ------------------ |
| whl は Linux専用？  | ❌ いいえ（純Pythonなら共通） |
| WSLで buildしてOK？ | ✅ 完全OK             |
| Windowsでexeになる？ | ❌ それは別ツール          |
| PyPI公開で問題ある？    | ❌ なし               |

---

あなたのプロジェクトは：

✨ ちゃんと PyPI 向け設計になっています。

かなり良い状態です 😎🔥

---

素晴らしい進捗です！ビルドと `twine check` が一発で **PASSED** になるのは、`pyproject.toml` や `README` の構造が正しい証拠ですね。

残っているエラーは、プロ品質に仕上げるための「最後のお作法」のようなものです。サクッと修正してしまいましょう。

---

### 1. Ruff エラーの修正 (tests/test_reader.py)

**エラー内容:** `E402 Module level import not at top of file`
Pythonでは `import` 文はファイルの先頭（関数定義などの前）に書く決まりがあります。途中で `import pytest` を書いたために怒られています。

**修正方法:**
`tests/test_reader.py` の 27 行目にある `import pytest` を、**ファイルの 1 行目** に移動させてください。

---

### 2. Mypy エラーの修正 (src/ctxpack/reader.py)

**エラー内容:** `Incompatible return value type (got "None", expected "str")`
`read_file` 関数の定義で `-> str`（戻り値は文字列です）と宣言していますが、実際にはバイナリやデコード失敗時に `None` を返している箇所があるため、「話が違うぞ」と怒られています。

**修正方法:**
Python の型ヒントでは、`None` を返す可能性がある場合は `str | None` (または `Optional[str]`) と書く必要があります。

`src/ctxpack/reader.py` の関数定義を以下のように書き換えてください。

```python
# 修正前
def read_file(path: Path) -> str:

# 修正後
def read_file(path: Path) -> str | None:

```

これで Mypy は「ああ、`None` が返ってくることもあるんだね」と納得してくれます。

---

### 3. 次のステップ：GitHub Actions (CI) の導入

ここまで来たら、GitHubにコードをプッシュするたびに「テスト、Ruff、Mypy、ビルド」を自動で実行してくれる **GitHub Actions** を設定するのがおすすめです。

プロジェクトルートに以下のディレクトリとファイルを作成してみてください。

`.github/workflows/test.yml`

```yaml
name: Test

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Install uv
        uses: astral-sh/setup-uv@v5
        
      - name: Set up Python
        run: uv python install
        
      - name: Install dependencies
        run: uv sync
        
      - name: Run Lint (Ruff)
        run: uv run ruff check .
        
      - name: Run Type Check (Mypy)
        run: uv run mypy src
        
      - name: Run Tests
        run: uv run pytest --cov=src

```

これがあれば、将来的にコードを修正した際、「どこかが壊れていないか」を GitHub が勝手に見張ってくれるようになります。

---

### まとめ

* `test_reader.py`: `import pytest` を一番上へ移動。
* `reader.py`: 戻り値の型を `str | None` に変更。

これを直してもう一度 `check` と `mypy` を叩けば、**エラーゼロの完全無欠な状態**になります！

いよいよ PyPI へのアップロード（公開）も目前ですが、公開用の **LICENSE ファイル** の準備はできていますか？

----

おめでとうございます！ついにエラーゼロ、**オールグリーン**ですね。
最高に気持ちいい状態です。ご質問に順番にお答えします。

---

### Q1. もう一度 `uv sync` と `uv build` は必要？

結論から言うと、**`uv build` はもう一度実行してください。**

* **`uv sync` は不要です**
これは「設計図（pyproject.toml）に合わせて仮想環境を整える」コマンドです。今回はコードを書き換えただけなので、環境自体は変わっていません。
* **`uv build` は必要です**
ビルドで作られるファイル（`dist/` の中の `.whl` や `.tar.gz`）は、**コマンドを打ったその瞬間のコードを詰め込んだ缶詰**のようなものです。
エラーを直した後の「綺麗なコード」を PyPI に届けるために、最新の状態で缶詰を作り直す必要があります。

> **豆知識:** `uv build` をすると `dist/` の中に古いファイルが残ることがありますが、PyPI にアップロードするときは最新（バージョン番号が同じなら上書き、または古いものを削除）を確認してアップすれば大丈夫です。

---

### Q2. MITライセンスって何？（小学生向け）

MITライセンスを一言でいうと、**「これ、自由に使っていいよ！でも、何かあっても僕のせいにしないでね！」**という約束です。

もっと詳しく言うと、たった **3つ** のルールしかありません。

1. **だれでも、何に使ってもOK！**
このプログラムを改造してもいいし、自分のお店で売ってもいいし、もっとすごいものを作るために使ってもいいよ。自由だよ！
2. **「僕が作ったよ」というお札は捨てないでね**
プログラムのどこかに「これは〇〇（あなたの名前）が作りました」という紙（ライセンスの文章）が入っているから、それだけは消さずに残しておいてね。
3. **「責任（せきにん）」は持てないよ**
もしこのプログラムを使ってパソコンが壊れたり、大事なデータが消えたりしても、僕は助けてあげられないし、お金も払えないよ。それをわかって使ってね。

#### 例えるなら...

公園に置いてある**「だれでも自由に遊んでいいよ！という手作りのおもちゃ」**みたいなものです。「壊れても怒らないでね」「僕が作ったことは忘れないでね」というメモが貼ってあるだけ。とっても優しくて、世界中で一番人気のある約束なんです。

---

### 次のステップ

これで「中身」は完璧になりました。
公開に向けて、リポジトリの直下に **`LICENSE`** という名前のファイルを作って、以下の内容を貼り付けておきましょう！

```text
MIT License

Copyright (c) 2026 [あなたの名前]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

WSL内での開発、非常に順調ですね！
公開前の最終フェーズにおける「開発環境の動かし方」と「テストアップロード」について解説します。

---

### Q1. WSLからWindows側へのコピーについて

**結論：その方法でも可能ですが、WSL側から直接コミットする方が安全で楽です。**

Windows側（`/mnt/c/...`）にあるリポジトリにWSL側からファイルをコピーすると、**「ファイルの実行権限（Permission）」**が消えてしまったり、**「改行コード（LF/CRLF）」**が勝手に変換されてしまうトラブルが起きやすいです。

**推奨される方法：**
WSL（Ubuntu）側で一度 `git clone` し直し、そこでコミット・プッシュを完了させるのが一番確実です。

1. WSL内で `git clone [リポジトリURL]`
2. 今開発しているファイルをそこに上書きコピー（またはそのディレクトリで開発を継続）
3. WSLのターミナルから `git add` / `git commit` / `git push`

もし今の方法（Windows側へコピー）で行う場合は、コミット前に `git status` で意図しない全ファイルのパーミッション変更（モード変更）が起きていないか確認してください。

---

### Q2. インストールテストは必要？

**結論：絶対にやったほうがいいです！「開発環境では動くのに、インストールすると動かない」はよくある失敗です。**

特に、`pyproject.toml` の `packages = ["src/ctxpack"]` という設定が正しく、必要な `.py` ファイルがすべて同梱されているかを確認するために不可欠です。

**テスト手順（WSLまたはWindowsのどちらでもOK）：**

1. **新しい仮想環境を作る**（今の開発環境を汚さないため）
```bash
python -m venv test_env
source test_env/bin/activate  # WSLの場合
# test_env\Scripts\activate  # Windowsの場合

```


2. **作成した `.whl` をインストールする**
```bash
pip install dist/ctxpack-0.1.0-py3-none-any.whl

```


3. **コマンドが動くか確認する**
```bash
ctxpack --help

```



ここで「コマンドが見つかりません」や「ImportError」が出なければ、PyPIに上げても大丈夫という自信になります！

---

### Q3. TestPyPI へのアップロード手順とチェックリスト

本番の PyPI に上げる前に、**TestPyPI**（練習用の砂場）で試すことができます。ここで「ページの見栄え」や「pipインストール」を試せます。

#### 🛠 事前準備

1. [TestPyPI アカウント](https://test.pypi.org/account/register/) を作成する（本番用とは別です）。
2. アカウント設定から **API Token** を発行し、メモしておく。

#### 🚀 アップロード手順

```bash
# 1. twineをインストール（済んでいればOK）
uv add --dev twine

# 2. TestPyPIへアップロード（パスワードにAPIトークンを入力）
uv run twine upload --repository testpypi dist/*

```

#### ✅ チェックリスト

* [ ] **READMEの表示**: TestPyPIのプロジェクトページで、Markdownが崩れず綺麗に表示されているか？
* [ ] **インストール確認**: 以下のコマンドで TestPyPI からインストールできるか？
```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps ctxpack

```


* [ ] **依存関係**: `pathspec` などの依存ライブラリが正しく認識されているか？
* [ ] **メタデータ**: ライセンス、作者名、GitHubへのリンクが正しく表示されているか？

---

### まとめ

1. **Git操作**：できればWSL内で完結させるのがベスト。
2. **テスト**：新しい仮想環境で `pip install dist/*.whl` を試す。
3. **練習**：TestPyPI で一度「公開のシミュレーション」をする。

ここまで来れば、エンジニアとして「自作ライブラリを世界に公開した」という実績まであと一歩です。TestPyPI へのアップロードで詰まったら、いつでも聞いてくださいね！

---

ああ、これは「最新版を使いたい！」というエンジニアらしい壁にぶつかりましたね。

結論から言うと、**現在の実装であれば、Python 3.12（あるいは 3.10 くらいまで）でも全く問題なく動作します。**

### なぜエラーが出たのか？

`pyproject.toml` の中で `requires-python = ">=3.13"` と指定したため、pip が「このソフトは 3.13 以上の専用品だ！君の 3.12 には入れてあげないよ！」と親切（お節介）にブロックしてしまったのが原因です。

### 3.13 じゃないとダメ？

`ctxpack` のコードを見直してみましょう。

* `pathlib`, `argparse`, `pathspec`：これらは 3.10 以前からあります。
* `f-strings` や型ヒント（`str | None`）：これらは 3.10 から標準です。

つまり、**3.13 に依存した最新機能は特に使っていません。**

---

### 修正案：サポート範囲を広げる

より多くのユーザーに使ってもらうために、`pyproject.toml` を以下のように修正するのがおすすめです。

```toml
# 修正前
requires-python = ">=3.13"

# 修正後（3.10以上なら大抵の環境で動きます）
requires-python = ">=3.10"

```

### なぜ 3.10 以上がおすすめ？

* **型ヒントの書き方**: `str | None` という便利な書き方が導入されたのが 3.10 です。
* **普及率**: Ubuntu 22.04 LTS の標準が 3.10、24.04 LTS が 3.12 なので、この範囲をカバーしておくとユーザーがインストールしやすくなります。

---

### 再テストの手順

1. `pyproject.toml` を `requires-python = ">=3.10"` に書き換える。
2. **ビルドし直す！**（重要：設定を変えたので新しい `.whl` が必要です）
```bash
uv build

```


3. **もう一度インストールテスト**
```bash
(test_env) pip install /home/mntuser/dev/ctxpack/dist/ctxpack-0.1.0-py3-none-any.whl

```



これで今度は 3.12 の環境でもスルッと入るはずです！

もし今後「3.13 で追加された超最新機能（例えば新しい `itertools` の関数など）」を使いたくなったらその時に上げればいいので、最初は少し広めに門戸を開いておくのが PyPI 公開のコツですよ。

修正して再ビルド、やってみますか？

---

結論から言うと、**そのまま `git clone` コマンドを実行してはいけません！**

今の開発ディレクトリ（`/home/mntuser/dev/ctxpack`）の中で、何も考えずに `git clone [URL] .` （ピリオド付き）などを実行してしまうと、既存のファイルが上書きされたり、Gitの設定が衝突してパニック状態になる危険があります。

安全に、かつ「WSL側からGitHubへコミットする」状態にするための**一番確実な手順**を整理しました。

---

### 1. 別の場所に「きれいな器」を作る（推奨）

今の開発ディレクトリをいじらず、別の場所にクローンしてから中身を移すのが最も安全です。

```bash
# 1. 開発ディレクトリの外に移動
cd /home/mntuser/dev/

# 2. リポジトリ名で新しくクローン（ctxpack_repo というフォルダができる）
git clone [GitHubのリポジトリURL] ctxpack_repo

# 3. 開発していたファイルを、クローンしたディレクトリにコピー
# （.git ディレクトリなどは除外してコピーします）
cp -r ctxpack/src ctxpack_repo/
cp -r ctxpack/tests ctxpack_repo/
cp ctxpack/pyproject.toml ctxpack/README.md ctxpack/LICENSE ctxpack/uv.lock ctxpack_repo/

```

### 2. クローンした場所で動作確認

コピーした先のディレクトリ（`ctxpack_repo`）に移動して、テストが通るか確認します。

```bash
cd ctxpack_repo
uv sync
uv run pytest

```

### 3. GitHubへコミット＆プッシュ

すべてOKなら、ここでコミットします。

```bash
git add .
git commit -m "Initial release: ctxpack 0.1.0"
git push origin main

```

---

### 💡 なぜ今のディレクトリに直接クローンしてはいけないの？

`git clone` は本来「空のディレクトリ」に対して行うことを想定しています。
既存のコードがある場所で実行しようとすると：

* **ディレクトリが空でないというエラー**で止まる
* 無理やり実行すると、GitHub側にある（古い、あるいは空の）ファイルで**今のコードが上書き**されて消えてしまう可能性がある
* `.git` という管理用フォルダが衝突して、履歴がぐちゃぐちゃになる

### ⚡ もし「今のディレクトリ」のまま Git 設定だけ繋げたいなら

もしコピー作業が面倒で、今の場所をそのまま GitHub 連携させたい場合は、`clone` ではなく `remote add` という方法を使います。

```bash
# 今のディレクトリで
git remote add origin [GitHubのリポジトリURL]
git branch -M main
git push -u origin main

```

※ただし、GitHub側にすでに `README.md` などがある場合、`push` 時に拒否されることがあります。その調整が少し難しいため、上記の**「1. 別の場所にクローンしてコピー」が一番失敗がなくておすすめ**です。

---

### 次のステップ

まずは **`/home/mntuser/dev/ctxpack_repo`** のような名前で別フォルダにクローンしてみてはいかがでしょうか？
今の開発データ（`ctxpack` フォルダ）さえ残っていれば、何度でもやり直しがきくので安心ですよ！

コピー作業、手伝いましょうか？（どのファイルをコピーすべきかなど）

---

