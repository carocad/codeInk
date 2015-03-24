"""
daVinci generates html files with drawings of your Python project source code.

Usage:
	daVinci draw
	daVinci -h | --help
	daVinci --version

Options:
	-h --help Show this screen.
	--version Show version.

"""

from os import getcwd
from docopt import docopt
from PkgParser import PkgHandler


def _main():
	'''daVinci generates html files with drawings of your Python project source code.'''
	arguments = docopt(__doc__, version = '0.0.1')

	if arguments['draw']:
		cwd = getcwd()
		pkg = PkgHandler(cwd)
		pkg.parse()

		print(pkg.defsToString())
	else:
		print(__doc__)

if __name__ == '__main__':
	_main()
