import cv2 as cv


def imageProcess(image, gamma):
    img = cv.imread(image, 1)
    cv.imshow("Original",img)
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                img[i][j][k] = 255 - img[i][j][k]
    cv.imshow('Negative', img)

    img = cv.imread(image, 1)
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                img[i][j][k] = 255*pow((img[i][j][k]/255), gamma)
    cv.imshow('Gamma Correction with y= '+str(gamma), img)

    cv.waitKey(0)
    cv.destroyAllWindows()


imageProcess('kupu.jpeg', 1.5)

