from flask import Flask, request
import cv2
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    image_data = request.data
    img_array = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    filename = os.path.join(UPLOAD_FOLDER, 'latest.jpg')
    cv2.imwrite(filename, img)
    return 'Image received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
