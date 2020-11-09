#Flask es un framework minimalista escrito en Python que permite crear aplicaciones 
# web rápidamente y con un mínimo número de líneas de código. 
#Jsonifi para convertir array en Json
#Request para poder recibir info, creo 
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from Usuarios import Usuario
from Clientes import Cliente




#Variable = Flask(__name__) esto debe de ir siempre, el app puede ser cualquier nombre
app = Flask(__name__)

#CORS(variable) habilita los CORS es para el FrontEnd
CORS(app)


#Variable = [] significa que estamos declarando una lista
#Si quisieramos declarar un arreglo usamos {}
#Usuarios = []


# Esto es para generar rutas----------
# El '/' es el URL
# Un LRU o localizador de recursos uniforme ​ es un identificador  
# de recursos uniforme cuyos recursos referidos pueden cambiar.
# https://es.wikipedia.org/wiki/Flask <--  ejemplo flask


# Creando una lista de usuarios, ESTE ES GLOBAL
Clientes = []


#APPEND agrega un elemento en la última posición del arreglo
Clientes.append(Cliente("Jose", "Martinez", "jOSE396.3", 1234, 1234))
Clientes.append(Cliente("lUIS", "Mar", "lUISITO", 1234, 1234))
Clientes.append(Cliente("Fer", "Perez", "fETRCHO", 12345, 12345))
Clientes.append(Cliente("Mario", "DO", "mAMMAA", 12346, 12346))
Clientes.append(Cliente("Marte", "EDz", "martes", 12346, 12346))
Clientes.append(Cliente("Julia", "DDDDez", "j3", 12346, 12346))







@app.route('/', methods=['GET'])
def rutaInicial():

    print("hola mundo")
    # El return me va a devolver la respuesta donde esté consumiendo la API, en 
    # este caso la estoy consumuendo en un navegador.
    # Una API es una interfaz de programación de aplicaciones 
    return("hola estudiantes")

#-------------------------------------

@app.route('/Usuarios', methods=['GET'])
def rutaUsuarios():

    nueva = Usuario('Byron', 'Apellido', 'Byron7h', 123, 123)

    print("hola mundo")
    return(nueva.getNombre())
    
#-----------------------------------ObtenerClientes-----------------------------------------------------------
@app.route('/Clientes', methods=['GET'])
def obtenerClientes():

    #cUANDO SE TRABAJA CON UNA VARIABLE GLOBAL, SE COLOCA GLOBAL
    global Clientes
    Datos = []
    #Con el for recorremos cada posición de mi lista
    for cliente in Clientes:

        #Un JSON recibe arreglos
        # Construyo un ibjeto de tipo dato conla estructura de un JSON, para después guardarlo en mi arreglo de datos
        Dato = {
        'nombre': cliente.getNombre(), 
        'apellido': cliente.getApellido(), 
        'usuario': cliente.getUsuario(), 
        'contra': cliente.getContra(), 
        'con_contra': cliente.getCon_contra()
        }
        Datos.append(Dato)
        #Acá vamosa usar la librería jsonify del flask para converir el arreglo en Json

    respuesta =jsonify(Datos)
    return(respuesta)

#-------------------------------AgregarCliente----------------------------------------------------------------
#Misma ruta, diferente método
@app.route('/Clientes/', methods=['POST'])
def AgregarCliente():


    #cUANDO SE TRABAJA CON UNA VARIABLE GLOBAL, SE COLOCA GLOBAL
    global Clientes

    nuevo = Cliente(request.json['nombre'], request.json['apellido'], request.json['usuario'], request.json['contra'], request.json['con_contra'])

    Clientes.append(nuevo)
    return("Se agregó un cliente")

#-----------------------------Consulta individual de Cliente------------------------------------------------------------------

# Misma ruta, diferente método

# ACA Le estoy diciendo mirá, vas a recibir un dato string y lo vas a guardar en la variable nombre
# Usamos de nuevo Get

@app.route('/Clientes/<string:usuario>', methods=['GET'])
# la varible que recibimos la agregamos como parámetro
def Obtener_Cliente_Individual(usuario):

    global Clientes
    Datos = []
    for Cliente in Clientes:
        if Cliente.getUsuario() == usuario:
            Dato = {
                'nombre': Cliente.getNombre(), 
                'apellido': Cliente.getApellido(), 
                'usuario': Cliente.getUsuario(), 
                'contra': Cliente.getContra(), 
                'con_contra': Cliente.getCon_contra()
                }
            Datos.append(Dato)
            break 

    respuesta = jsonify(Datos)   
    return(respuesta)


#----------------------------------modificar Cliente----------------------------------------------------
# lo de string quiere decir que se va a obtener ese dato del arreglo, solo(creo)
@app.route('/Clientes/<string:usuario>', methods=['PUT'])
# la varible que recibimos la agregamos como parámetro
# debe ser la misma del String
def ActualizarCliente(usuario):

    global Clientes

    #Otra forma de recorrer un arreglo, Desde 0 hasta como el .lenght de java
    # range da una sucesión de numeros desde 0 hasta el .length

    #vamos a rrecorrer el arreglo, y si encuentra el usuario va a hacer la actualización con lo que le enviemos
    for i in range(len(Clientes)):
        if usuario == Clientes[i].getUsuario():

            #Como lo creamos como en java, le cemos la posición y le mandamos lo que queremos
            # Como lo mandamos con un json, Debemos poner "el nombre dela categoría"
            
            
            #Aprovechando que ya tenmos un JSON lo mandamos directo
            # por eso usamos un request.json --> Como lo que teniamos en Postman, lo que va dentro de corchetes es lo de la primera columna
            #Por lo que deben ser los mismos nombres de las variables
            
            Clientes[i].setNombre(request.json['nombre'])
            Clientes[i].setApellido(request.json['apellido'])
            Clientes[i].setUsuario(request.json['usuario'])
            Clientes[i].setContra(request.json['contra'])
            Clientes[i].setCon_contra(request.json['con_contra'])

            break 
    return jsonify({'message':'Se actualizó el dato exitosamente'})



#---------------------------------------Eliminar Cliente------------------------------------------------
@app.route('/Clientes/<string:usuario>', methods=['DELETE'])
# la varible que recibimos la agregamos como parámetro
def Eliminar_cliente(usuario):

    global Clientes

    for i in range(len(Clientes)):
        if usuario == Clientes[i].getUsuario():

            #del lo que hace es borrar un objeto como tal
            del Clientes[i]

    return jsonify({'message':'Se eliminó el dato exitosamente'})























if __name__ == "__main__":
    app.run(port=3000, debug=True)