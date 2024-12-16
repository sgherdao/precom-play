#!/usr/bin/env bash

rc=0

for input_file in "$@"; do
    temp_file=$(mktemp)
    printf "\nprocessing $input_file"
    if pyang --keep-comments -f yang -p "$NCS_DIR/src/ncs/yang:BB-Automation/packages" "$input_file" -o "$temp_file"; then
        if ! cmp -s "$input_file" "$temp_file"; then
            mv "$temp_file" "$input_file"
            printf "modified $input_file"
            rc=1
        else
            rm "$temp_file"
            printf "No changes made to $input_file"
        fi
    else
        rm "$temp_file"
        printf "Failed to format $input_file"
        rc=1
    fi
done

exit $rc
