# VPS Provisioning with pyinfra

Ansible から pyinfra に移行したVPSプロビジョニング設定

## 必要条件

```bash
pip install pyinfra
```

## 使用方法

1. 設定ファイルをコピー
```bash
cp .env.sample .env
```

2. `.env` ファイルに実際の値を記入
   - AWS SES の SMTP 認証情報を設定
   - メール送信先アドレスを設定

3. AWS SES の設定
   - AWS Console で SES サービスに移動
   - SMTP 認証情報を作成
   - 送信元メールアドレスを認証
   - 必要に応じて Sandbox モードから本番モードに移行

4. デプロイ実行
```bash
# ドライラン
pyinfra inventory.py deploy.py --dry

# 実際のデプロイ
pyinfra inventory.py deploy.py
```

## プロジェクト構造

```
├── inventory.py          # ホスト定義
├── deploy.py             # メインデプロイスクリプト
├── config.py             # 設定管理
├── .env.sample           # 環境変数テンプレート
├── tasks/                # タスクモジュール
│   ├── base.py          # 基本パッケージ
│   ├── fail2ban.py      # 侵入防止設定
│   ├── logwatch.py      # ログ監視設定
│   ├── postfix.py       # メール設定
│   ├── docker.py        # Docker設定
│   ├── cronapt.py       # 自動更新設定
│   └── tmpl/            # 設定ファイルテンプレート
└── docs/                # ドキュメント
```

## Ansible からの変更点

- **YAML → Python**: 設定ファイルがPythonになり、より柔軟な記述が可能
- **vault → .env**: Ansible vault の代わりに環境変数で秘密情報を管理
- **playbook → deploy.py**: プレイブックがPythonスクリプトに
- **inventory → inventory.py**: インベントリもPythonで動的生成可能
- **Mailgun → AWS SES**: メール送信をMailgunからAWS SESに変更

## テスト実行

テストは testinfra を使用して実行します。

```bash
# testinfra のインストール
pip install testinfra

# すべてのテストを実行
pytest tests/

# 特定のテストファイルのみ実行
pytest tests/test_docker.py

# リモートホストでテストを実行
pytest --hosts=ssh://user@hostname tests/
```

### テストファイル構成

```
tests/
├── test_base_packages.py  # 基本パッケージのテスト
├── test_docker.py         # Dockerのテスト
├── test_fail2ban.py       # fail2banのテスト
├── test_postfix.py        # postfixのテスト
├── test_cronapt.py        # cron-aptのテスト
├── test_logwatch.py       # logwatchのテスト
└── test_services.py       # サービス状態のテスト
```

## 機能

* ユーザ作成・管理
* SSH セキュリティ設定
* Postfix メール設定
* fail2ban 侵入防止
* cron-apt 自動更新
* logwatch ログ監視
* docker コンテナ環境
* Mastodon インスタンス構築
