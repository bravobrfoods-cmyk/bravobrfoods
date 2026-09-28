"""Read original assets and make local review sheets; originals remain untouched."""
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFile
import sys, subprocess, json, zipfile
sys.path.insert(0, str(Path('.tools').resolve()))
import imageio_ffmpeg
ImageFile.LOAD_TRUNCATED_IMAGES = True
root = Path('assets')
out = Path('.qa'); out.mkdir(exist_ok=True)
files = sorted(p for p in root.rglob('*') if p.suffix.lower() in ['.png','.jpg','.jpeg','.webp'])
font_path = 'C:/Windows/Fonts/arial.ttf'
from PIL import ImageFont
font = ImageFont.truetype(font_path, 13)
inventory=[]
for batch in range(0,len(files),20):
    sheet = Image.new('RGB',(1200,1150),'#e8e5df'); draw=ImageDraw.Draw(sheet)
    for idx,p in enumerate(files[batch:batch+20]):
        x=(idx%5)*240; y=(idx//5)*285
        try:
            im=Image.open(p); inventory.append({'file':str(p),'size':im.size,'bytes':p.stat().st_size})
            im.thumbnail((224,225));
            if im.mode=='RGBA': sheet.paste(im,(x+(240-im.width)//2,y),im)
            else: sheet.paste(im.convert('RGB'),(x+(240-im.width)//2,y))
            label=f'{batch+idx}: {p.parent.name[:23]}\n{p.name[:31]}'
            draw.text((x+6,y+230),label,font=font,fill='#18232b')
        except Exception as exc: inventory.append({'file':str(p),'error':str(exc)})
    sheet.save(out/f'images-{batch//20}.jpg')
ffmpeg=imageio_ffmpeg.get_ffmpeg_exe()
for i,p in enumerate(root.rglob('*.mp4')):
    info=subprocess.run([ffmpeg,'-i',str(p)],capture_output=True,text=True).stderr
    (out/f'video-{i}.txt').write_text(str(p)+'\n'+info,encoding='utf-8')
    import re
    match=re.search(r'Duration: (\d+):(\d+):(\d+\.\d+)',info)
    duration=sum(float(v)*m for v,m in zip(match.groups(),[3600,60,1])) if match else 10
    sheet=Image.new('RGB',(1200,740),'#e8e5df'); draw=ImageDraw.Draw(sheet)
    for j,fraction in enumerate([.05,.22,.4,.58,.76,.92]):
        frame=out/f'frame-{i}-{j}.jpg'
        subprocess.run([ffmpeg,'-y','-ss',str(duration*fraction),'-i',str(p),'-frames:v','1','-vf','scale=600:-1',str(frame)],capture_output=True)
        if frame.exists():
            im=Image.open(frame); im.thumbnail((390,320)); sheet.paste(im,((j%3)*400,(j//3)*355+25))
    draw.text((10,5),str(p),font=font,fill='#18232b'); sheet.save(out/f'video-{i}.jpg')
for p in root.rglob('*.zip'):
    with zipfile.ZipFile(p) as z: inventory.append({'archive':str(p),'members':z.namelist()})
import pypdfium2 as pdfium
for i,p in enumerate(root.rglob('*.pdf')):
    doc=pdfium.PdfDocument(p)
    for j,page in enumerate(doc):
        im=page.render(scale=min(1,1400/page.get_width())).to_pil(); im.save(out/f'pdf-{i}-{j}.jpg')
    inventory.append({'pdf':str(p),'pages':len(doc)})
(out/'inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Inspected {len(files)} images; video sheets and PDF renders saved to .qa. ffmpeg: {ffmpeg}')
