print("## Program Python Konversi Suhu ##")
print("========================================================")
print()

celc = float(input("Masukkan suhu dalam Celcius: "))
fahr = (9/5 * celc) + 32
print(celc, "Derajat Celcius =", fahr, "Derajat Fahrenheit" )

fahr = float(input("Masukkan suhu dalam Fahrenheit: "))
celc = (5/9) * (fahr - 32)
print(fahr, "Derajat Fahrenheit =", "{:.2f}".format(celc), "Derajat Celcius" )

kelv = float(input("Masukkam suhu dalam Kelvin: "))
celc = kelv - 273.15
print(kelv, "Derajat Kelvin =", "{:.2f}".format(celc), "Derajat Celcius" )