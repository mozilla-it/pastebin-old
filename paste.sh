#!/bin/sh

# Usage info
show_help() {
cat << HELP
Usage: ${0#*/} [-h] [-s SYNTAX] [-t TITLE] [-p POSTER] [-e EXPIRY]
Send stdin to paste.mozilla.org, optionally with syntax/title/poster/expiry specified.
Resulting item will be opened in your browser.
HELP
}

# Process the options
# (getopts code adapted from http://mywiki.wooledge.org/BashFAQ/035#getopts)
params=""
# Trailing colon on option name means it expects a value
while getopts hs:t:p:e: opt; do
    case $opt in
        h)
            show_help
            exit 0
            ;;
        s)  params="$params -F syntax=$OPTARG"
            ;;
        t)  params="$params -F title=$OPTARG"
            ;;
        p)  params="$params -F poster=$OPTARG"
            ;;
        e)  params="$params -F expiry_days=$OPTARG"
            ;;
        *)
            show_help >&2
            exit 1
            ;;
    esac
done
shift "$((OPTIND-1))"

echo "Paste your content now, ^D to submit.\n---"

# make the API call
url=$(echo 'print("hi there")' | curl -s -X POST -F "content=@-" $params https://paste.mozilla.org/api/v2/)
echo -e "---\n$url"

# open in browser
#if [ -x "$(command -v xdg-open)" ];
#then
#xdg-open $url
#else
#    open $url
#fi
