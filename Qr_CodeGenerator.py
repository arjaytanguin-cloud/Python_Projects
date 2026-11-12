import qrcode

print("==========Welcome to QR Code Generator!!!==========")
text = input("Enter the text or URL to generate QR code: ")
img = qrcode.make(text)
img.save("qr_code.png")

print("QR code generated and saved as 'qr_code.png'.")

