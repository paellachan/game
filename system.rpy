
#     # Initialise inventory/profiles
#     call InventoryInit
#
#     scene black
#     with dissolve
#
#     # Call or show the screen
#     call screen InvenBase
#
#     return

label InventoryInit:

    python:
        # DEFINE INVENTORY ITEMS HERE
        Items = {
            "Temp1": {
                "Image": "clue1", # Name of item's image; should be defined below
                "Text": _("Un extraño mail recivido por Victoria la mañana siguiente a la muerte de Charles Goldberg. No se sabe quien lo envió."), # Original item description
                "State": "New", # Should always be New unless you want it show an Updated tag -- "State": "Updated" -- or no tag -- "State": "Seen"
                },
            "Temp2": {
                "Image": "clue2",
                "Text": _("Unos análisis de sangre adjuntados a un mail anónimo enviado la mañana siguiente a la muerte de Charles Goldberg. No son los típicos análisis rutinarios, e indican que la victima estaba siendo envenenada."),
                "State": "Seen",
                },
            "Temp3": {
                "Image": "clue3",
                "Text": _("I am trying to do clues by now."),
                "State": "New",
                },
            }

        Profiles = {
            "Jeff Reilly": {
                "Image": "chara1", # Name of item's image; should be defined below
                "Name": _("Jeff Reilly"), # Character's name
                "Status": _("Alive"), # Character's status
                "Occupation": _("Homicides detective"), # Character's job
                "Relationship": _("Dating Charlenne"), # Character's relationship
                "Text": _("Lleva 2 años trabajando en la comisaría del distrito Sur como detective de homicidios."), # Information along the bottom
                "State": "New", # Should always be New unless you want it show an Updated tag -- "State": "Updated" -- or no tag -- "State": "Seen"
                },
            }


        # Set starting inventory
        Inventory = [
            "Temp1",
            "Temp2",
            ]

        ProfileFolder = [
            "Jeff Reilly",
            ]


        # Fill empty inventory/profile slots with blank values
        for i in range(len(Inventory), InvenSize):
            Inventory.append(None)
        for i in range(len(ProfileFolder), InvenSize):
            ProfileFolder.append(None)

    return



# Buttons to access inventory and profiles
screen InvenBase():


    # Background Image
    # if renpy.get_screen("Profs") or renpy.get_screen("Inven") or renpy.get_screen("ProfDetail") or renpy.get_screen("InvenDetail"):
    #     add "InvBack"


    # Toggle quick menu when entering and leaving this screen
    # on "show" action SetVariable("quick_menu", False)
    # on "hide" action SetVariable("quick_menu", True)

    # Inventory button
    imagebutton:
        idle "EvButtonIdle"
        hover "EvButtonHover"
        action [ Hide("Profs"), Hide("ProfDetail"), Hide("InvenDetail"), If(not renpy.get_screen("Inven"), true=[ Show("Inven"), Hide("InvenBase"), SetVariable("quick_menu", False) ], false = [ Hide("Inven") ]) ]
        xpos 0
        ypos 40


    # Profiles button
    imagebutton:
        idle "ProfButtonIdle"
        hover "ProfButtonHover"
        action [ Hide("Inven"), Hide("InvenDetail"), Hide("ProfDetail"), If(not renpy.get_screen("Profs"), true=[ Show("Profs"), Hide("InvenBase") ], false = [ Hide("Profs") ]) ]
        xpos 0
        ypos 160


# Inventory screen
screen Inven():
    on "show" action SetVariable("quick_menu", False)


    modal True
    add "InvBack"

    on "show" action SetVariable("InvenPage", 0) # Make sure we always start on page 0

    $ PageStart = InvenPage * InvenPageSize

    add "InvTitle" xpos 310 ypos 30 # 'Inventory' tag

    textbutton _("CLOSE"):
        action Hide("Inven"), Show("InvenBase"), SetVariable("quick_menu", True) hover_sound "audio_switch.wav"
        xpos 1490
        ypos 40
        xanchor 1.0
        text_style "InvenButtonText"


    grid 3 3:
        xalign 0.5
        yalign 0.6
        xspacing 80
        yspacing 50
        for index in range(PageStart, PageStart + InvenPageSize): # Iterate over current inventory page
            $ Item = Inventory[index] # Get inventory entry
            if not Item: # If it's a blank entry
                add "InvEmpty" # Show blank
            else:
                imagebutton: # Make a button
                    idle "thumb_" + Items[Item]["Image"] # Add the thumbnail
                    action [ Hide("Inven"), Function(SetInventorySeen, Item), Show("InvenDetail", item=Item) ]

    use PageTags("Inventory")

    textbutton _("NAVIGATION"):

        xalign 0.4
        ypos 1000
        text_style "NavButtonText"

    hbox:
        xalign 0.6
        ypos 1000
        spacing 20

        for num in range(0, InvenSize / InvenPageSize):
            textbutton str(num + 1):
                action SetVariable("InvenPage", num)
                text_style "NavButtonText"



