import cv2
img= cv2.imread("solar-system.jpg")

cv2.putText(img,  
           "Sun",
           (20, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=2,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Mercury",
           (100, 260),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.8,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Venus",
           (200, 260),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.8,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Earth",
           (300, 270),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.8,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Mars",
           (400, 260),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.8,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Jupitar",
           (550, 390),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.8,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Saturn",
           (800, 310),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.8,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Uranus",
           (950, 320),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.8,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Neptune",
           (1100, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.8,  
           color=(255,255,255)
           )

cv2.putText(img,  
          "~~THE SOLAR SYSTEM~~",
           (400, 30),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=2,  
           color=(0,100,100)
           )

cv2.imwrite("Solar-system_with_name.jpg",img)

cv2.imshow("output",img)


cv2.waitKey(0)