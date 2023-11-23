import cv2
face_cascade = cv2.CascadeClassifier('C://Counting-number-of-faces-in-a-picture-using-python-opencv-master/haarcascade_frontalface_alt.xml')
  
image = cv2.imread("C://Counting-number-of-faces-in-a-picture-using-python-opencv-master/2.jpg")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
faces = face_cascade.detectMultiScale(grayImage)
  
if len(faces) == 0:
    print("No faces found")
  
else:
    print("Number of faces detected: " + str(faces.shape[0]))
    total_faces = faces.shape[0]
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),10)
  
    cv2.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
    cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
  
    # cv2.imshow('Image with faces',image)
    cv2.imwrite("C://Counting-number-of-faces-in-a-picture-using-python-opencv-master/output/out.jpeg", image)  
    cv2.waitKey(0)
    cv2.destroyAllWindows()