"""
Title: pyjokes_demo.py
Description: A simple demonstration of using the 'pyjokes' Python module to print one-liner programming jokes.

What are Modules:
    A Python module is a file that contains functions, classes, and variables.
    These modules are reusable and help organize code logically.

Example - pyjokes (version 0.8.3):
    A fun module that provides one-line jokes for programmers (Jokes as a Service).

Installation:
    You can install the pyjokes module using pip:
    Command: pip install pyjokes

What is pip:
    pip stands for "Pip Installs Packages"
    It is the package manager for Python that allows you to install and manage additional libraries and dependencies.

Usage:
    Run this script after installing the module to print a random programming joke.
"""

# Import the pyjokes library
import pyjokes

# Generate a joke and store it in the variable
joke = pyjokes.get_joke()

# Print the joke
print(joke)
