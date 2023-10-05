from persona import Persona


pacientes = []
medicos = []

def main():
    while True:
        print(f"""
        --- Bienvenido al sistema de gestión de laboratorio clínico Konoha SAS ---\n
            1. Registrar paciente \n
            2. Registrar médico \n
            3. Registrar orden \n
            4. Registrar examen \n
            5. Generar factura \n
            6. Salir
            """)

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            pass
            # registrar_paciente()
        elif opcion == "2":
            pass
            # registrar_medico()
        elif opcion == "3":
            pass
            # registrar_orden()
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

# Ejecuta la función main() si este archivo es el punto de entrada
if __name__ == "__main__":
    main()
