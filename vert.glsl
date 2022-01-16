#version 430

in int gl_VertexID;
in int gl_BaseVertex;

in vec4 p3d_Vertex;

uniform mat4 p3d_ModelViewProjectionMatrix;

out vec3 col;

void main()
{
	gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;


	int vert_index = gl_VertexID;
	// Alternatively:
	// int vert_index = gl_VertexID - gl_BaseVertex;

	if( vert_index == 0 )
		col = vec3( 1,0,0 );
	else if( vert_index == 2 )
		col = vec3( 0,1,0 );
	else if( vert_index == 4 )
		col = vec3( 0,0,1 );
	else if( vert_index == 6 )
		col = vec3( 0,1,1 );
	else
		col = vec3( 0.1,0.1,0.1 );	// dark grey
}
