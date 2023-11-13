import cv2

video = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier("haarcascade_smile.xml")
while True:
    ret, image = video.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), 3)
        smileCascade.detectMultiScale(gray, 1.8, 15)
        print("Image Saved")
        path = r'D:.jpg'
        cv2.imwrite(path, image)
    cv2.imshow('live video', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
