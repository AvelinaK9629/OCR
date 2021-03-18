import os
from flask import Flask, render_template, request, send_from_directory
from templates.tesserOCR import convert_toText
from test_ocr import extract_PanCard_Fields, extract_DriverLicense_Fields, extract_AadharCard_Fields

app = Flask(__name__)

UPLOAD_FOLDER = 'images'
CURR_DIRECTORY = os.getcwd()
image_folder = os.path.join(CURR_DIRECTORY,UPLOAD_FOLDER)

@app.route("/freeOCR")
def home():
    return render_template("OCR_Document_Selection.html")

# @app.route("/OCRTest")
# def OCRTest():
#     return render_template("OCR_Document_Selection.html")

@app.route("/convertToText", methods=['POST'])
def convert_image_to_Text():

    uploaded_file = request.files['img']
    filename = uploaded_file.filename
    path = os.path.join(image_folder,filename)
    print(path)

    uploaded_file.save(path)
    text = ''
    typeOfDocument = request.form.get("docType")
    print(typeOfDocument)

    if(typeOfDocument == 'panCard'):
        text = extract_PanCard_Fields(path)
        print(text)
        return render_template("OCR_PanCard_Extraction.html", Img_path=filename, Converted_text=text,
                               title="Converted Text")
    if (typeOfDocument == 'aadharCard'):
        text = extract_AadharCard_Fields(path)
        print(text)
        return render_template("OCR_AadharCard_Extraction.html", Img_path=filename, Converted_text=text,
                               title="Converted Text")
    if (typeOfDocument == 'drivingLincese'):
        text = extract_DriverLicense_Fields(path)
        print(text)
        return render_template("OCR_DrivingLicense_Extraction.html", Img_path=filename, Converted_text=text,
                               title="Converted Text")
    if (typeOfDocument == 'other'):
        text = convert_toText(path)
        print(text)
        return render_template("OCR_Converted_Text.html", Img_path=filename, Converted_text=text,
                               title="Converted Text")

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images",filename)

if __name__ == "__main__":
    app.run(debug=True)
