default question_a = False
default question_b = False
default question_c = False

label capitulo3:
    scene black with Dissolve(4.0)
    $ quick_menu = False
    scene bg_casahall with dissolve
    with dissolve
    play music "music_mansion.ogg" fadeout 1.0 fadein 5.0
    $ renpy.pause(3, hard=True)

    md "{i}The suspicious housekeeper guide us to the extravagant hall of the mansion.{/i}"
    md "{i}I observe in disbelief all the pompous details surrounding me. So places like that do really exist...{/i}"
    md "{i}I sigh, as I mentally compare it with the shabby hovel I can only afford. {/i}"
    md "{i}We are all equal but some are more equal than others, Huh?{/i}"


    window show
    $ renpy.pause(2, hard=True)
    $ quick_menu = True
    show nelly shocked at center with hpunch
    ny"Where do you think you're going?"
    md huh"Pardon?"
    show nelly smile at center with dissolve
    ny"Oh my!"
    show nelly normal at center with dissolve
    ny"Could you please wipe your...shoes, if I can call them that, before entering?"
    show nelly smile at center with dissolve
    ny"Young people has such a lousy taste nowadays. Don't you think?"
    md huh"{i}Talk about the pot calling the kettle black...{/i}"
    md happy"Sure, excuse me, please."
    md doomed"{i}Give me a break already, old psycho hag.{/i}"
    pause 1
    show nelly normal at cleft with dissolve
    show victoria normal at right
    with dissolve
    wr "Well..."
    show nelly smile at cleft with dissolve
    ny"Yes?"
    show victoria normal at right
    with dissolve
    wr "May we ask you some questions now?"
    hide victoria with dissolve
    show nelly smile at center with dissolve
    ny"Do I even have an choice?"

label menu_question_choices:
    if question_a and question_b and question_c:
        jump continue_main_story
    else:
        menu:
            "Charles Goldberg." if not question_a:
                jump question_a_choice
            "The day of the death." if not question_b:
                jump question_b_choice
            "Broken door." if not question_c:
                jump question_c_choice
            # "All done!" if question_a and question_b and question_c:


label question_a_choice:

    show nelly normal at center with dissolve
    ny"Charles Goldberg? I been working for him for more than 20 years now."
    show nelly sad at center with dissolve
    ny"To think that Miss Aldrich could marry such a man..."
    show victoria shocked at right
    with dissolve
    wr "Miss Aldrich?"
    hide victoria with dissolve
    show nelly surprised at center with dissolve
    ny"Oh, I mean Mrs Goldberg..."
    show nelly smile at center with dissolve
    ny"My dear, I have such a bad memory."
    show nelly normal at center with dissolve
    ny"Aldrich was her maiden name. "
    show nelly normal at center with dissolve
    ny"I was fortunate enough to serve Aldrich family them from the age of fourteen, as my mother also did."
    md huh"Wow, this must have been a really long time ago..."
    show nelly mad at center with dissolve
    show victoria shocked at right
    with hpunch
    wr "Reilly!"
    hide victoria with dissolve
    show nelly sad at center with dissolve
    ny "Helped Lady Mary to brough up the girls... With that delicate health of hers..."
    md huh"Who's that Lady Mary?"
    md huh"Listen, could you tell us something about Charles Goldberg ?"
    show nelly smile at center with dissolve
    ny "Oh,I beg you excuse my tendency to ramble."
    show nelly normal at center with dissolve
    ny "Charles Goldberg..."
    show nelly normal at center with dissolve
    ny "I remember the first time I saw him. A severe looking american man. It was at a party at Aldrich's mansion in Yorkshire."
    show victoria normal at right
    with dissolve
    wr "Yorkshire? In England?"
    hide victoria with dissolve
    show nelly smile at center with dissolve
    ny "Glad you attended your geography classes, miss."
    md mad"..."
    show nelly sad at center with dissolve
    ny "That's where my young lady met Charles Goldberg. A man much older than her, lacking any lineage..."
    md huh"{i}She doesn't seem very fond of Mr. Goldberg.{/i}"
    show nelly normal at center with dissolve
    ny "They fell in love and married soon after. And well... That's how I ended up here."
    show victoria thinking at right
    with dissolve
    wr "Following Mrs.Goldberg?"
    hide victoria with dissolve
    show nelly sad at center with dissolve
    ny "Of course, I could never leave her alone in such a place."
    md huh"{i}Such a place?{/i}"
    show victoria okay at right
    with dissolve
    wr "I see."
    show victoria thinking at right
    with dissolve
    wr "How has been working for him all those years?"
    hide victoria with dissolve
    show nelly doubt at center with dissolve
    ny "Nothing remarkable, really. A busy business man, hardly. "
    show nelly smile at center with dissolve
    ny "I must say at his favor his nature was pleasant enough."
    show victoria okay at right
    with dissolve
    wr "..."
    show victoria thinking at right
    with dissolve
    wr "Have you notice any changes in his behaviour recently?"
    wr "Anything odd?"
    hide victoria with dissolve
    show nelly doubt at center with dissolve
    ny "Not that I remember."
    show nelly smile at center with dissolve
    ny "He seemed to spend even more time away from home."
    md thinking"Any idea why?"
    show nelly doubt at center with dissolve
    ny "Who knows..."
    show nelly smile at center with dissolve
    ny "The secret to become an excelLent housekeeper is to never be indiscreet."
    show victoria normal at right
    with dissolve
    wr "Thank you, Miss Smith."
    hide victoria with dissolve
    $ question_a = True
    jump menu_question_choices

