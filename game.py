'''
Copyright (C) 2016 Ermiya Eskandary
This program is free software:
you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.
If not, see <http://www.gnu.org/licenses/>./gpl-howto.html
'''
# Game "data" - rooms and doors to get to different rooms in a way
pages = {
    'yourbedroom': {
        'desc': "You're lying in your bedroom after sleeping in late on Saturday. You can hear your Mom yelling at you: she wants you to go get the mail. You glance out the windows and see the bright sun shining in and a clear, blue sky. You live on the second floor, so you're going to have to get down to ground level. Yes, all the way down there.",
        'choices': [("Head out of your room to the top of the stairs.", 'topofthestairs'),
                    ("Ignore your Mom and try to get some more sleep.", 'ignoreyourmom'),
                    ("Forget all that walking, just jump out the window!", 'fallingdeath')]
    },
    'ignoreyourmom': {
        'desc': "You lie back down, but before you can get to sleep again, you hear your Mom yelling at you again to get the mail!",
        'choices': [("Fine. Get up and head out the window, the shortest path to the mailbox.", 'fallingdeath'),
                    ("Get up and head out of your room like a normal person.", 'topofthestairs'),
                    ("Continue to Ignore Mom.", 'continuetoignoremom')]
    },
    'continuetoignoremom': {
        'desc': "Your Mom stomps into your room. Like a whirlwind, she grabs up your gaming system, your laptop, and the extension cord to power all your electronics. She says, 'I'll trade you all these for the darn mail! Now go!' She stomps out of the room with her armload of stuff.",
        'choices': [("Roll over and go back to sleep. You'll get your stuff later.", 'backtosleep'),
                    ("Wake up just slightly and head out the window towards the mailbox far below.", 'fallingdeath'),
                    ("Realize you want your stuff, get up, and head out towards the stairs finally.", 'topofthestairs')]
    },
    'backtosleep': {
        'desc': "Ah, sweet sleep! You really do like the peaceful state of dreaming. You fly for a little bit, once right over your own mailbox. You fly towards the trees when you feel something hard and heavy hit you in the rear! Whack! Hey, that hurt! This is a crappy dream! Whack! Oh wait, this isn't a dream, it's your dad waking you up with a paddle! Whack!",
        'choices': [("Ahhhh! Jump up and dive out the window!", 'fallingdeath'),
                    ("Eeeek! Jump up and run through the hallway and down the stairs!", 'livingroom')]
    },
    'fallingdeath': {
        'desc': "Really? Did you think you were superman? Guess what? You're not. You can't fly. In fact, you just fell to your death. Sorry about that.",
        'end': 'yes'
    },
    'callyourmomforhelp': {
        'desc': "'Mooooooooommmmmmm!' You cry like a little girl for help. Maybe you are a little girl, in which case that actually makes sense. Either way, your mom sticks her head out of the back room, looks at you and the dog and laughs. 'Psst! Here, Buttercup!' The dog turns and looks at your mom, then quickly pads off after her. The way down the stairs is now clear.",
        'choices': [("Head down the stairs and to the living room.", 'livingroom')]
    },
    'livingroom': {
        'desc': "You are standing in the living room at the bottom of the stairs.",
        'choices': [("Head out the front door.", 'headoutthefrontdoor'),
                    ("Walk away from the mailbox and into the kitchen for a snack.", 'thekitchen'),
                    ("Go into the garage.", 'thegarage')]
    },
    'snarlingdogkillsyou': {
        'desc': "You feint to the left. The dog starts left. You run right, heading down the stairs. As you start to pass the snarling dog, you feel its teeth get a grip on your ankle. Just as the pain registers, you start to turn. Then you realize that you're running down stairs! You're not sure what part of your body hits the ground first as you and the dog tumble down the stairs, his teeth still locked on your leg. Before you reach the bottom, everything goes dark. Sorry, you didn't get the mail today.",
        'end': 'yes'
    },
    'headoutthefrontdoor': {
        'desc': "You open the door and step outside. As you squint your eyes in the bright sunlight, you head the door close and latch behind you...",
        'choices': [("Look around the front porch.", 'thefrontporch')]
    },
    'thekitchen': {
        'desc': "You are in the kitchen. It is shopping day, so there's no food around for you to grab. You wonder if there might be any cookies in the mail today.",
        'choices': [("Head out the back door, into the back yard.", 'backyard'),
                    ("Go to the living room.", 'livingroom')]
    },
    'thegarage': {
        'desc': "This is the garage, nowhere near the mailbox. Like most garages (except the ones in the movies), this garage is full of junk. It has got so much junk in it, you can't get to the garage door. Instead, you have to head into the house, or out one of the small doors from the garage.",
        'choices': [("Go back into the house.", 'livingroom'),
                    ("Head out the back door, into the back yard.", 'backyard'),
                    ("Go out the 'small' door to the side yard.", 'sideyard')]
    },
    'thefrontporch': {
        'desc': "You are standing on your front porch. The mailbox is not far away, just 50 yards or so. You squint when you look at it, but then suddenly something blocks the sun. Tim the bully stands between you and the mailbox. He's punching his own hand and grinning at you.",
        'choices': [
            ("The only way to beat a bully is to stand up to him! Attack him before he attacks you!", 'beatentoapulp'),
            ("Sure he's big, but he's slow. Run past him for the mailbox!", 'runforthemailbox'),
            ("Yell for Mom.", 'yellformom'), ("Run away from the bully (and the mailbox).", 'sideyard')]
    },
    'beatentoapulp': {
        'desc': "You stand like you've seen them in the movies. You start to dodge and weave, thinking that will help. As you start to move towards him, you are thinking about taking a shot with your left hand when something that feels like a massive hammer slams into the right side of your face. Before you can really realize how much that hurts, another hammer slams into the left side of your face. You think you heard something crack. Hey, when did the sun get over there? And why does everything look so fuzzy? My, isn't that a big boot? Sorry, the bully beat you to a pulp. No mail for you today.",
        'end': 'yes'
    },
    'runforthemailbox': {
        'desc': "It seems that Tim isn't as slow as he looks. When you try to run past him, he quickly and easily steps in your way!",
        'choices': [("You're still on the porch.", 'thefrontporch')]
    },
    'yellformom': {
        'desc': "Mom yells back, 'Shut up and get the mail already!'",
        'choices': [("You're still on the porch.", 'thefrontporch')]
    },
    'sideyard': {
        'desc': "This is the side yard. You are next to your house (nowhere near the mailbox). You can see a nice tree growing in your neighbour's yard, but you have to climb over a fence to get there.",
        'choices': [("Move towards the mailbox and onto your own front porch.", 'thefrontporch'),
                    ("That fence can't stop me! Head to the neighbour's yard.", 'neighboursyard'),
                    ("Since the mailbox is out front, let's head to the back yard.", 'backyard')]
    },
    'topofthestairs': {
        'desc': "Outside your room, there are stairs that lead down to the living room. Strangely enough, there is a rather large, snarling dog sitting on the stairs. It looks at you and growls, baring it's teeth.",
        'choices': [("Forget this, I'm going back to my room.", 'backtosleep'),
                    ("Run past the snarling dog.", 'snarlingdogkillsyou'),
                    ("Call Your Mom For Help", 'callyourmomforhelp'),
                    ("Go down the hallway to your brother's room.", 'brothersroom')]
    },
    'backyard': {
        'desc': "You are now behind your house. There is no sign that there has ever been a mailbox here.",
        'choices': [("Go around your house (towards the mailbox), and to the side yard.", 'sideyard'),
                    ("You've had enough sunlight for one day, head into the garage.", 'thegarage'),
                    ("Go for the back door to the house.", 'thekitchen'),
                    ("Wander away and into the woods behind your house.", 'inthewoods')]
    },
    'brothersroom': {
        'desc': "Your brother's room is a mess. That's no surprise. It smells like old, moldly gym socks. You look up when you hear a tapping on the window, only to realize that's from the tree that grows right outside his window.",
        'choices': [("Exit this smelly place, back to the stairs!", 'topofthestairs'),
                    ("Head out this window.", 'inatree')]
    },
    'inatree': {
        'desc': "You're in a tree outside your brother's room. There's a nice view from here, you can see the mailbox just a short distance away, up by the street.",
        'choices': [("Head back into your brother's window.", 'brothersroom'),
                    ("Climb down the tree.", 'neighboursyard')]
    },
    'neighboursyard': {
        'desc': "You find yourself in your neighbour's yard (they live close by). You're standing at the bottom of a large tree that looks quite easy to climb. Oh, and the neighbour's yard is fenced in. Why? Because they have a large, vicious rabbit that lives here. In fact, that's him, right over there, running towards you!",
        'choices': [("Climb up that tree as fast as you can.", 'inatree'),
                    ("Stand your ground! The rabbit isn't that big!", 'viciousrabbitattack'),
                    ("Run away! Run as fast as you can!", 'inthewoods')]
    },
    'viciousrabbitattack': {
        'desc': "Oh sure, it's just a little bunny. But look at the fangs, man! Too late, the vorpal rabbit has decapitated you. Sorry about that, the mail will have to wait for someone else to get it.",
        'end': 'yes'
    },
    'inthewoods': {
        'desc': "You made it through the woods. You can see a mailbox! Sorry, that's not your mailbox. That's the street behind your house.",
        'choices': [("Take a right and head north.", 'northblock'), ("Take a left and head south.", 'southblock')]
    },
    'northblock': {
        'desc': "You are north a block from the back side of your house, far from the mailbox. There is a parade going on here with circus animals and people all around. You know that your mailbox (and house) are to the right, but you see a policeman nearby, watching the parade. You know that 'the law' says you should walk on the left side of the street, but to do that, you need to cross the street...",
        'choices': [("Cross the street", 'crossthestreet'), ("Walk on the Wrong Side", 'walkonthewrongside'),
                    ("Wait for the parade", 'waitfortheparade'),
                    ("Head back south, into the woods behind your house.", 'inthewoods')]
    },
    'crossthestreet': {
        'desc': "You wait for a marching band to pass, and then you make a run for it. Sadly, you didn't check to see what was coming down the street next. It was the elephants. And no, not the slow elephants. There is a loud trumpeting sound, then you are squashed beneath the large feet of a grey elephant. The elephant isn't getting your mail for you, either.",
        'end': 'yes'
    },
    'walkonthewrongside': {
        'desc': "You are casually strolling along, half-watching the parade, but walking on the wrong side of the street. A policeman sees you and yells at you, 'Hey! You there! Stop!' He starts running towards you!",
        'choices': [("Stop and Wait", 'stopandwait'),
                    ("Run away from him and get lost in the crowd.", 'northyourstreet')]
    },
    'stopandwait': {
        'desc': "You stop and wait for the policeman. He slams into you and throws you on the ground. When you try and stand back up, he pulls his taser out and 50,000 volts are slammed through you. Wow, that hurts! The policeman knees you in the back and pulls your shoulder out of your socket as he puts the cuffs on you. You try and mention your mailbox, but he sprays mace in your face. You cough and sputter as he throws you in the back of his police car. Maybe if you get out on bail you can get the mail.",
        'end': 'yes'
    },
    'waitfortheparade': {
        'desc': "It is a long parade. There are animals and marching bands. There are fire trucks and cheerleaders. Hey look, there's some tractor floats coming your way now.",
        'choices': [("It's a long parade.", 'northblock')]
    },
    'southblock': {
        'desc': "You are standing at the end of the road, a block away from your house. As you start to head for your own street, you hear the wail of sirens and the squealing of tires. A car chase! Right here in your own neighbourhood! Neat, huh?",
        'choices': [("Go back up the street, away from the car chase and your mailbox.", 'inthewoods'),
                    ("Keep watching the car chase and head towards your own street.", 'carcrash')]
    },
    'carcrash': {
        'desc': "You walk down the sidewalk. You hear more tires squealing and the sirens get louder. You reach your street and start heading towards your mailbox. Just then, a police car turns the corner, sliding sideways. Another car slams into the police car, and the vehicle rolls over and crushes you. The last thing you see as everything goes dark is your mailbox, just out of your reach.",
        'end': 'yes'
    },
    'northyourstreet': {
        'desc': "You are at the north end of your street. You think you can see your mailbox sitting in front of your house to the south.",
        'choices': [("Head south, down your street, towards your mailbox.", 'constructionsite'),
                    ("Continue east to the next block over.", 'ablockaway')]
    },
    'ablockaway': {
        'desc': "You are a block away from your house, and nowhere near your mailbox.",
        'choices': [("Go south, down the next street over from your street.", 'ablockawaydeadend'),
                    ("Head west, towards your street.", 'northyourstreet'),
                    ("Go north, almost the opposite direction from your mailbox.", 'northdeadend')]
    },
    'northdeadend': {
        'desc': "You are at the end of yet another dead end in this suburban paradise that is your neighbourhood. You really should be looking to get to your mailbox before sunset.",
        'choices': [("Head back south.", 'ablockaway')]
    },
    'ablockawaydeadend': {
        'desc': "Welcome to the east block dead end. There's not much to see here, other than the perfectly manicured lawns. Oh, and an open sewer hole near the side of the road.",
        'choices': [("Head north to another street.", 'ablockaway'), ("Go down into the sewers.", 'mainsewers')]
    },
    'constructionsite': {
        'desc': "There is a large construction site here on your street. The sidewalk on your side of the street is under construction and there are large holes in the ground and heavy equipment working here.",
        'choices': [("Go back up the street, away from your mailbox.", 'northyourstreet'),
                    ("Walk through the construction site, towards your mailbox.", 'constructionpit'),
                    ("Follow the sidewalk detour signs.", 'followthesidewalkdetoursigns')]
    },
    'constructionpit': {
        'desc': "You step around the orange barrier and into the site. You step over some heavy equipment and step in some mud. As you step away, your foot slips and you slide into some wet cement. You fall on the ground and slide into a large constructiion pit. You hit your head on the way down and land in a pile of dynamite. Just as you are starting to wake up, you hear, 'Fire in the Hole' as the dynamite explodes... You're not sure if your own mailbox was destroyed in the blast, but you know you're not getting any mail today.",
        'end': 'yes'
    },
    'followthesidewalkdetoursigns': {
        'desc': "You are walking along the detoured sidewalk and you can see your house and mailbox across the street. You can see a bully standing on your front porch as well. The detour continues both north and south from here.",
        'choices': [("Head towards your mailbox, through the construction site.", 'constructionpit'),
                    ("Taunt the Bully from across the street.", 'tauntthebully'),
                    ("Follow the construction detour south.", 'southblock'),
                    ("Follow the construction detour north.", 'constructionsite')]
    },
    'tauntthebully': {
        'desc': "You stick your tongue out at the bully. Then you turn around and moon him. Strangely enough, he actually sees you and starts running towards you. He skillfully dodges the mud, wet concrete, and a pit. He is suddenly standing right next to you. He smiles and punches you in the face. The mailbox across the street is the last thing you see as your vision fades and you realize that you won't be getting the mail today...",
        'end': 'yes'
    },
    'mainsewers': {
        'desc': "You are at the bottom of the main sewer line. Yuck.",
        'choices': [("Head north, deeper into the sewers.", 'asmallsewer'),
                    ("Head south, towards a stronger sewer stink.", 'asmellysewer'),
                    ("Head east, towards a wetter sewer.", 'awetsewer'),
                    ("Head west, towards an echoing sewer.", 'asewerpit'),
                    ("Climb the ladder up and out of the sewers.", 'ablockawaydeadend')]
    },
    'asmallsewer': {
        'desc': "This is a much smaller sewer. You have to bend down to fit through this area.",
        'choices': [("Head south, towards a larger sewer space.", 'mainsewers'),
                    ("Head north, deeper into the sewers.", 'alittlesewer')]
    },
    'alittlesewer': {
        'desc': "You have to crawl at this point to continue through the sewers. This place is nasty.",
        'choices': [("Head south, towards a larger sewer space.", 'asmallsewer'),
                    ("Head north, deeper into the sewers.", 'atinysewer')]
    },
    'atinysewer': {
        'desc': "It is hard to breathe here because of the stink. The sewers continue north, but you're going to have to crawl to be able to fit there...",
        'choices': [("Crawl north, deeper into the sewers.", 'sewerdeadend'),
                    ("Head south, towards a larger sewer space.", 'alittlesewer')]
    },
    'sewerdeadend': {
        'desc': "You are crawling on your belly here and getting sewer goop all down your shirt. The sewer continues to get smaller and smaller until you simply cannot go any further.",
        'choices': [("Crawl back to the south.", 'atinysewer')]
    },
    'asmellysewer': {
        'desc': "This section of the sewer smells, somehow much worse than other areas.",
        'choices': [("Head north, away from the smelliest part of the sewer.", 'mainsewers'),
                    ("Go east, to see if you can find the source of the stink.", 'astinkysewer')]
    },
    'astinkysewer': {
        'desc': "Wow. It really stinks here. You've never smelled a sewer that was this horrible.",
        'choices': [("Head north, away from the serious stink.", 'awetsewer'),
                    ("Go west, where it is not quite a stinky.", 'asmellysewer')]
    },
    'awetsewer': {
        'desc': "This area of the sewer is very wet. You don't want to know why.",
        'choices': [("Go west, towards a dryer section of sewer.", 'mainsewers'),
                    ("Go east, where you can hear running water.", 'arunningsewer'),
                    ("Head south, where it smells a little worse.", 'astinkysewer')]
    },
    'arunningsewer': {
        'desc': "There is flowing sewage here. It smells. It smells bad. The flowing sewage heads off to the north.",
        'choices': [("Head north, to see where the sewage is going.", 'aslipperysewer'),
                    ("Head west, away from the flowing sewage.", 'awetsewer')]
    },
    'aslipperysewer': {
        'desc': "There is more sewage here. There is flowing sewage with some rather horrid large chunks. This is really getting nasty. The flow is flowing downhill, away from you. It is getting very slippery with all the raw sewage sliding around here.",
        'choices': [("Head south, away from the flowing sewage.", 'arunningsewer'),
                    ("Continue to follow the slipperty sewage north.", 'slidingdeath')]
    },
    'slidingdeath': {
        'desc': "You continue to head north and the sewer gets more and more slippery. You slip and fall and the sewage starts shoving you along. You start gaining speed and something soft and wet smacks you in the back of the head. It is pitch dark by now, so you couldn't see what it was if you wanted to. You start sliding up and down the sides of the sewer as the passage gets steeper. Suddenly you find yourself falling through space... In the darkness, you have no idea what is going on, or when it will end. You feel and hear the splash as you land in more sewage. You quickly go under the surface and are completely immersed in the sewage. You cannot tell which way is up. Your lungs are bursting, but you cannot even imagine opening your mouth. You struggle and swim around, but you bump into nothing but walls. Finally your lungs can take no more and you attempt to take a breath. You breathe in nothing but sewage. Thankfully, you do not last long before you pass out... Sorry, there will be no mail-getting for you today!",
        'end': 'yes'
    },
    'asewerpit': {
        'desc': "There is a large sewer pit here. There is stuff floating in the sewage. It's pretty darn nasty. If you jump or dive in, you're pretty sure you won't be able to get back up to where you are now.",
        'choices': [("Go east.", 'mainsewers'),
                    ("Jump right in and try to swim across the sewage!", 'swimmingthroughsewage'),
                    ("Dive in and search for a secret passage at the bottom.", 'sewerdeath')]
    },
    'swimmingthroughsewage': {
        'desc': "You jump right in and try and avoid the larger chunks floating around. This is nasty. After swimming for a minute, you see an area that opens up to a dry area of sewer and you can see light filtering in through an opening above!",
        'choices': [("Pull yourself out of the sewage and onto the open space.", 'adrysewer')]
    },
    'adrysewer': {
        'desc': "You are standing at a rather dry area of the sewer. There is a ladder that leads up to the street here.",
        'choices': [("Climb the ladder up and out of the sewers.", 'themailbox')]
    },
    'themailbox': {
        'desc': "Yes, really. You climb out of the sewer and find yourself standing right in front of your mailbox! You win! Oh sure, you might have a few cuts and bruises, and you really stink after swimming through that sewage, but you have made it to the mailbox! Hooray! You open the mailbox... and find that it is empty. I guess you didn't get any mail today...",
        'end': 'yes'
    },
    'sewerdeath': {
        'desc': "Really? Why would you do that? Okay... You dive in and plow right through some semi-soft sewage 'stuff.' When you get under the surface you realize how horrible this idea could be. You cannot see anything. You reach around in the darkness. You find nasty sewage stuff. Suddenly you realize you don't know which way is up. Without thinking, you open your eyes. Yeah, that didn't help at all. You are floating around in raw sewage, under the surface, lost... You're going to die, but this death is just too nasty for me to describe! Your mom is going to have to find someone else to get your mail today (and every other day, too, apparently).",
        'end': 'yes'
    },
    'INTRODUCTION': "Go Get The Mail! \n You have a simple task -- go and get the mail. Oh, it sounds easy, but could you ever imagine how many different things could get in your way?",
    'COPYRIGHT': "2016, by Ermiya Eskandary",
    'OUTRO': "Thanks for playing!",
}

