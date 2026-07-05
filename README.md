# Math_Painter_Project

A CLI app that treats input and creates a corresponding image file.

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Math_Painter_Project is a command-line interface (CLI) application designed to take mathematical expressions as input and generate visual representations of those expressions as image files. This tool aims to make complex mathematical concepts more accessible and engaging through graphical output.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Technology Stack](#technology-stack)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Features

### Expression Parsing
Math_Painter_Project parses mathematical expressions provided as input and converts them into a structured format.

### Image Generation
The parsed expressions are then rendered into image files, making it easy to visualize complex equations and functions.

### Customizable Output
Users can customize the output by specifying various parameters such as color schemes and file formats.

## How It Works

Math_Painter_Project follows these steps:

1. **Input Parsing**: The CLI reads mathematical expressions from the user.
2. **Expression Evaluation**: The parsed expressions are evaluated to determine their visual representation.
3. **Image Rendering**: The results are rendered into image files using a graphical library.

Here is an ASCII diagram illustrating the workflow:

```
User Input -> Expression Parser -> Image Renderer -> Output File
```

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Main programming language for development and execution. |
| Matplotlib | Library used for creating static, animated, and interactive visualizations in Python. |

## Requirements

To run Math_Painter_Project, you need:

- Python 3.11 or later
- Matplotlib library installed

You can install the required dependencies using pip:

```bash
pip install matplotlib
```

## Installation

To install Math_Painter_Project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/PartORG/Math_Painter_Project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Math_Painter_Project
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Math_Painter_Project does not require any configuration files or environment variables.

## Quick Start

To quickly get started with Math_Painter_Project, run the following command:

```bash
python main.py "x^2 + 3x + 2"
```

This will generate an image file named `result.png` containing the visual representation of the expression `x^2 + 3x + 2`.

## Usage

To use Math_Painter_Project, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the CLI with a mathematical expression as an argument:

    ```bash
    python main.py "expression"
    ```

Replace `"expression"` with the actual mathematical expression you want to visualize.

## Project Structure

```
Math_Painter_Project/
├── .gitignore
├── README.md
├── __pycache__/
│   ├── canvas.cpython-311.pyc
│   └── shapes.cpython-311.pyc
├── canvas.py
├── design.txt
├── main.py
└── result.png
```

- `canvas.py`: Contains the logic for rendering images.
- `design.txt`: Placeholder file for design-related information.
- `main.py`: The entry point of the application, where user input is processed and images are generated.

## License

Math_Painter_Project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.