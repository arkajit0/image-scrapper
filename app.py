from flask import Flask, render_template, request
import os
from main import image_scrapper
import time

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/search", methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        try:
            search_image = request.form['image_name'].replace(' ', '')
            number_of_image = int(request.form['number'])
            image_scrapper(image_name=search_image, number_of_image=number_of_image)
            # time.sleep(2)
            image_names = os.listdir('./static/images/store_image/'+search_image)
            return render_template('result.html', folder=search_image, pics=image_names)
        except Exception as e:
            print(e)
            return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

