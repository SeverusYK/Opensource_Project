
import numpy as np
import cv2

while True:
        #이미지 파일을 읽어옴 
        src = cv2.imread("Fruits.jpg", cv2.IMREAD_COLOR)

        #BGR을 HSV모드로 전환
        hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

        #HSV에서 BGR로 가정할 범위를 정의함
        lower_red= np.array([0,100,100])
        upper_red= np.array([4,255,255])

        #HSV이미지에서 빨간색만 추출하기 위한 임계값
        mask_red= cv2.inRange(hsv,lower_red,upper_red)

        #mask와 원본 이미지를 비트 연산함
        red= cv2.bitwise_and(src, src, mask=mask_red)

        cv2.imshow("RED", red)

        k= cv2.waitKey(1) & 0xFF
        if x == 27:
            break
