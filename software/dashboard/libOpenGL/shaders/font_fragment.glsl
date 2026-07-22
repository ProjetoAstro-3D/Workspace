#version 330 core

in vec2 TexCoords;

uniform sampler2D text;
uniform vec3 textColor;

out vec4 FragColor;

void main()
{
    float alpha = texture(text, TexCoords).r;

    FragColor = vec4(
        textColor,
        alpha
    );
}