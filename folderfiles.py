import cv2
import glob
import numpy as np
from PIL import Image

#shows transperancy
path = cv2.imread("blue.jpg")
bgra = cv2.cvtColor(path, cv2.COLOR_BGR2BGRA)
#transperancy number, if its 0 then it will be fully transparent
bgra[...,3] = 127
cv2.imwrite('result.png',bgra)
t= Image.open('result.png')
t.show()
cv2.waitKey(0)
cv2.destroyAllWindows()



path = glob.glob("C:/Users/Makerspace BC/Pictures/Camera Roll/*.jpg")
images1 = []
for file in path:
    img= cv2.imread(file)
    img= cv2.resize(img, (200,200))
    images1.append(img)
    num_rows, num_cols = img.shape[:2]
    translate = np.float32([[1,0,70],[0,1,110]])
    imgtran = cv2.warpAffine(img, translate, (num_cols + 70, num_rows +110))
    translate = np.float32([[1, 0, -30], [0,1,-50]])
    imgtran = cv2.warpAffine(imgtran, translate, (num_cols + 70 + 30, num_rows +110 +50))
    cv2.namedWindow('translation', cv2.WINDOW_NORMAL)
    cv2.imshow("translation", imgtran)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



