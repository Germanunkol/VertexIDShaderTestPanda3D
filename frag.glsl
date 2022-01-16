
#version 430

in vec3 col;

void main()
{
	gl_FragColor = vec4( col.xyz, 1 );
}
