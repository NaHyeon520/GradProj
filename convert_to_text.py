from image_preprocess import *
from extract_infos import *

def convert_to_text(img):
    processed_img=image_preprocess(img)
    extracted_img=extract_infos(processed_img)

    #ocr
    #email
    reader_en = easyocr.Reader(['en'])
    email = reader_en.readtext(extracted_img[0], detail=0)

    #title
    reader_ko = easyocr.Reader(['ko'])
    title = reader_ko.readtext(extracted_img[1], detail=0)

    #info
    info = reader_ko.readtext(extracted_img[2], detail=0, width_ths=10)

    #insert newline
    text='\n'.join(info)
    # return (email, title, text) -->tuple!!
    return (email, title, text)