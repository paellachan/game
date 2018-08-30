label capitulo1:
    scene black with Dissolve(4.0)
    $ quick_menu = True
    scene bg_comisariaentr
    with dissolve
    play music "music_comisary_theme.ogg" fadeout 1.0 fadein 8.0
    pause 2
    md "{i}It's almost 8 pm and of course there’s not a soul in the office. I wonder why am I still here. Oh, I remember now… I was caged by my darling boss.{/i}"
    md "{i}I anxiously run towards the door as if a strange hand were to suddenly catch me from behind.{/i}"
    md "{i}It’s been a quiet Monday. Suspiciously, too quiet if you ask me. {/i}"
    md "{i}Such a days make me uneasy. It may sound weird but… have you ever experienced that sensation?{/i}"
    md "{i}That sharp troubled feeling at the back of your mind when everything is going strangely well, and you are almost patiently waiting for something terrible to happen.{/i}"
    md "{i}Anyway, I grab my umbrella and jacket and proceed to go. This detective has a date!{/i}"
    md "{i}I look outside disappointedly. Autumn has come abruptly and It’s been raining all day long. The nauseating smell of the overflowed sewers floods the waterlogged streets.{/i}"
    md "{i}Great! This is such a perfect night for an expensive romantic dinner at Dorsia’s. I cannot stop thinking about spending 500 bucks dining with my shoes reeking of shit.{/i}"
    md "{i}Did I mention I love this city?{/i}"

    play sound "audio_footsteps_normal.ogg"
    md "{i}I turn around as I hear the sound of footsteps approaching me.{/i}"
    pause 2
    show jones normal
    with dissolve
    agente "Hey, Jeff! Going home already?"
    pause 1
    md "{i}It’s Theo Jones, we worked together for two years, shortly after I joined the police corp. Not a bad guy.{/i}"
    md normal" Yeah, I was about to leave. What’s up? Do you need anything?{p=1}{i}Please say no.{/i}"
    pause 1
    agente surprise"Oh, Are you in a hurry?"
    agente "Don't tell me… "
    with hpunch
    agente evil "That you have another date?"
    agente surprise"It’s the third or the fourth of this month? "
    md huh"Hey! If you’re trying to hurt me, try again!"
    show jones normal
    with dissolve
    md proud"I’m an attractive young policeman, dude. Let me enjoy the pleasures of this mortal life."
    md huh"Are your perhaps jealous of my freedom, now that you became a respectful happily married man?"
    md fool"{i}I do deserve a little bit of enjoyment with the living after spending the whole day surrounded by corpses, you know?{/i}"
    pause 1
    show jones smile
    with dissolve
    agente "Not at all. In fact I believe it would be better for you to settle down."
    show jones evil
    with dissolve
    agente "Aren’t you tired? I already have enough stress at work to deal with this dating madness of you."
    show jones normal
    with dissolve
    md huh"Dating madness..."
    md "But wait,Wasn’t Lisa also a cop? {w=0.7}It doesn’t sound too stress free to me."
    agente doubt "Well, we aren’t talking about me aren’t we?"
    md happy"He,he,he...Gotcha!"
    agente mad"Ehm…"
    show jones serious
    with dissolve
    agente"Well, about earlier..."
    md surprised "{i}Suddenly a shiver ran down my spine.{w=1} I have a bad feeling about this.{/i}"
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
    agente pleasant"But don’t worry, It’s been a very peaceful day. It’s probably nothing."
    md huh"Wanna bet who’s gonna spend the night in the office instead of dining with Charlene?"
    show jones scared
    with dissolve
    agente "She’s a hard nut to crack, uh? Those icy eyes give me goosebumps."
    md doomed"God knows I’ve tried!"
    agente evil"Someone you cannot seduce with your charms, huh? Must be sooo hard on Mr.Wonderful."
    md"What’s with you today?"
    agente pleasant"Just kidding, It’s funny how you get so defensive so quick."
    agente evil"Could it be..."
    md"Don’t go that way buddy… "
    agente smile"And there you go again!"
    md"Anyway...Weren’t you going home?"
    agente normal"Hahahaha Okay, okay..."
    agente smile"See you tomorrow,and good luck with Victoria."
    md doubt"Yeah, see you tomorrow..."
    hide jones
    with dissolve
    pause 1
    mdpov"{i}That bastard… Remember what i said about the good guy thing? Forget about it.{/i}"
    mdpov"{i} Well, going back to what I was saying earlier… I knew it, right? I wonder what the hell does Wright want at eight o'clock on a dark, stormy Monday night.{/i}"


    pause 1
    scene black with Dissolve(4.0,hard=True)
    play sound "audio_footsteps_normal.ogg"
    scene bg_comisaria
    with dissolve
    pause 1


    md "{i} I stride aggressively towards the office, where I find her robotically stamping papers.{/i}"
    md happy"Ehmmm…{w=0.5} Hello? Did you ask for me?"
    md doubt "I ran into Agent Jones when {b} I was about to go home {/b}and he told me..."
    md mad"{i}She just keeps on stamping the documents, ignoring my presence completely. {/i}"
    md huh"Excuse me?"
    md angry"..."
    md mad"{i}Dammit Victoria! {w=0.5}Pay {w=0.5}attention {w=0.5}to {w=0.5}me!{/i}"
    stop music fadeout 2.0
    play music "music_sad.ogg" fadeout 1.0 fadein 8.0
    pause 1
    show victoria surprised
    with dissolve

    wr "Oh! You are here already."
    md huh"{i}She notices now?{/i}"
    show victoria normal
    with dissolve
    wr" Excuse me, Detective. I was finishing sorting these documents."
    wr "I’m sorry to call you at this hour. Were you leaving already?"
    md worrid"{i}Somehow, the Inspector seemed worn out.{/i}"
    md happy"Yeah, I was about to leave. I have... something to do."
    md doubt"{i}Of course I won’t confess my plans to her.{/i}"
    show victoria worried
    with dissolve
    wr "Oh… So you have plans for tonight."
    md huh"{i}She seems disappointed… Well, I’m sorry for having a life, you know?{/i}"
    show victoria thinking
    with dissolve
    wr "Those plans are really urgent, right?"
    md doomed"{i}Now I was sure. I can cancel the date thing already. Wright, who never seems interested in asking personal questions was standing before me, almost begging me to stay.{/i}"
    md doubt"{i}She was being so exceptionally inquisitve I almost grew interested about what was going on.{/i}"
    show victoria okay
    with dissolve
    wr "..."
    pause 2
    show victoria smile
    with dissolve
    wr "Well then, I guess It can't be helped. See you tomorrow, Detective Reilly."
    md worried"{i}Her smile made my blood run cold.{/i}"
    md "Aren’t you going home, boss?"
    show victoria okay
    with dissolve
    wr "I still have some things to finish tonight."
    md worried"{i}I feel kind of bad about this...{/i}"
    show victoria smile
    with dissolve
    wr "Don’t make such a face! We can talk about this tomorrow."
