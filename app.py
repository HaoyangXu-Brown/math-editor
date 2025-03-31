import matplotlib
matplotlib.use('Agg')  # Set non-interactive backend
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify, send_file
import sympy as sp
from sympy.parsing.latex import parse_latex
import json
import io
import subprocess
import os
import numpy as np
from io import BytesIO
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'development-key')

@app.route('/')
def index():
    return render_template('editor.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        data = request.json
        filename = f"{data.get('title', 'document')}.json"
        print(filename)
        file = io.BytesIO()
        file.write(json.dumps(data).encode('utf-8'))
        file.seek(0)
        return send_file(
            file,
            as_attachment=True,
            download_name=filename,
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
        expr_str = latex.split('=')[0].strip()
        
        expr = parse_latex(expr_str)
        result = expr.evalf()
        
        if not result.is_Number:
            return jsonify({'error': 'No numerical answer'}), 400
            
        return jsonify({
            'result': sp.latex(result)
        })
    except Exception as e:
        return jsonify({'error': 'Invalid expression'}), 400

@app.route('/plot', methods=['POST'])
def plot_function():
    try:
        latex = request.json['latex']
        expr = parse_latex(latex)
        
        fig = plt.figure(figsize=(8, 4), dpi=100)
        ax = fig.add_subplot(111)
        
        x = sp.symbols('x')
        f = sp.lambdify(x, expr, modules=['numpy'])
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)
        
        ax.plot(x_vals, y_vals)
        ax.set_title(f'${sp.latex(expr)}$')
        ax.grid(True)
        
        buf = BytesIO()
        FigureCanvas(fig).print_png(buf)
        plt.close(fig)
        
        img_base64 = base64.b64encode(buf.getvalue()).decode('ascii')
        return jsonify({'image': img_base64})
        
    except Exception as e:
        return jsonify({'error': f'Plot error: {str(e)}'}), 400

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