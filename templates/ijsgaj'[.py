import webbrowser
import os
import threading
import time
from flask import Flask, render_template_string

app = Flask(__name__)

# Исправлено: добавлен автор в правильном падеже
phrase = "«Как ты думаешь, когда человек умирает? Когда пуля из пистолета пронзает его сердце? Нет. Когда на него нападает неизлечимая болезнь? Нет. Когда он съедает суп из смертельно ядовитых грибов? Нет. Человек умирает, когда люди его забывают!»"
author = "— Доктор Хирург"  # Исправлено имя персонажа (в оригинале "доктор Хирург")

# Исправлен HTML-код: теперь цитата в h1 слишком большая, перенес в p
html_code = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Крылатое выражение</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .card {
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
            max-width: 700px;
            margin: 20px;
        }
        .quote {
            color: #2c3e50;
            font-size: 1.3em;
            line-height: 1.6;
            margin-bottom: 20px;
            font-style: italic;
        }
        .author {
            color: #7f8c8d;
            font-size: 1.1em;
            text-align: right;
            border-top: 1px solid #eee;
            padding-top: 15px;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="quote">""" + phrase + """</div>
        <div class="author">""" + author + """</div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_code)

def open_html_file():
    """Создает HTML файл и открывает его в браузере"""
    try:
        file_name = "expression.html"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(html_code)
        
        full_path = os.path.abspath(file_name)
        webbrowser.open('file://' + full_path)
        print("✓ HTML файл создан и открыт в браузере!")
        print(f"  Путь: {full_path}")
    except Exception as e:
        print(f"✗ Ошибка при создании HTML файла: {e}")

def open_browser():
    """Открывает браузер после запуска сервера"""
    time.sleep(1.5)  # Ждем запуска сервера
    webbrowser.open('http://127.0.0.1:5000')
    print("✓ Браузер открыт по адресу: http://127.0.0.1:5000")

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 Запуск приложения...")
    print("=" * 50)
    
    # Запускаем браузер в отдельном потоке
    threading.Thread(target=open_browser, daemon=True).start()
    
    # Запускаем Flask сервер
    print("\n📡 Сервер запущен по адресу: http://127.0.0.1:5000")
    print("📝 Для остановки сервера нажмите Ctrl+C")
    print("=" * 50 + "\n")
    
    try:
        app.run(debug=True, use_reloader=False)  # Отключаем перезагрузчик для корректной работы потока
    except KeyboardInterrupt:
        print("\n\n👋 Сервер остановлен")
    finally:
        # Создаем HTML файл после остановки сервера
        open_html_file()
