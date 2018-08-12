################################################################
#Victoria
################################################################
####Blinking
image victoria_blink:
    choice(5.0):
        "victoriablank"
    choice:
        "victoriablink"
        pause 0.1
        "victoriablank"

    choice:
        "victoriablink"
        pause 0.1
        "victoriablank"
    pause 1.0
    repeat
####Body
image victoria shy:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_normal.png",
        (0,0), "images/chars/wright/victoria_shy.png",
        (0,0), "victoria_blink",
        )
image victoria shocked:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_normal.png",
        (0,0), "images/chars/wright/victoria_shocked.png",
        (0,0), "victoria_blink",
        )
image victoria serious:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_normal.png",
        (0,0), "images/chars/wright/victoria_serious.png",
        )
image victoria normal:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_normal.png",
        (0,0), "images/chars/wright/victoria_normal.png",
        (0,0), "victoria_blink",
        )
image victoria okay:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_normal.png",
        (0,0), "images/chars/wright/victoria_okay.png",
        )
image victoria smile:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_normal.png",
        (0,0), "images/chars/wright/victoria_smile.png",
        (0,0), "victoria_blink",
        )
image victoria surprised:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_normal.png",
        (0,0), "images/chars/wright/victoria_surprised.png",
        (0,0), "victoria_blink",
        )
image victoria thinking:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_cross.png",
        (0,0), "images/chars/wright/victoria_thinking.png",
        (0,0), "victoria_blink",
        )
image victoria worried:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_normal.png",
        (0,0), "images/chars/wright/victoria_worried.png",
        (0,0), "victoria_blink",
        )
################################################
####Car expressions
################################################
image victoria worried car:
    LiveComposite (
        (922,1093),
        (80,70), "images/chars/wright/victoria_worried.png",
        (80,70), "victoria_blink",
        )
################################################################
#Jones
################################################################

####Blinking
image jones_blink:
    choice(5.0):
        "jonesblank"
    choice:
        "jonesblink"
        pause 0.1
        "jonesblank"

    choice:
        "jonesblink"
        pause 0.1
        "jonesblank"
    pause 1.0
    repeat

