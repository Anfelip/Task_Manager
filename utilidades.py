import json
from rich.console import Console
from rich.table import Table

console = Console()

def cargar_tareas():
    with open("Tareas.json","r", encoding="utf-8") as archivo_tareas:
        tareas = json.load(archivo_tareas)
    return(tareas)

def guardar_tareas(tareas):
    with open("Tareas.json", "w", encoding="utf-8") as archivo_tareas:
        json.dump(tareas, archivo_tareas,indent=4, ensure_ascii=False)

def obtener_tareas(tareas):
    if not tareas:
        Console.print("[yellow]No hay tareas registradas.[/yellow]")
        return

    tabla = Table(title="Mis tareas", title_style="bold cyan")
    tabla.add_column("ID", justify="center", style="cyan", no_wrap=True)
    tabla.add_column("Descripción", style="white")
    tabla.add_column("Estado", justify="center")
    
    for tarea in tareas:
        estado = "[green]✔ Completada[/green]" if tarea["completada"] else "[red]✘ Pendiente[/red]"
        tabla.add_row(str(tarea["id"]), tarea["descripcion"], estado)

    console.print(tabla)

def crear_tarea(tareas, nombre, completada):
    nuevo_id = max((tarea["id"] for tarea in tareas), default=0)+1
    nueva_tarea = {
        "id": nuevo_id,
        "descripcion": nombre,
        "completada": completada,
    }
    return(nueva_tarea)

def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto and any(c.isalpha() for c in texto):
            return texto
        else:
            print("Ingrese un texto valido, sin numeros.")

def buscar_tarea(tareas, id_tarea):
    for t in tareas:
        if t["id"] == id_tarea:
            return t
    return None

def marcar_completado(tareas, id_tarea):
    tarea = buscar_tarea(tareas, id_tarea)
    if tarea is None:
        return False
    tarea["completada"] = True
    guardar_tareas(tareas)
    return True

def marcar_incompleto(tareas, id_tarea):
    tarea = buscar_tarea(tareas, id_tarea)
    if tarea is None:
        return False
    tarea["completada"] = False
    guardar_tareas(tareas)
    return True

def modificar_descripcion(tareas, id_tarea, mensaje):
    tarea = buscar_tarea(tareas, id_tarea)
    if tarea is None:
        return False
    tarea["descripcion"] = mensaje
    guardar_tareas(tareas)
    return True

def eliminar_tarea(tareas, id_tarea):
    tarea = buscar_tarea(tareas, id_tarea)
    if tarea is None:
        return False
    tareas.remove(tarea)
    guardar_tareas(tareas)
    return True
def verifica_id(tareas, mensaje):
    while True:
        try:
            obtener_tareas(tareas)
            id_tarea = int(input(mensaje))
            ids = [t["id"] for t in tareas]
            if id_tarea in ids:
                return id_tarea
            else:
                print("El id no existe")
        except ValueError:
            print("Introduzca un id valido")
