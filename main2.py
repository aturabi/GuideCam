import os

while True:
    os.system("for f in *.jpg; do mv $f cam_img.jpg; done")
    os.system("gsutil cp cam_img.jpg gs://images_store2")
