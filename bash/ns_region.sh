#!/bin/bash

getopts "foO" option
shift $(expr $OPTIND - 1)
cpcode="$1"

case $option in
        f)
                $COMMAND1
                ;;
        o)
                $COMMAND2
                ;;
        O)
                $COMMAND3
                ;;
        \?)
                echo -e "Usage: nsregion [OPTION] CPCODE
ex) Filestore: $nsregion -f 123456
ex) objectstore (NSDS): $nsregion -o 123456
ex) objectstore (NSOS): $nsregion -O 123456"
                ;;
esac