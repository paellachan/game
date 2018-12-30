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
####umbrella expressions
################################################
image victoria thinkingumb:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_rain.png",
        (0,0), "images/chars/wright/victoria_thinking.png",
        (0,0), "victoria_blink",
        )
image victoria normalumb:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_rain.png",
        (0,0), "images/chars/wright/victoria_normal.png",
        (0,0), "victoria_blink",
        )
image victoria smileumb:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_rain.png",
        (0,0), "images/chars/wright/victoria_surprised.png",
        (0,0), "victoria_blink",
        )
image victoria seriousumb:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_rain.png",
        (0,0), "images/chars/wright/victoria_serious.png",
        (0,0), "victoria_blink",
        )

image victoria shockedumb:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_rain.png",
        (0,0), "images/chars/wright/victoria_shocked.png",
        (0,0), "victoria_blink",
        )
image victoria okayumb:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_rain.png",
        (0,0), "images/chars/wright/victoria_okay.png",
        )
image victoria realizingumb:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_rain.png",
        (0,0), "images/chars/wright/victoria_realizing.png",
        )
image victoria madumb:
    LiveComposite (
        (922,1093),
        (0,0), "images/chars/wright/victoria_body_rain.png",
        (0,0), "images/chars/wright/victoria_reading.png",
        )
################################################
####Car expressions
################################################
image victoria thinkingcar:
    contains:
        LiveComposite (
            (922,1093),
            (80,70), "images/chars/wright/victoria_thinking.png",
            )
        my_shake
image victoria worriedcar:
    contains:
        LiveComposite (
            (922,1093),
            (80,70), "images/chars/wright/victoria_worried.png",
            (80,70), "victoria_blink",
            )
        my_shake
image victoria readingcar:
    contains:
        LiveComposite (
            (922,1093),
            (80,70), "images/chars/wright/victoria_reading.png",
            (80,70), "victoria_blink",
            )
        my_shake
image victoria realizingcar:
    contains:
        LiveComposite (
            (922,1093),
            (80,70), "images/chars/wright/victoria_realizing.png",
            (80,70), "victoria_blink",
            )
        my_shake
