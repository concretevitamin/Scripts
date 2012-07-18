"""
To truncate prefixes in files in given directories. It can be used to fix naming issues raised by Xunlei's offline downloads functionality, for instance.

Usage: trunc.py prefix_to_truncate list_of_directories
"""

# Date: Jul 16, 2012

import os, sys

def main():
    # get list of files in given path
    prefix_to_trunc = sys.argv[1]
    dirs = sys.argv[2:]

    # print files that start with the given string,
    # ask for yes
    files = []
    for directory in dirs:
        files += os.listdir(directory)
    matched_files = filter(lambda st: st.startswith(prefix_to_trunc), files)

    if not matched_files:
        print 'No matched files for prefix "%s".' % prefix_to_trunc
        sys.exit()

    print "Matched files:"
    for file_name in matched_files:
        print "*** " + file_name
    print "\nTruncating...\n",

    # truncate, print success message
    for file_name in matched_files:
        os.rename(file_name, file_name.replace(prefix_to_trunc, '', 1))
    print "Done."

if __name__ == '__main__':
    main()
