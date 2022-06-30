import cv2
import glob
import os
import random

path = "C:/Users/Makerspace BC/Pictures/Saved Pictures"
filenames = glob.glob(os.path.join(path, "*"))


def process(photo):
    # for filename in filenames:
    #     #print(filename)
    img = cv2.imread(filenames[photo])
    cv2.imshow("Slideshow", img)
    if cv2.waitKey(1000) == ord('q'):
        return


#
i = 5
while i > 0:
    i -= 1
    process(random.randint(0, len(filenames)))
