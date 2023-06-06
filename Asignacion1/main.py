import numpy
import cv2 as cv
import imageio
import os
dir_path = "frames/"
file_names = sorted((fn for fn in os.listdir(dir_path) if fn.endswith('.png')),key=lambda x: int(x.split('.')[0][6:]) )


framesnormal = []

for file_name in file_names:
    file_path = os.path.join(dir_path, file_name)
    img = imageio.imread(file_path)
    framesnormal.append(img)

output_path = "gifsinrestar.gif"
imageio.mimsave(output_path, framesnormal, 'GIF', duration=0.2)

framesresta = []
previous_img = cv.imread(os.path.join(dir_path, file_names[0]))

for file_name in file_names[1:]:
    file_path = os.path.join(dir_path, file_name)
    current_img = imageio.imread(file_path)
    diff_img = cv.subtract(previous_img, current_img)
    framesresta.append(diff_img)
    previous_img = current_img

output_path2 = "gifrestado.gif"
imageio.mimsave(output_path2, framesresta, 'GIF', duration=0.5)



