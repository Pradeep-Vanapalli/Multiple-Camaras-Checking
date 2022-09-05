import cv2

frame0 = cv2.VideoCapture("rtsp://admin:inndata123@10.10.5.201:554/cam/realmonitor?channel=1&subtype=0")
frame1 = cv2.VideoCapture(0)
while 1:
   ret0, img0 = frame0.read()
   ret1, img00 = frame1.read()
   img1 = cv2.resize(img0,(1080,1080))
   img2 = cv2.resize(img00,(1080,1080))
   if (frame0):
       print("Cam1 is working")
       cv2.imshow('Camara-1',img1)
   if (frame1):
       print("cam2 is working"  )
       cv2.imshow('Camara-2',img2)

   k = cv2.waitKey(30) & 0xff
   if k == 27:
      break

frame0.release()
frame1.release()
cv2.destroyAllWindows()