screen Profs():

    modal True
    add "InvBack"
    on "show" action SetVariable("quick_menu", False)

    on "show" action SetVariable("InvenPage", 0) # Make sure we always start on page 0

    $ PageStart = InvenPage * InvenPageSize

    add "ProfTitle" xpos 310 ypos 30 # 'Inventory' tag

    textbutton _("CLOSE"):
        action Hide("Profs"), Show("InvenBase"), SetVariable("quick_menu", True) hover_sound "audio_switch.wav"
        xpos 1490
        ypos 40
        xanchor 1.0
        text_style "InvenButtonText"


    grid 3 3:
        xalign 0.5
        yalign 0.6
        xspacing 80
        yspacing 50
        for index in range(PageStart, PageStart + InvenPageSize): # Iterate over current inventory page
            $ Item = ProfileFolder[index] # Get inventory entry
            if not Item: # If it's a blank entry
                add "InvEmpty" # Show blank
            else:
                imagebutton: # Make a button
                    idle Profiles[Item]["Image"] # Add the thumbnail
                    action [ Hide("Profs"), Function(SetProfileSeen, Item), Show("ProfDetail", item=Item) ]

    use PageTags("Profiles")

    textbutton _("NAVIGATION"):

        xalign 0.4
        ypos 1000
        text_style "NavButtonText"

    hbox:
        xalign 0.6
        ypos 1000
        spacing 20

        for num in range(0, InvenSize / InvenPageSize):
            textbutton str(num + 1):
                action SetVariable("InvenPage", num)
                text_style "NavButtonText"



# Extra screen for New/Updated tags
screen PageTags(type="Inventory"):
    modal True

    $ PageStart = InvenPage * InvenPageSize

    if type == "Inventory":
        $ source = Inventory
        $ source2 = Items
    elif type == "Profiles":
        $ source = ProfileFolder
        $ source2 = Profiles

    grid 3 3:
        xalign 0.5
        yalign 0.6
        xspacing 80
        yspacing 50
        for index in range(PageStart, PageStart + InvenPageSize): # Iterate over current inventory page
            $ Item = source[index] # Get inventory entry
            if not Item: # If it's a blank entry
                add Null(297, 240)
            else:
                if source2[Item]["State"] == "New": # If item has a New flag
                    add "InvNew"
                elif source2[Item]["State"] == "Updated": # If item has an Updated flag
                    add "InvUpdated"
                else:
                    add Null(297, 240)


# Displays an item with big image and text
screen InvenDetail(item=False):

    modal True
    add "InvBack"
    default TextAnchor = 0.5 # Set alignment of main text

    add "InvTitle" xpos 310 ypos 30

    textbutton _("CLOSE"):
        action Hide("InvenDetail"), Hide("Inven"), Show("InvenBase"), SetVariable("quick_menu", True) hover_sound "audio_switch.wav"
        xpos 1490
        ypos 40
        xanchor 1.0
        text_style "InvenButtonText"

    if item:
        add Items[item]["Image"] xalign 0.5 yalign 0.35
        text Items[item]["Text"] xalign 0.5 yalign 0.75 xanchor TextAnchor yanchor 0.0 xmaximum 1150 font "names.ttf" color "#212121"


    textbutton _("BACK"):
        action [ Hide("InvenDetail"), Show("Inven") ]
        xalign 0.5
        ypos 1000
        text_style "NavButtonText"



