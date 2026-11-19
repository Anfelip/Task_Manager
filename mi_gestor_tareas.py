import utilidades

""" funcion que almacena el flujo de funcionamiento de la aplicacion """
def init():
    tareas = utilidades.cargar_tareas()
    print("Menú inicial")
    print("1. Agregar tarea\n2. Contar tareas pendientes\n3. Ver tareas\n4. Marcar tarea completada\n5. Marcar tarea incompleta\n6. Modificar descripcion\n7. Eliminar tarea\n0. Salir")

    while True:
        try:
            menu_inicio = int(input("Que desea hacer?: "))
            if 0<=menu_inicio<=7:
                break
            else:
                print('Ingrese un numero entre 0 y 7')
        except ValueError:
            print("Opcion no valida")
        

    """ Agrega una nueva tarea """
    if menu_inicio == 1:
        descripcion = utilidades.validar_texto("Ingrese la descripcion de la tarea: ")
        nueva_tarea = utilidades.crear_tarea(tareas, descripcion, False)
        tareas.append(nueva_tarea)
        utilidades.guardar_tareas(tareas)

    #Se cuentan las tareas faltantes
    elif menu_inicio == 2:
        print(f"Tienes {utilidades.contar_tareas_pendientes(tareas)} tareas incompletas")

    #Se listan las tareas
    elif menu_inicio == 3:
        if tareas:
            utilidades.obtener_tareas(tareas)
        else:
            print("No hay tareas creadas")

    #Se marca completado una tarea
    elif menu_inicio == 4:
        id_tarea = utilidades.verifica_id(tareas, "Introduzca el Id a modificar: ")
        utilidades.marcar_completado(tareas, id_tarea)
        print("Tarea modificada con exito")

    #Se marca incompleta una tarea
    elif menu_inicio == 5:
        id_tarea = utilidades.verifica_id(tareas, "Introduzca el Id a modificar: ")
        utilidades.marcar_incompleto(tareas, id_tarea)
        print("Tarea modificada con exito")

    #Se modifica la descripcion de una tarea
    elif menu_inicio == 6:
        nueva_descripcion = utilidades.validar_texto("Introduzca la nueva descripcion: ")
        id_tarea = utilidades.verifica_id(tareas, "Introduzca el Id a modificar: ")
        utilidades.modificar_descripcion(tareas, id_tarea, nueva_descripcion)
        print("Tarea modificada con exito")

    #Se elimina una tarea
    elif menu_inicio == 7:
        id_tarea = utilidades.verifica_id(tareas, "Introduzca el Id a modificar: ")
        utilidades.eliminar_tarea(tareas, id_tarea)
        print("Tarea modificada con exito")

init()