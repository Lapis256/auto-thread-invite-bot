# auto-thread-invite-bot

## 動かし方
### 必要な物
Postgresql 13
Python 3.8 以上

### 事前準備
`env.sample`を参考にして`.env`を作成してください

### コマンド
```
psql -f table.sql <db name>
python -m venv .venv
source .venv/bin/activate
pip install -U pip wheel
pip install -Ur requirements.txt
python register_command.py
python main.py
```

## 使い方
/create_setting_panel <ロール>
このコマンドを使用すると指定したロールを管理するパネルが作成されます。
そして、スレッド作成時に指定したロールに対してメンションします。
