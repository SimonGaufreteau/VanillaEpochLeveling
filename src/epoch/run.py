import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from epoch.main_script import convert_all_guides

sys.path.append(str(Path(__file__).resolve().parent.parent))

from pathlib import Path

if __name__ == "__main__":
    convert_all_guides()
