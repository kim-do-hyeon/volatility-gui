import os
import sys
from src.util import *

def main():
    if not is_pyqt5_exists():
        print()
        print('='*50)
        print('You need a PyQt5 to run this program.')
        print('Install PyQt5 by entering the following command in the terminal')
        print()
        print('pip install pyqt5')
        print('='*50)
        print()
        sys.exit()

    create_directory('lib')
    create_directory('case')
    create_directory('src/data')

    import src.main as ui
    ui.main()


if __name__ == "__main__":
    main()
