from flask import Flask, render_template
import os

app = Flask(__name__)

# 画像フォルダのパスを設定
IMAGES_FOLDER = 'static/images'

@app.route('/')
def slideshow():
    # 画像ファイルの一覧を取得
    images = [f for f in os.listdir(IMAGES_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    return render_template('slideshow.html', images=images)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))