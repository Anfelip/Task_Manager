import utilidades

def init():
    tareas = utilidades.cargar_tareas()
    print("Menú inicial")
    print("1. Agregar tarea\n2. Ver tareas\n3. Marcar tarea completada\n4. Marcar tarea incompleta\n5. Modificar descripcion\n6. Eliminar tarea\n0. Salir")

    while True:
        try:
            menu_inicio = int(input("Que desea hacer?: "))
            if 0<=menu_inicio<=6:
                break
            else:
                print('Ingrese un numero entre 0 y 6')
        except ValueError:
            print("Opcion no valida")
        
    
    if menu_inicio == 1:
        descripcion = utilidades.validar_texto("Ingrese la descripcion de la tarea: ")
        nueva_tarea = utilidades.crear_tarea(tareas, descripcion, False)
        tareas.append(nueva_tarea)
        utilidades.guardar_tareas(tareas)

    elif menu_inicio == 2:
        if tareas:
            utilidades.obtener_tareas(tareas)
        else:
            print("No hay tareas creadas")

    elif menu_inicio == 3:
        id_tarea = utilidades.verifica_id(tareas, "Introduzca el Id a modificar: ")
        utilidades.marcar_completado(tareas, id_tarea)
        print("Tarea modificada con exito")

    elif menu_inicio == 4:
        id_tarea = utilidades.verifica_id(tareas, "Introduzca el Id a modificar: ")
        utilidades.marcar_incompleto(tareas, id_tarea)
        print("Tarea modificada con exito")

    elif menu_inicio == 5:
        nueva_descripcion = utilidades.validar_texto("Introduzca la nueva descripcion: ")
        id_tarea = utilidades.verifica_id(tareas, "Introduzca el Id a modificar: ")
        utilidades.modificar_descripcion(tareas, id_tarea, nueva_descripcion)
        print("Tarea modificada con exito")

    elif menu_inicio == 6:
        id_tarea = utilidades.verifica_id(tareas, "Introduzca el Id a modificar: ")
        utilidades.eliminar_tarea(tareas, id_tarea)
        print("Tarea modificada con exito")
    

init()