
-- xforms

uniform mat4 Projection;
uniform mat4 Modelview;
uniform mat3 NormalMatrix;

-- vert

in vec4 Position;
out vec4 vPosition;
void main()
{
    vPosition = Position;
    gl_Position = Projection * Modelview * Position;
}

-- geom

in vec4 vPosition[3];
out vec3 gNormal;

layout(triangles) in;
layout(triangle_strip, max_vertices = 18) out;

void main()
{
    vec3 A = vPosition[0].xyz;
    vec3 B = vPosition[1].xyz;
    vec3 C = vPosition[2].xyz;
    gNormal = NormalMatrix * normalize(cross(B - A, C - A));

    gl_Position = Projection * Modelview * vPosition[0];
    EmitVertex();
    gl_Position = Projection * Modelview * vPosition[1];
    EmitVertex();
    gl_Position = Projection * Modelview * vPosition[2];
    EmitVertex();
    EndPrimitive();
}

-- frag

in vec3 gNormal;
out vec4 FragColor;

uniform vec3 LightPosition = vec3(0, 0, 1);
uniform vec3 AmbientMaterial = vec3(0.1, 0.1, 0.1);
uniform vec4 DiffuseMaterial = vec4(1);

void main()
{

    vec3 N = normalize(gNormal);
    vec3 L = LightPosition;
    float df = dot(N, L);
    vec3 color = AmbientMaterial + df * DiffuseMaterial.rgb;

    FragColor = vec4(color, DiffuseMaterial.a);
}
