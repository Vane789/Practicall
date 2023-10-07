from Metodos.pacientes import *
from Metodos.medicos import *
from Metodos.examenes import *
from Metodos.ordenes import *

# Datos medicos
medico1 = Medico("CC", "123", "Alias Tati", "Cartagena", "23224334", "34355", "Ginecologa", "Carrera55#354")
medico2 = Medico("CC", "234", "Alias Andres", "Sernita", "45325", "34", "Neurologo", "Carrera45#354")
medico3 = Medico("CC", "456", "Alias Vanessa", "Cardona", "7675", "3433255", "Optamologa", "Carrer56#354")
laboratorio.medicos.append(medico1)
laboratorio.medicos.append(medico2)
laboratorio.medicos.append(medico3)

# Datos Examenes
examen1 = Examen("Hemograma","20-04-2026","14-02-2002","hola","100000")
examen2 = Examen("Colesterol","22-04-2026","15-03-2004","hola2", "200000")
examen3 = Examen("Glucosa","12-04-2026","16-03-2004","hola3" ,"300000")

laboratorio.examenes.append(examen1)
laboratorio.examenes.append(examen2)
laboratorio.examenes.append(examen3)


def main():
    while True:
        print(f"""
        --- Bienvenido al sistema de gestión de laboratorio clínico Konoha SAS ---\n
            1. Registrar orden \n
            2. Registrar examenes \n
            3. Registrar medico \n
            5. Generar factura \n
            6. Salir
            """)

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            crear_orden()
        elif opcion == "2":
            Paciente.validar_informacion()
        elif opcion == "3":
            Medico.validar_informacion()
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
    main()