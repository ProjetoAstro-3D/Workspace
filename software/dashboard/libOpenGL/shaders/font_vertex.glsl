#version 330 core

layout(location = 0) in vec2 a_pos;
layout(location = 1) in vec2 a_tex;

out vec2 TexCoord;

uniform vec2 offset;

void main()
{
    vec2 pos = a_pos + offset;

    gl_Position = vec4(pos, 0.0, 1.0);

    TexCoord = a_tex;
}