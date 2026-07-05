# Math_Painter_Project

A CLI app that treats input and creates a corresponding image file.

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)] [![License](https://img.shields.io/badge/license-MIT-green.svg)] [![Package Manager](https://img.shields.io/badge/package-manager-pip-yellow.svg)]

## Introduction

Math_Painter_Project is a command-line interface (CLI) application designed to take input and generate an image file. This project aims to provide a simple and efficient way to create images using Python, making it accessible for developers and artists alike.

The primary workflow involves running the CLI app with specific parameters, which then processes the input and outputs an image file. The project is structured to be easy to understand and extend, with clear separation of concerns between different components.

## Features

### Image Creation

- **What it does:** Treats input and creates a corresponding image file.
- **Why it exists:** To provide a simple way to generate images using Python.
- **Why it is useful:** Allows users to create custom images without needing extensive knowledge of image processing libraries.

## How It Works

The Math_Painter_Project consists of several key components:

1. **main.py**: The entry point for the application, which parses command-line arguments and invokes the appropriate functions.
2. **canvas.py**: Handles the creation of the canvas on which shapes will be drawn.
3. **shapes.py**: Contains functions to draw various shapes on the canvas.

The architecture is designed to be modular, making it easy to add new features or modify existing ones.

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python     | The primary programming language used for development. |
| PIL        | A library for image processing and generation. |

## Requirements

To run Math_Painter_Project, you need:

- Python 3.11 or later
- pip (Python package installer)

## Installation

You can install Math_Painter_Project using pip:

```bash
pip install git+https://github.com/PartORG/Math_Painter_Project.git
```

## Configuration

Math_Painter_Project does not require any configuration files or environment variables.

## Quick Start

To generate an image, run the following command:

```bash
math-painter --input input.txt --output output.png
```

Replace `input.txt` with your input file and `output.png` with the desired output file name.

## Usage

Here are some example commands to get you started:

- **Create a simple rectangle:**

  ```bash
  math-painter --shape rectangle --width 200 --height 100 --output rectangle.png
  ```

- **Draw multiple shapes:**

  ```bash
  math-painter --shapes circle,triangle --size 50 --output shapes.png
  ```

## Project Structure

```
Math_Painter_Project/
├── .gitignore
├── README.md
├── __pycache__/canvas.cpython-311.pyc
├── __pycache__/shapes.cpython-311.pyc
├── canvas.py
├── design.txt
├── main.py
├── result.png
└── shapes.py
```

- **.gitignore**: Specifies files and directories to be ignored by Git.
- **README.md**: This file.
- **canvas.py**: Handles the creation of the canvas.
- **design.txt**: Contains development guidelines or instructions.
- **main.py**: The entry point for the application.
- **result.png**: An example output image.
- **shapes.py**: Contains functions to draw shapes.

## Development

The project is developed using Python 3.11 and follows a modular architecture. Contributions are welcome, but please ensure that any new features or changes are well-documented and tested.

## Testing

No tests are currently available for Math_Painter_Project.

## Limitations

- The application does not support complex image operations.
- Error handling is minimal.

## License

Math_Painter_Project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.