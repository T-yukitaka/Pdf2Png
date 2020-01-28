from pdf2image import convert_from_path
import img2pdf
import glob
import os
import shutil
from tqdm import tqdm

paths = sorted(glob.glob('data/*.pdf'))
for pdf_path in paths:
    name = pdf_path.split('/')[-1].split('.pdf')[0]
    imgs_path = 'results/{}'.format(name)
    os.makedirs(imgs_path, exist_ok=True)
    
    print(name)
    print('Convert pdf to pillow...')
    imgs = convert_from_path(pdf_path)
    
    i=1
    for img in tqdm(imgs):
        img.save('{}/{:03d}.png'.format(imgs_path, i), 'png')
        i+=1
    print('Saved png file.')
    
    with open('results/{}_png.pdf'.format(name), 'wb') as f:
        imgs_list = sorted(glob.glob('{}/*.png'.format(imgs_path)))
        f.write(img2pdf.convert([i for i in imgs_list]))
        print('Saved pdf file.')

    shutil.rmtree(imgs_path)
    print('Remove image files.')
    shutil.move(pdf_path, 'done')
    print('Move pdf files to done directory.')
