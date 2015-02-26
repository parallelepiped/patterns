#!/usr/bin/python
"""
\033[95mrline - an EDA with UNIX core utility\033[0m
"""
import random
import subprocess
import sys, os

__author__ = 'Owen Martin'


def file_len(fname):
    p = subprocess.Popen(['stat', r'-Lf "%z"', fname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip()[1:-1])


def main():
    try:
        filename = sys.argv[1]
        fileobj = file(filename, "rU")
        filelen = file_len(filename)

        displacement = random.randint(1, filelen)
        # print displacement
        fileobj.seek(displacement)
        try:
            next(fileobj)
            output = next(fileobj)
        except StopIteration:
            fileobj.seek(0)
            output = next(fileobj)
        sys.stdout.write(output)

    except Exception:
        print sys.exc_info()[:2]
        print "Usage: rline FILE"


if __name__ == "__main__":
    main()