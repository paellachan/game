# Reilly

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




