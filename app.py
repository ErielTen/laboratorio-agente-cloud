from tasks import agregar_tarea, pendientes


def main(tareas_iniciales=None):
    tareas = list(tareas_iniciales) if tareas_iniciales else []
    while True:
        print("1. Agregar tarea")
        print("2. Ver tareas pendientes")
        print("3. Salir")

        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            titulo = input("Título: ")
            try:
                agregar_tarea(tareas, titulo, "General")
                print("Tarea agregada")
            except ValueError as error:
                print(error)
        elif opcion == "2":
            tareas_pendientes = pendientes(tareas)
            if not tareas_pendientes:
                print("No hay tareas pendientes")
                continue
            for tarea in tareas_pendientes:
                print(f'- {tarea["id"]}: {tarea["titulo"]}')
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
