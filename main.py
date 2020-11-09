#Flask es un framework minimalista escrito en Python que permite crear aplicaciones 
# web rápidamente y con un mínimo número de líneas de código. 

#Jsonifi para convertir array en Json
#Request para poder recibir info, creo 

from flask import Flask, jsonify, request
from flask_cors import CORS
import json

# Importando // from NOMBRE_ARCHIVO import NOMBRE_CLASE
from Clientes import Cliente
from Canciones import Cancion
from Solicitudes import Solicitud
from Administradores import Administrador
from Playlists import Playlist

#Variable = Flask(__name__) esto debe de ir siempre, el app puede ser cualquier nombre
app = Flask(__name__)

#CORS(variable) habilita los CORS es para el FrontEnd
CORS(app)


#Variable = [] significa que estamos declarando una lista
#Si quisieramos declarar un arreglo usamos {}
#Usuarios = []


# Creando una lista de usuarios, ESTE ES GLOBAL
# CREAMOS ARREGLOS PORQUE ESTAMOS UTILIZANDO LA MEMORIA DE PYTHON Y NO UNA BASE DE DATOS

Clientes = []
Administradores = []
Canciones = []
Solicitudes = []
Playlists=[]
#Agregando Admin Maestro
Administradores.append(Administrador('Usuario','Maestro','admin','admin'))
# Vamoa implementar un contador único para cada canción, forma easy --> un contador xd
id_canciones = 0
id_solicitudes = 0

#-------------------------------AgregarCliente----------------------------------------------------------------


#Misma ruta, diferente método     ID--> Nombre de usuario

#POST --> Crear
@app.route('/Clientes', methods=['POST'])
def AgregarCliente():


    #cUANDO SE TRABAJA CON UNA VARIABLE GLOBAL, SE COLOCA GLOBAL
    global Clientes
    global Playlists



    nombre = request.json['nombre']
    apellido = request.json['apellido']
    usuario = request.json['usuario']
    contra = request.json['contra']
    contra_2 = request.json['contra_2']


    #Variables bolleanas
    encontrado_cliente = False
    encontrado_admin = False

    #Verificaciones: Usuario no registrado, contraseñas iguales
    
    for i in range(len(Clientes)):
        if usuario == Clientes[i].getUsuario():
            encontrado_cliente = True
            
            break

    for i in range(len(Administradores)):
        if usuario == Administradores[i].getUsuario():
            encontrado_admin = True
            
            break
    
    if encontrado_cliente:
        return jsonify({

            'message': 'Failed',
            'reason': 'El usuario ya está en uso'
        })

    elif encontrado_admin:

        return jsonify({
            'message': 'Failed',
            'reason': 'El usuario ya está en uso'
        })


    else:

        if contra == contra_2:

            nuevo = Cliente(nombre, apellido, usuario, contra)
            #APPEND agrega un elemento en la última posición del arreglo
            Clientes.append(nuevo)

            id = usuario
            arreglo = []
            nuevo = Playlist (id, arreglo)
            Playlists.append(nuevo)


            return jsonify({
                'message':'Success',
                'reason':'Se ha creado el usuario'
                
                })

        else:
            return jsonify({
                'message':'Failedx2',
                'reason':'Las contraseñas no coinciden'
            }) 




#------------------------------------INGRESAR AL SISTEMA------------------------------------------------


@app.route('/Login', methods=['POST'])
def Login():

    global Clientes
    usuario = request.json['usuario']
    contra = request.json['contra']

     #Variables bolleanas
    encontrado_cliente = False
    encontrado_admin = False

    
    for i in range(len(Clientes)):
        if usuario == Clientes[i].getUsuario() and contra == Clientes[i].getContra():
            encontrado_cliente = True
            break

    for e in range(len(Administradores)):
        if usuario == Administradores[e].getUsuario() and contra == Administradores[e].getContra() :
            encontrado_admin = True
            break

    if encontrado_cliente:

        Dato ={
            
            'message': 'Success',
            'type':'Cliente'
        }

    elif encontrado_admin:

        Dato = {     
            'message': 'Success',
            'type':'Admin'
        }

    else:

        Dato = { 
            'message': 'Failed'
        }

    respuesta = jsonify(Dato)
    return (respuesta)

        

#--------------------------------------Recuperar contraseña --------------------------------------------


