<div align='center'>

<img src='externalAssets/KavaLogo.png' height='250'>

# Kava
## Learn, create, execute.
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-0.1-orange.svg)]()

</div>

Kava is a custom scripting language designed for simplicity and ease of use, implemented entirely in Python. It features a Java-like syntax with curly braces `{}`. Kava supports variables, arithmetic, conditionals, loops, functions and string operations making it suitable for educational purposes, scripting tasks, or as a foundation for more complex language features.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Language Syntax](#language-syntax)
- [Implementation Details](#implementation-details)

## Features

- **Simple Syntax**: Java-inspired with curly braces `{}`
- **Variables**: Optional type declaration using `var name[type] = value`
- **Arithmetic Operations**: `+`, `-`, `*`, `/` with operator precedence
- **Comparisons**: `==`, `!=`, `<`, `>`
- **String Handling**: Literals, concatenation, and operations
- **Control Flow**: `if-else` conditionals and `while` loops
- **Functions**: Define functions with parameters and return values
- **I/O**: `print` statements for output
- **Warnings & Errors**: Warnings for unused variables appear in **yellow**, errors in **red**
- **Comments**: Single-line comments with `#`

# Installation

If you're using Windows, <a href='https://github.com/santiagocalebe/Kava/releases/latest'>[click here]</a> to download the updated version of the interpreter.

## Prerequisites
- Python 3.8 or higher
- Git (optional, for cloning the repository)

## Setup
### 1. Clone the repository:

`git clone https://github.com/santiagocalebe/Kava.git`

`cd Kava`

### 2. Create a virtual environment:

`python -m venv .venv`

### 3. Activate the virtual environment:
- On Windows:
  ```
  .venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source .venv/bin/activate
  ```

### Adicional dependencies:
Colorama: `pip install colorama`

## Usage

# IF SOURCE-CODE:

Go to `cd src`

1. Create a `.kava` file with your Kava code.`

2. Drag & Drop your code into the interpreter (Interp.py).

2.1. Alternativly, you can use:
`python interp.py main.kava`

**Command Line Options**: The interpreter takes a single argument: the path to a `.kava` file. If the file is not found or lacks a `.kava` extension, an error will be displayed.

# IF .EXE BUILD:
Just create a .kava file with your code and throw it into the KavaInterpreter.exe.

## Language Syntax

Kava uses a C/Java-like syntax with optional type declarations.

### Lexical Elements
- **Identifiers**: Start with letter or `_`, followed by letters, digits, or `_`
- **Numbers**: Integers (e.g., `42`)
- **Strings**: Double-quoted (e.g., `"Hello"`)
- **Operators**: `+`, `-`, `*`, `/`, `==`, `!=`, `<`, `>`, `=`
- **Keywords**: `print`, `if`, `else`, `while`, `func`, `return`, `var`
- **Punctuation**: `(`, `)`, `{`, `}`, `[`, `]`, `,`

### Statements
- **Variable Declaration**: `var name[type] = expression` (type is optional)
- **Assignment**: `identifier = expression`
- **Print**: `print expression`
- **If-Else**: `if (condition) { statements } [else { statements }]`
- **While**: `while (condition) { statements }`
- **Function Definition**: `func identifier(parameters) { statements }`
- **Return**: `return expression`
- **Function Call**: `identifier(arguments)`

### Expressions
- **Primary**: `number | string | identifier | (expression)`
- **Binary Ops**: `expression op expression` (with precedence: `* /` > `+ -` > comparisons)
- **Function Call**: `identifier(arguments)`

**Notes**:
- Blocks use `{}`
- Functions can be recursive
- Variables are dynamically typed but can optionally specify a type using `[type]`
- Warnings for unused variables appear in yellow, errors in red

## Implementation Details

The Kava interpreter is built using a traditional compiler pipeline:

- **Lexer** (`lexer.py`): Converts source code into tokens
- **Parser** (`parser.py`): Builds an AST using recursive descent
- **Interpreter** (`interpreter.py`): Executes code while tracking variables and functions
- **AST** (`ast.py`): Defines syntax tree nodes

**Key design choices**:
- Dynamic Typing: Variables can optionally specify types `[type]`
- Warnings: Unused variables are printed in yellow
- Errors: Runtime errors are printed in red
- Scoping: Parameters shadow globals; proper cleanup on return

## Special Thanks
[@corecathx](https://github.com/corecathx/) - Inspiration, by [RSL](https://github.com/corecathx/RSL)

### Made with 💗 by Santiago, aka. Kava developer.
