# program celcius
Celcius = float(input('masukkan suhu dalam celcius :'))
print("suhu adalah",Celcius,"Celcius")

# reamur
reamur = (4/5)*Celcius
print ("suhu dalam reamur adalah ",reamur, "reamur")

#fahrenheit
fahrenheit = (9/5) * Celcius
print ("suhu dalam fahrenheit adalah ",fahrenheit, "fahrenheit")

#kelvin
kelvin = Celcius + 273
print ("suhu dalam kelvin",kelvin,"kelvin")

#latihan 01 fahrenheit ke kelvin
fahrenheit = float(input("masukkan data:","fahrenheit"))
celcius = 5/9*(fahrenheit-32) 
kelvin = celcius + 273
print ("suhu adalah",kelvin,"kelvin")


#latihan 02 kelvin ke fahrenheit
kelvin = float(input("masukkan data:","kelvin"))
celcius = kelvin-273
fahrenheit = 9/5*(celcius+32)
print ("suhu adalah",fahrenheit,"fahrenheit")