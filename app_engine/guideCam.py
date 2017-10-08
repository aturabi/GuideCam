from flask import Flask, request
from google.cloud import vision
from google.cloud.vision import types


from os import system

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def image_vision():
    client = vision.ImageAnnotatorClient()


    image = types.Image()
    image.source.image_uri = "gs://images_store2/cam_img.jpg"
    #get labels from google vision API
    response = client.label_detection(image=image)
    labels = response.label_annotations

    signage = 0

    #loop through labels, print and check for signage as a label
    print('Labels:')
    desc = request.args.get('description')
    for label in labels:
        print(label.description)
        if(label.description == desc):
           signage = 1
        
    if(signage == 1):
       return "YES"
    else:
       return "NO"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
