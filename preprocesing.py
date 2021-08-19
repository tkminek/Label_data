import fitz
import cv2 
import numpy as np
import os










def create_jpg():
    arr = os.listdir()
    index=9
    for file in arr:
        if file.split(".")[-1]=="pdf":            
            doc = fitz.open(file)
            number=doc.pageCount
            for i in range(number):
                page = doc.loadPage(i)  # number of page
                pix = page.getPixmap(matrix=fitz.Matrix(300/72, 300/72))
                output = "OUTPUT/facture_"+str(index+i)+".jpg"
                pix.writePNG(output)
            index+=1    
            print(str(file)+" : DONE")            


def uprava_jpg():
    arr = os.listdir("OUTPUT/")
    for jpg in arr:
        image = cv2.imread("OUTPUT/"+jpg)
        image = cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
        kernel = np.ones((1, 1), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        image = cv2.erode(image, kernel, iterations=1)
        cv2.imwrite("OUTPUT/"+jpg, image)





def main():    
    create_jpg()
    uprava_jpg()


if __name__ == '__main__':
    main()