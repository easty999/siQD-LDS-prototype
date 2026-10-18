"""add a visible design label to the turntable using blender's video editor."""
import bpy,json
from pathlib import Path
R=Path(__file__).resolve().parent;O=R/'renders'
clean=O/'tray-turntable-clean.mp4'
if not clean.exists():(O/'tray-turntable.mp4').rename(clean)
bpy.ops.wm.read_factory_settings(use_empty=True)
s=bpy.context.scene;s.sequence_editor_create()
movie=s.sequence_editor.sequences.new_movie('actual cad turntable',str(clean),channel=1,frame_start=1)
n=movie.frame_duration
overlay=s.sequence_editor.sequences.new_image('unbuilt design label',str(O/'turntable-overlay.png'),channel=2,frame_start=1)
overlay.frame_final_duration=n;overlay.blend_type='ALPHA_OVER'
s.render.resolution_x=1920;s.render.resolution_y=1080;s.render.resolution_percentage=100;s.render.fps=24
s.frame_start=1;s.frame_end=n;s.render.use_sequencer=True
s.view_settings.view_transform='Standard';s.view_settings.look='None'
s.render.image_settings.file_format='FFMPEG';s.render.ffmpeg.format='MPEG4';s.render.ffmpeg.codec='H264';s.render.ffmpeg.constant_rate_factor='HIGH'
s.render.filepath=str(O/'tray-turntable.mp4')
bpy.ops.wm.save_as_mainfile(filepath=str(R/'video-edit.blend'))
bpy.ops.render.render(animation=True)
s.render.image_settings.file_format='PNG'
for frame in [1,n//2,n]:
    s.frame_set(frame);s.render.filepath=str(O/f'turntable-check-{frame}.png');bpy.ops.render.render(write_still=True)
(O/'video-metadata.json').write_text(json.dumps({'width':1920,'height':1080,'fps':24,'frames':n,'seconds':n/24,'audio':False,'status':'unbuilt cad design, not experimental footage'},indent=2))
