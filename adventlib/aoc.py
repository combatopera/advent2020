from pathlib import Path
import sys

def main():
    for path in map(Path, sys.argv[1:]):
        exec(f"{path.read_text()}main()", {})

if '__main__' == __name__:
    main()