menu:
    "Leave.":
        jump leave

    "Stay.":
        jump stay


label leave:
    md shy"Okay. I guess...{w=0.7} We can continue this conversation tomorrow."
    show victoria okay
    with dissolve
    wr "Yeah. Take care, Detective Reilly"
    show victoria smile
    with dissolve
    md worried"{i}For some reason I feel horrible now.{/i}"
    md thinking"..."
    pause 1
    scene black with Dissolve(4.0,hard=True)
    play sound "audio_footsteps_normal.ogg"
    scene bg_comisariaentr
    with dissolve
    pause 1
    mdpov "{i}I walk towards the door disappointedly.{/i}"
    mdpov "{i}It's not like I lied to her, right?{/i}"
    mdpov "{i}It's true that I have plans for tonight... Though... Are they really that important?{/i}"
    mdpov "{i}I can't forget the vision of that sad smile of hers.{/i}"
    with hpunch
    mdpov "{i}Gosh! Get out of my head already!{/i}"
    mdpov "{i}I'm done with this.{/i}"
    mdpov "{i}I grab my phone, nervously typing the restaurant's number.{/i}"
    play sound "audio_phone_dialing.ogg"
    $ renpy.pause(3, hard=True)
    mdpov "{i}Hello?{/i}"
    mdpov "{i}Yeah{w=0.7}...{/i}"
    mdpov "{i}I'm sorry{w=0.7}...{/i}"
    mdpov "{i}{w=0.7}.{w=0.7}.{w=0.7}.{/i}"
    pause 2
    mdpov "{i}I did it.{/i}"
    mdpov "{i}I cancelled everything.{/i}"
    mdpov "{i}I guess I can text Charlene later...{w=0.7}Or maybe just fake my own death... Because that girl is sure intense.{/i}"
    mdpov "{i}I anxiously rush back to the office, somehow secretly content I did what I feel it was right.{/i}"
    pause 1
    scene black with Dissolve(4.0,hard=True)
    play sound "audio_footsteps_normal.ogg"
    scene bg_comisaria
    with dissolve
    pause 1
    with hpunch
    md worried "Boss!"
    md "{i}She's absently gathering some papers.{/i}"
    show victoria surprised
    with dissolve
    wr "???"
    show victoria surprised
    with dissolve
    wr "Detective! I thought you left already, did you forget something?"
    md fool"{i}She's all surprised...{/i}"
    md fool"{i}Look at my commitment Victoria! I foolishly fantasize. I am embarrassed just at the thought of it.{/i}"
    show victoria shy
    with dissolve
    wr "Detective?"
    jump continuar

