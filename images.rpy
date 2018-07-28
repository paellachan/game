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
# Reilly
################################################################
image side reilly normal = Image("chars/reilly/reilly normal.png", xalign=0.0, yalign=1.0)
image side reilly huh = Image("chars/reilly/reilly huh.png", xalign=0.0, yalign=1.0)
image side reilly angry = Image("chars/reilly/reilly angry.png", xalign=0.0, yalign=1.0)
image side reilly doubt = Image("chars/reilly/reilly doubt.png", xalign=0.0, yalign=1.0)
image side reilly happy = Image("chars/reilly/reilly happy.png", xalign=0.0, yalign=1.0)
image side reilly mad = Image("chars/reilly/reilly mad.png", xalign=0.0, yalign=1.0)
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

# name of the character.
