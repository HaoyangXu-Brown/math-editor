# Math Editor Web Application

A web-based editor for creating documents with mathematical formulas using LaTeX syntax. Designed for students and LaTeX beginners to write elegant maths!

## Features

- **Rich Text Editing**: 
  - Create multi-line documents
  - Mix regular text with mathematical formulas
  - Intuitive line management with auto-empty lines

- **Formula Support**:
  - LaTeX-based formula editing using MathQuill
  - In-place formula evaluation using SymPy
  - Visual boxed results for calculations

- **File Management (to be fixed)**:
  - Save documents as JSON files
  - Load previously saved documents
  - Maintain formula integrity during save/load

- **User Interface**:
  - Content-editable div for natural typing experience
  - Responsive toolbar with essential functions
  - Automatic empty line maintenance

## Technology Stack

**Frontend**:
- MathQuill (Formula editing)
- jQuery (DOM manipulation)
- HTML5 ContentEditable

**Backend**:
- Python 3
- Flask (Web framework)
- SymPy (Math evaluation)
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

### Basic Operations
1. **Add Formula**:
   - Click "Add Formula" button
   - Type LaTeX using MathQuill interface
   - Press Enter to evaluate

2. **Evaluate Formula**:
   - Right-click any formula
   - Automatic evaluation with SymPy
   - Results shown in boxed notation

3. **Save/Load Documents**:
   - Download: Click Download to save as JSON
   - Upload: Use file input to load JSON
   - Preserves text/formula structure

### Document Structure
- Each line is stored as array element
- Content types:
  ```json
  {
    "type": "math", 
    "latex": "\\sqrt{2}"
  }
  {
    "type": "text",
    "content": "Explanation text"
  }
  ```

### Empty Line Management
- Automatically maintains 2 empty lines
- Ensures cursor accessibility
- Handles line breaks automatically
- Preserved during document load/save

## Limitations
- Basic text formatting only
- No image support
- Limited LaTeX command support
- Web browser only (no mobile optimization)

## License
MIT License - Free for educational and personal use

## Contribution
Issues and PRs welcome. Please follow standard:
- PEP8 for Python code
- ESLint for JavaScript
- Semantic HTML markup