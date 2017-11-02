#!/usr/bin/python

import os
from PIL import Image
from PIL import ImageFilter

if os.environ['INPUT_DATA_DIR'] =='' or os.environ['OUTPUT_DATA_DIR']=='':
    print "No environment variables"

for i in os.listdir(os.environ['INPUT_DATA_DIR']):
    image = Image.open(os.environ['INPUT_DATA_DIR']+'/'+i)
    image.filter(ImageFilter.BLUR)
    image.save(os.environ['OUTPUT_DATA_DIR']+ '/' + i)
    
    print os.environ['OUTPUT_DATA_DIR']+ '/' + i
