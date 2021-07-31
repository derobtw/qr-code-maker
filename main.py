import qrcode

data1=input('Data for QR Code: ')
imgname=input('Image name to save: ')

qr = qrcode.QRCode(
	version=1,
	box_size=15,
	border=5
)

data = f'{data1}'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save(f'{imgname}.png')
