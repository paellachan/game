    # Character list
define md = Character("Detective Reilly", image="reilly")
define wr = Character("Inspector Wright")
define agente = Character("Officer Jones", image="jones")

label start:
    $ quick_menu = False
    stop music
    play music "tension.ogg" fadeout 1.0 fadein 8.0
    # Intro
    scene black with Dissolve(4.0, hard=True)
    $ renpy.pause(4, hard=True)

    show bg_intro with Dissolve(7.0):
        xalign 1.0 yalign 0.0
        pause 2
        ease 28.0 xalign 0.0
    $ renpy.pause(30, hard=True)
    stop music
    scene black with Dissolve(2.0, hard=True)
    $ renpy.pause(3, hard=True)
    show text "West District Commissary, 7:56 P.M." at truecenter
    with dissolve
    $ renpy.pause(4, hard=True)
    hide text
    with dissolve
    jump capitulo1
