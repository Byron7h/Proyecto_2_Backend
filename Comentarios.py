class Comentario:
#def -> define método
#init entre paréntesis le paso los parámetros
#__init__ es lo que nosotros conocemos como METODO CONSTRUCTOR

    def __init__(self,id,arreglo):

        self.id = id
        self.arreglo = arreglo



# Creamos los métodos Get y Set de toda la vida para poder acceder a la info

    def getId(self):
        return self.id
    
    def getArreglo(self):
        return self.arreglo
    
# Recordatorio Set le estamos mandando un nuevo valor, y este nos lo guarda en el "this".nombre por ejemplo
# osea lo reconoce y lo guarda en lugar de

    def setId(self, id):
        self.id = id  

    def setComentario(self, coment):
        self.arreglo.append(coment)
 