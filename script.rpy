# Character list
define md = Character("Detective Reilly", image="reilly")
define mdpov = Character("Detective Reilly", image="none")
define wr = Character("Inspector Wright", image="victoria")
define agente = Character("Officer Jones", image="jones")
define c = Character("Mrs.Cordelia Goldberg")
define n = Character("Housekeeper Nelly")

label start:
    $ quick_menu = False
    stop music
    play music "music_tension.ogg" fadeout 1.0 fadein 8.0
    # Intro
    scene black with Dissolve(4.0, hard=True)
    $ renpy.pause(3, hard=True)

    show bg_intro with Dissolve(7.0):
        xalign 1.0 yalign 0.0
        pause 5
        ease 27.0 xalign 0.0
    $ renpy.pause(27, hard=True)
    stop music
    scene black with Dissolve(2.0, hard=True)
    $ renpy.pause(3, hard=True)
    show text "West District Commissary, 7:56 P.M." at truecenter
    with dissolve
    $ renpy.pause(4, hard=True)
    hide text
    with dissolve
    jump capitulo1
