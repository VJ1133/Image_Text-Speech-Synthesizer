import io
from google.cloud import vision
from google.cloud.vision_v1 import types
vision = vision.ImageAnnotatorClient()
image_value = 'albert-einstein-quotes-01-scaled.jpg'
with io.open(image_value,'rb') as files:
        content  = files.read()
image = types.Image(content=content)
value_response = vision.text_detection(image = image)
image_to_text = value_response.text_annotations
output_text = open('quotes.txt', 'w')
for texts in image_to_text:
    print(texts.description)
    print(texts.description, file = output_text)
output_text.close()