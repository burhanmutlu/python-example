import cv2
import numpy as np

img = cv2.imread("deneme.jpg",0) 

height = img.shape[0] ; width = img.shape[1]

cv2.imshow("org", img)

if(width>height):
    N = int(height/2)  
else:
    N = int(width/2)

arr = np.zeros([N,N,1],dtype=np.uint8)

for i in range(N):
    for j in range(N):
        arr[j][i] = img[N+j][N+i]

temp = np.zeros([height,width,1],dtype=np.uint8)

for i in range(0,N*2,2):
    for j in range(0,N*2,2):
        temp[j][i] = arr[int(j/2)][int(i/2)]
        temp[j+1][i] = arr[int(j/2)][int(i/2)]
        temp[j+1][i+1] = arr[int(j/2)][int(i/2)]
        temp[j][i+1] = arr[int(j/2)][int(i/2)]

        
        
cv2.imshow("zoom in", temp)

k=cv2.waitKey(0)
if k==ord('q'):
    cv2.destroyAllWindows()