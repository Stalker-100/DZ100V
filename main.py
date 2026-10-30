from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def site1():
    img_url = url_for('static', filename='12345.jpg')

    html_content = f'''
        <h1>Это Я</h1>
        <p>Здесь соц сети - t.me/@shokhmardon1</p>
        <img src="{img_url}" alt="Мое фото" style="max-width: 100px;">
        <h2>Любимые игры</h2>
        <p>Skyrim, CS 1.6, Minecraft</p>
    '''
    return html_content

if __name__ == '__main__':
    app.run()
