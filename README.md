Here's the updated README.md reflecting the new features:

# Math & Code Editor Web Application

A web-based editor for creating technical documents with mathematical formulas and executable Python code. Designed for students, educators, and developers to create interactive technical content!

## Features

- **Multi-Content Editing**:
  - Create documents with text, math, and code blocks
  - Mix formatted content with executable code
  - Intuitive block management with instant focus

- **Mathematical Features**:
  - LaTeX-based formula editing using MathQuill
  - In-place formula evaluation using SymPy
  - Visual boxed results for calculations
  - Customizable font sizing

- **Code Execution**:
  - Python code execution with real-time output
  - Syntax highlighting with CodeMirror
  - Ctrl+Enter shortcut for quick execution
  - Colored output (green success/red errors)

- **File Management**:
  - Save documents as JSON files
  - Load previously saved documents
  - Preserves all content types (text/math/code)

- **User Interface**:
  - Dark theme with technical aesthetic
  - Responsive toolbar with font size control
  - Content-editable interface with white cursor
  - Automatic code block formatting

## Technology Stack

**Frontend**:
- MathQuill (Formula editing)
- CodeMirror (Code editing)
- jQuery (DOM manipulation)
- HTML5 ContentEditable

**Backend**:
- Python 3
- Flask (Web framework)
- SymPy (Math evaluation)
- Subprocess (Code execution)
- JSON (Data serialization)

## Installation

1. **Prerequisites**:
   - Python 3.6+
   - pip package manager

2. **Setup**:
```bash
git clone [your-repo-url]
cd math-editor
pip install -r requirements.txt
```

3. **Run Application**:
```bash
python app.py
```
Visit `http://localhost:5000` in your browser

## Usage Guide

### Core Operations
1. **Add Content**:
   - **Formula**: Click "Add Formula" > Type LaTeX
   - **Text**: Click "Insert Text" > Start typing
   - **Code**: Click "Insert Code" > Write Python

2. **Evaluate Content**: (to be fixed)
   - **Formulas**: Press Enter in formula field
   - **Code**: Click Run button or Ctrl+Enter
   - Results appear immediately below content

3. **File Management**: (to be fixed)
   - **Download**: Click Download to save as .json
   - **Upload**: Use Upload button to load files
   - Preserves all formatting and outputs

4. **Customization**:
   - Adjust font size using slider (12-32px)
   - Dark theme optimized for long sessions

### Document Structure
```json
[
  {
    "type": "math",
    "latex": "\\sqrt{2}"
  },
  {
    "type": "text",
    "content": "Sample text"
  },
  {
    "type": "code",
    "code": "print('Hello World')",
    "output": "Hello World"
  }
]
```

## Security Notes
- Code execution runs actual Python interpreter
- Recommended for local/trusted network use only
- Add sandboxing for production deployments

## Limitations
- Basic text formatting only (no bold/italic)
- No image/table support
- Limited LaTeX command support
- Web browser only (no mobile optimization)
- Code execution timeout at 10 seconds

## License
MIT License - Free for educational and personal use

## Contribution
Issues and PRs welcome. Please follow:
- PEP8 for Python code
- ESLint for JavaScript
- Semantic HTML markup
- CodeMirror extension guidelines