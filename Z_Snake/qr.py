import qrcode #install this packages to use this programm
import image #install this packages to run this program

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

utube = 'https://www.youtube.com/channel/UCVyYaRP4KE6h5ih8nounGsQ/featured'
qr.add_data(utube)
qr.make(fit=True)
img = qr.make_image(fill="red",back_color="white")
img.save('test.png')
