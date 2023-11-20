from reportlab.pdfgen import canvas
import qrcode
import os 
from PIL import Image
import time
from flask import send_file

class GeneratorQrKod:

    
    def generate_qr_code(self, link, filename, back_color, fill_color):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        qr.add_data(link) 
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)  
        qr_img_path = os.path.join('generateqrKodData', f"{filename}.png")
        qr_img.save(qr_img_path)
        return qr_img_path
    

    def generate_qr_code_pdf(self, link, filename, back_color, fill_color):
        qr_img_path = self.generate_qr_code(link, filename, back_color , fill_color)  
        time.sleep(5)
        qr_img = Image.open(qr_img_path)
        pdf_path = os.path.join("generateqrKodData", f"{filename}.pdf")
        c = canvas.Canvas(pdf_path)

        qr_width, qr_height = qr_img.size
        c.drawInlineImage(qr_img, x=150, y=700 - qr_height, width=qr_width, height=qr_height)
        c.save()


    def clear_folder(self):
        if os.path.exists('generateqrKodData') and os.path.isdir('generateqrKodData'):
            for file_name in os.listdir('generateqrKodData'):
                file_path = os.path.join('generateqrKodData', file_name)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"File removed: {file_path}")
            print(f"Folder cleared: {'generateqrKodData'}")
        else:
            print(f"Folder not found: {'generateqrKodData'}")


