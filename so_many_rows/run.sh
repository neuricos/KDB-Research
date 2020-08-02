#!/bin/bash

usage() { echo "Usage: $0 [-c] [-f]" 1>&2; exit 1; }

while getopts ":c:f:" o; do
    case "${o}" in
        c)
            cols=${OPTARG}
            ;;
        f)
            file=${OPTARG}
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND - 1))

if [ -z "${cols}" ] || [ -z "$file" ] ; then
    usage
fi

rm -rf output.txt
for i in {1..3} ; do
    # Clean up
    rm -rf hdb
    mkdir hdb
    python3 gen_q_script.py -c ${cols} -f ${file} > calc.q
    rlwrap q calc.q 2>/dev/null 1>>output.txt
    rm -rf hdb/.DS_Store
    rlwrap q reimport.q 2>/dev/null 1>>output.txt
    echo "" >>output.txt
done

./analyze.rb