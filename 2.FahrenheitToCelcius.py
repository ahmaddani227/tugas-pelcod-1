print("## Program Python Konversi Suhu Fahrenheit ke Celcius ##")
print("========================================================")
print()

fahr = float(input("Masukkan suhu dalam Fahrenheit: "))
celc = (5/9) * (fahr - 32)
print(fahr, "Derajat Fahrenheit =", "{:.2f}".format(celc), "Derajat Celcius" )