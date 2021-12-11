import numpy as np
from PIL import Image
import glob
import os

def createFolder(directory):
def join_it(colarray, namesave, extent, savepath):
    images = colarray
    nimages = [ ]
    total_height = 0
    max_width = 0
    # find the width and height of the final image
    for img in images:
        max_width = max(max_width, img.size[0])

    for img in images:
      if img.size[0] != max_width:
        wpercent = (max_width/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((max_width,hsize), Image.ANTIALIAS)
      total_height += img.size[1]
      nimages.append(img)

    # create a new image with the appropriate height and width
    new_img = Image.new('RGB', (max_width, total_height))

    # Write the contents of the new image
    current_height = 0
    for img in nimages:
      new_img.paste(img, (0,current_height))
      current_height += img.size[1]
    # Save the image
    
    new_img.save('{0}/joined/{1}.{2}'.format(savepath, namesave, extent))

wtpath = input("\nPlease enter a path:")
picformat = input("\nPlease enter a extension name:")

image_list = []
col_image = []
if glob.glob(wtpath +'/*.' + picformat) == []:
    print("\nThere is no file with this format!\n")
    quit()
if glob.glob('*.' + picformat) != []:
    for filename in glob.glob(wtpath +'/*.' + picformat):
        im=Image.open(filename)
        image_list.append(im)

numjoin = input("\nHow many pictures you want to combine per image:")
numjoin = int(numjoin)

nums = divmod(len(image_list), numjoin)

    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)        
createFolder(wtpath + '/joined/')

for x in range(nums[0]):
    for y in range(numjoin):
        col_image.append(image_list[0])
        del image_list[0]
    join_it(col_image, str(x), picformat, wtpath)
    col_image = []
if image_list != []:
    join_it(image_list, str(nums[0]), picformat, wtpath)