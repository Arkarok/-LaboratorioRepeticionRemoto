print("Numero entero mayor que 0")


a=int(input("Digita un numero entero, Por favor: "))


if a>0:
  print("El numero es mayor que 0")

else:
  print("El numero no es mayor que 0")

print("Numero entero mayor que 0, Modificaciones")

for a in range(-5,5):
  if a>0:
    print(str(a) + " El numero es mayor que 0")
  elif a==0:
    print(str(a) + " El numero es igual a 0")
  else:
    print(str(a) + " El numero no es mayor que 0")

