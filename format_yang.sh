#!/usr/bin/env bash

# Create a temporary file
temp_file=$(mktemp)
input_file="$1"
#pyang --ignore-errors --keep-comments -f yang "$input_file" -o "$temp_file"
pyang --keep-comments -f yang "$input_file" -o "$temp_file"
mv $temp_file $input_file
#gsed -i 's/[ \t]*$//' "$input_file"
