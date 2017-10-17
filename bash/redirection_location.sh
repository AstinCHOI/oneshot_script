#!/bin/bash

## help
# IFS='' (or IFS=) prevents leading/trailing whitespace from being trimmed.
# -r prevents backslash escapes from being interpreted.
# || [[ -n $line ]] prevents the last line from being ignored if it doesn't end with a \n (since read returns a non-zero exit code when it encounters EOF).

filename="$1"

while IFS='' read -r line || [[ -n "$line" ]]; do
    # For URLencode
	# line=$(python -c "import sys, urllib as ul; print ul.quote_plus('$line')")
	kurl=$(curl -s -I -X GET $line | grep Location)
	location="${kurl:10}"
	if [[ -z $location ]]; then
		echo "## $line"
	else
		echo "${kurl:10}" # Location :
	fi
done < "$filename"
