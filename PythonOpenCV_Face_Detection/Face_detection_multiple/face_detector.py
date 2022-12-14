import cv2, glob

all_img = glob.glob("*.jpg")
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

for image in all_img:
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detect.detectMultiScale(gray, 1.3, 5)

    for(x, y, w, h) in faces:
        f_img = cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
    
    cv2.imshow("Face detect", f_img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()