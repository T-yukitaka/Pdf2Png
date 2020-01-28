# MakeGif

pdfの印刷で文字化けを防ぐ方法．

pdfを一度pngの画像に変換する．

## Prerequisites
- macOS
- python 3

## Getting Started
### Instalattion
- Clone this repo:
```
git clone https://github.com/T-yukitaka/Pdf2Png.git
cd Pdf2Png
```

- Mac Setting
You need to install poppler using brew.
```
brew install poppler
```

- Conda Environment Setting
```
conda env create -n Pdf2Png -f environment.yml

pip install -r requirements.txt
```

- Convert pdf to png:
```
python Pdf2Png.py
```