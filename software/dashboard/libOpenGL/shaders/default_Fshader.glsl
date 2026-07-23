#version 330 core

in vec3 normal;

out vec4 FragColor;

void main()
{
    // Cor base (#CCFF00)
    vec3 baseColor = vec3(0.8, 1.0, 0.0);

    // Direção da luz
    vec3 lightDir = normalize(vec3(0.3, 1.0, 0.5));

    // Normal normalizada
    vec3 N = normalize(normal);

    // Iluminação difusa (Lambert)
    float diffuse = max(dot(N, lightDir), 0.0);

    // Luz ambiente para não ficar totalmente preto
    float ambient = 0.25;

    vec3 color = baseColor * (ambient + diffuse);

    FragColor = vec4(color, 1.0);
}