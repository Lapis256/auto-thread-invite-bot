# auto-thread-invite-bot

## 動かし方
```
python -m venv .venv
source .venv/bin/activate
pip install -U pip wheel
pip install -Ur requirements.txt
```

## 使い方
スレッドが作成されると ThreadListener という名前のロールをメンションするBotです。
ロール名の大文字、小文字は区別されません。

### 注意
Botに 全てのロールにメンション の権限を付与するか、ThreadListener をメンション出来るように設定してください。
