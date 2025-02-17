# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Similar al ejercicio de "calificaciones":

Debe caluclar el promedio de todas las notas que se encuentra
almacenadas en una lista llamada "notas" que ya
hemos definido al comienzo del archivo

Luego transformar la califiación en una letra
según la siguiente escala:
- Si el puntaje es mayor igual a 90 --> imprimir A
- Si el puntaje es mayor igual a 80 --> imprimir B
- Si el puntaje es mayor igual a 70 --> imprimir C
- Si el puntaje es mayor igual a 60 --> imprimir D
- Si el puntaje es menor a  60      --> imprimir F

A medida que recorre las notas, no debe considerar como válidas aquellas
que son negativas, en ese caso el alumno estuvo ausente

Debe contar la cantidad de notas válidas y la cantidad de ausentes
'''

print("Mi organizador académico (#_#)")
# Empezar aquí la resolución del ejercicio

# Para calcular el promedio primero debe obtener la suma
# de todas las notas, que irá almacenando en esta variable

sumatoria = 0           # Ya le hemos inicializado en 0

cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

# Realice aquí el bucle para recorrer todas las notas
# y cacular la sumatoria

for nota in notas:
    if nota < 0:
        cantidad_ausentes += 1
    else:
        cantidad_notas += 1

print('cantidad de notas =',cantidad_notas)

for nota in notas:
    if nota < 0:
        pass
    else:
        sumatoria += nota
print('sumatoria =', sumatoria)
# Terminado el bucle calcule el promedio como
# promedio = sumatoria / cantidad_notas
promedio = sumatoria / cantidad_notas

print ('promedio=',promedio)
# Utilice la nota promedio calculada y transformela
# a calificación con letras, imprima en pantalla el resultado

if promedio < 60:
    print('Calificación promedio = F')
elif promedio < 70:
    print('Calificación promedio = D')
elif promedio < 80:
    print('Calificación promedio = C')
elif promedio < 90:
    print('Calificación promedio = B')
else:
    print('Calificación promedio = A')

# Imprima en pantalla al cantidad de ausentes
print('cantidad de ausentes =',cantidad_ausentes)
