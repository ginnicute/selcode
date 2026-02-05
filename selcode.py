#!/usr/bin/env python3
import random
import sys
import argparse

def generate_code():
    """generating multiple codes."""
    first_part = random.randint(0, 999)
    second_part = random.randint(0, 999)
    return f"{first_part:03d}-{second_part:03d}"

def show_ascii_art():
    """Display ASCII art banner"""
    return """
.oPYo.        8                    8
8             8                    8
`Yooo. .oPYo. 8 .oPYo. .oPYo. .oPYo8 .oPYo.
    `8 8oooo8 8 8    ' 8    8 8    8 8oooo8
     8 8.     8 8    . 8    8 8    8 8.
`YooP' `Yooo' 8 `YooP' `YooP' `YooP' `Yooo'
:.....::.....:..:.....::.....::.....::.....:
::::::::::::::::::::::::::::::::::::::::::::
::::::::by Ginnicute::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::
"""

def main():
    # Create description with ASCII art
    description = f"""{show_ascii_art()}
generator verification codes for cliens.
    """

    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
  Using:
  %(prog)s gen              generate 1 code
  %(prog)s gen -n 5         generate N codes
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commads:')

    # gen
    gen_parser = subparsers.add_parser('gen',
                                      help='generate verification codes',
                                      epilog="""
Examples:
  selcode gen              # 1 code
  selcode gen -n 5         # 5 codes
  selcode gen --number 10  # 10 codes
                                      """)

    gen_parser.add_argument('-n', '--number',
                          type=int,
                          default=1,
                          metavar='Number of codes to generate. (Default: 1)',
                          help='')

    args = parser.parse_args()

    if args.command == 'gen':
        if args.number < 1:
            print("Error: The number of codes must be a positive number.", file=sys.stderr)
            sys.exit(1)

        for i in range(args.number):
            code = generate_code()
            print(f"Ваш код-подтверждение: {code}")

    elif not args.command:
        parser.print_help()

    else:
        print(f"Error! Unknow argument: {args.command}", file=sys.stderr)
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
