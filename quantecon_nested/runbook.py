from jupyter_book.commands import main
from pathlib import Path
import shutil
import context

if __name__ == "__main__":
    build_dir = context.this_dir / "mini_book/_build"
    if build_dir.is_dir():
        print(f"removing {build_dir}")
        shutil.rmtree(build_dir)
    else:
        print(f"couldn't fine {build_dir}")
    main()
