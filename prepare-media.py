"""Create web derivatives without modifying supplied originals. Requires Pillow and imageio-ffmpeg."""
from pathlib import Path
from PIL import Image, ImageOps
import subprocess, sys
sys.path.insert(0,str(Path('.tools').resolve()))
import imageio_ffmpeg
out=Path('assets/web'); out.mkdir(exist_ok=True)
base=Path('assets/empresarial/clients')
foodbase=Path('assets/foods/clients')
sources={
 'farmacia':base/'FARMACIA MOGI GUAÇU/Fotos Drogaria/_GM_1320.JPG',
 'farmacia-atendimento':base/'FARMACIA MOGI GUAÇU/Fotos Drogaria/_GM_1334.JPG',
 'rosendo':foodbase/'RESTAURANTE JAMBALAYA E ROSENDO/FACHADAS RESTAURANTES/rosendo1.jpeg',
 'jambalaya':foodbase/'RESTAURANTE JAMBALAYA E ROSENDO/FACHADAS RESTAURANTES/FRENTE.jpg',
 'manutencao':base/'WS ROCHA MANUTENCAO/WhatsApp Image 2026-08-17 at 09.43.39.jpeg',
 'chaveiro':base/'CHAVEIRO WS ROCHA/video-poster.jpg',
 'logo-farmacia':base/'FARMACIA MOGI GUAÇU/logo faramacia sem fundo.png',
 'logo-rosendo':foodbase/'RESTAURANTE JAMBALAYA E ROSENDO/LOGOS/Rosendo sem Fundo.png',
 'logo-jambalaya':foodbase/'RESTAURANTE JAMBALAYA E ROSENDO/LOGOS/LOGO JAMBALAYA.png',
 'logo-manutencao':base/'WS ROCHA MANUTENCAO/ws rocha logo sem fundo.png',
 'logo-chaveiro':base/'CHAVEIRO WS ROCHA/logo-ws-rocha.png',
 'bravo-logo':Path('assets/foods/images/logo-bravo-br-foods-sem-fundo.png'),
 'social':Path('assets/foods/images/banner.png'),
}
for name,p in sources.items():
    im=ImageOps.exif_transpose(Image.open(p))
    if 'logo' in name and im.mode=='RGBA': im=im.crop(im.getbbox())
    for width in ([480] if 'logo' in name else [640,1280]):
        copy=im.copy(); copy.thumbnail((width,1600)); copy.save(out/f'{name}{"" if "logo" in name else "-"+str(width)}.webp',quality=85,method=6)
logo=Image.open('assets/foods/images/logo-bravo-br-foods-sem-fundo.png'); logo.thumbnail((96,96)); logo.save(out/'favicon.png')
ff=imageio_ffmpeg.get_ffmpeg_exe()
hero='assets/foods/videos/hero-bravo-br-foods.mp4'
subprocess.run([ff,'-y','-i',hero,'-an','-c:v','libx264','-preset','slow','-crf','26','-pix_fmt','yuv420p','-movflags','+faststart','assets/foods/videos/hero-web.mp4'],check=True,capture_output=True)
for name,second in [('hero-poster',.7),('delivery',2.2),('operacao',5.8),('salao',8.5)]:
    temp=Path('.qa')/(name+'.png')
    subprocess.run([ff,'-y','-ss',str(second),'-i',hero,'-frames:v','1',str(temp)],check=True,capture_output=True)
    im=Image.open(temp)
    for width in [640,1280]:
        copy=im.copy(); copy.thumbnail((width,1280)); copy.save(out/f'{name}-{width}.webp',quality=86,method=6)
if (out/'gastronomia-original.jpg').exists():
    im=Image.open(out/'gastronomia-original.jpg')
    for w in [640,1280]:
        copy=im.copy(); copy.thumbnail((w,1600)); copy.save(out/f'gastronomia-{w}.webp',quality=86,method=6)
print('Web media ready. Original files preserved.')
# New brand assets share the web media directory; originals stay in their brand folders.
for name, source in {
    'consultoria-logo': 'assets/consultoria/images/LOGOS/logo oficial sem fundo.png',
    'empresarial-logo': 'assets/empresarial/images/Logo da Bravo BR EMPRESARIAL SEM FUNDO.png',
    'consultoria-social': 'assets/consultoria/images/CARDS/Card principal.png',
    'consultoria-favicon': 'assets/consultoria/images/LOGOS/favicon somente logo sem textos sem fundo.png',
}.items():
    im = Image.open(source)
    if name.endswith('-logo') and im.mode == 'RGBA':
        box = im.getchannel('A').point(lambda value: 255 if value > 100 else 0).getbbox()
        if box:
            im = im.crop((max(0, box[0]-20), max(0, box[1]-20), min(im.width, box[2]+20), min(im.height, box[3]+20)))
    im.thumbnail((1200, 1200) if 'social' in name else (640, 640))
    im.save(out / (name + '.webp'), quality=90, method=6)

import io
for brand in ['consultoria', 'empresarial']:
    source = next(Path('assets', brand, 'videos').glob('*.mp4'))
    subprocess.run([ff, '-y', '-i', str(source), '-an', '-c:v', 'libx264', '-preset', 'slow', '-crf', '26', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(out / (brand + '-hero.mp4'))], check=True, capture_output=True)
    result = subprocess.run([ff, '-ss', '0.7', '-i', str(source), '-frames:v', '1', '-f', 'image2pipe', '-vcodec', 'png', '-'], check=True, capture_output=True)
    im = Image.open(io.BytesIO(result.stdout))
    for width in [640, 1280]:
        copy = im.copy()
        copy.thumbnail((width, 1280))
        copy.save(out / f'{brand}-poster-{width}.webp', quality=87, method=6)
