import cv2

video = cv2.VideoCapture("vtest.avi")

_, frame = video.read()


full_body = cv2.CascadeClassifier("haarcascade_fullbody.xml")

cv2.namedWindow("image")

def nothing(x):
    pass


cv2.createTrackbar("saveim","image",0,1,nothing)

save_counter = 0

while video.isOpened():
    _, frame = video.read()

    gray_im = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    bodys = full_body.detectMultiScale(gray_im,2.01,3)

    for x, y, w, h in bodys:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        frame[y:y+h, x:x+w, 0] = 255
        if cv2.getTrackbarPos("saveim","image") == 1:
            detected_person = frame[y:y+h, x:x+w]
            kaydetme_yolu = f"files/insan{save_counter}.png"
            cv2.imwrite(kaydetme_yolu,detected_person)
            save_counter += 1
            if save_counter == 5:
                save_counter = 0


    cv2.imshow("image",frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break



video.release()
cv2.destroyAllWindows()

