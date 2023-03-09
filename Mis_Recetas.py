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


def mostrar_categoria(ruta):
    print("Categorias: ")
    ruta_categoria = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categoria.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias


def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista)+1):
        eleccion_correcta  = input("\n Elige una categoria: ")

    return lista[int(eleccion_correcta)-1]

def mostrar_receta(ruta):
    print("Recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1

    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = 'x'
    while not eleccion_receta.isnumeric() or  int(eleccion_receta) not in range(1, len(lista)+1):
        eleccion_receta = input("\n elige una receta: ")

    return lista[int(eleccion_receta)-1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta")
        nombre_receta = input() +'.txt'
        print("Escribe tu receta")
        contenido_receta = input()
        ruta_nueva = Path(ruta,nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("lo siento esa receta ya existe")

def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoria")
        nombre_categoria = input()

        ruta_nueva = Path(ruta,nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"tu categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("lo siento esa categoria ya existe")

def eliminar_receta(receta):
    #unlink es el metodo para eliminar un archivo
    Path(receta).unlink()
    print(f"la receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"la categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresar =  'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\n presione V para volver al menu: ")

menu = 0

if menu == 1:
    #mostrar categorias
    mis_categorias = mostrar_categoria(mi_ruta)

    #elegir categoria
    mi_categoria = elegir_categoria(mis_categorias)

    #mostrar receeta
    mis_recetas = mostrar_receta(mi_categoria)

    #elegir  receta
    mi_receta =elegir_recetas(mis_recetas)

    #leer receta
    leer_receta(mi_receta)

    #volver inicio
    volver_inicio()

    
elif menu == 2:
    # mostrar categorias
    mis_categorias = mostrar_categoria(mi_ruta)

    # elegir categoria
    mi_categoria = elegir_categoria(mis_categorias)

    #crear receta
    crear_receta(mi_categoria)
    
    #volver inicio
    volver_inicio()


elif menu == 3:
    #crear categoria
    crear_categoria(mi_ruta)

    #volver al inicio
    volver_inicio()


elif menu == 4:
    # mostrar categorias
    mis_categorias = mostrar_categoria(mi_ruta)

    # elegir categoria
    mi_categoria = elegir_categoria(mis_categorias)

    # mostrar receeta
    mis_recetas = mostrar_receta(mis_categorias)

    # elegir  receta
    mi_receta = elegir_recetas(mis_recetas)

    # eliminar receta
    eliminar_receta(mi_receta)

    # volver inicio
    volver_inicio()


elif menu == 5:
    # mostrar categorias
    mis_categorias = mostrar_categoria(mi_ruta)
    
    # elegir categoria
    mi_categoria = elegir_categoria(mis_categorias)

    #eliminar categorias
    eliminar_categoria(mi_categoria)

    #volver inicio
    volver_inicio()


elif menu == 6:
    #finalizar programa

