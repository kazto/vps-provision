# AWS SES 設定ガイド

VPSプロビジョニングでメール送信にAWS SESを使用するための設定手順

## AWS SES 初期設定

### 1. AWS Console での設定

1. **AWS Management Console** にログイン
2. **Simple Email Service (SES)** サービスに移動
3. リージョンを選択 (推奨: us-east-1)

### 2. SMTP 認証情報の作成

1. SES ダッシュボードで **SMTP Settings** を選択
2. **Create SMTP Credentials** をクリック
3. IAM ユーザー名を設定 (例: `ses-smtp-user`)
4. **Download Credentials** でCSVファイルをダウンロード
5. 認証情報を記録:
   - SMTP Username
   - SMTP Password

### 3. 送信元メールアドレスの認証

1. **Verified identities** に移動
2. **Create identity** をクリック
3. **Email address** を選択
4. 送信元として使用するメールアドレスを入力
5. 認証メールを確認してリンクをクリック

### 4. Sandbox モードの解除 (本番環境)

初期状態はSandboxモードで、認証済みアドレスにのみ送信可能:

1. **Account dashboard** に移動
2. **Request production access** をクリック
3. 申請フォームを記入:
   - Use case description
   - Website URL
   - 送信予定量
4. AWS の承認を待つ (通常24時間以内)

## プロビジョニング設定

### 1. 環境変数の設定

`.env` ファイルに以下を設定:

```bash
# AWS SES 設定
AWS_SES_REGION=us-east-1
AWS_SES_USERNAME=AKIAI...  # SMTP Username
AWS_SES_PASSWORD=BPwq...   # SMTP Password
SES_RELAY_HOST=email-smtp.us-east-1.amazonaws.com

# メール設定
LOGWATCH_MAILTO=alerts@example.com
LOGWATCH_MAILFROM=server@example.com
CRONAPT_MAILTO=admin@example.com
```

### 2. リージョン別エンドポイント

主要リージョンのSMTPエンドポイント:

| リージョン | エンドポイント |
|-----------|----------------|
| us-east-1 | email-smtp.us-east-1.amazonaws.com |
| us-west-2 | email-smtp.us-west-2.amazonaws.com |
| eu-west-1 | email-smtp.eu-west-1.amazonaws.com |
| ap-northeast-1 | email-smtp.ap-northeast-1.amazonaws.com |

## テスト手順

### 1. 設定テスト

```bash
# 構文チェック
python test_deploy.py

# ドライラン実行
pyinfra inventory.py deploy.py --dry
```

### 2. メール送信テスト

デプロイ後、以下でメール送信をテスト:

```bash
# logwatch 手動実行
sudo logwatch --mailto alerts@example.com

# cron-apt 設定確認
sudo cat /etc/cron-apt/config
```

## トラブルシューティング

### よくある問題

1. **認証エラー**
   - SMTP認証情報が正しいか確認
   - リージョンとエンドポイントが一致しているか確認

2. **送信制限エラー**
   - Sandboxモードの場合、送信先が認証済みか確認
   - 送信レート制限に達していないか確認

3. **DNS/接続エラー**
   - ファイアウォールで587ポートが開いているか確認
   - DNS解決ができているか確認

### ログ確認

```bash
# Postfix ログ
sudo tail -f /var/log/mail.log

# システムログ
sudo tail -f /var/log/syslog
```

## セキュリティ考慮事項

- SMTP認証情報は`.env`ファイルで管理し、バージョン管理に含めない
- IAMユーザーには最小限の権限のみ付与
- 定期的に認証情報をローテーション
- 送信量とアクセスログを監視