label stay:
    md worried"{i}I stand before her for some seconds in silence.{/i}"
    md worried"{i}I'll feel terrible if I leave her, anyway.{/i}"
    md worried"{i}Charlene will probably kill me for this but...{/i}"
    show victoria surprised
    with dissolve
    wr "Is anything wrong? You'll  be late."
    jump continuar

label continuar:
    md worried"No....{w=0.7}I just....{w=0.7}I was just thinking..."
    pause 2
    md shy"That my plans aren't that important after all."
    show victoria surprised
    with dissolve
    wr "..."
    wr "I see."
    show victoria okay
    with dissolveá
    wr "But..."
    show victoria thinking
    with dissolve
    wr "Are you sure? I don't want you to feel forced to stay. I can take care of this."
    show victoria shy
    with dissolve
    md doomed"{i}She glances at me with a tiring look. Who are you trying to fool, Miss Workaholic?{/i}"
    md shy"It's fine, It's fine! C'mon! Tell me what you need."
    show victoria surprised
    with dissolve
    wr "As you wish then."
    pause 2
    show victoria smile
    with dissolve
    wr " In that case, I'm...{w=0.7}I'm happy you stayed."
    pause 2
    md shy"Don't mention it... It's my job after all."
    show victoria thinking
    with dissolve
    wr "..."
    show victoria normal
    with dissolve
    wr "Then...{w=0.7}May I ask you to come to my office?"
    show victoria worried
    with dissolve
    wr "I would like to show you something..."
    pause 1
    hide victoria
    with dissolve
    scene black with Dissolve(4.0,hard=True)
    play sound "audio_footsteps_normal.ogg"
    scene bg_comisaria_despacho
    with dissolve
    pause 1
    md "{i}Sigo a Victoria obedientemente en silencio.{/i}"
    md "{i}Su despacho es una habitación bastante grande. Todo está limpio y bien organizado, como no podía ser de otra manera tratándose de ella.{/i}"
    md "{i}No hay nada aquí que pueda darme ningún tipo de información personal sobre ella. El olor es agradable, ambientandor quizá?{/i}"
    show victoria normal
    with dissolve
    wr "Bien...{w=0.7}Podría hacerle una pregunta, Detective Reilly?"
    md huh"{i}Two years working with her and she still calls me Detective Reilly...{/i}"
    md fool"{i}Gosh Victoria, Is Jeff that hard to pronounce?{/i}"
    show victoria surprised
    with dissolve
    wr "Detective?"
    md smile"Yeah! Go ahed!"
    pause 1
    show victoria serious
    with dissolve
    wr "Ha visto usted las notícias de hoy por casualidad?"
    md happy"Sí, las he visto. ¿Ha pasado algo?"
    md doubt"{i}Casi me da un infarto al pensar que iba a preguntarme sobre lo de esta noche otra vez.{/i}"
    show victoria thinking
    with dissolve
    wr "Dígame, ha habido algo que le haya llamado la atención?"
    md thinking"Hmmm..."
    md doubt"I really don't know... I don't recall anything worth mentioning."
    show victoria okay
    with dissolve
    wr "..."
    pause 1
    show victoria normal
    with dissolve
    wr "Charles Goldberg, el presidente de uno de los bancos más grandes del país murió ayer por la noche."
    md surprised"¡Ah, sí! Un ataque fulminante al corazón, no?"
    show victoria normal
    with dissolve
    wr "Fue encontrado muerto en su casa a las afueras del barrio oeste. Aparentemente estaba trabajando en su despacho cuando ocurrió."
    show victoria thinking
    with dissolve
    wr "Cuando la ama de llaves fue a avisarle para cenar no obtuvo respuesta alguna. La puerta estaba cerrada desde dentro y después de varios intentos en vano, acabó llamando a la policía. "
    md surprised"She didn't have the key?"
    wr "Only the victim and his wife own the key."
    md doomed"{i}The victim?... Hold on there, Victoria.{/i}"
    md huh"Anyway..."
    md doubt"A male in almost his sixties with a stressful job, probably not leading the healthiest life style...A heart attack sounds plausible enough for me."
    show victoria thinking
    with dissolve
    wr "It may be the case. {w=0.7}But the question is..."
    show victoria serious
    with dissolve
    wr "What was the cause."
    stop music fadeout 5.0
    play music "music_mystery.ogg" fadeout 1.0 fadein 5.0
    md surprised"Huh? What do you mean?"
    wr "Here, take a look at that."
    md huh"{i}Victoria takes a printed paper from her bilder and hands it over to me.{/i}"
    $ quick_menu = False
    window hide dissolve
    show mail
    $ renpy.pause(5, hard=True)
    $ renpy.pause()
    hide mail
    window show dissolve
    $ quick_menu = True
    md huh"What the hell is that?"
    md thinking"Any pshycho could have written something like that... The new has been published and broadcasted all over the country."
    md huh"Couldn't it just be a grim joke?"
    show victoria thinking
    with dissolve
    wr "That's the first think I thought..."
    md doubt"..."
    show victoria serious
    with dissolve
    wr "Obviously an anonymous mail without any type of real evidence it's not enough to open an investigation, you may figure."
    wr "But then...The mail came with something peculiar attached to it."
    md doubt"..."
    wr "Here."
    pause 1
    md worried "{i}Victoria places a handful of stapled papers over the desk. As I look closer, I identify what seems the results of a blood test analysis.{/i}"
    $ quick_menu = False
    window hide dissolve
    show mail2
    $ renpy.pause(5, hard=True)
    $ renpy.pause()
    hide mail2
    window show dissolve
    $ quick_menu = True
    show victoria worried
    with dissolve
    md doubt"What's that?"
    show victoria serious
    with dissolve
    wr "A blood test results from, allegedly, Charles Golberg."
    show victoria thinking
    with dissolve
    wr "And It's not a routinary blood test, I must say."
    show victoria thinking
    with dissolve
    wr "Is very likely that the victim suspected he was being poisoned."
    md surprised"Poisoned?"
    wr "I spent the last four hours trying to unravel wether they're counterfeit or not."
    md doubt"And they are?"
    show victoria serious
    with dissolve
    wr "I'm afraid...{w=0.7}We have a case."
    pause 1
    md huh"Wait{w=0.7}.{w=0.7}.{w=0.7}."
    with hpunch
    md surprised"Whaat?"
    show victoria normal
    with dissolve
    pause 2
    scene black with Dissolve(2.0, hard=True)
    screen slow_text( txt ):
        add Text(txt, slow_cps=12) xalign 0.5 yalign 0.5
    play driving "audio_rain.ogg" fadeout 1.0 fadein 4.0
    $ renpy.pause(4, hard=True)
    show screen slow_text('No sé que era...')
    $ renpy.pause(4, hard=True)
    show screen slow_text('Quizá me había levantado con el pie izquierdo aquel día.')
    $ renpy.pause(4, hard=True)
    hide text with dissolve
    show screen slow_text('Quizá aquella lluvia incesante era algún tipo de presagio')
    $ renpy.pause(4, hard=True)
    hide text with dissolve
    show text "No sé muy bien como, aquella noche me vi envuelto en algo más turbio de lo que en un principio había imaginado." at truecenter
    $ renpy.pause(4, hard=True)
    hide text with dissolve
    stop music fadeout 3.0
    $ renpy.pause(4, hard=True)
    show text "West District Commissary, 8:46 P.M." at truecenter
    with dissolve
    $ renpy.pause(4, hard=True)
    hide text
    with dissolve
    jump capitulo2
    return
