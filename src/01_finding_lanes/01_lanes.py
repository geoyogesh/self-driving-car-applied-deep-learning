import cv2
print('started..')

image = cv2.imread('./images/finding_lane/test_image.jpg')
cv2.imshow('result', image)
cv2.waitKey(0)

print('completed..')