def main_Function(pages, startpage):
    ''''
    Main game function
    pages : a dictionary of game pages.
    startpage : starting page
    pageid : starting pageid.
    '''
    # Check the pages using the function "check_Pages"
    if not check_Pages(pages):
        # Display an error message
        print("there is some error in the pages data, ending game")
        return None
    # Display the page "INTRODUCTION"
    print(pages.get("INTRODUCTION"))
    # Display the page "COPYRIGHT"
    print("\n\nCopyright: " + pages.get("COPYRIGHT") + "\n")

    # Starting page
    page = pages[startpage]
    # Display the page's description
    print(page['desc'] + '\n')
    # If the page isn't an "end" page where there are no other pages left, continue
    while not page.get("end", None):
        # Find out what your choice is, acting accordingly
        pageid = move(page['choices'])
        # Current page is the page where the user moved to
        page = pages[pageid]
        # Display the description for the new page
        print("\n", page['desc'], "\n")
    # If there are no other choices left, on an "end" page, ask them if they want to play again
    # If yes
    if page['end'] == 'yes':
        # Play again
        playagain()
    # If not
    else:
        # Should never happen - debugging purposes
        print("This shouldn't happen!")
def check_Pages(pages):
    '''
    Checks if everything is ok so we can move on - makes sure that every page has choices coming off it or it is an "end" page. We also assume that UPPERCASE pageids are special, and aren't real pages - for example pages like COPYRIGHT and OUTRO aren't part of the game
    '''
    # Variable to check the status of everything
    allok = True
    # Loop through the pageids
    for pageid in pages:
        # If they are uppercase, skip them
        if pageid.isupper():
            # we skip over INTRODUCTION, COPYRIGHT and OUTRO
            continue
        # Current page is the pageid of the page given as input to the function
        page = pages[pageid]
        # Get the choices available
        choices = page.get('choices', [])
        # Check for end page - is it the end of the game ?
        end = page.get('end', None)
        # If we have choices and an "end" page
        if choices and end:
            # Display the page id and relevant information - for debugging purposes
            print(pageid, ": choices and end, both defined")
            # Everything isn't ok
            allok = False
        # If we don't have choices and there isn't an "end" page
        if not choices and end != "yes":
            # Display the page id and relevant information - for debugging purposes
            print(pageid, ": no choices and end isn't 'yes'")
            # Everything isn't ok
            allok = False
    # Return the variable which defines if everything is ok
    return allok
