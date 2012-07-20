"""
To truncate prefixes in files in given directories. It can be used to fix naming issues raised by Xunlei's offline downloads functionality, for instance.

Usage: trunc.py prefix_to_truncate list_of_directories
"""

# Date: Jul 16, 2012

import os, os.path, sys

def main():
    # get list of files in given path
    prefix_to_trunc = sys.argv[1]
    dirs = sys.argv[2:]

    # print files that start with the given string,
    files = {}
    matched_files = {}
    for directory in dirs:
        files[directory] = os.listdir(directory)
    for directory in files:
	matched = filter(lambda st: st.startswith(prefix_to_trunc), files[directory])
	if matched: matched_files[directory] = matched

    if not matched_files:
        print 'No matched files for prefix "%s".' % prefix_to_trunc
        sys.exit()

    print "Matched files:\n"
    for file_name in sum(matched_files.values(), []):
        print "\t" + file_name
    print "\nTruncating...",

    # truncate, print success message
    for directory in matched_files:
	for file_name in matched_files[directory]:
	    os.rename(os.path.join(directory, file_name), os.path.join(directory, file_name.replace(prefix_to_trunc, '', 1)))

    print "Done."

if __name__ == '__main__':
    main()
