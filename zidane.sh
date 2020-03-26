#!/bin/bash

PROJECT_DIR=`dirname $0`
VIRTUALENV=$PROJECT_DIR/venv/bin/activate
MAIN=$PROJECT_DIR/main.py

source $VIRTUALENV && python3 $MAIN