@app.route('/Recuperar/<string:usuario>', methods=['GET'])
def Recuperar_contrasena(usuario):

    global Clientes

     #Variables bolleanas
    encontrado_cliente = False
    encontrado_admin = False

    
    for i in range(len(Clientes)):
        if usuario == Clientes[i].getUsuario():
            encontrado_cliente = True
            
            break

    for e in range(len(Administradores)):
        if usuario == Administradores[e].getUsuario():
            encontrado_admin = True
            
            break


    if encontrado_cliente:

        Dato ={
            
            'message': 'Success',
            'contra': Clientes[i].getContra()
        }

    elif encontrado_admin:

        Dato ={
            
            'message': 'Success',
            'contra': Administradores[e].getContra()
        }

    else:

        Dato ={
            
            'message': 'Failed',
            'reason': 'No se encontró el usuario'
        }

    respuesta = jsonify(Dato)
    return (respuesta)


    




#--------------------------------------Mostrar Usuarios registrados --------------------------------------------


@app.route('/Clientes_Registrados', methods=['GET'])
#Queremos que en esta ruta nos devuelva los datos de las personas
def obtenerClientes():
    #Usamos la variable global para usar una variable declarada en el ambito global
    global Clientes
    global Administradores
    Datos = []
    #Los for se pueden trabajar como un for each, es decir un objeto dentro de los objetos

    for i in range(len(Administradores)):
        
        Dato = {
            'tipo': "Admin",
            'nombre': Administradores[i].getNombre(),
            'apellido' : Administradores[i].getApellido(), 
            'usuario' : Administradores[i].getUsuario(), 
            'contra' : Administradores[i].getContra()
            }
        Datos.append(Dato)

    for i in range(len(Clientes)):
        
        Dato = {
            'tipo': "Cliente",
            'nombre': Clientes[i].getNombre(),
            'apellido' : Clientes[i].getApellido(), 
            'usuario' : Clientes[i].getUsuario(), 
            'contra' : Clientes[i].getContra()
            }
        Datos.append(Dato)
    
    #En este caso usamos jsonify para convertir nuestro arreglo en un objeto JSON
    #Para que sea reconocible en el navegador y tengamos la respuesta no como 
    #un arreglo, si no como un objeto JSON
    respuesta = jsonify(Datos)
    return(respuesta)



#--------------------------------------Mostrar Usuario idividual --------------------------------------------

@app.route('/Obtener_Usuario/<string:usuario>', methods=['GET'])
def Obtener_Usario(usuario):

    global Clientes
    global Administradores

     #Variables bolleanas
    encontrado_cliente = False
    encontrado_admin = False

    
    for i in range(len(Clientes)):
        if usuario == Clientes[i].getUsuario():
            encontrado_cliente = True
            
            break

    for e in range(len(Administradores)):
        if usuario == Administradores[e].getUsuario():
            encontrado_admin = True
            
            break


    if encontrado_cliente:

        Dato ={
            
            'message': 'Cliente',
            
            'nombre': Clientes[i].getNombre(),
            'apellido' : Clientes[i].getApellido(), 
            'usuario' : Clientes[i].getUsuario(), 
            'contra' : Clientes[i].getContra()
        }

    elif encontrado_admin:

        Dato ={
            
            'message': 'Administrador',
            'nombre': Administradores[e].getNombre(),
            'apellido' : Administradores[e].getApellido(), 
            'usuario' : Administradores[e].getUsuario(), 
            'contra' : Administradores[e].getContra()
        }

    else:

        Dato ={
            
            'message': 'Failed',
            'reason': 'No se encontró el usuario'
        }

    respuesta = jsonify(Dato)
    return (respuesta)




#--------------------------------------Actualizar Usuario --------------------------------------------


