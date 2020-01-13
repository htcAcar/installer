import sys, os
import argparse
from mini_installer import file_read
from mini_installer import version
#!/usr/bin/env python -c
# -*- coding: utf-8 -*-


file_name="installation.yaml"

def main():
    parser = argparse.ArgumentParser(description='Does an installation according to installation.yaml file in the current directory.')
    #parser.add_argument('-f', '--file', type=str, metavar=' ', help='Yaml/Yml file of installation description, if it is not provided installation.yaml in the current directory will be used.', required=False)
    parser.add_argument('-v', '--vars', type=str, metavar=' ', help='String variables array like VAR1=value1 VAR2=value2 ', required=False)

    args = parser.parse_args()

    if args.vars is not None:
        version.replace_version_from_cmd(args.vars)

    #if args.file is None:
    if os.path.isfile("installation.yaml") is False:
        parser.print_help()
        file_read.read_yml(input("Please enter a path for yaml file\n"))
        return
    # else:
    #        file_name = args.file

    file_read.read_yml(file_name)

if __name__ == '__main__':
    main()