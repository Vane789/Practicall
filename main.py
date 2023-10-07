from Metodos.pacientes import *
from Metodos.examenes import *
from Metodos.ordenes import *
from Metodos.medicos import *

# Datos medicos
medico1 = Medico("CC", "123", "Tati", "Cartagena", "23224334", "34355", "Ginecologa", "Carrera55#354")
medico2 = Medico("CC", "234", "Andres", "Sernita", "45325", "34", "Neurologo", "Carrera45#354")
medico3 = Medico("CC", "456", "Vanessa", "Cardona", "7675", "3433255", "Optamologa", "Carrer56#354")


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
            1. Registrar orden y examen \n
            2. Registrar medico \n
            3. Ver todos los paciente \n
            4. Ver las ordenes de un paciente \n
            5. Salir
            """)

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            validar_informacion()
        elif opcion == "2":
            crear_medico()
        elif opcion == "3":
            ver_todos_pacientes()
        elif opcion == "4":
            pass
            ver_ordenes_paciente()    
        elif opcion == "5":
            pass
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()