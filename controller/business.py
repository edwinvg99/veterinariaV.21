from model import model
from datetime import datetime



def iniciar_sesion(username, password,Veterinaria1):

    for Usuarios in Veterinaria1.Usuarios:
            if Usuarios.username == username and Usuarios.password == password:
                Veterinaria1.usuario_actual= Usuarios.rol
                return Usuarios
    return False


def cerrar_sesion():
        usuario_actual = None
        

def registrar_usuario(username, password, rol,Veterinaria1):
    if rol=='Vendedor':
        Vendedor=model.usuario(username,password,"Vendedor")
        Veterinaria1.Usuarios.append(Vendedor)
        print('Vendedor registrado correctamente')
    elif rol=='Veterinario':   
        veterinario=model.usuario(username,password,"veterinario")
        Veterinaria1.Usuarios.append(veterinario)
        print('veterinario registrado correctamente')
    else:
        #Se uso un menu pensando en que el usuario no se vaya a equivocar ingresando el ROL de la persona por lo cual este else no sera muy util 
        print('Por favor intentalo de nuevo')
        exit()   
    
def registrar_Persona(cedula, nombre, edad, Veterinaria1):
    for persona in Veterinaria1.personas:
        if persona.cedula == cedula:
            print("Error: la cédula ya existe en el sistema.")
            return
    
    nuevo_vendedor = model.Persona(cedula, nombre, edad)
    Veterinaria1.personas.append(nuevo_vendedor)
    print(f'{nombre} registrado correctamente')
    print('')
    
    
    print("Por favor, elija el rol de la persona que ingreso")
    print("1. Veterinario")
    print("2. Vendedor")
    print("3. Dueño")

    opcion = input("Escriba el número de su opción: ")

    if opcion == "1":
        rolP = "Veterinario"
    elif opcion == "2":
        rolP = "Vendedor"
    elif opcion == "3":
        pass
    else:
        print("Opción inválida. Por favor, elija una opción del 1 al 3.")
        print('')
        exit()

   
    
    if opcion=='1' or opcion=='2':
        registrar_usuario(input('Ingrese el usuario: '),input('Ingrese la contraseña: '),rolP,Veterinaria1)
        print("")
    else:
        print('')
        print('Gracias por confiar en nosotros')








def registrar_historia_clinica(id_mascota, fecha, medico, motivo_consulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, id_orden, historial_vacunacion, alergias, detalle_procedimiento, Veterinaria1):
# Buscar la mascota por id
    mascota = buscar_mascota_por_id(id_mascota, Veterinaria1)
    mascota_existente = mascota != None

    if not mascota_existente:
        print('La mascota no existe en el sistema')
        return

    # Crear el objeto HistoriaClinica
    historia_clinica = model.HistoriaClinica(id_mascota, fecha,medico, motivo_consulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, id_orden, historial_vacunacion, alergias, detalle_procedimiento)

    # Verificar si ya existe una historia clínica para la mascota en la fecha especificada
    if id_mascota in Veterinaria1.historiasClinicas and fecha in Veterinaria1.historiasClinicas[id_mascota]:
        print(f'Ya existe una historia clínica para la mascota con id {id_mascota} registrada en la fecha {fecha}.')
        return

    # Agregar la historia clínica a la lista correspondiente
    if id_mascota not in Veterinaria1.historiasClinicas:
        Veterinaria1.historiasClinicas[id_mascota] = {}

    Veterinaria1.historiasClinicas[id_mascota][fecha] = historia_clinica
    print('')
    print('Historia registrada con exito')
    print(fecha)




def buscar_historia_clinica(id_mascota, fecha, Veterinaria1):

    print(' ')
    if id_mascota in [mascota.id for mascota in Veterinaria1.mascotas] and fecha in Veterinaria1.historiasClinicas[id_mascota]:
        historia_clinica = Veterinaria1.historiasClinicas[id_mascota][fecha]
        print(f'Historia clínica de la mascota con id {id_mascota} registrada en la fecha {fecha}:')
        print(f'Motivo de consulta: {historia_clinica.motivo_consulta}')
        print(f'Sintomatología: {historia_clinica.sintomatologia}')
        print(f'Diagnóstico: {historia_clinica.diagnostico}')
        print(f'Procedimiento: {historia_clinica.procedimiento}')
        print(f'Medicamento: {historia_clinica.medicamento}')
        print(f'Dosis: {historia_clinica.dosis}')
        print(f'ID de orden: {historia_clinica.id_orden}')
        print(f'Historial de vacunación: {historia_clinica.historial_vacunacion}')
        print(f'Alergias: {historia_clinica.alergias}')
        print(f'Detalle del procedimiento: {historia_clinica.detalle_procedimiento}')
    else: 
        print("La historia clinica no existe")





def registrar_mascota(id, nombre, cedula_dueno, edad, especie, raza, caracteristicas, peso,
Veterinaria1):
    print('Ingreso a metodo registrar mascota')
    # Verificar si la mascota ya existe en el sistema
    for Mascota in Veterinaria1.mascotas:
        if Mascota.id == id :
            print("Error al ingresar la mascota: la mascota ya existe en el sistema.") ###########################
            return
    
    # Verificar si el dueño está registrado en el sistema
    dueno_existente = False
    for persona in Veterinaria1.personas:
        if persona.cedula == cedula_dueno:
            dueno_existente = True
            break

    if not dueno_existente:
        print("El dueño no está registrado en el sistema.")
        return
    
    # Si la mascota no existe y el dueño está registrado, registrar la mascota
    nueva_mascota = model.Mascota(id, nombre, cedula_dueno, edad, especie, raza, caracteristicas, peso)
    Veterinaria1.mascotas.append(nueva_mascota)
    print('____________________________________________')
    print(f"La mascota {nombre} se registró con éxito.")
    print('')
    

