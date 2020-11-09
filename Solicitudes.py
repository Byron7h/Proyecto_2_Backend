class Solicitud:
#def -> define método
#init entre paréntesis le paso los parámetros
#__init__ es lo que nosotros conocemos como METODO CONSTRUCTOR

    def __init__(self,id,nombre,artista,album,fecha,imagen,spotify,youtube):

        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.album = album
        self.fecha = fecha
        self.imagen = imagen
        self.spotify = spotify
        self.youtube = youtube


# Creamos los métodos Get y Set de toda la vida para poder acceder a la info

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre
    
    def getArtista(self):
        return self.artista
    
    def getAlbum(self):
        return self.album

    def getImagen(self):
        return self.imagen

    def getFecha(self):
        return self.fecha 

    def getSpotify(self):
        return self.spotify
    
    def getYoutube(self):
        return self.youtube
    
# Recordatorio Set le estamos mandando un nuevo valor, y este nos lo guarda en el "this".nombre por ejemplo
# osea lo reconoce y lo guarda en lugar de

    def setId(self, id):
        self.id = id  

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setArtista(self, artista):
        self.artista = artista
    
    def setAlbum(self, album):
        self.album = album    
    
    def setImagen(self, imagen):
        self.imagen = imagen

    def setFecha(self, fecha):
        self.fecha = fecha 

    def setSpotify(self, spotify):
        self.spotify = spotify 

    def setYoutube(self, youtube):
        self.youtube = youtube
