from panda3d.core import *
from direct.showbase.ShowBase import ShowBase

base = ShowBase()

meshes = loader.loadModel( "StandardCube.bam" )

meshes.reparentTo( render )

shader = Shader.load(Shader.SL_GLSL, "vert.glsl", "frag.glsl")

meshes.set_shader( shader )

base.cam.setPos( 0, -7, 0 )


def createAxes( size, bothways=False, thickness=1 ):

    lines = LineSegs()
    lines.setThickness( thickness )

    lines.setColor( 1,0.1,0.1,0.1 )
    if bothways:
        lines.moveTo( -size, 0, 0 )
    else:
        lines.moveTo( 0, 0, 0 )
    lines.drawTo( size, 0, 0 )

    lines.setColor( 0.1,1,0.1,0.1 )
    if bothways:
        lines.moveTo( 0, -size, 0 )
    else:
        lines.moveTo( 0, 0, 0 )
    lines.drawTo( 0, size, 0 )

    lines.setColor( 0.1,0.1,1,0.1 )
    if bothways:
        lines.moveTo( 0, 0, -size )
    else:
        lines.moveTo( 0, 0, 0 )
    lines.drawTo( 0, 0, size )

    geom = lines.create()
    return geom

geom = createAxes( 3 )
render.attachNewNode( geom )

base.run()
