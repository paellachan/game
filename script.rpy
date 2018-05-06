    # Character list
define md = Character("Detective Reilly", image="reilly")
define wr = Character("Inspector Wright")
define agente = Character("Officer Jones", image="jones")



label start:

    # Intro

    scene black with dissolve
    pause 3

    show bg_intro with Dissolve(5.0):
        xalign 1.0 yalign 0.0
        pause 2
        ease 15.0 xalign 0.0

    $ renpy.pause(20, hard=True)
    jump capitulo1
