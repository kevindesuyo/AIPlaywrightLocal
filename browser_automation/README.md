# ブラウザ自動化ツール

このツールはLangChainとPlaywrightを利用し、Streamlit UIを通じてユーザーの入力に基づくブラウザ操作を自動化します。

## 主な機能

- 自然言語によるブラウザ操作の自動化
- ナビゲーション、検索、クリック、コンテンツ抽出など複雑なブラウザフローの実行
- フォーム入力や要素待機などの拡張カスタムツール
- シンプルで直感的なユーザーインターフェース

## インストール方法

1. リポジトリをクローン:
```bash
git clone <repository-url>
cd browser-automation
```

2. 仮想環境を作成して有効化:
```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

3. 必要なパッケージをインストール:
```bash
pip install -r requirements.txt
```

4. Playwright用のChromiumブラウザをインストール:
```bash
python -m playwright install chromium
```

## 設定

1. プロジェクトのルートディレクトリに`.env`ファイルを作成:
```
OPENAI_API_KEY=your_openai_api_key_here
```

2. `your_openai_api_key_here`をご自身のOpenAI APIキーに置き換えてください。APIキーは[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)から取得できます。

## 使い方

1. アプリケーションを起動:
```bash
python main.py
```

2. ブラウザで [http://localhost:8501](http://localhost:8501) にアクセス

3. 必要に応じてOpenAI APIキーを入力

4. テキストエリアにブラウザ操作指示を入力

5. 「Run Automation」をクリックして実行

## サンプル指示

以下はテスト用のサンプル指示です:

1. **シンプルなナビゲーションと情報抽出**:
   ```
   google.comにアクセスし、「LangChain tutorials」で検索し、最初の結果のタイトルを教えて。
   ```

2. **Wikipedia検索と要約**:
   ```
   wikipedia.orgに移動し、「Artificial Intelligence」で検索、記事に移動し、最初の段落を要約して。
   ```

3. **ニュース集約**:
   ```
   news.ycombinator.comにアクセスし、トップ5件のストーリーのタイトルを教えて。
   ```

## 詳細オプション

- **詳細なエージェントステップ表示**: エージェントが実行する詳細なステップを表示します。
- **最大イテレーション数**: タスク完了までの最大反復回数を設定できます。

## プロジェクト構成

- `main.py`: アプリケーションのエントリーポイント
- `env_setup.py`: 環境設定ユーティリティ
- `browser_setup.py`: Playwrightブラウザ初期化
- `langchain_setup.py`: LangChainツールキット設定
- `agent_setup.py`: ブラウザ操作エージェント設定
- `custom_tools.py`: 拡張ブラウザ操作用カスタムツール
- `browser_flow.py`: ブラウザ操作フロー定義
- `streamlit_app.py`: Streamlit UI実装

## トラブルシューティング

- **OpenAI APIキーの問題**: `.env`ファイルやUIで正しく設定されているか確認してください。
- **ブラウザ初期化エラー**: `python -m playwright install chromium`でPlaywrightが正しくインストールされているか確認してください。
- **エージェント実行エラー**: 詳細なエージェントステップを確認し、どこで失敗しているか特定してください。

## ライセンス

このプロジェクトはMITライセンスで提供されています。詳細はLICENSEファイルをご覧ください。
