# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import textwrap


def phanpy_say(text, length=40):
    return build_bubble(text, length) + build_phanpy()


def build_phanpy():
    return '''
         \   ／￣￣￣￣ヽ
          \ ｜・ Ｕ     |
            ｜|(ﾉ       |つ
            L||_|￣ ￣|_|
    '''


def build_bubble(text, length=40):
    bubble = []

    lines = normalize_text(text, length)

    border_size = len(lines[0])

    bubble.append('  ' + '_' * border_size)

    for index, line in enumerate(lines):
        border = get_border(lines, index)

        bubble.append('%s %s %s' % (border[0], line, border[1]))

    bubble.append('  ' + '-' * border_size)

    return '\n'.join(bubble)


def normalize_text(text, length):
    lines = textwrap.wrap(text, length)
    max_length = len(max(lines, key=len))
    return [line.ljust(max_length) for line in lines]


def get_border(lines, index):
    if len(lines) < 2:
        return ['<', '>']

    elif index == 0:
        return ['/', '\\']

    elif index == len(lines) - 1:
        return ['\\', '/']

    else:
        return ['|', '|']


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: phan.py [message]')
        sys.exit(0)

    print(phanpy_say(sys.argv[1]))
