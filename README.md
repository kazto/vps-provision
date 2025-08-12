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

3. デプロイ実行
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

## 機能

* ユーザ作成・管理
* SSH セキュリティ設定
* Postfix メール設定
* fail2ban 侵入防止
* cron-apt 自動更新
* logwatch ログ監視
* docker コンテナ環境
* Mastodon インスタンス構築
