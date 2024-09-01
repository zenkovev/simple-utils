#!/bin/bash

# ./chmod_actions.sh ../main

MY_DIR_PATH=$1
find $MY_DIR_PATH -type f -exec chmod 664 {} \;
find $MY_DIR_PATH -type d -exec chmod 775 {} \;

