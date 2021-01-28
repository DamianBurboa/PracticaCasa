from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

def dibujarPasto():
    glColor3f(0.427,0.819,0.321)
    glBegin(GL_QUADS)
    glVertex3f(-1.0,-0.6,0)
    glVertex3f(1.0,-0.6,0)
    glVertex3f(1.0,-1.0,0)
    glVertex3f(-1.0,-1.0,0)
    glEnd()

def dibujarSol():
    glColor3f(0.921,0.898,0.301)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.6, sin(angulo) * 0.2 + 0.6,0.0)
    glEnd()

def dibujarCasa():
    glColor3f(0.788,0.596,0.364)
    glBegin(GL_QUADS)
    glVertex3f(-0.20,0.1,0)
    glVertex3f(0.70,0.1,0)
    glVertex3f(0.70,-0.70,0)
    glVertex3f(-0.20,-0.70,0)
    glEnd()

def dibujarnube():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 - 0.2, sin(angulo) * 0.05 + 0.5 ,0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.24 - 0.0, sin(angulo) * 0.08 + 0.57 ,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.20 + 0.50, sin(angulo) * 0.06 + 0.70 ,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.10 + 0.70, sin(angulo) * 0.05 + 0.75 ,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.10 + 0.75, sin(angulo) * 0.05 + 0.45 ,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.20 + 0.55, sin(angulo) * 0.05 + 0.50 ,0.0)
    glEnd()

def dibujartecho():
    glColor3f(0.890,0.333,0.054)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.40,0.1,0)
    glVertex3f(0.25,0.45,0)
    glVertex3f(0.90,0.1,0)
    glEnd()

def dibujarventana():
    #Marco de la ventana
    glColor3f(0.658,0.560,0.058)
    glBegin(GL_QUADS)
    glVertex3f(0.30,-0.05,0)
    glVertex3f(0.60,-0.05,0)
    glVertex3f(0.60,-0.30,0)
    glVertex3f(0.30,-0.3,0)
    glEnd()

    #Vidrio de la ventana
    glColor3f(0.239,0.819,0.741)
    glBegin(GL_QUADS)
    glVertex3f(0.32,-0.07,0)
    glVertex3f(0.58,-0.07,0)
    glVertex3f(0.58,-0.28,0)
    glVertex3f(0.32,-0.28,0)
    glEnd()

    #lineas de la ventana
    glColor3f(0.658,0.560,0.058)
    glBegin(GL_QUADS)
    glVertex3f(0.32,-0.173,0) #izqArr
    glVertex3f(0.58,-0.173,0) #derArr
    glVertex3f(0.58,-0.182,0) #derAba
    glVertex3f(0.32,-0.182,0) #IzqAba
    glEnd()

    glColor3f(0.658,0.560,0.058)
    glBegin(GL_QUADS)
    glVertex3f(0.44,-0.07,0) #izqArr
    glVertex3f(0.46,-0.07,0) #derArr
    glVertex3f(0.46,-0.28,0) #derAba
    glVertex3f(0.44,-0.28,0) #IzqAba
    glEnd()

def dibujarPuerta():
    #Puerta
    glColor3f(0.545,0.639,0.592)
    glBegin(GL_QUADS)
    glVertex3f(0.15,-0.38,0) #izqArr
    glVertex3f(0.40,-0.38,0) #derArr
    glVertex3f(0.40,-0.70,0) #derAba
    glVertex3f(0.15,-0.70,0) #IzqAba
    glEnd()

    #Perilla
    glColor3f(0.380,0.388,0.384)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.020 + 0.35, sin(angulo) * 0.020 - 0.53 ,0.0)
    glEnd()

def dibujarArbol():
    #Tronco
    glColor3f(0.788,0.596,0.364)
    glBegin(GL_QUADS)
    glVertex3f(-0.75,-0.2,0) #izqArr
    glVertex3f(-0.60,-0.2,0) #derArr
    glVertex3f(-0.60,-0.70,0) #derAba
    glVertex3f(-0.75,-0.70,0) #izqAba
    glEnd()

    #Hojas
    glColor3f(0.196,0.470,0.180)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.675, sin(angulo) * 0.2 -0.2 ,0.0)
    glEnd()

    glColor3f(0.196,0.470,0.180)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.15 - 0.675, sin(angulo) * 0.15 - 0.03 ,0.0)
    glEnd()

    glColor3f(0.196,0.470,0.180)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.10 - 0.675, sin(angulo) * 0.10 + 0.1 ,0.0)
    glEnd()

def dibujar():
    #rutinas de dibujo
    dibujarPasto()
    dibujarSol()
    dibujarCasa()
    dibujarnube()
    dibujartecho()
    dibujarventana()
    dibujarPuerta()
    dibujarArbol()

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0.474,0.780,0.752,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()