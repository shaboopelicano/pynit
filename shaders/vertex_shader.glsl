#version 150 core

in vec3 position;
in vec3 cor;
out vec3 corSaida;

void main()
{
    corSaida = cor;
    gl_Position = vec4(position, 1.0);
}