@app.route('/Usuarios/<string:usuario>', methods=['PUT'])
def ActualizarUsuario(usuario):

    global Clientes
    global Administradores
    global Playlists 
    #Otra forma de usar el for es como la manera tradicional
    #Con un indice y para eso utilizamos el range(numero)
    #Donde dara el rango de numeros desde 0 hasta el numero enviado como parametro
     #Variables bolleanas
    encontrado_cliente = False
    encontrado_admin = False

    prueba_igualdad = False
    prueba_existencia = True




    for i in range(len(Clientes)):
        if usuario == Clientes[i].getUsuario():
            encontrado_cliente = True
            if request.json['usuario'] == Clientes[i].getUsuario():
                prueba_igualdad = True

            
            break

    for e in range(len(Administradores)):
        if usuario == Administradores[e].getUsuario():
            encontrado_admin = True
            if request.json['usuario'] == Administradores[e].getUsuario():
                prueba_igualdad = True
            
            break

    
    if prueba_igualdad:

        if encontrado_cliente:
        

            Clientes[i].setNombre(request.json['nombre'])
            Clientes[i].setApellido(request.json['apellido'])
            Clientes[i].setUsuario(request.json['usuario'])
            Clientes[i].setContra(request.json['contra'])

            Dato ={ 
                'message': 'Success',
                'reason': 'Se actualizó el cliente',
            }

        elif encontrado_admin:

            Administradores[e].setNombre(request.json['nombre'])
            Administradores[e].setApellido(request.json['apellido'])
            Administradores[e].setUsuario(request.json['usuario'])
            Administradores[e].setContra(request.json['contra'])

            Dato ={
                'message': 'Success',
                'reason':'Se actualizó el Administrador',
            }

        else:

            Dato ={         
                'message': 'Failed',
            }

    else:


        for o in range(len(Clientes)):
            if request.json['usuario'] == Clientes[o].getUsuario():
                prueba_existencia = False
            
                break

        for u in range(len(Administradores)):
            if request.json['usuario'] == Administradores[u].getUsuario():
                prueba_existencia = False
            
                break

        if prueba_existencia:

            if encontrado_cliente:
        

                Clientes[i].setNombre(request.json['nombre'])
                Clientes[i].setApellido(request.json['apellido'])
                Clientes[i].setUsuario(request.json['usuario'])
                Clientes[i].setContra(request.json['contra'])

                Dato ={ 
                    'message': 'Success',
                    'reason': 'Se actualizó el cliente'
                }

                encontrada_playlist = False
                nuevo_id = request.json['usuario']

                for i in range(len(Playlists)):
                    if usuario == Playlists[i].getId():
                        encontrada_playlist = True         
                        break

    
                if encontrada_playlist:
                    Playlists[i].setId(nuevo_id)



            elif encontrado_admin:

                Administradores[e].setNombre(request.json['nombre'])
                Administradores[e].setApellido(request.json['apellido'])
                Administradores[e].setUsuario(request.json['usuario'])
                Administradores[e].setContra(request.json['contra'])

                Dato ={
                    'message': 'Success',
                    'reason':'Se actualizó el Administrador'
                }

            else:

                Dato ={         
                    'message': 'Failed',
                    'reason':'No se encontró el usuario'                 
                }

        else :
            Dato ={           
                'message': 'Failed',
                'reason': 'El usuario ya está en uso'
            }
    respuesta = jsonify(Dato)
    return (respuesta)


#--------------------------------------Eliminar usuario --------------------------------------------


@app.route('/Eliminar/<string:usuario>', methods=['DELETE'])
def EliminarUsuario(usuario):
    

    global Clientes
    global Administradores

    encontrado_cliente = False
    encontrado_admin = False

    for i in range(len(Clientes)):
        if usuario == Clientes[i].getUsuario():
            encontrado_cliente = True
            
            break

    for e in range(len(Administradores)):
        if usuario == Administradores[e].getUsuario():
            encontrado_admin = True
            
            break

    if encontrado_cliente:
        del Clientes[i]


        Dato ={           
            'message': 'Se eliminó el cliente',
        }

    elif encontrado_admin:

        del Administradores[e]
        Dato ={
          
            'message': 'Se eliminó el Administrador',
        }

    else:

        Dato ={         
            'message': 'No se encontró el usuario',
        }

    respuesta = jsonify(Dato)
    return (respuesta)


#-------------------------------------- Agregar canciones --------------------------------------------

