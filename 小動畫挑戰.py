# Easy animation

import time , sys
dot = 1
increasingDot = True

try:
    while True:
        print('.' * dot)
        time.sleep(0.2)

        if increasingDot:
            dot = dot +1
            if dot == 3:
                increasingDot = False

        else:
            dot = dot -1
            if dot == 1:
                increasingDot = True

except KeyboardInterrupt:
    sys.exit()