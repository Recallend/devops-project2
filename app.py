# app.py
from flask import Flask, request, render_template_string
from PIL import Image
import pytesseract
import io

app = Flask(__name__)

# Simple HTML page for uploading documents
HTML_PAGE = """
<!doctype html>
<title>Document Scanner</title>
<h2>Upload Document</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=document>
  <input type=submit value=Upload>
</form>
{% if text %}
<h3>Extracted Text:</h3>
<pre>{{ text }}</pre>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    extracted_text = None
    if request.method == "POST":
        file = request.files.get("document")
        if file:
            img = Image.open(io.BytesIO(file.read()))
            extracted_text = pytesseract.image_to_string(img)
    return render_template_string(HTML_PAGE, text=extracted_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
