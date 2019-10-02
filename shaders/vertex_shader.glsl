#version 150 core

in vec3 position;
in vec3 cor;
in vec2 textura;
out vec3 corSaida;
out vec2 texturaSaida;

void main()
{
    corSaida = cor;
    texturaSaida = textura;
    gl_Position = vec4(position, 1.0);
}