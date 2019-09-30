from OpenGL.GL import *
import OpenGL.GL.shaders
from OpenGL.GLU import *
import os

class ShaderLoader:
    def __init__(self,arquivo):
        self.shader_code = None
        self.shader_code2 = None
        self.shader_program = None
        self.ler_shader(arquivo)
        self.criar_shader()

    def ler_shader(self,arquivo):
        diretorio = (os.path.dirname(os.path.abspath(__file__)))
        dir_raiz = os.path.abspath(os.path.join(diretorio,os.pardir))
        shader_dir = os.path.abspath(os.path.join(dir_raiz,"shaders"))
        shader_src = os.path.abspath(os.path.join(shader_dir,arquivo))
        self.shader_code = open(shader_src,"r+").read()
        
        shader_src2 = os.path.abspath(os.path.join(shader_dir,"fragment_shader.glsl"))
        self.shader_code2 = open(shader_src2,"r+").read()
        
        
        
    
    def criar_shader(self):
        self.shader_program = OpenGL.GL.shaders.compileProgram(
            OpenGL.GL.shaders.compileShader(self.shader_code,GL_VERTEX_SHADER),
            OpenGL.GL.shaders.compileShader(self.shader_code2,GL_FRAGMENT_SHADER)
        )
    
    def usar_programa(self):
        glUseProgram(self.shader_program)

        
        
        
    
        
        