# Displays a profile with text
screen ProfDetail(item=False):
    add "InvBack"
    add "InvProf" xpos 365 ypos 120

    modal True
    default TextAnchor = 0.0 # Set alignment of main text

    add "ProfTitle" xpos 310 ypos 30

    textbutton _("CLOSE"):
        action Hide("ProfDetail"), Hide("Profs"), Show("InvenBase"), SetVariable("quick_menu", True) hover_sound "audio_switch.wav"
        xpos 1490
        ypos 40
        xanchor 1.0

        text_style "InvenButtonText"

    if item:
        add Profiles[item]["Image"] xalign 0.2675 yalign 0.2

        if ProfileStructure == "Normal":
            text "NAME:" xalign 0.40 yalign 0.20 xanchor 0.0 font "names.ttf" color "#212121" size 24
            text "OCCUPATION:" xalign 0.40  yalign 0.24 xanchor 0.0 font "names.ttf" color "#212121" size 24
            text "RELATIONSHIP:" xalign 0.40 yalign 0.28 xanchor 0.0 font "names.ttf" color "#212121" size 24
            text "STATUS:" xalign 0.40 yalign 0.32 xanchor 0.0 font "names.ttf" color "#212121" size 24

            text Profiles[item]["Name"].upper() xalign 0.55 yalign 0.20 xanchor 0.0 font "names.ttf" color "#212121" size 22 # .upper() puts all text into uppercase; remove it for normal capitalisation
            text Profiles[item]["Occupation"].upper() xalign 0.55 yalign 0.24 xanchor 0.0 font "names.ttf" color "#212121" size 22
            text Profiles[item]["Relationship"].upper() xalign 0.55 yalign 0.28 xanchor 0.0 font "names.ttf" color "#212121" size 22
            text Profiles[item]["Status"].upper() xalign 0.55 yalign 0.32 xanchor 0.0 font "names.ttf" color "#212121" size 22

        elif ProfileStructure == "Alt":
            text "NAME:    " + Profiles[item]["Name"].upper() xalign 0.45 yalign 0.16 xanchor 0.0 font "names.ttf"
            text "OCCUPATION:    " + Profiles[item]["Occupation"].upper() xalign 0.45 yalign 0.22 xanchor 0.0 font "names.ttf" color "#212121"
            text "RELATIONSHIP:    " + Profiles[item]["Relationship"].upper() xalign 0.45 yalign 0.28 xanchor 0.0 font "names.ttf" color "#212121"
            text "STATUS:    " + Profiles[item]["Status"].upper() xalign 0.45 yalign 0.34 xanchor 0.0 font "names.ttf" color "#212121"

        text Profiles[item]["Text"] xalign 0.225 yalign 0.48 xanchor TextAnchor yanchor 0.0 xmaximum 1050 font "names.ttf" color "#212121"


    textbutton _("BACK"):
        action [ Hide("ProfDetail"), Show("Profs") ]
        xalign 0.5
        ypos 1000
        text_style "NavButtonText"



# DEFINE IMAGES HERE


image InvBack = "ui/background_inv.png"
image InvProf = "ui/background_profile.png"
image EvButtonIdle = "ui/bt_info.png"
image ProfButtonIdle = "ui/bt_profiles.png"

image EvButtonHover = im.MatrixColor("ui/bt_info.png", im.matrix.brightness(0.25))
image ProfButtonHover = im.MatrixColor("ui/bt_profiles.png", im.matrix.brightness(0.25))

image InvTitle = "ui/inv_title.png"
image ProfTitle = "ui/profiles_title.png"

image InvEmpty = "ui/empty_data.png"
image InvNew = "ui/new_tag.png"
image InvUpdated = "ui/updated_tag.png"


image clue1 = "ui/clue1.png"
image thumb_clue1 = "ui/thumb_clue1.png"

image clue2 = "ui/clue2.png"
image thumb_clue2 = "ui/thumb_clue2.png"

image clue3 = "ui/clue3.png"
image thumb_clue3 = "ui/thumb_clue3.png"


image chara1 = "ui/thumb_chara1.png"



