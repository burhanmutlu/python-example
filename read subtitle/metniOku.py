"""from gtts import gTTS
from io import BytesIO

tts = gTTS('merhaba burhan bugün nasılsın iyimisin', lang="tr")
mp3_fp = BytesIO()
tts.write_to_fp(mp3_fp)

import musicplayer """

"""
from gtts import gTTS
from io import BytesIO
import pygame
 
def speak(text, language='en'):
	mp3_fo = BytesIO()
	tts = gTTS(text, lang=language)
	tts.write_to_fp(mp3_fo)
	pygame.mixer.music.load(mp3_fo, 'mp3')
	pygame.mixer.music.play()
	# return mp3_fo
 
pygame.init()
pygame.mixer.init()
# sound.seek(0)
speak("Python is cool always")"""


import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\tesseract.exe"
#read image
img = cv2.imread("sample.jpg")
# get grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#noise removal
noise=cv2.medianBlur(gray,3)
# thresholding# converting it to binary image by Thresholding
# this step is require if you have colored image because if you skip this part
# then tesseract won’t able to detect text correctly and this will give incorrect #result
thresh = cv2.threshold(noise, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#Configuration
config = ("-l eng — oem 3 — psm 3")
# pytessercat
text = pytesseract.image_to_string(thresh,config=config)
print(text)