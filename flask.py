from flask import Flask, send_file
from io import BytesIO
import zipfile
from reportlab.pdfgen import canvas

app = Flask(__name__)

def generate_pdf(content):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 100, content)
    pdf.save()
    buffer.seek(0)
    return buffer.read()

def create_zip_file(pdf1, pdf2):
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zip_file:
        zip_file.writestr('file1.pdf', pdf1)
        zip_file.writestr('file2.pdf', pdf2)
    buffer.seek(0)
    return buffer.read()

@app.route('/api/files/download')
def download_files():
    # Generate PDF files
    pdf1 = generate_pdf("Content of PDF 1")
    pdf2 = generate_pdf("Content of PDF 2")

    # Create a ZIP file
    zip_file = create_zip_file(pdf1, pdf2)

    # Send the ZIP file to the client
    return send_file(
        BytesIO(zip_file),
        download_name='files.zip',
        as_attachment=True,
        mimetype='application/zip'
    )

if __name__ == '__main__':
    app.run(debug=True)
