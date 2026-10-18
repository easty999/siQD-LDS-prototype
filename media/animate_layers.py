"""assembled-to-exploded clip. run with blender 2.93 in background mode."""
import bpy,json
from pathlib import Path
from mathutils import Vector
R=Path(__file__).resolve().parent;O=R/'renders'
bpy.ops.wm.open_mainfile(filepath=str(R/'fixture-scene.blend'))
bpy.context.preferences.filepaths.save_version=0
s=bpy.context.scene
def find(prefix):return next(o for o in s.objects if o.name.startswith(prefix))
tray=find('01 |');slide=find('03 |');upper=find('04 |');lower=find('05 |');cell=find('06 |');board=find('07 |')
spacers=[o for o in s.objects if o.name.startswith('02 |')]
grids=[o for o in s.objects if o.name.startswith('cell grid')]
for o in s.objects:o.animation_data_clear()
for o in [tray,slide,upper,lower,cell,board]+spacers+grids:o.hide_render=False
find('studio floor').hide_render=True
def move(o,start,end):
    o.location=start;o.keyframe_insert(data_path='location',frame=1);o.keyframe_insert(data_path='location',frame=36)
    o.location=end;o.keyframe_insert(data_path='location',frame=132);o.keyframe_insert(data_path='location',frame=192)
    for curve in o.animation_data.action.fcurves:
        for k in curve.keyframe_points:
            k.interpolation='BEZIER';k.handle_left_type='AUTO_CLAMPED';k.handle_right_type='AUTO_CLAMPED'
move(tray,(0,0,0),(0,0,27))
move(slide,(0,0,2.5),(0,0,45.5))
move(upper,(-15,-15,4),(-15,-15,64))
move(lower,(-15,-15,-6),(-15,-15,12))
move(cell,(0,0,-6.25),(0,0,0))
for o in grids:move(o,tuple(o.location),(o.location.x,o.location.y,o.location.z+6.25))
for o in spacers:
    x,y,z=o.location
    move(o,(x,y,-8),(x+(-12 if x<0 else 12),y+(-8 if y<0 else 8),-8))
c=s.camera;c.location=(110,-175,130);target=Vector((0,0,24))
c.rotation_euler=(target-c.location).to_track_quat('-Z','Y').to_euler()
c.data.type='ORTHO';c.data.ortho_scale=194;c.data.shift_x=.14
s.render.engine='BLENDER_WORKBENCH';s.display.shading.light='STUDIO';s.display.shading.color_type='MATERIAL'
s.display.shading.show_shadows=True;s.display.shading.show_cavity=True;s.display.shading.cavity_type='BOTH'
s.display.shading.background_type='WORLD';s.world.color=(.91,.94,.94)
s.render.resolution_x=1920;s.render.resolution_y=1080;s.render.resolution_percentage=100
s.render.fps=24;s.frame_start=1;s.frame_end=192
s.render.image_settings.file_format='PNG'
for f in [1,84,132]:
    s.frame_set(f);s.render.filepath=str(O/f'layers-check-{f}.png');bpy.ops.render.render(write_still=True)
s.frame_set(1);s.render.image_settings.file_format='FFMPEG';s.render.ffmpeg.format='MPEG4';s.render.ffmpeg.codec='H264';s.render.ffmpeg.constant_rate_factor='HIGH'
s.render.filepath='//renders/layers-clean.mp4'
bpy.ops.file.make_paths_relative();bpy.ops.wm.save_as_mainfile(filepath=str(R/'layers-animation.blend'),compress=True)
bpy.ops.render.render(animation=True)
# add the readable labels as a separate, editable video-editor layer.
bpy.ops.wm.read_factory_settings(use_empty=True)
s=bpy.context.scene;s.sequence_editor_create()
movie=s.sequence_editor.sequences.new_movie('assembled to separated',str(O/'layers-clean.mp4'),channel=2,frame_start=1)
movie.blend_type='ALPHA_OVER'
bg=s.sequence_editor.sequences.new_effect('white background',type='COLOR',channel=1,frame_start=1,frame_end=193);bg.color=(1,1,1)
movie.transform.scale_x=.78;movie.transform.scale_y=.78;movie.transform.offset_x=-50
overlay=s.sequence_editor.sequences.new_image('part names',str(O/'layers-overlay.png'),channel=3,frame_start=1)
overlay.frame_final_duration=192;overlay.blend_type='ALPHA_OVER'
s.render.resolution_x=1920;s.render.resolution_y=1080;s.render.resolution_percentage=100;s.render.fps=24
s.frame_start=1;s.frame_end=192;s.render.use_sequencer=True
s.view_settings.view_transform='Standard';s.view_settings.look='None'
s.render.image_settings.file_format='FFMPEG';s.render.ffmpeg.format='MPEG4';s.render.ffmpeg.codec='H264';s.render.ffmpeg.constant_rate_factor='HIGH'
s.render.filepath=str(O/'assembled-to-exploded.mp4')
bpy.ops.wm.save_as_mainfile(filepath=str(R/'layers-video-edit.blend'),compress=True)
bpy.ops.file.make_paths_relative();bpy.ops.wm.save_as_mainfile(filepath=str(R/'layers-video-edit.blend'),compress=True)
bpy.ops.render.render(animation=True)
s.render.image_settings.file_format='PNG'
for f in [1,84,132]:
    s.frame_set(f);s.render.filepath=str(O/f'layers-preview-{f}.png');bpy.ops.render.render(write_still=True)
(O/'layers-metadata.json').write_text(json.dumps({'duration_seconds':8,'fps':24,'frames':192,'width':1920,'height':1080,'audio':False,'motion':'assembled hold 1.5s; ease apart 4s; separated hold 2.5s','status':'unbuilt design; glass and cell are illustrative'},indent=2))
