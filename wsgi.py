from filemanager import app

if __name__ == "__main__":
    app.run()
```

### 4. **`Procfile`** (For Heroku/Railway deployment)
```
web: gunicorn wsgi:app