def move(choices):
    '''
    Moves the user from page to page based on choices
    Get player move from choices, returning a pageid.
    choices:  a list of page choices, where each choice is: text, nextpage.
    '''
    # Display a bit of text
    print("----From here, you can -----")
    # Start our numbering with 1
    ii = 1
    # Valid choices in a dictionary, as the name suggests
    valid_choices = {}
    # Loop through the choices
    for choice in choices:
        # Save the text
        text = choice[0]
        # Save the pageid
        pageid = choice[1]
        # Name the different parts of the choice, with more meaningful names
        # We str(ii) as the user input will be a string
        valid_choices[str(ii)] = pageid
        # Display the choices, numbered, and their text
        print(ii, ")", text)
        # Increment the numbers so we don't have two choices with 1)
        ii += 1
    # Answer - user input
    ans = None
    # If we don't have an answer, get the user input (answer) and clean it up
    while ans is None:
        # Get user input
        ans = input("Choose from " + str(sorted(valid_choices)) + ":  ").lower().strip()
        # If we have a valid answer
        if ans in valid_choices:
            # Return the answer chosen - a page id
            return valid_choices[ans]
        # If we don't have a valid answer
        else:
            # Display an error message
            print("Your answer,", ans, ", isn't in the choices\n")
            # Set the answer as "None" so that we can ask again
            ans = None

def playagain():
    '''
    Prompts user if they want to play again
    '''
    # Keep asking when function is called
    while True:
        # Ask for input from user
        try:
            # Asking user if they want to play again and converting it to lower case characters
            replay = input("Do you want to play again? ").lower()
        # If user inputs an inappropiate value
        except ValueError:
            # Ask again
            print("Sorry, Invalid Entry")
            continue
        # If the user says "yes" in one form or the other
        if replay in ("yes","y","true","t"):
            # Run the game again
            main()
            return()
        # If the user says "no" in one form or the other
        elif replay in ("no","n","false","f"):
            # Display the "OUTRO" page
            print (pages.get("OUTRO"))
            return
        # If input is invalid, ask again
        else:
            print("Invalid entry, Please enter yes or no")


# Start the game - main loop
def main():
    # Only execute when user wants to run the module as a program
    if __name__ == "__main__":
        # Beginning page as input to the main function
        main_Function(pages, "yourbedroom")
# Call main loop
main()
