################################################################
#Jones
################################################################

####Eyes
image joneseyes1 = "images/chars/jones/exp/jones_eyes_normal.png"
image joneseyes2 = "images/chars/jones/exp/jones_eyes_mad.png"
image joneseyes3 = "images/chars/jones/exp/jones_eyes_sorry.png"
image joneseyes4 = "images/chars/jones/exp/jones_eyes_surprise.png"
image joneswink = "images/chars/jones/exp/jones_eyes_wink.png"
####Blinking
image jones_blink:
    choice(5.0):
        "joneseyes1"
    choice:
        "joneswink"
        pause 0.1
        "joneseyes1"

    choice:
        "joneswink"
        pause 0.1
        "joneseyes1"
    pause 1.0
    repeat
image jones_blinkmad:
    choice(5.0):
        "joneseyes2"
    choice:
        "joneswink"
        pause 0.1
        "joneseyes2"

    choice:
        "joneswink"
        pause 0.1
        "joneseyes2"
    pause 1.0
    repeat
image jones_blinksorry:
    choice(5.0):
        "joneseyes3"
    choice:
        "joneswink"
        pause 0.1
        "joneseyes3"

    choice:
        "joneswink"
        pause 0.1
        "joneseyes3"
    pause 1.0
    repeat
image jones_blinksurprise:
    choice(5.0):
        "joneseyes4"
    choice:
        "joneswink"
        pause 0.1
        "joneseyes4"
        pause 0.1
        "joneswink"
        pause 0.1
        "joneseyes4"
    choice:
        "joneswink"
        pause 0.1
        "joneseyes4"
    pause 1.0
    repeat
####Eyes
image jones normal:
    LiveComposite (
        (497,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/exp/jones_mouth_normal.png",
        (0,0), "jones_blink",
        (0,0), "images/chars/jones/exp/jones_eyebrows_normal.png"
        )
image jones serious:
    LiveComposite (
        (497,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/exp/jones_mouth_serious.png",
        (0,0), "jones_blink",
        (0,0), "images/chars/jones/exp/jones_eyebrows_serious.png"
        )
image jones mad:
    LiveComposite (
        (497,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/exp/jones_mouth_serious.png",
        (0,0), "jones_blinkmad",
        (0,0), "images/chars/jones/exp/jones_eyebrows_mad.png"
        )
image jones sorry:
    LiveComposite (
        (497,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/exp/jones_mouth_doubt.png",
        (0,0), "jones_blinksorry",
        (0,0), "images/chars/jones/exp/jones_sweat.png",
        (0,0), "images/chars/jones/exp/jones_eyebrows_sorry.png"
        )
image jones smile:
    LiveComposite (
        (497,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/exp/jones_mouth_laugh.png",
        (0,0), "images/chars/jones/exp/jones_eyes_wink.png",
        (0,0), "images/chars/jones/exp/jones_eyebrows_normal.png"
        )
image jones surprise:
    LiveComposite (
        (497,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/exp/jones_mouth_surprise.png",
        (0,0), "jones_blinksurprise",
        (0,0), "images/chars/jones/exp/jones_eyebrows_normal.png"
        )
image jones pleasant:
    LiveComposite (
        (497,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/exp/jones_mouth_laugh.png",
        (0,0), "jones_blink",
        (0,0), "images/chars/jones/exp/jones_eyebrows_normal.png"
        )
image jones doubt:
    LiveComposite (
        (497,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/exp/jones_mouth_doubt.png",
        (0,0), "images/chars/jones/exp/jones_sweat.png",
        (0,0), "images/chars/jones/exp/jones_eyes_doubt.png",
        (0,0), "images/chars/jones/exp/jones_eyebrows_sorry.png"
        )
image jones evil:
    LiveComposite (
        (497,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/exp/jones_mouth_laugh.png",
        (0,0), "images/chars/jones/exp/jones_eyes_cynic.png",
        (0,0), "images/chars/jones/exp/jones_eyebrows_mad.png"
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
