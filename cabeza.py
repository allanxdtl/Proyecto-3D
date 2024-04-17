from cubo import Cube
from circulos import Sphere
from cilindro import Cilindro
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Cabeza:
    def DibujarCabeza(self):
        cubitos = Cube()
        cilindritos = Cilindro()
        circulos = Sphere()
        
        #Cabeza
        circulos.drawSphere([239,238,244], 5, 100, 100)
        glTranslate(3, 0.3, -0.45)
        
        #Ojo derecho y pupila
        cilindritos.drawCilindro([111,84,187], 1, 5, 100, 100)
        glTranslate(0,0, 0.01)
        cilindritos.drawCilindro([255,255,255], 0.40, 5, 100, 100)