@app.route('/Canciones', methods=['POST'])
def AgregarCanciones():


    #cUANDO SE TRABAJA CON UNA VARIABLE GLOBAL, SE COLOCA GLOBAL
    global Canciones
    global id_canciones


    id = id_canciones
    nombre = request.json['nombre']
    artista = request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spotify = request.json['spotify']
    youtube = request.json['youtube']
    arreglo = []

    nuevo = Cancion (id, nombre, artista, album, fecha, imagen, spotify, youtube,arreglo)
    Canciones.append(nuevo)
    id_canciones = id_canciones + 1

    Dato ={ 
        'message': 'Success',
        'reason': 'Se agregaron las canciones exitosamente'
    }

    respuesta = jsonify(Dato)
    return (respuesta)
        

#--------------------------------------Mostrar Canciones Registradas --------------------------------------------


@app.route('/Canciones_Registradas', methods=['GET'])
#Queremos que en esta ruta nos devuelva los datos de las canciones
def obtenerCanciones():
    #Usamos la variable global para usar una variable declarada en el ambito global
    global Canciones
    Datos = []
    #Los for se pueden trabajar como un for each, es decir un objeto dentro de los objetos

    for i in range(len(Canciones)):
        
        Dato = {
            'id': Canciones[i].getId(),
            'nombre': Canciones[i].getNombre(),
            'artista': Canciones[i].getArtista(),
            'album': Canciones[i].getAlbum(),
            'fecha': Canciones[i].getFecha(),
            'imagen': Canciones[i].getImagen(),
            'spotify': Canciones[i].getSpotify(),
            'youtube': Canciones[i].getYoutube()
            }

        Datos.append(Dato)
    
    #En este caso usamos jsonify para convertir nuestro arreglo en un objeto JSON
    #Para que sea reconocible en el navegador y tengamos la respuesta no como 
    #un arreglo, si no como un objeto JSON
    respuesta = jsonify(Datos)
    return(respuesta)




#--------------------------------------Mostrar Canciones Registradas Para Canciones_Cliente--------------------------------------------


@app.route('/Canciones_Registradas_2', methods=['GET'])
#Queremos que en esta ruta nos devuelva los datos de las canciones
def obtenerCanciones_2():
    #Usamos la variable global para usar una variable declarada en el ambito global
    global Canciones
    Datos = []
    #Los for se pueden trabajar como un for each, es decir un objeto dentro de los objetos

    for i in range(len(Canciones)):
        
        Dato = {
            'id': Canciones[i].getId(),
            'spotify': Canciones[i].getSpotify()
            }

        Datos.append(Dato)
    
    #En este caso usamos jsonify para convertir nuestro arreglo en un objeto JSON
    #Para que sea reconocible en el navegador y tengamos la respuesta no como 
    #un arreglo, si no como un objeto JSON
    respuesta = jsonify(Datos)
    return(respuesta)







#--------------------------------------Obtener cancion individual --------------------------------------------


@app.route('/Obtener_Cancion/<int:ide>', methods=['GET'])
def Obtener_Cancion(ide):

    global Canciones


     #Variables bolleanas
    encontrado_ide = False

    
    for i in range(len(Canciones)):
        if ide == Canciones[i].getId():
            encontrado_ide = True
            
            break


    if encontrado_ide:

        Dato = {
            'id': Canciones[i].getId(),
            'nombre': Canciones[i].getNombre(),
            'artista': Canciones[i].getArtista(),
            'album': Canciones[i].getAlbum(),
            'fecha': Canciones[i].getFecha(),
            'imagen': Canciones[i].getImagen(),
            'spotify': Canciones[i].getSpotify(),
            'youtube': Canciones[i].getYoutube()
            }
    else:

        Dato ={

            'message': 'Failed',
            'reason': 'No se encontró el usuario'
        }

    respuesta = jsonify(Dato)
    return (respuesta)




#-------------------------------------- Actualizar Canción --------------------------------------------


@app.route('/Actualizar_Cancion/<int:ide>', methods=['PUT'])
def ActualizarCancion(ide):

    global Canciones
    global Administradores

    cancion_encontrada = False





    for i in range(len(Canciones)):
        if ide == Canciones[i].getId():
            cancion_encontrada = True
           
            break
    
    if cancion_encontrada:

        Canciones[i].setNombre(request.json['nombre'])
        Canciones[i].setArtista(request.json['artista'])
        Canciones[i].setAlbum(request.json['album'])
        Canciones[i].setFecha(request.json['fecha'])
        Canciones[i].setImagen(request.json['imagen'])
        Canciones[i].setSpotify(request.json['spotify'])
        Canciones[i].setYoutube(request.json['youtube'])

        Dato ={
            'message': 'Success',
            'reason':'Se actualizó la canción',
        }

    else:

        Dato ={         
            'message': 'Failed',
        }


    respuesta = jsonify(Dato)
    return (respuesta)



