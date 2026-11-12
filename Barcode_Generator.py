import barcode
from barcode.writer import ImageWriter

print("======Welcome to the Barcode Generator!=======")
print("This program generates a barcode image from the input number.")
print("Please enter a number to encode into a barcode.")
code = input("Enter number to encode: ")

barcode_obj = barcode.get("code128", code, writer=ImageWriter())
barcode_obj.save("barcode")

print("Barcode generated and saved as 'barcode.png'.")