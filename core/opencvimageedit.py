from django.conf import settings
import numpy as np
import cv2

# settings yerine
# djecommerce/settings/base.py

# referans path
# core/opencvimageedit.py


# path olarak resmin urlsi verilecek
# anasayfada ve diğer sayfalardan
# görüntülenen elemanların üzerine tıklandığında
# imageedit.html üzerine gidecek


def img_prc(img):
    # clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (11, 11), 0)


def process(path):
    img = cv2.imread(path, 1)

    if type(img) is np.ndarray:
        print(img.shape)
