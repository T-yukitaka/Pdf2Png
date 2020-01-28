# Pdf2Png
How to prevent garbled characters in pdf printing.

(pdfの印刷で文字化けを防ぐ方法．)

## Prerequisites
- macOS
- python 3

## Getting Started
### Instalattion
- Clone this repo:
    ```
    git clone https://github.com/T-yukitaka/Pdf2Png.git
    cd Pdf2Png
    mkdir data done results
    ```

- Mac Setting
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
### Convert
Convert pdf to png  once and convert to pdf.
1. Preparing pdf file.
    ```
    data/hoge.pdf
    ```
2. Convert pdf to png.
    ```
    python Pdf2Png.py
    ```
3. Get converting pdf file.
    ```
    results/hoge_png.pdf
    ```