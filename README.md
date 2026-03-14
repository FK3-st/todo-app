# Todo App

CLIとWeb APIで使えるタスク管理ツールです。

## 機能
- タスクの追加・一覧・完了・削除・検索

## 使い方

### CLI
```
python main.py add "タスク名"
python main.py list
python main.py done 1
python main.py delete 1
python main.py search キーワード
```

### Web API
```
uvicorn api:app --reload
```
`http://localhost:8000/docs`からAPIを操作できます。

## 技術
- Python
- FastAPI
- pytest
```

