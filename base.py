import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from cabeza import Cabeza
from brazos import Brazos
from piernas import Piernas
from torso import Torso

# Variables para el zoom y la rotación
zoom_factor = 1.0
angleX = 0.0
angleY = 0.0

#Instancias de los componentes que se van a dibujar
brazos = Brazos()
cabeza = Cabeza()
piernas = Piernas()
torso = Torso()

#Aqui se insertan todos los metodos para hacer el dibujo
def draw_figures():
    cabeza.DibujarCabeza()
    brazos.DibujarBrazos()
    piernas.DibujarPiernas()
    torso.DibujarTorso()
def setup_lighting():
    glEnable(GL_LIGHTING)  # Habilita la iluminación
    glEnable(GL_LIGHT0)    # Habilita la fuente de luz 0
    
    # Configura la posición y el color de la luz
    light_position = [5.0, 5.0, 5.0, 1.0]  # La luz se encuentra en el punto (5, 5, 5)
    light_color = [1.0, 1.0, 1.0, 1.0]      # Color blanco
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)
    
    # Especifica el modelo de iluminación y el cálculo de sombras
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    
#Metodo para establecer los dibujos    
def draw():
    global angleX, angleY
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -6.0)
    glRotatef(angleX, 1.0, 0.0, 0.0)
    glRotatef(angleY, 0.0, 1.0, 0.0)
    glScalef(zoom_factor, zoom_factor, zoom_factor)  # Aplicar el factor de zoom
    draw_figures() #aqui llamamos a la funcion para dibujar
    glutSwapBuffers()

#metodo para detectar teclas para mover la camara
def special_key_pressed(key, x, y):
    global angleX, angleY
    if key == GLUT_KEY_UP:
        angleX -= 5.0
    elif key == GLUT_KEY_DOWN:
        angleX += 5.0
    elif key == GLUT_KEY_LEFT:
        angleY -= 5.0
    elif key == GLUT_KEY_RIGHT:
        angleY += 5.0
    glutPostRedisplay()

#Metodo para hacer zoom con la rueda del mouse
def mouse_wheel(button, direction, x, y):
    global zoom_factor
    if direction > 0:
        zoom_factor *= 1.1  # Zoom in (aumentar el factor de zoom)
    else:
        zoom_factor *= 0.9  # Zoom out (reducir el factor de zoom)
    glutPostRedisplay()

#Metodo para establecer parametros de la ventana y dibujo
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Proyecto 3D Graficacion")
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glutDisplayFunc(draw)
    glutSpecialFunc(special_key_pressed)
    glutMouseWheelFunc(mouse_wheel)  # Asignar la función del mouse wheel
    glutMainLoop()

if __name__ == "__main__":
    main()