#!/usr/bin/env python3

import subprocess
import sys
import time


# === Configure these ===

PRINT_FORMAT = '{}'
POLL_TIME_SECONDS = 0.3
XCLIP_CHANT = 'xclip -selection clipboard -o'.split()


# === Boring code ===

def get_clipboard():
    xclip_result = subprocess.run(
        XCLIP_CHANT,
        stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
        universal_newlines=True
    )
    if xclip_result.returncode != 0:
        print('scrape_clipboard.py: error while reading clipboard, aborting.',
              file=sys.stderr)
        exit(2)
    return xclip_result.stdout


def run():
    try:
        last = None
        while True:
            current = get_clipboard()
            if last != current:
                print(PRINT_FORMAT.format(current), flush=True)
                last = current
            time.sleep(POLL_TIME_SECONDS)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('usage: {}  # No options.  Use the source, Luke!'.format(sys.argv[0]),
              file=sys.stderr)
        exit(1)
    print('Hit Ctrl-C to stop.', file=sys.stderr)
    run()
