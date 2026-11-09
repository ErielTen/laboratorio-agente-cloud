import unittest
from tasks import agregar_tarea, completar_tarea, pendientes

class TestTasks(unittest.TestCase):
    
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación", "Estudio")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertEqual(tarea["categoria"], "Estudio")
        self.assertFalse(tarea["completada"])

    def test_agregar_tarea_categoria_vacia(self):
        tareas = []
        with self.assertRaises(ValueError):
            agregar_tarea(tareas, "Leer documentación", "   ")
        
    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Estudio")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_pendientes_filtra_por_categoria_sin_case_sensitive(self):
        tareas = []
        agregar_tarea(tareas, "Leer documentación", "Estudio")
        agregar_tarea(tareas, "Implementar feature", "Trabajo")
        agregar_tarea(tareas, "Repasar apuntes", "estudio")
        completar_tarea(tareas, 3)

        filtradas = pendientes(tareas, "ESTUDIO")
        self.assertEqual(len(filtradas), 1)
        self.assertEqual(filtradas[0]["titulo"], "Leer documentación")
        self.assertEqual(pendientes(tareas, "Inexistente"), [])
        self.assertEqual(pendientes(tareas, "   "), [])

if __name__ == '__main__':
    unittest.main()
