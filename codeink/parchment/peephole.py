""" parses a python module and find information about classes, functions
    and import statements there.

    * Copyright (c) 2015 Camilo Roca, carocad@unal.edu.co
"""

import ast
import astunparse
import copy
import textwrap

def parse(path):
    "parse a file at path and returns an AST tree structure"
    with open(path) as source_code:
        return ast.parse(source_code.read(), path)

def get_classes(node):
    "get the class definitions inside node"
    return filter( (lambda child: isinstance(child, ast.ClassDef)),  node.body)

def get_functions(node):
    "get the function definitions inside node"
    return filter( (lambda child: isinstance(child, ast.FunctionDef)),  node.body)

def get_imports(node):
    "get the import definitions inside node"
    return filter( (lambda child: isinstance(child, ast.Import)), node.body)

def get_importsFrom(node):
    "get the import from definitions inside node"
    return filter( (lambda child: isinstance(child, ast.ImportFrom)), node.body)

def get_attr(node, name):
    "get the attribute of node or None if the attribute doesn't exist"
    if name == 'doc':
        return str(ast.get_docstring(node, clean=True))
    if hasattr(node, name):
        return getattr(node, name)
