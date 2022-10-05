# this is the simplest example of usage Tesseract with Python

import cv2
import pytesseract
from pytesseract import Output
from PIL import Image

try:
    from PIL import Image
except ImportError:
    import Image

filename='images/DRP90461344.pdf.png'
img = cv2.imread(filename)

# French text image to string
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))
#print(pytesseract.image_to_string(filename))

print(pytesseract.image_to_string(filename, lang='eng'))

# Get information about orientation and script detection
#print(pytesseract.image_to_osd(Image.open(filename)))

exit()

# all ocr results stored in dictionary
#content = pytesseract.image_to_data(img, lang='pol', output_type=Output.DICT)
content = pytesseract.image_to_data(img, output_type=Output.DICT)
print(content.keys())
#print(content)

# we can print text (which is list, thus we can easily find particular expression in it)
print(content['text'])

# or join it to have a string
output = " ".join(content['text'])
print(output)

# custom_config = r'--oem 3 --psm 6'
# txt_content = (pytesseract.image_to_string(img, config=custom_config))
#
#
# with open('results/invoice.txt', 'w') as file:
#     file.write(txt_content)
