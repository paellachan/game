
################################################################
#RAIN
################################################################
init:


    image rain:

        "fx/rain1.png"
        0.2
        "fx/rain3.png"
        0.2
        "fx/rain2.png"
        0.2
        repeat


################################################################
# tremble
################################################################
init:
    transform my_shake:
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 4 yoffset -4
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
        repeat
################################################################
# tremble
################################################################
init:

    image parabrisas:

        "fx/parabrisas1.png"
        0.2
        "fx/parabrisas2.png"
        0.2
        "fx/parabrisas3.png"
        0.2
        "fx/parabrisas4.png"
        0.2
        "fx/parabrisas3.png"
        0.2
        "fx/parabrisas2.png"
        0.2
        "fx/parabrisas1.png"
        3.0
        repeat