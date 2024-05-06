from cubo import Cube
from circulos import Sphere
from cilindro import Cilindro
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Torso:
    def DibujarTorso(self):
     cubitos = Cube()
     cilindritos = Cilindro()
     circulos = Sphere()
     
     #Primer cubo parte frontal fila 1
     glPushMatrix()
     glTranslate(-1.8, -5, 0.5)
     glRotate(-5, 0, 0, 1)
     glScale(1, 1, 0.5)
     cubitos.drawCubo([143,201,198], 1.8)
     glPopMatrix()
     
     glPushMatrix()
     glTranslate(0, -5, -0.1)
     glScale(1, 1, 1.1)
     cubitos.drawCubo([179,144,196], 1.8)
     glPopMatrix()
     
     glPushMatrix()
     glTranslate(1.8, -5, 0.5)
     glRotate(5, 0, 0, 1)
     glScale(1, 1, 0.5)
     cubitos.drawCubo([232,181,187], 1.8)
     glPopMatrix()
     
     #fila 2
     glPushMatrix()
     glTranslate(-1.8, -6.5, 0.5)
     glRotate(-5, 0, 0, 1)
     glScale(1, 1, 0.5)
     cubitos.drawCubo([230,228,232], 1.8)
     glPopMatrix()
     
     glPushMatrix()
     glTranslate(0, -6.5, 0.4)
     glScale(1, 1, 0.5)
     cubitos.drawCubo([98,181,124], 1.8)
     glPopMatrix()
     
     glPushMatrix()
     glTranslate(1.8, -6.5, 0.5)
     glRotate(5, 0, 0, 1) 
     glScale(1, 1, 0.5)
     cubitos.drawCubo([230,228,232], 1.8)
     glPopMatrix()
     
     #fila 3
     glPushMatrix()
     glTranslate(-1.8, -8, 0.5)
     glRotate(-5, 0, 0, 1)
     glScale(1, 1, 0.5)
     cubitos.drawCubo([179,144,196], 1.8)
     glPopMatrix()
     
     glPushMatrix()
     glTranslate(0, -8, 0.4)
     glScale(1, 1, 0.5)
     cubitos.drawCubo([253,189,91], 1.8)
     glPopMatrix()
     
     glPushMatrix()
     glTranslate(1.8, -8, 0.5)
     glRotate(5, 0, 0, 1)
     glScale(1, 1, 0.5)
     cubitos.drawCubo([143,201,198], 1.8)
     glPopMatrix()
     
     #Parte de atras del torso
     #fila 1
     glPushMatrix()
     glTranslate(-1.8, -5, -0.5)
     glRotate(-5, 0, 0, 1)
     glScale(1, 1, 0.7)
     cubitos.drawCubo([135,199,158], 1.8)
     glPopMatrix()
     
     glPushMatrix()
     glTranslate(1.8, -5, -0.5)
     glRotate(5, 0, 0, 1)
     glScale(1, 1, 0.7)
     cubitos.drawCubo([230,228,232], 1.8)
     glPopMatrix()
     
     #fila 2
     glPushMatrix()
     glTranslate(-1.8, -6.5, -0.5)
     glRotate(-5, 0, 0, 1)
     glScale(1, 1, 0.7)
     cubitos.drawCubo([230,152,181], 1.8)
     glPopMatrix()
     
     glPushMatrix()
     glTranslate(0, -6.5, -0.4)
     glScale(1, 1, 0.7)
     cubitos.drawCubo([112,179,185], 1.8)
     glPopMatrix()
     
     glPushMatrix()
     glTranslate(1.8, -6.5, -0.5)
     glRotate(5, 0, 0, 1)
     glScale(1, 1, 0.7)
     cubitos.drawCubo([223,165,79], 1.8)
     glPopMatrix()
     
     #fila 3
     glPushMatrix()
     glTranslate(-1.8, -8, -0.5)
     glRotate(-5, 0, 0, 1)
     glScale(1, 1, 0.7)
     cubitos.drawCubo([224,228,229], 1.8)
     glPopMatrix()
     
     glPushMatrix()
     glTranslate(0, -8, -0.4)
     glScale(1, 1, 0.7)
     cubitos.drawCubo([178,147,185], 1.8)
     glPopMatrix()
     
     glPushMatrix()
     glTranslate(1.8, -8, -0.5)
     glRotate(5, 0, 0, 1)
     glScale(1, 1, 0.7)
     cubitos.drawCubo([136,204,153], 1.8)
     glPopMatrix()