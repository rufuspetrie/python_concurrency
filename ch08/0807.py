import cv2

face_cascade = cv2.CascadeClassifier("input/haarcascade_frontalface_default.xml")

for filename in ["obama1.jpg", "obama2.jpg"]:
    im = cv2.imread("input/" + filename)
    gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(im)

    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x,y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow(f"{len(faces)} faces found", im)
    cv2.waitKey(0)

print("Done.")