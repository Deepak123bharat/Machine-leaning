import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

img = cv2.imread("G:\\Udit's Folder\\Uditphoto.jpg")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05,
                                      minNeighbors = 5)

print(type(faces))

print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, x, y, (x+w ,y+h), (0,255,0), 3)
    

#re = cv2.resize(img,(200,200))  (for resizing)

#cv2.imshow("Legend",img)

cv2.waitKey(1500)

cv2.destroyAllWindows()
