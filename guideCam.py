import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import argparse
import io

from google.cloud import vision
from google.cloud.vision import types

# Windows dependencies
# - Python 2.7.6: http://www.python.org/download/
# - OpenCV: http://opencv.org/
# - Numpy -- get numpy from here because the official builds don't support x64:
#   http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

# Mac Dependencies
# - brew install python
# - pip install numpy
# - brew tap homebrew/science
# - brew install opencv

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

cv2.imshow('frame', rgb)
out = cv2.imwrite('capture.jpg', frame)

client = vision.ImageAnnotatorClient()

with io.open('capture.jpg', 'rb') as image_file:
        content = image_file.read()

image = types.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)

cap.release()
cv2.destroyAllWindows()


