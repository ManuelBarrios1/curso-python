# Declaramos una variable
calificacion = input("Introduce tu calificacion de la AZ-900: ")

calificacion = int(calificacion)

# Preguntamos si la calificacion es menos a 700
if calificacion < 700 : 
    print("Vees. por no estudiar") # Si es menor a 700, muestra esto
elif calificacion == 700 :
    print("Panzazoooo")
elif calificacion > 1000 :
    print("mientes!!! no puedes sacar más de mil")
else : # Si no se cumple el if anterior, pasa a esta línea
    print("felicidades, para por tu certificadop") # se ejecuta si nunguno de los if se cumple

# Verificador de mayoria de edad
edad = input("introduce tu edad ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenido al mamitas")
elif edad > 100 :
    print("Si vienes acompañados de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("ni que fueras viejero del tiempo")
else :
    print("No puedes llevarte esos cigarros")
