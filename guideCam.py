import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import argparse
import io
import pyttsx

from google.cloud import vision
from google.cloud.vision import types
from google.cloud import datastore

from os import system

# Dependencies
# - brew install python
# - pip install numpy
# - brew tap homebrew/science
# - brew install opencv

#capture a frame from camera
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

#show frame and write to jpg file
cv2.imshow('frame', rgb)
out = cv2.imwrite('capture.jpg', frame)

client = vision.ImageAnnotatorClient()

#open image file
with io.open('capture.jpg', 'rb') as image_file:
        content = image_file.read()

image = types.Image(content=content)

#get labels from google vision API
response = client.label_detection(image=image)
labels = response.label_annotations

signage = 0

#loop through labels, print and check for signage as a label
print('Labels:')
for label in labels:
    print(label.description)
    if(label.description == 'signage' or label.description == 'sign' or label.description == 'stop sign'):
	signage = 1

stopFound = 0
if(signage):
    response2 = client.text_detection(image=image)
    texts = response2.text_annotations
    print('Texts:')

    for text in texts:
        print(format(text.description))
        if(format(text.description) == 'STOP'):
            print('checkit')
            stopFound = 1
    if(stopFound == 1):
        system('say yes there is a stop sign')
    else:
        system('say no there is no stop sign')
else:
    system('say no there is no stop sign')

cap.release()
cv2.destroyAllWindows()


