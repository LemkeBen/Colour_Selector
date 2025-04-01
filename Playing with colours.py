import time

from matplotlib.colors import hsv_to_rgb
import numpy as np
import matplotlib.pyplot as plt
import keyboard
x = 35

while True:
    if keyboard.is_pressed('a'):
        print('a')
        if x != 255:
            x+=1
        else:
             x=0

        plt.subplot(1, 2, 1)
        plt.imshow(hsv_to_rgb([[[x / 255, 1, 1]]]))

        time.sleep(0.05)

    elif keyboard.is_pressed('d'):
        print('d')
        if x != 0:
            x-=1
        else:
            x=255

        plt.subplot(1, 2, 1)
        plt.imshow(hsv_to_rgb([[[x / 255, 1, 1]]]))

        time.sleep(0.05)

    elif keyboard.is_pressed('s'):
        time.sleep(0.05)
        print(x)
    else:
        x=x

    plt.subplot(1, 2, 1)
    plt.imshow(hsv_to_rgb([[[x/255,1,1]]]))

    plt.show()





