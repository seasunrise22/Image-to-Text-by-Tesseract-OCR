import pytesseract
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
result = open("C:\\Users\\Lee\\Desktop\\scan_image\\output.txt","w",encoding='UTF-8')

path_dir = 'C:\\Users\\Lee\\Desktop\\scan_image'
file_list = os.listdir(path_dir)

for file_name in file_list :
    if file_name == "output.txt":
        continue
    result.write(pytesseract.image_to_string('C:\\Users\\Lee\\Desktop\\scan_image\\'+file_name,lang='ENG+KOR',config='--psm 4 -c preserve_interword_spaces=1')+'\n')
result.close()
print("추출이 완료되었습니다. 확인부탁드립니다.")

