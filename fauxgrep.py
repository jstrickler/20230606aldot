import fileinput
from argparse import ArgumentParser
import re
import logging

logging.basicConfig(
    filename="fauxgrep.log",
)
logger = logging.getLogger()

parser = ArgumentParser(description="Faux grep")

parser.add_argument('-i', dest="ignorecase", action="store_true", help="Ignore case")
parser.add_argument('-n', dest="lineno", action="store_true", help="Show line numbers")
parser.add_argument('-f', dest="filename", action="store_true", help="Show file names")
parser.add_argument('-d', dest="debug", action="store_true", help="Output debugging info")
parser.add_argument('search_term', help='Search term')
parser.add_argument("file_paths", help="Files to search", nargs="*")

options = parser.parse_args()   # auto-uses sys.argv

if options.debug:
    logger.setLevel(logging.DEBUG)

rx = re.compile(options.search_term, re.I if options.ignorecase else 0) 

logging.info("Search term: %s", options.search_term)

for raw_line in fileinput.input(options.file_paths):
    if rx.search(raw_line):  # if rx matches line
        line = raw_line.rstrip()
        if options.filename:
            print(fileinput.filename(), end=" ")
        if options.lineno:
            print(fileinput.filelineno(), end=" ")
        print(line)



