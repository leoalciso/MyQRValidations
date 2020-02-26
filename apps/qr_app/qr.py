import qrcode, bcrypt, random
qr = qrcode.QRCode(
version=1,
error_correction=qrcode.constants.ERROR_CORRECT_L,
box_size=10,
border=4,
)
qr.add_data('Kevin and Leo')
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('image.png')