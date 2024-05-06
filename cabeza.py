from cubo import Cube
from circulos import Sphere
from cilindro import Cilindro
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from metodos import *

class Cabeza:
    def DibujarCabeza(self):
        cubitos = Cube()
        cilindritos = Cilindro()
        circulos = Sphere()
        
        #Cabeza
        circulos.drawSphere([239,238,244], 5, 100, 100)
        glPushMatrix()
        glTranslate(3, 0.3, -0.45)
        
        #Ojo derecho y pupila
        cilindritos.drawCilindro([111,84,187], 1, 5, 100, 100)
        glTranslate(0,0, 0.01)
        cilindritos.drawCilindro([255,255,255], 0.40, 5, 100, 100)
        
        #Ceja derecha
        glTranslate(-1, 0.9, 5)
        glRotate(90, 0, 1, 0)
        glRotate(-30, 1, 0, 0)
        cilindritos.drawCilindro([111,84,187], 0.20, 0.80, 100, 100)
        
        glTranslate(0,0,0.78)
        glRotate(14, 1, 0, 0)
        cilindritos.drawCilindro([111,84,187], 0.20, 0.5, 100, 100)
        
        glTranslate(0,0,0.50)
        glRotate(30, 0.50, 0, 0)
        cilindritos.drawCilindro([111,84,187], 0.20, 0.7, 100, 100)
        
        glTranslate(0,0,0.50)
        glRotate(30, 0.50, 0, 0)
        cilindritos.drawCilindro([111,84,187], 0.20, 0.7, 100, 100)
        glPopMatrix()
        
        #Ojo izquierdo
        glPushMatrix()
        glTranslate(-2.5, 0, 5)
        glRotate(90, 0, 1, 0)
        glRotate(-20, 1, 0, 0)
        cilindritos.drawCilindro([111,84,187], 0.20, 0.7, 100, 100)
        
        
        glTranslate(0,0, 0.50)
        glRotate(18, 1, 0, 0)
        cilindritos.drawCilindro([111,84,187], 0.20, 0.7, 100, 100)
        
        glTranslate(0,0,0.50)
        glRotate(20, 0.50, 0, 0)
        cilindritos.drawCilindro([111,84,187], 0.20, 0.7, 100, 100)
        glPopMatrix()
        
        #Ceja izquierda
        glPushMatrix()
        glTranslatef(0, 0,5.012)
        glTranslatef(-2.1, 1.9, -0.1)
        glRotatef(90, 0, 1, 0)
        glRotatef(30, 1,0,0)
        cilindritos.drawCilindro([111,84,187], 0.2, 1.9, 100, 100)
        glPopMatrix()
        
        """Torso temporal
        mover esto a su respectiva clase cuando se pueda"""

        
        #Cabello
        """glPushMatrix()
        glTranslate(0, 7.0, 0)
        circulos.drawSphere([111,84,187], 5, 100, 100)
        glPopMatrix()"""
        
        #Sonrisa
        glPushMatrix()
        
        glRotate(10, 1,0,0)
        glTranslate(0.5, -6.5, 5.33)
        glScale(23, 23, 0)
        glLineWidth(5)
        draw_lines_connected_variant([255,255,255], ([-0.2630019765707,1.2954625680823],
                                                     [-0.0772164491156,1.3688593196695],
                                                     [0.2393070421044,1.4124386409244],
                                                     [0.3310529815885,1.3619783742082],
                                                     [0.3516958179724,1.245002301366],
                                                     [0.2507752845399,1.1509627133949],
                                                     [0.0856325934686,1.1165579860884],
                                                     [-0.1574941461641,1.1165579860884],
                                                     [-0.246946437161,1.1693119012917],
                                                     [-0.2836448129547,1.2289467619563]))
        
        
        draw_line([0,0,0], (-0.1631652185078, 1.33490425028), (-0.0978592854995, 1.1165579860884))
        draw_line([0,0,0], (0.00277112303888, 1.379872116123), (0.0856325934686,1.1165579860884))
        draw_line([0,0,0], (0.1590293450559,1.3895021560534), (0.2507752845399,1.1509627133949))
        
        glPopMatrix()
        
        #Cabello
        glPushMatrix()
        glTranslatef(0, 3.5, 0)
        circulos.drawSphere([111,84,187], 3, 100, 100)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(1.5, 3.16, 0)
        circulos.drawSphere([111,84,187], 3, 100, 100)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(-1.5, 3.16, 0)
        circulos.drawSphere([111,84,187], 3, 100, 100)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(0, 2.9, -2.3)
        circulos.drawSphere([111,84,187], 3, 100, 100)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(0, 0.9, -2.7)
        circulos.drawSphere([111,84,187], 3, 100, 100)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(0, -0.1, -2.7)
        circulos.drawSphere([111,84,187], 3, 100, 100)
        glPopMatrix()
        
        #Segunda seccion trasera
        glPushMatrix()
        glTranslate(2, 2.9, -2.3)
        circulos.drawSphere([111,84,187], 3, 100, 100)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(2, 0.9, -2.7)
        circulos.drawSphere([111,84,187], 3, 100, 100)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(2, -0.1, -2.7)
        circulos.drawSphere([111,84,187], 3, 100, 100)
        glPopMatrix()
        
        #Tercera Seccion trasera
        glPushMatrix()
        glTranslate(-2, 2.9, -2.3)
        circulos.drawSphere([111,84,187], 3, 100, 100)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(-2, 0.9, -2.7)
        circulos.drawSphere([111,84,187], 3, 100, 100)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(-2, -0.1, -2.7)
        circulos.drawSphere([111,84,187], 3, 100, 100)
        glPopMatrix()
        
        #FINAL
        glPushMatrix()
        glTranslate(-3.7, -3, -3.8)
        glRotate(90, 0, 1, 0)
        cilindritos.drawCilindro([111,84,187], 0.7, 7.4, 100, 100)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(-3.7, -3.5, -3.8)
        glRotate(90, 0, 1, 0)
        cilindritos.drawCilindro([111,84,187], 0.7, 7.4, 100, 100)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(-3.7, -4.0, -3.8)
        glRotate(90, 0, 1, 0)
        cilindritos.drawCilindro([111,84,187], 0.7, 7.4, 100, 100)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(-3.7, -4.5, -3.8)
        glRotate(90, 0, 1, 0)
        cilindritos.drawCilindro([111,84,187], 0.7, 7.4, 100, 100)
        glPopMatrix()