import webbrowser
import os



phrase = "«Как ты думаешь, когда человек умирает? Когда пуля из пистолета пронзает его сердце? Нет. Когда на него нападает неизлечимая болезнь? Нет. Когда он съедает суп из смертельно ядовитых грибов? Нет. Человек умирает, когда люди его забывают!»"
author = "доктором Хирилюком"




html_code = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Крылатое выражение</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f2f5;
        }}
        .card {{
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            text-align: center;
            max-width: 600px;
        }}
        h1 {{ color: #2c3e50; }}
        p {{ color: #7f8c8d; font-style: italic; font-size: 1.2em; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{phrase}</h1>
        <p>{author}</p>
    </div>
</body>
</html>
"""




file_name = "expression.html"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(html_code)




full_path = os.path.abspath(file_name)
webbrowser.open('file://' + full_path)

print("Файл создан и открыт в браузере!")