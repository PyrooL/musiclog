import sys
from cli import main_cli

def main():
    if len(sys.argv) == 1 or '--gui' in sys.argv:
        # can probably handle this better with click
        sys.argv.remove('--gui')
        # main_gui()
        print("PLACEHOLDER: GUI not implemented yet, please use CLI interface :)")
    else: 
        main_cli()

if __name__ == "__main__":
    main()