def buscar_mascota_por_id(id,Veterinaria1):
        # Buscar la mascota por ID en la lista de mascotas existentes
        print(' ')
        for Mascota in Veterinaria1.mascotas:
            if Mascota.id == id:
                # Imprimir los datos de la mascota
                print("Datos de la mascota:")
                print('')
                print("ID:", Mascota.id)
                print("Nombre:", Mascota.nombre)
                print("Cédula del dueño:", Mascota.cedula_dueno)
                print("Edad:", Mascota.edad)
                print("Especie:", Mascota.especie)
                print("Raza:", Mascota.raza)
                print("Características:", Mascota.caracteristicas)
                print("Peso:", Mascota.peso)
                return Mascota

        # Si no se encuentra la mascota, imprimir un mensaje y devolver None
        print("No se encontró ninguna mascota con el ID proporcionado.")
        return None
    
    
    
    
    
    
    
    
    


def crear_orden(id_orden, id_mascota, cedula_dueno, cedula_veterinario, medicamento, dosis, veterinaria1):
    
    for Orden in veterinaria1.ordenes:
        if Orden.id_orden == id_orden:
            print("La orden ya existe en el sistema")
            return
        
    nueva_orden= model.Orden(id_orden, id_mascota, cedula_dueno,cedula_veterinario,medicamento,dosis)
    veterinaria1.ordenes.append(nueva_orden)
    print('')
    print("La orden se ha registrado correctamente")
    print('')
    
    id_busqueda_orden= id_orden
    
    buscar_ordenID(id_busqueda_orden,veterinaria1)
    
def buscar_ordenID(id_orden, Veterinaria1):
    print('VALIDAR INGRESO AL BUSCAR ORDEN')
    for Orden in Veterinaria1.ordenes:
        if Orden.id_orden == id_orden:
            
            print("Datos de la orden" ,Orden.id_orden)
            print("*************************************")
            print("ID mascota: " ,Orden.id_mascota)
            print("Cedula dueño: " ,Orden.cedula_dueno)
            print("Cedula veterinario: " ,Orden.cedula_veterinario)
            print("Medicamento recetado", Orden.medicamento)
            print("Dosis enviada: ", Orden.dosis)
            print("Orden generada a la fecha: ", Orden.fecha_generacion)
            print("*****************************************************")
        else:
            print("No se encontro una orden con ese ID")
            return None
            
def anular_orden(self, id_orden, id_mascota, id_dueño, id_veterinario):
    # Buscar la orden por su ID
        for orden in self.lista_ordenes:
            if orden.id_orden == id_orden and orden.id_mascota == id_mascota \
                    and orden.id_dueño == id_dueño and orden.id_veterinario == id_veterinario:
                # Cambiar el estado de la orden a "Anulada" y registrar la fecha de anulación
                orden.estado = "Anulada"
                orden.fecha_anulacion = datetime.now()

                # Buscar la historia clínica correspondiente y agregar un registro de anulación de la orden
                for mascota in self.lista_mascotas:
                    if mascota.id == id_mascota and mascota.cedula_dueño == id_dueño:
                        if id_mascota in self.historias_clinicas:
                            historia = self.historias_clinicas[id_mascota]
                        else:
                            historia = {}
                            self.historias_clinicas[id_mascota] = historia
                        registro = {
                            "fecha": datetime.now(),
                            "medico_veterinario": id_veterinario,
                            "motivo_consulta": "Anulación de orden de venta",
                            "sintomatologia": "",
                            "diagnostico": "",
                            "procedimiento": "",
                            "medicamento": "",
                            "dosis_medicamento": "",
                            "id_orden": id_orden,
                            "historial_vacunacion": "",
                            "alergias_medicamentos": "",
                            "detalle_procedimiento": "",
                            "anulacion_orden": True
                        }
                        historia[registro["fecha"]] = registro
                print("La orden ha sido anulada con éxito.")
                return
        print("No se encontró la orden con los datos proporcionados.")





def registrar_factura_venta(id_factura,id_orden, nombre_producto, valor, cantidad, Veterinaria1):
  #  orden_objeto=model.Orden()
    
    #for FacturaVenta in Veterinaria1.ordenes:
        if id_orden in [Orden.id_orden for Orden in Veterinaria1.ordenes]:
            factura_nueva= model.FacturaVenta(id_factura,id_orden, nombre_producto,valor,cantidad)
            Veterinaria1.facturas_ventas.append(factura_nueva)
            
            print("Se ha registrado  la factura")
            
            id_busqueda_factura= id_orden
    
            buscar_ordenID(id_busqueda_factura,Veterinaria1)
        else:
               
         print("la orden no existe en el sistema")

def consultar_facturas_ventas(id_orden, veterinaria1):
    for FacturaVenta in veterinaria1.facturas_ventas:
        if FacturaVenta.id_orden == id_orden:
            print("******************************************")
            print("Datos de la factura" , FacturaVenta.id_factura)
            print("*************************************")
            print("orden asociada NO. : " ,FacturaVenta.id_orden)
            print("Nombre del medicamento: " ,FacturaVenta.nombre_producto)
            print("precio por unidad: " ,FacturaVenta.valor)
            print("Cantidad a llevar", FacturaVenta.cantidad)
            
            print("*****************************************************")