#---------------------------------Eliminar Canción -----------------------------------------------

@app.route('/Eliminar_Cancion/<int:ide>', methods=['DELETE'])
def EliminarCancion(ide):
    

    global Canciones

    cancion_encontrada = False


    for i in range(len(Canciones)):
        if ide == Canciones[i].getId():
            cancion_encontrada = True
            
            break


    if cancion_encontrada:
        del Canciones[i]


        Dato ={           
            'message': 'Se eliminó la canción',
        }

    else:

        Dato ={         
            'message': 'No se encontró la cancion',
        }

    respuesta = jsonify(Dato)
    return (respuesta)


#-------------------------------Agregar Admin----------------------------------------------------------------


#Misma ruta, diferente método     ID--> Nombre de usuario

#POST --> Crear
@app.route('/Agregar_Admin', methods=['POST'])
def AgregarAdmin():


    #cUANDO SE TRABAJA CON UNA VARIABLE GLOBAL, SE COLOCA GLOBAL
    global Clientes
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    usuario = request.json['usuario']
    contra = request.json['contra']
    contra_2 = request.json['contra_2']


    #Variables bolleanas
    encontrado_cliente = False
    encontrado_admin = False

    #Verificaciones: Usuario no registrado, contraseñas iguales
    
    for i in range(len(Clientes)):
        if usuario == Clientes[i].getUsuario():
            encontrado_cliente = True
            
            break

    for i in range(len(Administradores)):
        if usuario == Administradores[i].getUsuario():
            encontrado_admin = True
            
            break
    
    if encontrado_cliente:
        return jsonify({

            'message': 'Failed',
            'reason': 'El usuario ya está en uso'
        })

    elif encontrado_admin:

        return jsonify({
            'message': 'Failed',
            'reason': 'El usuario ya está en uso'
        })


    else:

        if contra == contra_2:

            nuevo = Administrador(nombre, apellido, usuario, contra)
            #APPEND agrega un elemento en la última posición del arreglo
            Administradores.append(nuevo)
            return jsonify({
                'message':'Success',
                'reason':'Se ha creado el administrador'
                
                })

        else:
            return jsonify({
                'message':'Failedx2',
                'reason':'Las contraseñas no coinciden'
            }) 




#-------------------------------------- Agregar Solicitud --------------------------------------------

@app.route('/Agregar_Solicitud', methods=['POST'])
def AgregarSolicitud():


    #cUANDO SE TRABAJA CON UNA VARIABLE GLOBAL, SE COLOCA GLOBAL
    global Solicitudes
    global id_solicitudes


    id = id_solicitudes
    nombre = request.json['nombre']
    artista = request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spotify = request.json['spotify']
    youtube = request.json['youtube']

    nuevo = Solicitud (id, nombre, artista, album, fecha, imagen, spotify, youtube)
    Solicitudes.append(nuevo)
    id_solicitudes = id_solicitudes + 1

    Dato ={ 
        'message': 'Success',
        'reason': 'Se agregaró la solicitud exitosamente'
    }

    respuesta = jsonify(Dato)
    return (respuesta)



#--------------------------------------Mostrar Solicitudes Registradas --------------------------------------------


@app.route('/Solicitudes_Registradas', methods=['GET'])
#Queremos que en esta ruta nos devuelva los datos de las canciones
def obtenerSolicitudes():
    #Usamos la variable global para usar una variable declarada en el ambito global
    global Solicitudes
    Datos = []
    #Los for se pueden trabajar como un for each, es decir un objeto dentro de los objetos

    for i in range(len(Solicitudes)):
        
        Dato = {
            'id': Solicitudes[i].getId(),
            'nombre': Solicitudes[i].getNombre(),
            'artista': Solicitudes[i].getArtista(),
            'album': Solicitudes[i].getAlbum(),
            'fecha': Solicitudes[i].getFecha(),
            'imagen': Solicitudes[i].getImagen(),
            'spotify': Solicitudes[i].getSpotify(),
            'youtube': Solicitudes[i].getYoutube()
            }

        Datos.append(Dato)
    
    #En este caso usamos jsonify para convertir nuestro arreglo en un objeto JSON
    #Para que sea reconocible en el navegador y tengamos la respuesta no como 
    #un arreglo, si no como un objeto JSON
    respuesta = jsonify(Datos)
    return(respuesta)


