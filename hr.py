#!/usr/bin/env python
import math
import os
import sys


def hr(*symbols):
    symbols = symbols or ('#', )
    
    cols = _get_terminal_size()[0]
    
    for symbol in symbols:
        repeat_count = int(math.ceil(float(cols) / len(symbol)))
        output = symbol * repeat_count
        print output[:cols]


def cli():
    args = sys.argv[1:]
    hr(*args)


def _get_terminal_size():
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct
            cr = \
                struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
        except:
            return
        return cr
    
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

    return int(cr[1]), int(cr[0])


if __name__ == '__main__':
    cli()
