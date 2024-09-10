#!/bin/bash

# Compile the Python file stored in $PYFILE to bytecode
if [ -z "$PYFILE" ]; then
  echo "Error: PYFILE environment variable is not set."
  exit 1
fi

# Compile the Python file
python3 -m py_compile $PYFILE

# Rename the output to match the required format (add 'c' to the filename)
OUTPUT_FILE="${PYFILE}c"

# Move the compiled .pyc file to the current directory and rename it
mv "__pycache__/"*.pyc ./$OUTPUT_FILE

# Clean up the __pycache__ directory
rm -rf __pycache__

