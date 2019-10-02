#version 150 core

out vec4 outColor;
in vec3 corSaida;
in vec2 texturaSaida;
uniform sampler2D samplerTex;

void main()
{

    //outColor = vec4(corSaida, 1.0);
    outColor = texture(samplerTex,texturaSaida);
}