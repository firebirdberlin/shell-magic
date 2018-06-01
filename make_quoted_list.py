#!/usr/bin/env python3

import mimetypes
import sys
import os


def exit_error(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    exit(-1)


filename = sys.argv[1] if len(sys.argv) > 1 else None

if not filename or not os.path.exists(filename):
    exit_error(f'File not found {filename}')

mime_type, encoding = mimetypes.guess_type(filename)

if not mime_type.startswith('text/'):
    exit_error(f'Wrong mime type: {mime_type}')

items = []
with open(filename, 'r') as f:
    items = [line.strip() for line in f.readlines()]

for item in items[:-1]:
    print(f"'{item}',", end='')

print(f"'{items[-1]}'")
