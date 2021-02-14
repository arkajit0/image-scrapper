from flask import Flask, render_template, request
import os
from main import image_scrapper


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_image = request.form['image_name'].replace(' ', '')
        number_of_image = int(request.form['number'])
        image_scrapper(image_name=search_image, number_of_image=number_of_image)
        image_names = os.listdir('./static/images/'+search_image)
        return render_template('index.html', folder=search_image, pics=image_names)
    else:

        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
