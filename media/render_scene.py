"""rebuild the fixture visuals in blender 2.93. run with blender -b -P this_file.
the tray, masks and spacers come from the delivered stl files.
the slide and cell are explanatory placeholders, not measured hardware.
"""
import bpy, math
from pathlib import Path
from mathutils import Vector

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'media'/'renders'; OUT.mkdir(exist_ok=True)
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
scene=bpy.context.scene
scene.render.engine='CYCLES'; scene.cycles.samples=24
scene.cycles.use_denoising=True
scene.render.resolution_x=1920;scene.render.resolution_y=1080;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
scene.world.color=(0.3,0.3,0.3)
scene.view_settings.view_transform='Standard';scene.view_settings.look='Medium High Contrast'
scene.view_settings.exposure=0;scene.view_settings.gamma=1

def mat(name,color,rough=.5,metal=0):
    m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
    b=m.node_tree.nodes.get('Principled BSDF');b.inputs['Base Color'].default_value=(*color,1)
    b.inputs['Roughness'].default_value=rough;b.inputs['Metallic'].default_value=metal
    return m
teal=mat('tray | proposed opaque polymer',(.035,.35,.40))
dark=mat('mask | material still to be chosen',(.035,.045,.055))
orange=mat('spacers',(.96,.36,.10))
glass=mat('slide | tinted solid for visibility',(.36,.78,.85),.2)
blue=mat('illustrative cell | dimensions not specified',(.025,.055,.12),.28)
silver=mat('illustrative cell grid',(.45,.58,.64),.4,.4)
ground=mat('background',(.84,.88,.90))
objects=[]
def mesh(name,file,loc,material):
    bpy.ops.import_mesh.stl(filepath=str(ROOT/'cad'/file));o=bpy.context.object;o.name=name;o.location=loc
    o.data.materials.append(material);objects.append(o);return o
def box(name,size,loc,material):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name
    o.dimensions=size;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    o.data.materials.append(material);return o
tray=mesh('01 | actual tray mesh','tray.stl',(0,0,0),teal)
parts=[tray]
spacers=[mesh('02 | actual spacer mesh','spacer.stl',(x,y,-8),orange) for x in [-45,37] for y in [-19,11]]
slide=box('03 | slide envelope, not printed',(75,25,1),(0,0,2.5),glass)
upper=mesh('04 | upper aperture mask','mask.stl',(-15,-15,4),dark)
lower=mesh('05 | cell-plane aperture mask','mask.stl',(-15,-15,-6),dark)
cell=box('06 | illustrative cell only',(30,30,.4),(0,0,-6.25),blue)
grid=[]
for x in range(-12,13,3):grid.append(box('cell grid | schematic',(.12,28,.03),(x,0,-6.03),silver))
board=box('07 | illustrative insulating support',(106,54,1.5),(0,0,-9),ground)
extras=spacers+[slide,upper,lower,cell,board]+grid
floor=box('studio floor',(2000,2000,1),(0,0,-10.3),ground)
def hide(items,value):
    for o in items:o.hide_render=value
def camera(loc,target,scale):
    if not scene.camera:
        bpy.ops.object.camera_add();scene.camera=bpy.context.object
    c=scene.camera;c.location=loc;c.rotation_euler=(Vector(target)-c.location).to_track_quat('-Z','Y').to_euler();c.data.type='ORTHO';c.data.ortho_scale=scale
def light(name,loc,power,size):
    bpy.ops.object.light_add(type='AREA',location=loc);o=bpy.context.object;o.name=name;o.data.energy=power;o.data.size=size
    o.rotation_euler=(-o.location).to_track_quat('-Z','Y').to_euler()
light('large softbox',(0,-80,140),300000,110)
light('fill',(80,50,80),180000,90)
def render(name):scene.render.filepath=str(OUT/name);bpy.ops.render.render(write_still=True)

hide(extras,True);camera((105,-135,105),(0,0,0),125);render('tray-raw.png')
hide(extras,False);camera((100,-140,120),(0,0,-1),140);render('assembly-raw.png')
# separate the same components so the stack is easy to explain.
tray.location.z=6
slide.location.z=20.5
upper.location.z=33
camera((100,-160,115),(0,0,9),150);render('exploded-raw.png')
scene['status']='unbuilt design; slide, film colour and cell are illustrative'
scene['mesh_source']='cad/tray.stl, cad/spacer.stl, cad/mask.stl'
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/'media'/'fixture-scene.blend'))
# render the physical tray geometry as a short turntable, using the fast studio renderer.
hide(extras,True);tray.location.z=0;floor.hide_render=True
scene.render.engine='BLENDER_WORKBENCH'
scene.display.shading.light='STUDIO';scene.display.shading.color_type='MATERIAL'
scene.display.shading.show_shadows=True;scene.display.shading.show_cavity=True
scene.display.shading.cavity_type='BOTH';scene.display.shading.background_type='WORLD'
scene.world.color=(.84,.88,.90)
scene.render.resolution_x=1920;scene.render.resolution_y=1080
scene.render.fps=24;scene.frame_start=1;scene.frame_end=144
camera((105,-135,105),(0,0,0),125)
tray.rotation_euler.z=0;tray.keyframe_insert(data_path='rotation_euler',frame=1)
tray.rotation_euler.z=2*math.pi;tray.keyframe_insert(data_path='rotation_euler',frame=145)
for curve in tray.animation_data.action.fcurves:
    for key in curve.keyframe_points:key.interpolation='LINEAR'
scene.render.image_settings.file_format='FFMPEG';scene.render.ffmpeg.format='MPEG4';scene.render.ffmpeg.codec='H264';scene.render.ffmpeg.constant_rate_factor='HIGH'
scene.render.filepath=str(OUT/'tray-turntable-clean.mp4')
bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/'media'/'turntable-scene.blend'))
bpy.ops.render.render(animation=True)
