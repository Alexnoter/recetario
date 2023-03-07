import os
from pathlib import Path
from os import system


mi_ruta = Path(Path.home(),"Recetas")

def contar_receta(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

#mostrar menu inicio
def inicio():
    system('cls')
    print('*'*50)
    print('*'*5+" BIENBENIDO AL ADMINISTRADOR DE RECETAS "+'*'*5)
    print('*'*50+'\n')

    print(f'las recetas se encuentran en {mi_ruta}')
    print(f'total recetas: {contar_receta(mi_ruta)}')

    eleccion_menu = 'x'
    #isnumeric() nos devuelve true si es numerico
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion: ")
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria Nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa''')
        eleccion_menu = input()
    return eleccion_menu


inicio()

menu = 0

if menu == 1:
    #mostrar categorias
    #elegir categoria
    #mostrar receeta
    #elegir  receta
    #leer receta
    #volver inicio
    pass
elif menu == 2:
    # mostrar categorias
    # elegir categoria
    #crear receta
    #volver inicio
    pass
elif menu == 3:
    #crear categoria
    #volver al inicio
    pass
elif menu == 4:
    # mostrar categorias
    # elegir categoria
    # mostrar receeta
    # elegir  receta
    # eliminar receta
    # volver inicio
    pass
elif menu == 5:
    # mostrar categorias
    # elegir categoria
    #eliminar categorias
    #volver inicio
    pass
elif menu == 6:
    #finalizar programa
    pass
