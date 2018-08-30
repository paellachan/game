

label evidences1:

    scene black with Dissolve(4.0)
    play music "music_car.ogg" fadeout 1.0 fadein 8.0
    window hide
    scene bg_casafuera
    stop audio
    stop music
    # play audio "audio_carstop.ogg"  fadein 5.0
    show car at carfx
    show rainh
    pause 5
    # play audio "audio_cardoor.ogg"
    pause 2
    show victoria thinkingumb with dissolve
    show rainh
    call InventoryInit
    show screen InvenBase


    wr"So here we are."
    md normal"yep"
    wr"You can ask me anything"
    $ InventoryAdd("Temp3")
    wr"I just added something to the inventory"
    md normal"Don't you tell me"
    md normal"What is it?"
    $ ItemUpdate(
        "Temp3",
         image="clue3",
         text="I'm replacing this item's text with new information!",
    )
    md normal"Don't you tell me"
    md normal"What is it?"
    return
