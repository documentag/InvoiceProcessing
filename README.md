# InvoiceProcessing
OCR for changing invoices into xml files extracting special data

https://pypi.org/project/pytesseract/

## TODO
petla do wykonania

pdf
pdf2jpg.sh IN


pdf to img
pdf to txt

![img.png](img.png)
## START

python pdf2jpg.py
python3 ocr_image_preprocess.py
python jpg2txt.py pdf/RG_100068630897.pdf0.jpg

## Linux
Possible cause of this error is that you installed pytesseract with pip without installing the binary. If that is the case, you can install it as following:

sudo apt update && sudo apt upgrade
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
sudo apt-get install tesseract-ocr-all


## Python

command -v pip
command -v pip3
pip install --user pipenv


python -m pip install --upgrade pip
python3 -m pip install --upgrade pip

pipenv install 
pipenv run
&& pipenv shell

## Project

pip install -r requirements.txt
python3 -m pip install -r requirements.txt

python3 pip install -r requirements.txt
pip install -r requirements.txt

## Images

pip install pdf2image
python3 -m pip install pdf2image


## numpy scipy pillow


pip install numpy scipy pillow

## opencv-python

https://github.com/opencv/opencv-python
https://pypi.org/project/opencv-python/


You can also force pip to build the wheels from the source distribution. Some examples:

pip install --no-binary opencv-python opencv-python
pip install --no-binary :all: opencv-python


## tesseract

https://github.com/tesseract-ocr/tesseract

pip install pytesseract


