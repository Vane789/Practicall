from laboratorio import laboratorio
from Modelos.examen import Examen
from datetime import datetime
from Modelos.paciente import Paciente

def crear_examenes(examenes):
    print("""
        -------------------------------------------------------
                        [ REGISTRAR EXAMENES ]
        -------------------------------------------------------
        """)
        
    cantidad_examenes = int(input("Cantidad de exámenes que requiere el paciente: "))
    print("""Lista de examenes""")
    for examen in laboratorio.examenes:
        print(f"Tipo de examen: {examen.get_tipo_de_examen()} Valor: {examen.get_valor()}")
        
    for i in range(cantidad_examenes):
        tipo_examen = input(f"\nExamen {i + 1}: ")
        encontrado = False
        valor = ""
        
        fecha_cita = input("Ingrese la fecha de la cita: ")
        fecha_realizacion_examen = input("Ingrese la fecha de realización del examen: ")
        observacion = input("Ingrese la observacion: ")
        
        for examen in laboratorio.examenes:
            if tipo_examen == examen.get_tipo_de_examen():
                valor = examen.get_valor()
                encontrado = True
                break

        nuevo_examen = Examen(
           tipo_examen,
           fecha_cita,
           fecha_realizacion_examen,
           observacion,
            valor,
        )
        examenes.append(nuevo_examen)
        print("---" * 20)
        print("Examen guardado con los siguientes datos:")
        examenes[i].mostrar_datos()
        print("---" * 20)
