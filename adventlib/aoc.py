'Run the given files.'
from pathlib import Path
import sys

def main():
    for path in sys.argv[1:]:
        exec(f"{Path(path).read_text()}main()", dict(__file__ = path))

if '__main__' == __name__:
    main()
