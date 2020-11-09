# Creamos  clase
#Para definir una clase, es recomendable usar otro archivo
#Para tener todo mas ordenado
# vamos a crear una clase de tipo persona, para simular como lo trabajabamos en java
class Usuario :

#def -> define método
#init entre paréntesis le paso los parámetros

#__init__ es lo que nosotros conocemos como METODO CONSTRUCTOR
#Es el primer metodo a ejecutarse en la clase persona
#Hay muchos mas metodos pero este es el importante
#Usamos self para hacer referencia a este objeto
#Es como si usaramos el this en java

# en pyton no es necesario crear las variables antes

    def __init__(self,nombre,apellido,usuario,contra,con_contra):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.contraseña = contra
        self.con_contra = con_contra


    #En este caso no existe el encapsulamiento, asi que
    #Creamos nuestros metodos get y set

    #Los metodos get tienen como parametro el self, es decir
    #Que hace referencia a si mismo, pero este no se envia.
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getUsuario(self):
        return self.usuario

    def getContra(self):
        return self.contra

    def getCon_contra(self):
        return self.con_contra    



    #Los metodos set tambien llevan el parametro self, para saber
    #En que variable se guardara el valor que estamos mandandao

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setUsuario(self, usuario):
        self.usuario = usuario    
    
    def setContra(self, contra):
        self.contra = contra

    def setCon_contra(self, con_contra):
        self.con_contra = con_contra 

