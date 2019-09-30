import ctypes
user32 = ctypes.windll.user32

NOME_JANELA = "Teste OpenGL"
SPEC_MONITOR = user32.GetSystemMetrics(0) , user32.GetSystemMetrics(1)
LARGURA_JANELA = 800
ALTURA_JANELA = 600
POSX = int((SPEC_MONITOR[0] / 2  ) - (LARGURA_JANELA / 4)) 
POSY = int((SPEC_MONITOR[1] / 2 ) - (ALTURA_JANELA / 4)) 
