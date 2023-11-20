from flask import Flask, Blueprint, render_template, request, send_file, flash
from controllers.qrkodControllers import GeneratorQrKod
import os
qrcodeGen_bp = Blueprint('/qrkodgenerator', __name__)
qrcodeDownload_bp = Blueprint('/download_qr/<filename>', __name__)


@qrcodeGen_bp.route('/qrkodgenerator', methods=['GET', 'POST'])
def QrcodeGenrator():
    try:
        if request.method == 'POST':
            link = request.form.get('link')
            filename = request.form.get('filename')
            fill_color = request.form.get('fill_color')
            back_color = request.form.get('back_color')

            qrkod_controller = GeneratorQrKod()
            
            qrkod_controller.generate_qr_code_pdf(link ,filename, fill_color, back_color)
            return render_template('downloadqrkod.html', qrcode=[filename])
        return render_template('qrkodgenerator.html')    
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')
        return render_template('error.html') 
    

@qrcodeDownload_bp.route('/download_qr/<filename>.<file_type>', methods=['GET'])
def DownloadQrcodeFile(filename, file_type):
    try:
        folder_path = "generateqrKodData"
        file_path = os.path.join(folder_path, f'{filename}.{file_type}')

        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return "Plik nie istnieje."
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')
        return render_template('error.html') 
    



    