#-------------------------------------- Eliminar solicitud --------------------------------------------

@app.route('/Eliminar_Solicitud/<int:ide>', methods=['DELETE'])
def EliminarSolicitud(ide):
    
    global Solicitudes

    solicitud_encontrada = False


    for i in range(len(Solicitudes)):
        if ide == Solicitudes[i].getId():
            solicitud_encontrada = True
            
            break


    if solicitud_encontrada:
        del Solicitudes[i]


        Dato ={           
            'message': 'Se eliminó la solicitud',
        }

    else:

        Dato ={         
            'message': 'No se encontró la solicitud',
        }

    respuesta = jsonify(Dato)
    return (respuesta)


#-------------------------------------- Agregar de Solicitud a Canción --------------------------------------------

@app.route('/Cambiar_a_Cancion', methods=['POST'])
def Cambiar_aCancion():

    id_solicitud = int(request.json['id'])

    global Solicitudes
    global Canciones
    global id_canciones
    solicitud_encontrada = False


    for i in range(len(Solicitudes)):
        if id_solicitud == Solicitudes[i].getId():
            solicitud_encontrada = True
            
            break

    if solicitud_encontrada:


        id = id_canciones
        nombre = Solicitudes[i].getNombre()
        artista = Solicitudes[i].getArtista()
        album = Solicitudes[i].getAlbum()
        fecha = Solicitudes[i].getFecha()
        imagen = Solicitudes[i].getImagen()
        spotify = Solicitudes[i].getSpotify()
        youtube = Solicitudes[i].getYoutube()
        arreglo = []

        nuevo = Cancion (id, nombre, artista, album, fecha, imagen, spotify, youtube,arreglo)
        Canciones.append(nuevo)
        id_canciones = id_canciones + 1

        del Solicitudes[i]

        Dato ={ 
            'message': 'Success',
            'reason': 'Se agregó la canción'
        }

    else:
        Dato ={ 
            'message': 'Failed',
            'reason': 'Ocurrió un error en la Api'
        }

    respuesta = jsonify(Dato)
    return (respuesta)


#---------------------------------------  Crear Playlist  ------------------------------------------------------
@app.route('/Playlist', methods=['POST'])
def AgregarPlaylist():


    #cUANDO SE TRABAJA CON UNA VARIABLE GLOBAL, SE COLOCA GLOBAL
    global Playlists
    global id_canciones


    id = request.json['id']
    arreglo = []
    nuevo = Playlist (id, arreglo)
    Playlists.append(nuevo)

    Dato ={ 
        'message': 'Success',
        'reason': 'Se ha creado la playlist'
    }

    respuesta = jsonify(Dato)
    return (respuesta)


#-----------------------Guardar en PLaylist------------------------------------------------

@app.route('/Guardar_en_Playlist', methods=['POST'])
#Queremos que en esta ruta nos devuelva los datos de las canciones
def GuardandoEnPLaylist():
    #Usamos la variable global para usar una variable declarada en el ambito global
    global Playlists
    global Canciones
    existe_playlist = False

    id_cancion = int(request.json['id_cancion'])
    id_playlist = request.json['id_playlist']

    encontrado_ide = False

    
    for i in range(len(Canciones)):
        if id_cancion == Canciones[i].getId():
            encontrado_ide = True
            
            break


    if encontrado_ide:

        Dato = {
            'id': Canciones[i].getId(),
            'nombre': Canciones[i].getNombre(),
            'artista': Canciones[i].getArtista(),
            'album': Canciones[i].getAlbum(),
            'fecha': Canciones[i].getFecha(),
            'imagen': Canciones[i].getImagen(),
            'spotify': Canciones[i].getSpotify(),
            'youtube': Canciones[i].getYoutube()
            }

        for i in range(len(Playlists)):

            if Playlists[i].getId() == id_playlist:
                existe_playlist = True
            
                break

        if existe_playlist:
            Playlists[i].setCancion_a_laPlaylist(Dato)

            Dat = { 
                'message': 'Success',
                'reason': 'Se agregó la canción a la playlist'
            }

        else:     
        
            Dat = { 
                'message': 'Fail',
                'reason': 'No se encpntró la Playlist'
            }

    else:

        Dat ={

            'message': 'Failed',
            'reason': 'No se encontró la canción'
        }

    respuesta = jsonify(Dat)
    return (respuesta)


