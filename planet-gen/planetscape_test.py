#!/usr/bin/python3

import sys

from planetscape import Planetscape

if len(sys.argv) >= 2:
    for i in range(1, int(sys.argv[1])):
        p = Planetscape()
        p.main()
        print("\n")
else:
    planetscape.main()
