from matplotlib.colors import hsv_to_rgb
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
x = 100

while True:
    more_or_less = input("a or d?")
    if more_or_less == "a":
        if x != 255:
            x+=1
        else:
            print("Max")
    elif more_or_less == "d":
        if x != 0:
            x-=1
        else:
            print("Min")
    elif more_or_less == "show":
        print(x)
    else:
        print("error")

    plt.subplot(1, 2, 1)
    plt.imshow(hsv_to_rgb(np.full((100, 100, 3), fill_value=x, dtype=np.uint8) / 255.0))

    plt.show()




