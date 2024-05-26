from flask import Flask, render_template, jsonify, url_for
import os

app = Flask(__name__, template_folder='static/templates')


# profiles = [
#     {'name': 'Angelina Jolie', 'photo_url': 'images/foto_1-1.jpg', 'slide_url': 'images/slide_1-1.jpg'},
#     {'name': 'Anne Hathaway', 'photo_url': 'images/foto_2-1.jpg', 'slide_url': 'images/slide_2-1.jpg'},
#     {'name': 'Catherine Zeta-Jones', 'photo_url': 'images/foto_16-1.jpg', 'slide_url': 'images/slide_16-1.jpg'},
#     {'name': 'Dana Davis', 'photo_url': 'images/foto_5-1.jpg', 'slide_url': 'images/slide_5-1.jpg'},
#     {'name': 'Danai Jekesay Gurira', 'photo_url': 'images/foto_17-1.jpg', 'slide_url': 'images/slide_17-1.jpg'},
#     {'name': 'Dilraba Dilmurat', 'photo_url': 'images/foto_18-1.jpg', 'slide_url': 'images/slide_18-1.jpg'},
#     {'name': 'Elizabeth Taylor', 'photo_url': 'images/foto_14-1.jpg', 'slide_url': 'images/slide_14-1.jpg'},
#     {'name': 'Emma Stone', 'photo_url': 'images/foto_12-1.jpg', 'slide_url': 'images/slide_12-1.jpg'},
#     {'name': 'Guli Nezha', 'photo_url': 'images/foto_19-1.jpg', 'slide_url': 'images/slide_19-1.jpg'},
#     {'name': 'Halle Berry', 'photo_url': 'images/foto_15-1.jpg', 'slide_url': 'images/slide_15-1.jpg'},
#     {'name': 'Jennifer Lawrence', 'photo_url': 'images/foto_7-1.jpg', 'slide_url': 'images/slide_7-1.jpg'},
#     {'name': 'Jennifer Lynn Lopez', 'photo_url': 'images/foto_22-1.jpg', 'slide_url': 'images/slide_22-1.jpg'},
#     {'name': 'Julia Roberts', 'photo_url': 'images/foto_9-1.jpg', 'slide_url': 'images/slide_9-1.jpg'},
#     {'name': "Lupita Nyong'o", 'photo_url': 'images/foto_10-1.jpg', 'slide_url': 'images/slide_10-1.jpg'},
#     {'name': 'Margot Robbie', 'photo_url': 'images/foto_3-1.jpg', 'slide_url': 'images/slide_3-1.jpg'},
#     {'name': 'Marilyn Monroe', 'photo_url': 'images/foto_8-1.jpg', 'slide_url': 'images/slide_8-1.jpg'},
#     {'name': 'Meryl Streep', 'photo_url': 'images/foto_13-1.jpg', 'slide_url': 'images/slide_13-1.jpg'},
#     {'name': 'Sandra Bullock', 'photo_url': 'images/foto_4-1.jpg', 'slide_url': 'images/slide_4-1.jpg'},
#     {'name': 'Scarlett Johansson', 'photo_url': 'images/foto_6-1.jpg', 'slide_url': 'images/slide_6-1.jpg'},
#     {'name': 'Shaunette Renee Wilson', 'photo_url': 'images/foto_11-1.jpg', 'slide_url': 'images/slide_11-1.jpg'},
#     {'name': 'Victoria Song', 'photo_url': 'images/foto_21-1.jpg', 'slide_url': 'images/slide_21-1.jpg'},
#     {'name': 'Yang Mi', 'photo_url': 'images/foto_20-1.jpg', 'slide_url': 'images/slide_20-1.jpg'},   
# ]

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/images')
# def list_images():
#     # Criando uma cópia do array images_data
#     images_with_url = []
#     for profile in profiles:
#         # Copiando cada item e adicionando o caminho da URL
#         image_copy = profile.copy()
#         image_copy['photo_url'] = url_for('static', filename=profile['photo_url'])
#         image_copy['slide_url'] = url_for('static', filename=profile['slide_url'])
#         images_with_url.append(image_copy)

#     return jsonify(images_with_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)