label capitulo2:
    scene black with Dissolve(4.0)
    play music "music_sad.ogg" fadeout 1.0 fadein 8.0
    play audio "audio_rain.ogg"
    $ quick_menu = False
    scene bg_policestation at my_shake
    show victoria worried car at my_shake
    show parabrisas at my_shake
    show rain
    $ quick_menu = True


    md "{i}Y aquí estoy, en la puerta de la comisaría esperando a Victoria bajo la lluvia. Dios...debería estar cenando con Charlenne.{/i}"

    md "{i}¿Es que Dios me odia?{/i}"

    md "{i}Pero da igual...Algo en mi me impedía dejarla tirada esta noche gris y tormentosa.{/i}"
    md "{i}Hablando de Victoria...¿Dónde diablos se ha metido?{/i}"
    md "{i}¿Dónde diablos te has metido, jefa? Me estoy congelado.{/i}"
    md "{i}Esto es horrible en serio...{/i}"

    return
