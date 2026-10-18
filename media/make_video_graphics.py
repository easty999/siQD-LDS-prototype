"""make the lowercase video cards from the actual renders and model results.
requires pillow. no fabricated measurement data is used.
"""
from pathlib import Path
import json
from PIL import Image,ImageDraw,ImageFont
R=Path(__file__).resolve().parent
O=R/'renders'; O.mkdir(exist_ok=True)
BG='#f2f5f4';INK='#132d34';MUTED='#506269';TEAL='#087f89';ORANGE='#b9572d'
def font(size,bold=False):
    paths=[Path('C:/Windows/Fonts')/('arialbd.ttf' if bold else 'arial.ttf'),Path('/usr/share/fonts/truetype/dejavu')/('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf')]
    for p in paths:
        if p.exists():return ImageFont.truetype(str(p),size)
    return ImageFont.load_default()
def text(d,xy,s,size=30,fill=INK,bold=False):d.text(xy,s,font=font(size,bold),fill=fill)
def card(title,sub):
    im=Image.new('RGB',(1920,1080),BG);d=ImageDraw.Draw(im)
    text(d,(72,46),title,56,bold=True);text(d,(76,120),sub,29,MUTED)
    return im,d
def footer(d,s):
    d.rectangle((0,990,1920,1080),fill=INK);text(d,(72,1015),s,28,'#ffffff')

im,d=card('a holder for the experiment','same cell. different slides. a way to keep the comparison consistent.')
raw=Image.open(O/'tray-raw.png').resize((1536,864),Image.Resampling.LANCZOS)
im.paste(raw,(320,160));d=ImageDraw.Draw(im)
text(d,(74,300),'90 x 38 x 4 mm',34,bold=True)
text(d,(74,365),'20 x 20 mm',34,TEAL,bold=True);text(d,(74,410),'light opening',28,MUTED)
text(d,(74,610),'removable',33,bold=True);text(d,(74,655),'glass slide',33,bold=True)
footer(d,'unbuilt design • rendered from the cad mesh • no physical test yet')
im.save(O/'tray-hero.png')

for src,out,title,sub,labels,points in [
 ('assembly-raw.png','assembly-labeled.png','how it would sit together','the slide changes; the cell and its wiring stay fixed.',
 ['upper light mask','slide envelope','slide tray','four spacers','cell below the tray'],
 [(1040,400),(1300,600),(1430,800),(1270,895),(915,740)]),
 ('exploded-raw.png','exploded-labeled.png','what each part does','parts are separated here so the arrangement is easier to see.',
 ['upper light mask','glass slide envelope','tray with a slide pocket','8 mm spacers','lower mask + cell','insulating support'],
 [(960,235),(1300,470),(1380,700),(1290,910),(900,785),(630,935)])]:
    im,d=card(title,sub);raw=Image.open(O/src).resize((1344,756),Image.Resampling.LANCZOS);im.paste(raw,(500,190));d=ImageDraw.Draw(im)
    for i,(label,(x,y)) in enumerate(zip(labels,points),1):
        yy=235+(i-1)*102
        d.ellipse((75,yy,119,yy+44),fill=TEAL);text(d,(87,yy+3),str(i),29,'white',True)
        text(d,(139,yy+4),label,27)
        xx=500+x*.7; yy2=190+y*.7
        d.ellipse((xx-24,yy2-24,xx+24,yy2+24),fill=TEAL,outline='white',width=3);text(d,(xx-9,yy2-19),str(i),29,'white',True)
    footer(d,'unbuilt design • slide/cell are illustrative • colours do not predict film appearance')
    im.save(O/out)

im,d=card('what the experiment needs to compare','the holder helps keep the position fixed. controls help explain a change.')
cards=[('01','bare cell','nothing added'),('02','plain glass','check the slide'),('03','plain polymer','check the host'),('04','low qd loading','first film mixture'),('05','high qd loading','second film mixture')]
for i,(n,a,b) in enumerate(cards):
    x=72+i*355;d.rounded_rectangle((x,235,x+330,495),radius=18,fill='white',outline='#c5d9da',width=2)
    text(d,(x+25,260),n,30,TEAL,True);text(d,(x+25,335),a,30,bold=True);text(d,(x+25,405),b,25,MUTED)
text(d,(78,565),'the main comparison',39,bold=True)
text(d,(78,630),'plain polymer  →  quantum-dot film  →  plain polymer',37,TEAL)
text(d,(78,700),'check reference current and temperature throughout.',31)
text(d,(78,782),'make three separate samples per coated condition.',31)
text(d,(78,838),'repeat readings help check consistency; they are not new samples.',31,MUTED)
footer(d,'proposed experiment • no measured gain yet • a negative result still counts')
im.save(O/'how-the-test-works.png')

r=json.loads((R.parent/'data/processed/results.json').read_text())['corrected_global_tilt']
im,d=card('the corrected model still shows a loss','global-tilt input • assumed cell response and film spectra')
x0,y0=190,865
for value in [0,10,20,30,40]:
    y=y0-value*14;d.line((x0,y,1030,y),fill='#c9d8da',width=2);text(d,(105,y-18),str(value),28,MUTED)
for x,key,label,col in [(330,'baseline_mA_cm2','baseline',TEAL),(690,'lds_mA_cm2','with film',ORANGE)]:
    v=r[key];top=y0-v*14;d.rounded_rectangle((x,top,x+210,y0),radius=8,fill=col)
    text(d,(x+35,top-55),f'{v:.2f}',36,col,True);text(d,(x+10,900),label,30)
text(d,(120,215),'current density (milliamps per square centimetre)',30,MUTED)
text(d,(1180,360),f"{r['delta_mA_cm2']:.2f}",115,ORANGE,True)
text(d,(1188,505),'milliamps per',33);text(d,(1188,550),'square centimetre',33)
text(d,(1188,660),'quantum yield: 0.6',31,MUTED);text(d,(1188,710),'capture: 0.7',31,MUTED)
footer(d,'simulation, not a measurement • these assumptions do not predict a finished prototype')
im.save(O/'model-result.png')

im=Image.new('RGBA',(1920,1080),(0,0,0,0));d=ImageDraw.Draw(im)
d.rectangle((0,0,1920,128),fill=(19,45,52,245));text(d,(70,35),'removable-slide holder',44,'white',True)
d.rectangle((0,992,1920,1080),fill=(19,45,52,245));text(d,(70,1017),'unbuilt cad design • 90 x 38 x 4 mm • not experimental footage',28,'white')
im.save(O/'turntable-overlay.png')
print('created five video cards and the animation overlay')
