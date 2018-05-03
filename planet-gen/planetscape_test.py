#!/usr/bin/python3

import planetscape, sys

if len(sys.argv) >= 2:
    for i in range(1, int(sys.argv[1])):
        planetscape.main()
else:
    planetscape.main()
