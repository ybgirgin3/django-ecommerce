import numpy as np
import os
import cv2

# settings yerine
# djecommerce/settings/base.py

# referans path
# core/opencvimageedit.py


# path olarak resmin urlsi verilecek
# anasayfada ve diğer sayfalardan
# görüntülenen elemanların üzerine tıklandığında
# imageedit.html üzerine gidecek

resimler = []


for i in os.listdir(os.getcwd()):
    if i.endswith('jpg'):
        resimler.append(i)

for name in resimler:
    new_name = 'cv_' + name


    img = cv2.imread(name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (11, 11), 0)

    cv2.imwrite(new_name, blur)

