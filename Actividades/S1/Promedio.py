print("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar, ¿Cuál es tu nombre?: ")

algoritmos = int(input(nombre + " ¿Cuál es tu calificación de Algoritmos?: "))
poo = int(input(nombre + " ¿Cuál es tu calificación de Programación Orientada a Objetos?: "))
bases_datos = int(input(nombre + " ¿Cuál es tu calificación de Bases de Datos?: "))
desarrollo_web = int(input(nombre + " ¿Cuál es tu calificación de Desarrollo Web?: "))
redes = int(input(nombre + " ¿Cuál es tu calificación de Gestión de Redes?: "))
arquitectura = int(input(nombre + " ¿Cuál es tu calificación de Arquitectura de Software?: "))
python = int(input(nombre + " ¿Cuál es tu calificación de Python?: "))

promedio = (algoritmos + poo + bases_datos + desarrollo_web + redes + arquitectura + python) / 7

if promedio >= 60:
    print(" :( " + nombre + " aprobaste por pura suerte: ", round(promedio, 2))
elif promedio >= 70:
    print("Que te digo " + nombre + "pero Hechale ganas: ", round(promedio, 2))
elif promedio >= 80:
    print("Vas mejorando " + nombre + "No me convences: ", round(promedio, 2))
elif promedio >= 90:
    print("Eso ya esta mejor " + nombre + "pero puedes mejorar: ", round(promedio, 2))
elif promedio == 100:
    print("Ya Ahora si te mereces tu mercho" + nombre + "Llegaste al top: ", round(promedio, 2))
else:
    print("Que wey " + nombre + " reprobaste JAJAJAJAJAJA: ", round(promedio, 2))
print("Fin")