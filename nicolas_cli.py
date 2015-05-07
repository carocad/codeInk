r"""
nicolas draws your Python modules into a graph.

Usage:
	nicolas draw <directory> [--ignore <pattern>...]
	nicolas portrait <filepath>
	nicolas blame <filepath>
	nicolas trace <filepath>
	nicolas (-h | --help)
	nicolas --version

Options:
	-h --help	Show this screen.
	--version	Show version.
	--ignore	Pattern to ignore.

"""

import os
import sys
import docopt
from nicolas import artist
from nicolas import __version__

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
		print(' Coming soon :)')
	elif arguments['blame']:
		print(' Coming soon :)')
	else:
		print(__doc__)
	return 0 # success

if __name__ == '__main__':
	status = main()
	sys.exit(status)
