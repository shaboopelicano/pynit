import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from ui.config import *
from utils.shader_loader import ShaderLoader
import numpy
import sys


class Janela:
    def __init__(self):
        # self.vertices = [
        #     0.0, 0.0, 0.0,
        #     0.5, 0.0, 0.0,
        #     0.5, 0.5, 0.0,
        # ]
        self.vertices = [
            -0.5, -0.5, 0.0,1.0,0.0,0.0,
            0.0, 0.0, 0.0,0.0,1.0,0.0,
            0.0, -0.5, 0.0,0.0,0.0,1.0,
            -0.5,0.0,0.0,0.0,0.0,0.0
        ]
        self.cores = [
            0.0, 0.0, 0.0
        ]
        self.indices = [
            0,1,2,
            0,3,1
        ]
        self.vertices = numpy.array(self.vertices, dtype=numpy.float32)
        self.cores = numpy.array(self.cores, dtype=numpy.float32)
        self.indices = numpy.array(self.indices, dtype=numpy.uint32)

        self.inicializar_ui()

    def inicializar_ui(self):
        if not glfw.init():
            raise Exception("GLFW não pode ser incializado.")
        self.janela = glfw.create_window(
            LARGURA_JANELA, ALTURA_JANELA, NOME_JANELA, None, None)
        if not self.janela:
            glfw.terminate()
            raise Exception("Janela não pode ser criada.")
        glfw.set_window_pos(self.janela, POSX, POSY)
        glfw.make_context_current(self.janela)
        glfw.set_key_callback(self.janela, self.callback_teclado)

        glClearColor(0.0, 0.0, 0.0, 1.0)
        self.vertex_shader = ShaderLoader("vertex_shader.glsl")

    def rodar(self):
        self.setup_buffers()
        while not glfw.window_should_close(self.janela):
            self.atualizar_cores()
            glfw.poll_events()
            self.desenhar()
            glfw.swap_buffers(self.janela)
        glfw.terminate()

    def callback_teclado(self, janela, key, scancode, action, mods):
        if key is glfw.KEY_ESCAPE:
            glfw.set_window_should_close(janela, True)
        elif key is glfw.KEY_A:
            self.mover_triangulo_esq()
        elif key is glfw.KEY_D:
            self.mover_triangulo_dir()

    def setup_buffers(self):
        # gera o buffer
        # seta o buffer apontado por vbo como corrente ? ??
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        # aloca os dados para aquele buffer , passando o tipo do buffer , o tamanho que eles ocupam em bytes
        # os dados em si e a finalidade deles
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes,
                     self.vertices, GL_STATIC_DRAW)
        
        self.ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER,self.indices.nbytes,self.indices,GL_STATIC_DRAW)


    def desenhar(self):
        # for i in range(len(self.vertices)):
        #     if i == 2 or i == 5 or i == 8:
        #         continue
        #     else:
        #         self.vertices[i] = self.vertices[i] + 0.01

        # glBufferSubData(GL_ARRAY_BUFFER,0,self.vertices.nbytes,self.vertices)

        # pega o id daquele atributo no shader
        position = glGetAttribLocation(
            self.vertex_shader.shader_program, "position")
        cor = glGetAttribLocation(
            self.vertex_shader.shader_program, "cor")
        # passa os dados para aqueel atributo
        # id do atributo , tamanho , tipo , normalizado ?, a separacao entre cada conjunto e o inicio
        # glVertexAttribPointer(position, 3, GL_FLOAT,
        #                       GL_FALSE, 12, ctypes.c_void_p(0))
        glVertexAttribPointer(position, 3, GL_FLOAT,
                              GL_FALSE, 24, ctypes.c_void_p(0))
        glVertexAttribPointer(cor, 3, GL_FLOAT,
                              GL_FALSE, 24, ctypes.c_void_p(12))
        glEnableVertexAttribArray(position)
        glEnableVertexAttribArray(cor)

        # vbo2 = glGenBuffers(1)
        # glBindBuffer(GL_ARRAY_BUFFER, vbo2)
        # glBufferData(GL_ARRAY_BUFFER, self.cores.nbytes,
        #              self.cores, GL_STATIC_DRAW)
        # cor = glGetAttribLocation(self.vertex_shader.shader_program, "cor")
        # glVertexAttribPointer(cor, 3, GL_FLOAT, GL_FALSE,
        #                       0, ctypes.c_void_p(0))
        # glEnableVertexAttribArray(cor)

        glUseProgram(self.vertex_shader.shader_program)

        glClear(GL_COLOR_BUFFER_BIT)
        # glDrawArrays(GL_TRIANGLES, 0, 3)
        glDrawElements(GL_TRIANGLES,6,GL_UNSIGNED_INT,None)

        
        # glDeleteBuffers(1,[vbo])
        # glDeleteBuffers(1,[vbo2])

    def atualizar_cores(self):
        for i in range(3):
            self.cores[i] = self.cores[i] + numpy.float32(0.01)
        
    def mover_triangulo_esq(self):
        self.vertices[0] = self.vertices[0] - numpy.float32(0.01)
        self.vertices[3] = self.vertices[3] - numpy.float32(0.01)
        self.vertices[6] = self.vertices[6] - numpy.float32(0.01)
        
    def mover_triangulo_dir(self):
        self.vertices[0] = self.vertices[0] + numpy.float32(0.01)
        self.vertices[3] = self.vertices[3] + numpy.float32(0.01)
        self.vertices[6] = self.vertices[6] + numpy.float32(0.01)
        
