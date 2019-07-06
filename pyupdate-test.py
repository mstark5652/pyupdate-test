#
# Created by mstark on July 5, 2019
#
# Copyright 2019 Michael Stark. All Rights Reserved.
#

import os, sys, argparse
from config import VERSION

def main(options):

    if options.version:
        print("pyupdate-test {}".format(VERSION))
        sys.exit(0)
    print("Hello!")

def parse(argv):

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action="store_true", help="Print the current version number.")

    return parser.parse_args(args=argv)

if __name__ == "__main__":
    argv = sys.argv[1:]
    main(parse(argv))