image victoria normalcar:
    contains:
        LiveComposite (
            (922,1093),
            (80,70), "images/chars/wright/victoria_normal.png",
            (80,70), "victoria_blink",
            )
        my_shake
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
image jones scared:
    LiveComposite (
        (501,912),
        (0,0), "images/chars/jones/jones_body.png",
        (0,0), "images/chars/jones/jones_scared.png",
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
image reilly doubtcar:
    contains:
            LiveComposite (
            (345,443),
            (820,170), "images/chars/reilly/reilly_doubt.png",
            (820,170), "reilly_blink",
            )
            img_scale
            my_shake
image reilly surprisedcar:
    contains:
            LiveComposite (
            (345,443),
            (820,170), "images/chars/reilly/reilly_surprisedcar.png",
            (820,170), "reilly_blink",
            )
            img_scale
            my_shake
image reilly failcar:
    contains:
            LiveComposite (
            (345,443),
            (820,170), "images/chars/reilly/reilly_fail.png",
            (820,170), "reilly_blink",
            )
            img_scale
            my_shake
image reilly failcar2:
    contains:
            LiveComposite (
            (345,443),
            (820,170), "images/chars/reilly/reilly_fail2.png",
            )
            img_scale
            my_shake
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
image reilly doomedcar:
    contains:
            LiveComposite (
            (345,443),
            (820,170), "images/chars/reilly/reilly_doomed.png",
            )
            img_scale
            my_shake
image reilly shycar:
    contains:
            LiveComposite (
            (345,443),
            (820,170), "images/chars/reilly/reilly_shy.png",
            (820,170), "reilly_blink",
            )
            img_scale
            my_shake
image reilly thinkingcar:
    contains:
            LiveComposite (
            (345,443),
            (820,170), "images/chars/reilly/reilly_thinking.png",
            )
            img_scale
            my_shake
image reilly car:
    contains:
            LiveComposite (
            (345,443),
            (820,170), "images/chars/reilly/reilly_car.png",
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
image side reilly huh:
    contains:
            LiveComposite (
            (345,443),
            (30,0), "images/chars/reilly/reilly_body.png",
            (30,0), "images/chars/reilly/reilly_huh.png",
            (30,0), "reilly_blink",
            )
            img_align
image side reilly angry:
    contains:
            LiveComposite (
            (345,443),
            (30,0), "images/chars/reilly/reilly_body.png",
            (30,0), "images/chars/reilly/reilly_angry.png",
            (30,0), "reilly_blink",
            )
            img_align
image side reilly doubt:
    contains:
            LiveComposite (
            (345,443),
            (30,0), "images/chars/reilly/reilly_body.png",
            (30,0), "images/chars/reilly/reilly_doubt.png",
            (30,0), "reilly_blink",
            )
            img_align
image side reilly happy:
    contains:
            LiveComposite (
            (345,443),
            (30,0), "images/chars/reilly/reilly_body.png",
            (30,0), "images/chars/reilly/reilly_happy.png",
            )
            img_align
image side reilly mad:
    contains:
            LiveComposite (
            (345,443),
            (30,0), "images/chars/reilly/reilly_body.png",
            (30,0), "images/chars/reilly/reilly_mad.png",
            (30,0), "reilly_blink",
            )
            img_align
image side reilly proud:
    contains:
            LiveComposite (
            (345,443),
            (30,0), "images/chars/reilly/reilly_body.png",
            (30,0), "images/chars/reilly/reilly_proud.png",
            )
            img_align
image side reilly surprised:
    contains:
            LiveComposite (
            (345,443),
            (30,0), "images/chars/reilly/reilly_body.png",
            (30,0), "images/chars/reilly/reilly_surprised.png",
            (30,0), "reilly_blink",
            )
            img_align
image side reilly doomed:
    contains:
            LiveComposite (
            (345,443),
            (30,0), "images/chars/reilly/reilly_body.png",
            (30,0), "images/chars/reilly/reilly_doomed.png",
            )
            img_align
image side reilly worried:
    contains:
            LiveComposite (
            (345,443),
            (30,0), "images/chars/reilly/reilly_body.png",
            (30,0), "images/chars/reilly/reilly_worried.png",
            (30,0), "reilly_blink",
            )
            img_align
image side reilly shy:
    contains:
            LiveComposite (
            (345,443),
            (30,0), "images/chars/reilly/reilly_body.png",
            (30,0), "images/chars/reilly/reilly_shy.png",
            (30,0), "reilly_blink",
            )
            img_align
image side reilly fool:
    contains:
            LiveComposite (
            (345,443),
            (30,0), "images/chars/reilly/reilly_body.png",
            (30,0), "images/chars/reilly/reilly_fool.png",
            )
            img_align
image side reilly thinking:
    contains:
            LiveComposite (
            (345,443),
            (30,0), "images/chars/reilly/reilly_body.png",
            (30,0), "images/chars/reilly/reilly_thinking.png",
            )
            img_align
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
################################################################
#Nelly
################################################################
####Blinking
image nelly_blink:
    choice(5.0):
        "victoriablank"
    choice:
        "nellyblink"
        pause 0.1
        "victoriablank"

    choice:
        "nellyblink"
        pause 0.1
        "victoriablank"
    pause 1.0
    repeat
####Body
image nelly normal:
    LiveComposite (
        (458,770),
        (0,0), "images/chars/nelly/body.png",
        (0,0), "images/chars/nelly/normal.png",
        (0,0), "nelly_blink",
        )
image nelly doubt:
    LiveComposite (
        (458,770),
        (0,0), "images/chars/nelly/body.png",
        (0,0), "images/chars/nelly/doubt.png",
        (0,0), "nelly_blink",
        )
image nelly huh:
    LiveComposite (
        (458,770),
        (0,0), "images/chars/nelly/body.png",
        (0,0), "images/chars/nelly/huh.png",
        (0,0), "nelly_blink",
        )
image nelly mad:
    LiveComposite (
        (458,770),
        (0,0), "images/chars/nelly/body.png",
        (0,0), "images/chars/nelly/mad.png",
        (0,0), "nelly_blink",
        )
image nelly shocked:
    LiveComposite (
        (458,770),
        (0,0), "images/chars/nelly/body.png",
        (0,0), "images/chars/nelly/shocked.png",
        (0,0), "nelly_blink",
        )
image nelly smile:
    LiveComposite (
        (458,770),
        (0,0), "images/chars/nelly/body.png",
        (0,0), "images/chars/nelly/smile.png",
        )
image nelly surprised:
    LiveComposite (
        (458,770),
        (0,0), "images/chars/nelly/body.png",
        (0,0), "images/chars/nelly/surprised.png",
        (0,0), "nelly_blink",
        )
image nelly troubled:
    LiveComposite (
        (458,770),
        (0,0), "images/chars/nelly/body.png",
        (0,0), "images/chars/nelly/troubled.png",
        (0,0), "nelly_blink",
        )