image jones normal:
    LiveComposite (
        (501,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/jones_normal.png",
        (0,0), "jones_blink",
        )
image jones serious:
    LiveComposite (
        (501,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/jones_serious.png",
        (0,0), "jones_blink",
        )
image jones mad:
    LiveComposite (
        (501,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/jones_mad.png",
        (0,0), "jones_blink",
        )
image jones sorry:
    LiveComposite (
        (501,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/jones_sorry.png",
        (0,0), "jones_blink",
        )
image jones smile:
    LiveComposite (
        (501,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/jones_smile.png",
        (0,0), "jones_blink",
        )
image jones surprise:
    LiveComposite (
        (501,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/jones_surprised.png",
        (0,0), "jones_blink",
        )
image jones pleasant:
    LiveComposite (
        (501,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/jones_pleasant.png",
        (0,0), "jones_blink",
        )
image jones doubt:
    LiveComposite (
        (501,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/jones_doubt.png",
        (0,0), "jones_blink",
        )
image jones evil:
    LiveComposite (
        (501,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/jones_evil.png",
        (0,0), "jones_blink",
        )


################################################################
#Cordelia
################################################################
####Blinking
image dog_blink:
    choice(4.0):
        "victoriablank"
    choice:
        "dogblink"
        pause 0.1
        "victoriablank"

    choice:
        "dogblink"
        pause 0.1
        "victoriablank"
    pause 2.0
    repeat

image cordelia_blink:
    choice(5.0):
        "victoriablank"
    choice:
        "cordeliablink"
        pause 0.1
        "victoriablank"

    choice:
        "cordeliablink"
        pause 0.1
        "victoriablank"
    pause 1.0
    repeat
####Body
image cordelia annoyed:
    LiveComposite (
        (416,890),
        (0,0), "images/chars/cordelia/cordelia_body.png",
        (0,0), "images/chars/cordelia/cordelia_annoyed.png",
        (0,0), "dog_blink",
        )
image cordelia smile:
    LiveComposite (
        (416,890),
        (0,0), "images/chars/cordelia/cordelia_body.png",
        (0,0), "images/chars/cordelia/cordelia_smile.png",
        (0,0), "cordelia_blink",
        (0,0), "dog_blink",
        )
image cordelia surprised:
    LiveComposite (
        (416,890),
        (0,0), "images/chars/cordelia/cordelia_body.png",
        (0,0), "images/chars/cordelia/cordelia_surprised.png",
        (0,0), "cordelia_blink",
        (0,0), "dog_blink",
        )
image cordelia thinking:
    LiveComposite (
        (416,890),
        (0,0), "images/chars/cordelia/cordelia_body.png",
        (0,0), "images/chars/cordelia/cordelia_thinking.png",
        (0,0), "cordelia_blink",
        (0,0), "dog_blink",
        )
image cordelia normal:
    LiveComposite (
        (416,890),
        (0,0), "images/chars/cordelia/cordelia_body.png",
        (0,0), "images/chars/cordelia/cordelia_normal.png",
        (0,0), "cordelia_blink",
        (0,0), "dog_blink",
        )
################################################################
# Reilly
################################################################
# Blinking
################################################################
image reilly_blink:
    choice(4.0):
        "reillyblank"
    choice:
        "reillyblink"
        pause 0.1
        "reillyblank"

    choice:
        "reillyblink"
        pause 0.1
        "reillyblank"
    pause 2.0
    repeat
# Side image positioning amd scaling
################################################################
transform img_align:
    xalign 0.0 yalign 1.0

transform img_scale:
    xzoom 1.29 yzoom 1.29
# Car images
################################################################
image reilly normalcar:
    contains:
            LiveComposite (
            (345,443),
            (820,170), "images/chars/reilly/reilly_normal.png",
            (820,170), "reilly_blink",
            )
            img_scale
            my_shake
image reilly madcar:
    contains:
            LiveComposite (
            (345,443),
            (820,170), "images/chars/reilly/reilly_mad.png",
            (820,170), "reilly_blink",
            )
            img_scale
            my_shake
# Side Images
################################################################
image side reilly normal:
    contains:
            LiveComposite (
            (345,443),
            (30,0), "images/chars/reilly/reilly_body.png",
            (30,0), "images/chars/reilly/reilly_normal.png",
            (30,0), "reilly_blink",
            )
            img_align

image side reilly huh = Image("chars/reilly/reilly huh.png", xalign=0.0, yalign=1.0)
image side reilly angry = Image("chars/reilly/reilly angry.png", xalign=0.0, yalign=1.0)
image side reilly doubt = Image("chars/reilly/reilly doubt.png", xalign=0.0, yalign=1.0)
image side reilly happy = Image("chars/reilly/reilly happy.png", xalign=0.0, yalign=1.0)
image side reilly mad :
    contains:
            LiveComposite (
            (345,443),
            (30,0), "images/chars/reilly/reilly_body.png",
            (30,0), "images/chars/reilly/reilly_mad.png",
            (30,0), "reilly_blink",
            )
            img_alignR
image side reilly proud = Image("chars/reilly/reilly proud.png", xalign=0.0, yalign=1.0)
image side reilly surprised = Image("chars/reilly/reilly surprised.png", xalign=0.0, yalign=1.0)
image side reilly doomed = Image("chars/reilly/reilly doomed.png", xalign=0.0, yalign=1.0)
image side reilly worried = Image("chars/reilly/reilly worried.png", xalign=0.0, yalign=1.0)
image side reilly shy = Image("chars/reilly/reilly shy.png", xalign=0.0, yalign=1.0)
image side reilly fool = Image("chars/reilly/reilly fool.png", xalign=0.0, yalign=1.0)
image side reilly thinking = Image("chars/reilly/reilly thinking.png", xalign=0.0, yalign=1.0)
transform change_transform(old, new):
    contains:
        old
        alpha 1.0
        linear 0.3 alpha 0.0
    contains:
        new
        alpha 0.0
        linear 0.3 alpha 1.0

define config.side_image_change_transform = change_transform