label question_b_choice:
    show nelly doubt at center with dissolve
    ny"Oh, my..."
    show nelly sad at center with dissolve
    ny"It's so recent I still can't..."
    md huh"{i}...{/i}"
    show victoria normal at right
    with dissolve
    wr "I understand, but this is very important, Miss Smith."
    hide victoria with dissolve
    show nelly sad at center with dissolve
    ny"Okay..."
    show nelly normal at center with dissolve
    ny"It was an unusual sunday, very quiet, very tranquil."
    ny"Mrs.Goldberg and her daughter, Katherine had decided to spend the weekend at the Hamptons summer house."
    show nelly smile at center with dissolve
    ny"I stayed to assist Mr.Goldberg."
    show victoria thinking at right
    with dissolve
    wr "Why he didn't go with them?"
    hide victoria with dissolve
    show nelly doubt at center with dissolve
    ny"I guess he was busy as usual."
    md huh"Even in sunday?"
    show nelly smile at center with dissolve
    ny"God knows what is the truth and what is a..."
    md doubt"What?"
    show nelly normal at center with dissolve
    ny"He was working at his home office, nothing unusual."
    show nelly normal at center with dissolve
    ny" I prepared some tea about 5 o'clock, knocked on the door, obtaining no response..."
    show victoria thinking at right
    with dissolve
    wr "And called the police."
    hide victoria with dissolve
    show nelly smile at center with dissolve
    ny"Exactly as you say."
    show victoria thinking at right
    with dissolve
    wr "Did he met with someone that day?"
    hide victoria with dissolve
    show nelly doubt at center with dissolve
    ny"I don't recall so, he didn't leave the house and nobody came. So I guess he didn't."
    show victoria okay at right
    with dissolve
    wr "I see."
    hide victoria with dissolve
    $ question_b = True
    jump menu_question_choices

label question_c_choice:
    show nelly sad at center with dissolve
    ny"That hideous door always getting stuck...I can't believe we survived for this long without a gatekeeper."
    md huh"{i}Yeah, How could I possible imagine a life witout one, huh?{/i}"
    show victoria thinking at right
    with dissolve
    wr "It has been broken for a long time?"
    hide victoria with dissolve
    show nelly normal at center with dissolve
    ny"Since friday night if I'm not mistaken."
    show nelly doubt at center with dissolve
    ny"We repair it, it works for a while, and then it got stuck again. This old house is such a nightmare to take care of. "
    show victoria normal at right
    with dissolve
    wr "Was Mr. Goldberg the one taking care of the door?"
    hide victoria with dissolve
    show nelly mad at center with dissolve
    ny"Of course not!"
    show nelly smile at center with dissolve
    ny"We do have a janitor, of course."
    md doomed "{i}To not to have one, so aggravating.{/i}"
    show nelly doubt at center with dissolve
    ny"He should have come sunday afternoon to fix it, but he couldn't come."
    show victoria shocked at right
    with dissolve
    wr "Why?"
    hide victoria with dissolve
    show nelly doubt at center with dissolve
    ny"He called, told me he was not feeling well."
    show nelly smile at center with dissolve
    ny"He's a hardworking young man, I let him rest."
    show victoria normal at right
    with dissolve
    wr "What's his name?"
    hide victoria with dissolve
    show nelly shocked at center with hpunch
    ny"Ro...Hm.... u...Hm...Dric..."
    md huh"Pardon?"
    show nelly doubt at center with dissolve
    ny"Jesus Christ, those hispanic names..."
    md surprised "..."
    show nelly doubt at center with dissolve
    ny"Rodrigo Queentana."
    md huh"Queentana? It must be Quintana."
    show nelly smile at center with dissolve
    ny"Whatever it is."
    show victoria thinking at right
    with dissolve
    wr "For how long has he been working here?"
    hide victoria with dissolve
    show nelly doubt at center with dissolve
    ny"About two years now."
    show victoria okay at right
    with dissolve
    wr "That's all for now, thank you."
    hide victoria with dissolve
    $ question_c = True
    jump menu_question_choices

label continue_main_story:
    "Here the game goes on!"

    return
