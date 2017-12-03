# The script of the game goes in this file

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("")
define wr = Character("Inspectora Wright")
define agente = Character("Agente Jones")

# The game starts here.

label start: 

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_comisaria

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # m "{i}{/i}" m "" wr""

   
    m "{i}Son casi las ocho y ya no hay ni dios en la comisaría. Corro hacia la salida como si una mano extraña fuese a cogerme por detrás, ha sido un lunes tranquilo. Demasiado tranquilo.{/i}"
    m "{i}Estos días me ponen nervioso. Os sonará raro, pero… ¿Sabéis esa sensación? Esa ansiedad punzante que sientes en el cogote cuando todo va bien y eres feliz y parece que estés contando los segundos antes de que todo se vaya a la mierda.{/i}"
    m "{i}Bueno, cojo el paraguas y la chaqueta ¡Este poli tiene una cita! El otoño ha llegado de repente. Lleva todo el día lloviendo y el olor de las cloacas desbordadas inunda las calles encharcadas.{/i}"
    m "{i}¡Genial! Es la noche perfecta para una cenita romántica en el Dorsia. No paro de pensar en que voy a dejarme 200 pavos mientras como con los pies oliéndome a mierda.{/i}"
    
    agente "¡Hey, Jeff! ¿Vas a casa?"
    m "{i}Un escalofrío en la nuca. Tengo un mal presentimiento.{/i}"
    agente "La inspectora te estaba buscando, no sé qué quiere."
    m "¿Porqué no le has dicho que ya me había ido?"
    agente "Lo siento, tio."
    
    m "{i}Os lo estaba comentando hace un segundo ¿no? Me pregunto qué demonios quiere Wright a las ocho de la maldita tarde de un lunes tormentoso y oscuro.{/i}"
    m "{i}Camino a zancadas violentas hacia su escritorio donde la encuentro sellando unos papeles de forma mecánica.{/i}"
    
    m "¿Hola?¿Quería algo inspectora? "
    m "Acabo de cruzarme al agente Jones cuando ya estaba {b}saliendo por la puerta para irme a casa{/b}¿sabe? Me ha dicho que me estaba buscando."
    m "{i}Sigue poniendo los condenados sellos como una máquina, ignorando por completo mi presencia. Cada vez estoy más cabreado. {/i}"
    m "¿Oiga?"
    m "..."
    m "{i}Maldita sea Victoria ¡Hazme caso!{/i}"
    
    show wright_normal
    wr "Disculpe, Jefferson. Estaba intentando acabar de clasificar estos documentos."
    wr "Sí, le estaba buscando. Perdone por avisarle a estas horas, pero ha sido algo repentino ¿Se iba ya?"
    m "{i}La inspectora parecía algo cansada. Probablemente llevase en la comisaría más de 14 horas.{/i}"
    m "Eso es, ya salía por la puerta. Tengo algo de prisa."
    show wright_happy
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
    wr "Vaya, eso es maravilloso detective. Celebro que comparta conmigo estas confesiones tan íntimas. Después de todo llevamos ya seis años trabajando juntos."
    m "{i}Ese tono sarcástico me heló la sangre. A ella no le interesaba otra respuesta que no fuese mi disponibilidad total para quedarme a hacer horas extras no pagadas hasta dios sabe cuando.{/i}"
    m "Bueno¿Qué necesita? Tengo algo de prisa."
    show wright_normal
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
    show wright_normal
    wr "Vayamos a mi despacho, voy a enseñarle algo."
    m "¿Ahora?"
    
    jump continuar
   
label continuar:  
    show wright_normal
    m "¿Es una broma? Mira Victoria, llevo aquí desde las 8 de la mañana. "
    m "{i}El despacho está algo vacío, aunque muy ordenado. La verdad, conociendo a Victoria me sorprendería que fuese de otra manera. Hay un olor familiar y agradable ¿Un ambientador quizá? {/i}"
    wr "Preste atención Jefferson. ¿Ha visto hoy las noticias?"
    m "Sí, esta mañana ¿Porqué?No ha pasado nada¿No? Bueno, la ha palmado el banquero ese, el del Bank of SeaShore. Un ataque al corazón o algo así."
    wr "Exacto."
    m "¿Y? Ha sido una muerte por causas naturales. Homicidios no pinta nada en esto."
    hide wright_normal
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
    show wright_normal
    wr "Llevo un par de horas intentando averiguar si éstos documentos son falsos o no."
    m "¿Y lo son?"
    wr "Me temo que tenemos un caso."

    
    return
