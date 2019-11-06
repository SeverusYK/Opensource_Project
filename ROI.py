import cv2


mouse_is_pressing = False
start_x, start_y = -1, -1


def mouse_callback(event, x, y, flags, param):
    global start_x, start_y,mouse_is_pressing

    img_result = img_color.copy()

    if event == cv2.EVENT_LBUTTONDOWN:  #마우스 좌클릭 감지

        mouse_is_pressing = True
        start_x, start_y = x, y   # 자르기 시작할 좌표 세팅 

        cv2.circle(img_result, (x,y), 10, (0, 255, 0), -1) #자르기 시작하는 곳을 클릭하면 초록색의 아주 작은 점이 찍히면서 시작됨 

        cv2.imshow("img_color", img_result)

    elif event == cv2.EVENT_MOUSEMOVE: #마우스가 클릭되고 움직이는 동안 실행 

        if mouse_is_pressing:
            cv2.rectangle(img_result, (start_x, start_y), (x, y), (0, 200, 0), 3)  # 마우스가 눌리는 동안 직사각형을 그리기 위함(초록색으로, 굵기 3)

            cv2.imshow("img_color", img_result)

    elif event == cv2.EVENT_LBUTTONUP:  #마우스의 클릭을 멈추면 실행 

        mouse_is_pressing = False

        img_fruit = img_color[start_y:y, start_x:x]               # 이미지를 원한 만큼 자름 
        img_fruit = cv2.cvtColor(img_fruit, cv2.COLOR_BGR2GRAY);  #회색으로 검출하기 위한 작업
        img_fruit = cv2.cvtColor(img_fruit, cv2.COLOR_GRAY2BGR);


        img_result[start_y:y, start_x:x] = img_fruit
        cv2.imshow("img_color", img_result)
        cv2.imshow("img_fruit", img_fruit)



img_color = cv2.imread('Fruits.jpg', cv2.IMREAD_COLOR) # 이미지를 읽어옴

cv2.imshow("img_color", img_color)
cv2.setMouseCallback('img_color', mouse_callback)


cv2.waitKey(0)

cv2.destroyAllWindows()

