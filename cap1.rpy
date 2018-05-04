label capitulo1:
    scene bg_comisariaentr
    with dissolve
    play music "comisary_theme.ogg" fadeout 1.0 fadein 8.0
    pause 2

    
    md"{i}It's almost 8 pm and of course there’s not a soul in the office. I wonder why am I still here. Oh, I remember now… I was caged by my darling boss.{/i}"
    md"{i}I anxiously run towards the door as if a strange hand were to suddenly catch me from behind.{/i}"
    md "{i}It’s been a quiet Monday. Suspiciously, too quiet if you ask me. {/i}"
    md "{i}Such a days make me uneasy. It may sound weird but… have you ever experienced that sensation? That sharp troubled feeling at the back of your mind when everything is going strangely well, and you are almost patiently waiting for something terrible to happen.{/i}"
    md "{i}Anyway, I grab my umbrella and jacket and proceed to go. This detective has a date!{/i}"
    md "{i}I look outside disappointedly. Autumn has come abruptly and It’s been raining all day long. The nauseating smell of the overflowed sewers floods the waterlogged streets.{/i}"
    md "{i}Great! This is such a perfect night for an expensive romantic dinner at Dorsia’s. I cannot stop thinking about spending 500 bucks dining with my shoes reeking of shit.{/i}"
    md "{i}Did I mention I love this city?{/i}"
    
    play sound "footsteps_normal.ogg"
    md "{i}I turn around as I hear the sound of footsteps approaching me.{/i}"
    pause 2
    show jones normal
    with dissolve
    agente "Hey, Jeff! Going home already?"
    pause 1
    md"{i}It’s Theo Jones, we worked together for two years, shortly after I joined the police corp. Not a bad guy.{/i}"
    md normal" Yeah, I was about to leave. What’s up? Do you need anything?"
    pause 1
    md huh"{i}Please say no.{/i}"
    pause 1
    agente happy "Are you in a hurry? Could it be… that you have another date? It’s the third or the fourth of this month? "
    md huh"Hey! If you’re trying to hurt me, try again!"
    md"I’m an attractive young policeman, dude. Let me enjoy the pleasures of this mortal life. Are your perhaps jealous of my freedom, now that you became a respectful happily married man?"
    md huh"{i}I do deserve a little bit of enjoyment with the living after spending the whole day surrounded by corpses, you know?{/i}"
    pause 1
    show jones happy
    with dissolve
    agente "Not at all. In fact I believe it would be better for you to settle down. Aren’t you tired? I already have enough stress at work to deal with this dating madness of you."
    show jones normal
    with dissolve
    md huh"Dating madness..."
    md"But wait,Wasn’t Lisa also a cop? It doesn’t sound too stress free to me."
    agente mad "Well, we aren’t talking about me aren’t we?"
    md happy"He,he,he...Gotcha!"
    agente "Ehm…"
    show jones serious
    with dissolve
    agente"Well, about earlier..."
    md serious"{i}Suddenly a shiver ran down my spine. I have a bad feeling about this.{/i}"
    pause 1
    agente "Subzero was looking for you a moment ago."
    with hpunch
    md mad"Shh… Don’t call her that! She may hear us! Why didn’t you tell her I already left?"
    md doomed"{i}See? I knew I was doomed.{/i}"
    show jones mad
    with dissolve
    agente "I’m sorry I’m not that good of a psychic to know you have a date, man."
    show jones sorry
    with dissolve
    agente "I still can tell her you left."
    agente "But don’t worry, It’s been a very tranquil day. It’s probably nothing."
    md huh"Wanna bet who’s gonna spend the night in the office instead of dining with Charlene?"
    show jones normal
    with dissolve
    agente "She’s a hard nut to crack, uh? Those icy eyes give me goosebumps."


menu:
    "Respuesta políticamente correcta.":
        jump wright1

    "Respuesta de gallito.":
        jump wright2
        
label wright1:  
    m "No es para tanto, no te voy a mentir, es una persona estricta, pero hace bien su trabajo. He aprendido mucho trabajando con ella."
    jump continuacion1
    
label wright2:  
    m "¡Y que lo digas! Sinceramente creo que debería relajarse un poco."
    jump continuacion2
    
label continuacion1:  
    agente "Siempre me ha dado esa impresión. Aunque sigue dándome un poco de miedo esa mirada suya."
    agente "Bueno, te dejo. Ahora soy yo el que se va a casa. Ya me contarás mañana. ¡Suerte!"
    hide jones
    with dissolve
    jump continuacion3

    
label continuacion2:  
    agente "Shhhh... ¡Como te oiga lo llevas claro!"
    m "Bah! Está demasiado metida en sus casos como para preocuparse por la opinión de su minion. {i}Espero...{/i}"
    agente "Bueno, te dejo. Ahora soy yo el que se va a casa. Ya me contarás mañana. ¡Suerte!"
    m "Vaya cara qué tienes... ¡Nos vemos mañana!"
    hide jones
    with dissolve
    jump continuacion3

