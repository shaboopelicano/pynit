#version 150 core

out vec4 outColor;
in vec3 corSaida;

void main()
{
    outColor = vec4(corSaida, 1.0);
}