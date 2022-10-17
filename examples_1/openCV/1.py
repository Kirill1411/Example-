import cv2

# faces_cascades = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# img = cv2.imread('test.jpg')
# img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = faces_cascades.detectMultiScale(img2)
# print(faces)

# cv2.imshow(img2)
# cv2.waitKey(0)

img = cv2.imread('test.jpg')
print(img.shape)
# img = cv2.resize(img, (500, 500))
# cv2.imshow('Result', img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture('Testvideo.avi')

# while True:
#     success, frame = cap.read()

#     img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = faces_cascades.detectMultiScale(img2)

#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break