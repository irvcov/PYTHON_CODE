

class Lector(object):

    def __init__(self, archivo):
        self.archivo =  archivo
        
    def leer_archivo(self):
        contenido = []
        my_file = open(self.archivo,"r")
        for line in my_file:
            contenido.append(line)
        my_file.close()
        return contenido
        
    def escribir_archivo(self,cadena):
        my_file = open(self.archivo,"w") # "a" append "w" write
        my_file.write(cadena)
        my_file.close()
        
        