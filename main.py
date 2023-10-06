from Metodos.pacientes import *
from Metodos.medicos import *

medico1 = Medico("CC", "123", "Alias Tati", "Cartagena", "23224334", "34355", "Ginecologa", "Carrera45#354")
laboratorio.medicos.append(medico1)

def main():
    while True:
        print(f"""
        --- Bienvenido al sistema de gestión de laboratorio clínico Konoha SAS ---\n
            1. Registrar exámenes \n
            2. Registrar médico \n
            3. Registrar orden \n
            5. Generar factura \n
            6. Salir
            """)

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            validar_paciente()
        elif opcion == "2":
            validar_medico()
        elif opcion == "3":
            pass
            crear_orden()
        elif opcion == "4":
            pass
            # registrar_examen()
        elif opcion == "5":
            pass
            # generar_factura()
        elif opcion == "6":
            pass
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    pass
    main()