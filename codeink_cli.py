r"""
codeink draws your Python modules into a graph.

Usage:
	codeink draw <directory> [--exclude <pattern>...]
	codeink portrait <filepath>
	codeink blame <filepath> [--exclude <pattern>...]
	codeink trace <filepath>
	codeink (-h | --help)
	codeink --version

Options:
	-h --help	Show this screen.
	--version	Show version.
	--exclude	files to ignore on the analysis (Unix shell-style wildcards)

"""

import os
import sys
import docopt
from codeink import artist
from codeink import __version__

def main(args=None):
	arguments = docopt.docopt(__doc__, version = __version__)

	if arguments['draw']:
		path = os.path.abspath(arguments['<directory>'])
		ignore = arguments['<pattern>']
		artist.draw(path, ignore)
	elif arguments['trace']:
		path = os.path.abspath(arguments['<filepath>'])
		artist.trace(path)
	elif arguments['portrait']:
		path = os.path.abspath(arguments['<filepath>'])
		artist.portrait(path)
	elif arguments['blame']:
		path = os.path.abspath(arguments['<filepath>'])
		ignore = arguments['<pattern>']
		artist.blame(path, ignore)
	else:
		print(__doc__)
	return 0 # success

if __name__ == '__main__':
	status = main()
	sys.exit(status)