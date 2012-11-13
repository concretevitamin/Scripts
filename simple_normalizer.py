"""Usage: python simple_normalize
The script reads multiple lines from stdin, treating each line as a path to
normalize, and prints normalized paths to stdout one per line.
"""
import sys

def simple_normalize(paths):
    """Given a list of paths, return a list of normalized paths."""
    res = []
    for path in paths:
        splits = path.strip().split('/')
        if splits[-1] == '.': splits.append('')
        take = [False] * len(splits)
        for i in xrange(0, len(splits)):
            if splits[i] == '..' and i > 0: take[i - 1] = False
            if splits[i] not in ['.', '..']: take[i] = True
        res.append('/'.join([tup[0] for tup in zip(splits, take) if tup[1]]))
    return res

if __name__ == '__main__':
    print '\n'.join(simple_normalize(sys.stdin.readlines()))
