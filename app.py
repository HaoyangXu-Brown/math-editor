from flask import Flask, render_template, request, jsonify, send_file
import sympy as sp
from sympy.parsing.latex import parse_latex
import json
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('editor.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        content = request.json
        # Create in-memory file
        file = io.BytesIO()
        file.write(json.dumps(content).encode('utf-8'))
        file.seek(0)
        return send_file(
            file,
            as_attachment=True,
            download_name='document.json',
            mimetype='application/json'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        content = json.load(file)
        return jsonify({'content': content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        latex = request.json['latex']
        expr = parse_latex(latex)
        result = sp.latex(expr.doit())
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)