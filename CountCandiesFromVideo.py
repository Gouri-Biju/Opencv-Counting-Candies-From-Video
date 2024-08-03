import cv2
def candy_count(image,desiredArea=100):
    # greyscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Blured
    blured = cv2.GaussianBlur(gray, (3, 3), None)
     # adaptive threshholding
    threshAdap = cv2.adaptiveThreshold(blured, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    contours, hierarchy = cv2.findContours(threshAdap, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    big_size_contours = 0
    for index, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        print(index, area)
        if area > desiredArea:
            print("taking counter at index : ", index)
            big_size_contours = big_size_contours + 1
        else:
            print("ignoring counter at index : ", index)
    return big_size_contours

if __name__ =='__main__':
    print('ran directly')
    vs = cv2.VideoCapture('./video/candies_on_table.mov')

    while True:
        grabbed, frame = vs.read()
        if grabbed == False:
            print("video ended")
            break
        else:
            answer = candy_count(frame,100)
            print(answer)
            cv2.putText(frame,f"count:{answer}",(30,30),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),1)
            cv2.imshow('output',frame)
            cv2.waitKey(1)