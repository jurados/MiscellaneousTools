# -*- coding: utf-8 -*-
import sys
import qrcode

try:
    url = sys.argv[1]
except:
    url = None

# Creating an instance of QRCode class
qr_img = qrcode.QRCode(version = 1,
                       box_size = 10,
                       border = 3)

if url == None:
    url = input('')

# Adding data to the instance 'qr'
qr_img.add_data(data="https://www.javatpoint.com/python-tutorial")

# Using the make() function
qr_img.make(fit=True)

# Using the make_image() function
qr_img = qr_img.make_image(fill_color = "cyan", back_color = "black")  

# Saving the QR code image
qr_img.save("QR_image.png")  