init -2:
    style InvenButtonText:
        font "names.ttf"
        color "#000000"
        hover_color "#900000"
        insensitive_color "#000000"
        size 32
        hover_sound "audio_switch.wav"

    style NavButtonText:
        font "names.ttf"
        color "#000000"
        hover_color "#900000"
        insensitive_color "#000000"
        size 32
        hover_sound "audio_switch.wav"

    python:
        # Set size of inventory
        InvenSize = 36 # Total size; Must be a multiple of InvenPageSize
        InvenPageSize = 9 # Number of items to display per page
        InvenPage = 0
        ProfileStructure = "Normal" # Set this to "Alt" for a different way of showing profiles; restart required


        # SET INVENTORY ITEM(S) TO 'SEEN'
        def SetInventorySeen(item=False):
            global Inventory
            global Items
            if item:
                Items[item]["State"] = "Seen"
            else:
                for inv in Inventory:
                    if inv:
                        Items[inv]["State"] = "Seen"

        # SET PROFILE(S) TO 'SEEN'
        def SetProfileSeen(item=False):
            global ProfileFolder
            global Profiles
            if item:
                Profiles[item]["State"] = "Seen"
            else:
                for inv in ProfileFolder:
                    if inv:
                        Profiles[inv]["State"] = "Seen"


        # ADD ITEM TO INVENTORY
        # Call this normally -- $ InventoryAdd("itemname") -- to add a new item at the end of the list
        # Call this with first -- $ InventoryAdd("itemname", first=True) -- to add a new item to the beginning of the list
        def InventoryAdd(item=False, first=False):
            global Inventory
            if item:
                if first:
                    Inventory.insert(0, item)
                    for e, i in enumerate(Inventory):
                        if i == None:
                            del Inventory[e]
                            break
                else:
                    for e, i in enumerate(Inventory):
                        if i == None:
                            Inventory[e] = item
                            break

        # REMOVE ITEM FROM INVENTORY
        # Call this -- $ InventoryRemove("itemname") -- to remove an item from inventory
        def InventoryRemove(item=False):
            global Inventory
            if item:
                index = Inventory.index(item)
                del Inventory[index]

        # ADD PROFILE TO FOLDER
        def ProfileAdd(item=False, first=False):
            global ProfileFolder
            if item:
                if first:
                    ProfileFolder.insert(0, item)
                    for e, i in enumerate(ProfileFolder):
                        if i == None:
                            del ProfileFolder[e]
                            break
                else:
                    for e, i in enumerate(ProfileFolder):
                        if i == None:
                            ProfileFolder[e] = item
                            break

        # REMOVE PROFILE FROM INVENTORY
        def ProfileRemove(item=False):
            global ProfileFolder
            if item:
                index = ProfileFolder.index(item)
                del ProfileFolder[index]


        # UPDATE ITEM INFO
        # Call this with any combination of its keyword arguments to assign or change the relevant detail
        # Example: $ ItemUpdate(
        #                    "BigClue",
        #                    image="bigclue_version2",
        #                    text="I'm replacing this item's text with new information!",
        #                    )
        def ItemUpdate(item, image=False, text=False, state=False):
            global Items
            if image:
                Items[item]["Image"] = image
            if text:
                Items[item]["Text"] = text

            if state:
                Items[item]["State"] = state
            else:
                Items[item]["State"] = "Updated"


        # UPDATE PROFILE INFO
        # Call this with any combination of its keyword arguments to assign or change the relevant detail
        # Example: $ ProfileUpdate(
        #                        "Person1",
        #                        image="person1_dead",
        #                        name="Person 1, AKA 'The Claw'",
        #                        status="Alive",
        #                        occupation="Burglar",
        #                        relationship="Sister of Person 2",
        #                        text="I'm replacing this profile's text with new information!",
        #                        )
        # Example 2: $ ProfileUpdate(
        #                        "Person1",
        #                        status="Deceased",
        #                        )

        def ProfileUpdate(item, image=False, text=False, state=False):
            global Profiles
            if image:
                Profiles[item]["Image"] = image
            if name:
                Profiles[item]["Name"] = text
            if status:
                Profiles[item]["Status"] = text
            if occupation:
                Profiles[item]["Occupation"] = text
            if relationship:
                Profiles[item]["Relationship"] = text
            if text:
                Profiles[item]["Text"] = text

            if state:
                Profiles[item]["State"] = state
            else:
                Profiles[item]["State"] = "Updated"
