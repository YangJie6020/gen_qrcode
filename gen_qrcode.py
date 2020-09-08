import pandas as pd
import qrcode

df = pd.read_excel('list1.xlsx', sheet_name="Sheet1")

index = 0

for value in df.values:

	url = value[0]

	print(url)
	
	index = index + 1

	print("make " + str(index) + ".png")

	qr = qrcode.QRCode(
		version=10,
		error_correction=qrcode.constants.ERROR_CORRECT_H,
		box_size=8,
		border=4
	)

	qr.add_data(url)

	qr.make(fit=True)

	img = qr.make_image()

	img.save("" + str(index) + ".png")
