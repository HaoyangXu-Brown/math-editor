from flask import Flask, render_template, request, jsonify, send_file
import sympy as sp
from sympy.parsing.latex import parse_latex
import json
import io
import subprocess
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'development-key')

@app.route('/')
def index():
    return render_template('editor.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        content = request.json
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

@app.route('/execute', methods=['POST'])
def execute_code():
    try:
        code = request.json['code']
        process = subprocess.run(
            ['python', '-c', code],
            capture_output=True,
            text=True,
            timeout=10
        )
        return jsonify({
            'output': process.stdout,
            'error': process.stderr
        })
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Execution timed out'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)