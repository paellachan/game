

label evidences1:

    scene black with Dissolve(4.0)
    play music "music_car.ogg" fadeout 1.0 fadein 8.0
    window hide
    scene bg_casafuera
    stop audio
    stop music
    play audio "audio_carstop.ogg"  fadein 5.0
    show car at carfx
    show rainh
    $ renpy.pause(6, hard=True)
    play audio "audio_cardoor.ogg" fadein 3.0
    show victoria normalumb with dissolve
    window show
    #call InventoryInit
    #show screen InvenBase
    pause 1
    with hpunch
    md surprised"Woah!"
    md happy"Menuda mansión...Así que así es como viven los ricos ¿eh?"
    show victoria thinkingumb
    with dissolve
    wr"Supongo que sí."
    md doubt"..."
    pause 1
    md shy"{i}Como era de esperar, Wright no parece sorprendida{/i}"
    show victoria normalumb
    with dissolve
    wr"Detective, deberíamos llamar al timbre."
    show victoria seriousumb
    with dissolve
    wr"Hay que darse prisa, podrían estar destruyéndose pruebas. "
    pause 1
    md huh"Claro...  "
    md shy"{i}Victoria parece algo tensa...{/i}"
    play audio "audio_doorbell.ogg"
    pause 1
    wr"..."
    pause 1
    md doubt"... "
    pause 2

    md worried"No contesta nadie."
    md thinking"Quizá se huelan algo y hayan huído..."
    show victoria okayumb
    with dissolve
    wr"Es una teoría plausible, sin embargo, hay luces encendidas."
    show victoria normalumb
    with dissolve
    wr"Pruebe otra vez."
    md huh"Está bien..."
    play audio "audio_doorbell.ogg"
    pause 1
    md huh"Esto empieza a oler mal..."
    show victoria thinkingumb
    with dissolve
    wr"La casa es muy grande y quizá no hayan oído el tim..."
    with hpunch
    ny"¡Basta! ¿Pero que diablos creen qué hacen?"
    show victoria shockedumb
    with hpunch
    md surprised"!!!"
    with hpunch
    hide victoria
    pause 1


    scene bg_casafuera2 with flash
    show car at carpos
    show rainh

    play audio "audio_metaldoor.ogg"  fadein 0.0
    play music "music_comisary_theme.ogg" fadeout 1.0 fadein 2.0

    pause 2

    show nelly mad at center with hpunch
    ny"¿Quienes son ustedes? ¿¿ Y qué hora creen que es??"
    show nelly normal at center with dissolve
    ny"Ya hemos hablado con la prensa, no tenemos nada que decir."
    show nelly mad at center with hpunch
    ny" Y ahora ¡Largo de aquí!"
    pause 1
    show victoria shockedumb at right
    show nelly mad at cleft with dissolve
    with dissolve
    wr"..."
    show victoria normalumb at right
    with dissolve
    wr "Sentimos muchísimo ocasionarle molestias, señora. Soy la inspectora Victoria Wright, y este es mi compañero Jefferson Reilly."
    md huh"Hola."
    show nelly doubt at cleft with  dissolve
    show victoria seriousumb at right
    with dissolve
    wr" Nos gustaría hacerle unas preguntas."
    show nelly smile at cleft with dissolve
    ny" ¿Y como sé yo que son verdaderos policías, eh? ¿Creen que me he caído de un guindo o qué?"
    show nelly normal at cleft with dissolve
    show victoria shockedumb at right
    with dissolve
    wr "¿Disculpe?"
    md angry"{i}¿Pero de qué va esta vieja?{/i}"
    show victoria okayumb at right
    with dissolve
    wr "Le ruego que se calme, señora..."
    show nelly huh at cleft with dissolve
    ny"¿Que me calme?"
    show nelly mad at cleft with dissolve
    ny"¡Llevo todo el día soportando a los carroñeros de su gremio!"
    show victoria shockedumb  at right
    with dissolve
    wr "Nosotros no somos..."
    show nelly smile at cleft with dissolve
    ny"Por el amor de dios, ¿Pero saben que hora es? ¿Es que no queda ni un ápice de ética en ese repugnante gremio suyo?"
    show victoria normalumb at right
    with dissolve
    wr "Le repito que somos agentes de policia, y que si no es molestia, querríamos ..."
    show nelly mad at cleft with hpunch
    ny"¡Pues claro que es molestia!"
    md mad"¡Oiga!"
    show nelly shocked at cleft with hpunch
    md huh"¿Sabe que obstruir una investigación puede considerarse un delito?"
    show victoria shockedumb  at right
    with hpunch
    show nelly surprised at cleft with dissolve
    ny"¿Una investigación?"
    show victoria seriousumb at right
    with hpunch
    wr "Reilly!"
    show nelly smile at cleft with dissolve
    ny"Está bien, enseñenme las placas."
    show victoria normalumb at right
    with dissolve
    wr "... Aquí tiene."
    md mad"..."
    show nelly shocked at cleft with dissolve
    ny"Hmmm"
    md huh"¿Va a dejarnos entrar ya? Me estoy congelando."
    show nelly doubt at cleft with dissolve
    ny"Bueno, vayamos dentro. Pero no hagan ruido, la señora está durmiendo ¿saben?"
    show nelly normal at cleft with dissolve
    ny"Como comprenderán está muy afectada por todo esto."
    ny"Vengan por aquí."
    hide nelly with dissolve
    pause 2
    show victoria madumb at center
    with dissolve
    wr "Reilly."
    md happy"¿Sí?"
    pause 1
    show victoria normalumb at center
    with dissolve
    wr "Haz el favor de calmarte."
    hide victoria with dissolve
    pause 1
    md worried"..."
    # $ InventoryAdd("Temp3")
    # $ ItemUpdate(
    #     "Temp3",
    #      image="clue3",
    #      text="I'm replacing this item's text with new information!",
    # )

    return
