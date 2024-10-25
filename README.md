# RuleBasedASTSystem
## Overview

This project is a Python-based Rule-Based AST (Abstract Syntax Tree) Evaluation System that allows users to define rules as strings, convert those rules into an AST representation, and evaluate them against given data. This system can be applied to use cases such as cohort segmentation, dynamic filtering, or matching data against defined rules.

## Features

- **AST Representation of Rules**: Parses rule strings into an AST, enabling structured evaluation.
- **Combination of Multiple Rules**: Supports combining multiple rules into a single AST, enabling complex conditional checks.
- **Evaluation Engine**: Evaluates rules against data dictionaries to verify if conditions are met.
- **Error Handling**: Includes handling for invalid inputs and undefined attributes.

## System Requirements

- **Python 3.x**
- **PyCharm IDE** (optional but recommended for development)

## Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/RAMKRISHNAN02/RuleBasedASTSystem.git
    cd RuleBasedASTSystem
    ```
   
2. **Install Dependencies**:
   This project doesn’t require any external dependencies, so you can directly run it in a Python environment.

3. **Run the Code**:
   Open the project in PyCharm or another editor, or run the script directly from the command line.

## Code Explanation

### Node Class

The `Node` class is the fundamental building block for constructing the AST. Each node represents either an operator or an operand in the AST.

```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value  # The operator or operand
        self.left = left    # Left child node
        self.right = right  # Right child node
