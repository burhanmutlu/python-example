import cv2 
import numpy as np #  çok boyutlu dizilerle ve matrislerle çalışmamızı sağlayan kütüphane
import random 

width = 512; height = 512

img = 255 * np.ones((height, width), np.uint8) #tek renk sanırım
#28px de bir kare. oran orantı
birpx = (int)((width) / 28) 

f = open("matrisdegerleri.txt", "w")
f.write("\t")
for i in range(birpx):
    f.write("\t  %d. sütun" % (i))
f.write("\n")

i = 0; s = 0

#img[100:200,50:150]=255
while True:
    #sayılar 18in katı olsun çünkü 1px = 18px benim programda. hizalı olmasını sağlar
    while True:
        randX = random.randint(birpx, (width-birpx-1)) # 493 + 18 = 511
        if(randX % birpx == 0): break
    while True:
        randY = random.randint(birpx, (width-birpx-1))
        if(randY % birpx == 0): break
    # random noktaları siyah yapma ve 1px = 18px yapma
    for j in range(birpx):
        f.write("%d. satır->\t" % (s)) 
        for k in range(birpx):
            img[randX+j][randY+k] = 0
            metin = "[%d] [%d]\t" % ((randX+j),  (randY+k))
            f.write(metin)
        #1.for   
        f.write("\n"); s += 1        
    #asıl while
    i += 1
    if(i >= 500): break
#döngü bitti



img[216:400,162:200]=0
img[200:300,100:150]=255
cv2.imshow("QR Code",img)

f.close()  
k=cv2.waitKey(0)
if k==ord('q'):
    cv2.imwrite("QRCODE.jpg", img) 
    cv2.destroyAllWindows()