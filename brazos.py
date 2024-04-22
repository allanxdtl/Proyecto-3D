from cubo import Cube
from circulos import Sphere
from cilindro import Cilindro
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Brazos:
    def DibujarBrazos(self):
        cubitos = Cube()
        cilindritos = Cilindro()
        circulos = Sphere()
        
        #Brazo izquierdo
        