label continuacion3:  

    
    m "{i}Os lo estaba comentando hace un segundo ¿no? Me pregunto qué demonios quiere Wright a las ocho de la maldita tarde de un lunes tormentoso y oscuro.{/i}"
    m "{i}Camino a zancadas violentas hacia su escritorio donde la encuentro sellando unos papeles de forma mecánica.{/i}"
    
    pause 1
    scene bg_comisaria
    with dissolve
    
    md happy"¿Hola?¿Quería algo inspectora? "
    md "Acabo de cruzarme al agente Jones cuando ya estaba {b}saliendo por la puerta para irme a casa{/b}¿sabe? Me ha dicho que me estaba buscando."
    md huh"{i}Sigue poniendo los condenados sellos como una máquina, ignorando por completo mi presencia. Cada vez estoy más cabreado. {/i}"
    md annoyed"¿Oiga?"
    md "..."
    md mad"{i}Maldita sea Victoria ¡Hazme caso!{/i}"
    
    show victoria normal
    with dissolve

    wr "Disculpe, Jefferson. Estaba intentando acabar de clasificar estos documentos."
    wr "Sí, le estaba buscando. Perdone por avisarle a estas horas, pero ha sido algo repentino ¿Se iba ya?"
    md "{i}La inspectora parecía algo cansada. Probablemente llevase en la comisaría más de 14 horas.{/i}"
    md happy"Eso es, ya salía por la puerta. Tengo algo de prisa."
    show wright happy
    with dissolve

    wr "¿Tiene usted algo que hacer esta noche?¿Algún compromiso?"
    m "{i}Ahora estaba seguro. Ya podía ir cancelando esa reserva. La inspectora Wright, también conocida como SubZero, haciendo referencia a su desarrollada calidez emocional, nunca hacía preguntas personales.{/i}"
   
menu:
    "Tengo una reserva en el Dorsia a las 8.":
        jump dorsia

    "No es asunto suyo.":
        jump borde
        
label dorsia:  
    m "¿Sabe dónde es, no? Ese sitio tan caro donde los camareros llevan esas pajaritas horteras de los 80. Hace un par de meses que estoy viendo a una chica, ya sabe a lo que me refiero ¿no?"
    show wright_mad
    with dissolve
    wr "Vaya, eso es maravilloso detective. Celebro que comparta conmigo estas confesiones tan íntimas. Después de todo llevamos ya seis años trabajando juntos."
    m "{i}Ese tono sarcástico me heló la sangre. A ella no le interesaba otra respuesta que no fuese mi disponibilidad total para quedarme a hacer horas extras no pagadas hasta dios sabe cuando.{/i}"
    m "Bueno¿Qué necesita? Tengo algo de prisa."
    show victoria normal
    wr "Esa reserva en el Dorsia…"
    wr "Cancélela."
    m "¡¿Quéeee?! Oiga no puede..."
    wr "Vayamos a mi despacho, voy a enseñarle algo."
    m "¡Eh!¡Inspectora! Esto no es justo!"
    
    jump continuar

label borde:  
    show wright_wtf
    wr "No era mi intención incomodarle detective."
    m "{i}Aunque tenía la misma cara inexpresiva de siempre noté un tono de tristeza en su voz.{/i}"    
    m "Bueno¿Qué necesita? Tengo algo de prisa."
    show victoria normal
    wr "Vayamos a mi despacho, voy a enseñarle algo."
    m "¿Ahora?"
    
    jump continuar
   
label continuar:  
    show victoria normal
    m "¿Es una broma? Mira Victoria, llevo aquí desde las 8 de la mañana. "
    pause 2
    stop music fadeout 5.0 
    play music "tension.ogg" fadeout 1.0 fadein 5.0
    m "{i}El despacho está algo vacío, aunque muy ordenado. La verdad, conociendo a Victoria me sorprendería que fuese de otra manera. Hay un olor familiar y agradable ¿Un ambientador quizá? {/i}"
    wr "Preste atención Jefferson. ¿Ha visto hoy las noticias?"
    m "Sí, esta mañana ¿Porqué?No ha pasado nada¿No? Bueno, la ha palmado el banquero ese, el del Bank of SeaShore. Un ataque al corazón o algo así."
    wr "Exacto."
    m "¿Y? Ha sido una muerte por causas naturales. Homicidios no pinta nada en esto."
    hide victoria normal
    wr "Eso creía yo también, hasta que hace un par de horas recibimos este correo. Lo he impreso, léalo."
    show mail
    m "¿Qué diablos es esto? Cualquier pirado ha podido escribir algo así. Ha salido en todos los periódicos y en los canales de noticias. Puede ser una broma macabra."
    hide mail
    show wright_mad
    wr "Evidentemente un email anónimo sin ningún tipo de evidencia no es suficiente para empezar una investigación. Pero échele un vistazo a esto."
    hide wright_mad
    show mail2
    m "{i}La inspectora pone varios folios grapados encima de la mesa. Parecen los resultados de unos análisis de sangre. {/i}"
    hide mail2
    show victoria normal
    wr "Llevo un par de horas intentando averiguar si éstos documentos son falsos o no."
    m "¿Y lo son?"
    wr "Me temo que tenemos un caso."

    
    return