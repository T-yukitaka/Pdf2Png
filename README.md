# Pdf2Png

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

- Conda Environment Setting:
```
conda env create -n Pdf2Png -f environment.yml

source activate Pdf2Png

pip install -r requirements.txt
```

- Directories:
```
${root}
├── data
├── done
├── results
├── README.md
├── Pdf2Png.py
├── environment.yml
└── requirements.txt
```

- Convert pdf to png:
1. Preparing pdf file.

`data/hoge.pdf`
2. Convert pdf to png.
```
python Pdf2Png.py
```
3. Get converting pdf file.

`results/hoge_png.pdf`