#--------------------------------------Mostrar Canciones de una playlist--------------------------------------------


@app.route('/Canciones_Registradas_Playlist/<string:ide>', methods=['GET'])
#Queremos que en esta ruta nos devuelva los datos de las canciones
def obtenerCncionesPlaylist(ide):
    #Usamos la variable global para usar una variable declarada en el ambito global
    global Playlists
    Datos = []
    #Los for se pueden trabajar como un for each, es decir un objeto dentro de los objetos
    existe_playlist = False

    for i in range(len(Playlists)):

        if Playlists[i].getId() == ide:
            existe_playlist = True
            
            break


    if existe_playlist:
        Datos = Playlists[i].getArreglo()


    else:     
        
        Datos = { 
            'message': 'Fail',
            'reason': 'No se encpntró la Playlist'
        }
    respuesta = jsonify(Datos)
    return(respuesta)




#----------------------- Modificar id de la PLaylist------------------------------------------------


@app.route('/Cambiar_id_playlist/<string:id_playlist>', methods=['PUT'])
def ActualizarId_playlist(id_playlist):

    global Playlists
    #Otra forma de usar el for es como la manera tradicional
    #Con un indice y para eso utilizamos el range(numero)
    #Donde dara el rango de numeros desde 0 hasta el numero enviado como parametro
     #Variables bolleanas
    encontrada_playlist = False
    nuevo_id = request.json['usuario_nuevo']




    for i in range(len(Playlists)):
        if id_playlist == Playlists[i].getId():
            encontrada_playlist = True         
            break

    
    if encontrada_playlist:
        Playlists[i].setId(nuevo_id)
        Dato ={ 
            'message': 'Success',
            'reason': 'Se actualizó el id de la playlist'
            }

    else:

        Dato ={           
            'message': 'Failed',
            'reason': 'No se encontró la playlist'
        }

    respuesta = jsonify(Dato)
    return (respuesta)


#--------------------------------------Mostrar Comentarios de una Cancion--------------------------------------------


@app.route('/Comentarios_Cancion/<int:id_cancion>', methods=['GET'])
#Queremos que en esta ruta nos devuelva los datos de las canciones
def obtenerComentarios(id_cancion):
    #Usamos la variable global para usar una variable declarada en el ambito global
    global Canciones
    Datos = []
    #Los for se pueden trabajar como un for each, es decir un objeto dentro de los objetos
    existe_cancion = False

    for i in range(len(Canciones)):

        if Canciones[i].getId() == id_cancion:
            existe_cancion = True       
            break


    if existe_cancion:
        Datos = Canciones[i].getArreglo()


    else:     
        
        Datos = { 
            'message': 'Fail',
            'reason': 'No se encpntró la Cancion'
        }
    respuesta = jsonify(Datos)
    return(respuesta)




#----------------------- Guardar Comentario ------------------------------------------------

@app.route('/Guardar_Comentario', methods=['POST'])
#Queremos que en esta ruta nos devuelva los datos de las canciones
def GuardandoComent():
    #Usamos la variable global para usar una variable declarada en el ambito global
    global Playlists
    global Canciones

    id_cancion = int(request.json['id_cancion'])
    user_cliente = request.json['usuario']
    coment = request.json['comentario']

    encontrado_ide = False

    
    for i in range(len(Canciones)):
        if id_cancion == Canciones[i].getId():
            encontrado_ide = True
            
            break


    if encontrado_ide:

        Dato = {
            'usuario': user_cliente,
            'comentario': coment
            }

        Canciones[i].setComentario(Dato)

        Dat = { 
            'message': 'Success',
            'reason': 'Se agregó el comentario'
         }

    else:

        Dat ={

            'message': 'Failed',
            'reason': 'No se encontró la canción'
        }

    respuesta = jsonify(Dat)
    return (respuesta)













if __name__ == "__main__":
    app.run(port=3000, debug=True)

    