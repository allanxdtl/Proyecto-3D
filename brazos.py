from cubo import Cube
from circulos import Sphere
from cilindro import Cilindro
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Brazos:
    
    def __init__(self):
        self.posicion_esfera = 0.0
        self.direccion = 0.5

    def actualizar_posicion_esfera(self):
        # Actualiza la posición de la esfera
        self.posicion_esfera += 0.01 * self.direccion

        # Cambia la dirección cuando la esfera llega a ciertos límites
        if self.posicion_esfera > 5:
            self.direccion = -0.5
        elif self.posicion_esfera < -5:
            self.direccion = 0.5
            
    def timer_callback(self, value):
        self.actualizar_posicion_esfera()
        glutPostRedisplay()
        glutTimerFunc(200, self.timer_callback, 0)
    
    def DibujarBrazos(self):
        #self.actualizar_posicion_esfera()
        cilindritos = Cilindro()
        circulos = Sphere()
        
        glutTimerFunc(16, self.timer_callback, 0)
        
        glPushMatrix()
        glTranslate(0, -4.3, 0)
        #Brazo izquierdo
        glPushMatrix()
        glTranslate(-4, -1.2, -0.050)
        glRotate(90, 0, 1, 0)
        glRotate(-15, 1, 0, 0)
        glRotate(45, 0, self.posicion_esfera, 0)
        cilindritos.drawCilindro([255,255,255], 0.6, 1.5, 100, 100)
        glTranslate(0, -0.2, -1)
        glRotate(-8, 1, 0, 0)
        cilindritos.drawCilindro([255,255,255], 0.6, 1.5, 100, 100)
        glTranslate(0, 0, -0.5)
        cilindritos.drawCilindro([255,255,255], 0.6, 0.5, 100, 100)
        circulos.drawSphere([255,255,255], 0.6, 100, 100)
        glPopMatrix()
        
        #Brazo derecho
        glPushMatrix()
        glTranslate(2.6, -0.8, -0.050)
        glRotate(90, 0, 1, 0)
        glRotate(1, 1, 0, 0)
        cilindritos.drawCilindro([255,255,255], 0.6, 1.5, 100, 100)
        glTranslate(0, 0, 1)
        glRotate(-1, 1, 0, 0)
        cilindritos.drawCilindro([255,255,255], 0.6, 1, 100, 100)
        glTranslate(0, 0, 1)
        glRotate(-4.5, 1, 0, 0)
        cilindritos.drawCilindro([255,255,255], 0.6, 1, 100, 100)
        glTranslate(0, 0, 1)
        circulos.drawSphere([255,255,255], 0.6, 100, 100)
        glPopMatrix()
        
        #Pelota
        glPushMatrix()
        glTranslate(-4, -2.4+self.posicion_esfera, 1.3)
        circulos.drawSphere([255,0,0], 1.5, 100, 100)
        glPopMatrix()
        
        #Cosito de la mano
        glPushMatrix()
        
        glTranslate(5.4,-0.2,-0.06)
        glScalef(1, 0.8,1)
        circulos.drawSphere([168,139,178], 0.63, 100, 100)
        
        #Ojitos del cosito
        glPushMatrix()
        glTranslate(-0.2, 0.61, 0.09)
        circulos.drawSphere([103,83,117], 0.1, 100, 100)
        glPopMatrix()
        glPushMatrix()
        glTranslate(0.2, 0.61, 0.09)
        circulos.drawSphere([103,83,117], 0.1, 100, 100)
        glPopMatrix()
        glPushMatrix()
        glTranslate(-0.1, 0.61, 0.4)
        circulos.drawSphere([103,83,117], 0.1, 100, 100)
        glPopMatrix()
        glPopMatrix()
        glPopMatrix()