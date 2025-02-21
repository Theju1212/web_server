from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__, static_folder="www")

# Route for serving HTML files
@app.route('/')
def serve_index():
    return send_from_directory("www", "index.html")

@app.route('/<path:filename>')
def serve_static(filename):
    file_path = os.path.join("www", filename)
    
    if os.path.exists(file_path):
        return send_from_directory("www", filename)
    else:
        return """
        <html>
        <head><title>404 Not Found</title></head>
        <body><h1>404 - Page Not Found</h1><a href='/'>Go Home</a></body>
        </html>
        """, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
