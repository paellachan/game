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
    md "{i}Such a days make me uneasy. It may sound weird but… have you ever experienced that sensation? That sharp troubled feeling at the back of your mind when everything is going strangely well, and you are almost patiently waiting for something terrible to happen.{/i}"
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
    md"I’m an attractive young policeman, dude. Let me enjoy the pleasures of this mortal life. Are your perhaps jealous of my freedom, now that you became a respectful happily married man?"
    md huh"{i}I do deserve a little bit of enjoyment with the living after spending the whole day surrounded by corpses, you know?{/i}"
    pause 1
    show jones smile
    with dissolve
    agente "Not at all. In fact I believe it would be better for you to settle down.{w=0.7} Aren’t you tired? I already have enough stress at work to deal with this dating madness of you."
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
    show jones normal
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
    agente pleasant"hahahaha Okay, okay..."
    agente normal"See you tomorrow, good luck with Victoria."
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


    md "{i} I stride aggressively towards her desk, where I find her robotically stamping papers.{/i}"
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
    wr "That's right, I was looking for you. I’m sorry to call you out at this hour, but something suddenly came up. Were you leaving already?"
    md worrid"{i}Somehow, the Inspector looked worn out.{/i}"
    md happy"Yeah, I was about to leave. I have... something to do."
    md doubt"{i}Of course I won’t confess my plans to her.{/i}"
    show victoria worried
    with dissolve
    wr "Oh… So you have plans for tonight."
    md huh"{i}Now she seems disappointed… Well, I’m sorry for not living here and having a life, you know?{/i}"
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
    show victoria surprised
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
    show victoria normal
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
    mdpov "{i}I anxiously rush back to the office. Somehow I was secretly content I did what I feel it was right.{/i}"
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
    md fool"{i}She's all surprised. Look at my commitment Victoria! I foolishly fantasize. I was embarrassed just at the thought of it.{/i}"
    show victoria shy
    with dissolve
    wr "Detective?"
    jump continuar

label stay:
    md worried"{i}I stand before her for some seconds in silence. A quiet determination takes over me.{/i}"
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
    with dissolve
    wr "But..."
    show victoria thinking
    with dissolve
    wr "Are you sure? I don't want you to feel forced to stay. I can take care of this."
    show victoria shy
    with dissolve
    md doomed"{i}She glances at me with a tiring look. Who are you trying to fool, Miss Workaholic?{/i}"
    md shy"It's fine, It's fine!C'mon! Tell me what you need."
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
    md "{i}I follow Victoria to her office in silence.{/i}"
    md "{i}It's a fairly big room,clean and well organized, as expected from her. There's no sight of any personal item, any trace that could give me information about her life. The smell is somehow different, nicer. Air freshener, maybe?{/i}"
    show victoria normal
    with dissolve
    wr "Well... I would like to ask you something, Detective Reilly."
    md huh"{i}Two years working with her and she still calls me Detective Reilly...{/i}"
    md fool"{i}Gosh Victoria, Is Jeff that hard to pronounce?{/i}"
    pause 1
    show victoria serious
    with dissolve
    wr "Have you seen the news this morning?"
    md happy"Yeah, I did."
    md doubt"{i}I'm surprised by the odd question, though.{/i}"
    show victoria thinking
    with dissolve
    wr "And tell me...Was there any headline that called your attention?"
    md thinking"Hmmm..."
    md doubt"I really don't know... I don't recall anything worth mentioning."
    show victoria okay
    with dissolve
    wr "..."
    pause 1
    show victoria normal
    with dissolve
    wr "Charles Goldstein, the chairman of the biggest bank in this city was found dead at his home in the West Suburvs."
    md surprised"Oh, that! He had a heart attack, didn't he?"
    md doubt"An male in almost his sixties, and stressful job, more likely not leading the healthiest life style...A heart attack sounds probable enough."
    show victoria thinking
    with dissolve
    wr "It may be the case. But..."
    show victoria serious
    with dissolve
    wr "The question is...What was the cause."
    stop music fadeout 5.0
    play music "music_mystery.ogg" fadeout 1.0 fadein 5.0
    md surprised"Huh? What do you mean?"
    wr "Here, take a look at that."
    md surprised"{i}Victoria takes a printed paper from her bilder and hands it over me.{/i}"
    $ quick_menu = False
    window hide dissolve
    show mail
    $ renpy.pause(5, hard=True)
    $ renpy.pause()
    hide mail
    window show dissolve
    $ quick_menu = True
    md huh"What the hell is that?"
    md thinking"Any pshycho could have written something like that... The new has been published and broadcasted all over the country.{w=0.7}It can just be a grim joke..."
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
    md worried "{i}Victoria places a handful of stapled papers over the desk. As I look closer, I identify what seem the results of a blood test analysis.{/i}"
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
    wr "I spent the last four hours trying to unravel wether they counterfeit or not."
    md shocked"And they are?"
    show victoria serious
    with dissolve
    wr "I'm afraid we have a case."



    return
