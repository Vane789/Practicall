from laboratorio import laboratorio
import datetime


consecutivo = 1

def crear_orden(consecutivo, medico):
    paciente = input("Ingrese el nombre del paciente: ")
    numero_orden_medico = input("Ingrese el número de orden del médico: ")

    nueva_orden = {
        "consecutivo": consecutivo,
        "paciente": paciente,
        "medico": medico,
        "fecha_solicitud": datetime.date.today(),
        "fecha_ingreso": datetime.date.today(),
        "numero_orden_medico": numero_orden_medico,
    }
    consecutivo += 1
    
    laboratorio.ordenes.append(nueva_orden)

    print(f"Datos de la orden{nueva_orden} ")
    print(f"Orden Creada y agregada a la lista de órdenes")