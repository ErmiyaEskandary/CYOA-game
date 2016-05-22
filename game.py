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
# import time
# Main Loop
def main():
    # "Make the book"
    story = make_book()
    # "Read" the book
    story.read()

# Creates the "book"
def make_book():
    # The main story and the choices available
    story = Book('Go Get The Mail! \n You have a simple task -- go and get the mail. Oh, it sounds easy, but could you ever imagine how many different things could get in your way?\n BTW, if you think this game does not finish, then you are mistaken.',
                 'Read LICENSE.MD for license info',
                 'Thank you for playing!')
    story['bedroom'] = Page('You are lying in your bedroom after sleeping in late on Saturday. You can hear your mom yelling at you: she wants you to go get the mail. You glance out the windows and see the bright sun shining in and a clear, blue sky. You live on the second floor, so you are going to have to get down to ground level. Yes, all the way down there.',
                          topofthestairs='Head out of your room to the top of the stairs.',
                          ignoreyourmom='Ignore your mom and try to get some more sleep.',
                          fallingdeath='Forget all that walking, just jump out the window!')
    story['ignoreyourmom'] = Page('You lie back down, but before you can get to sleep again, you hear your mom yelling at you again to get the mail!',
                         fallingdeath='Fine. Get up and head out the window, the shortest path to the mailbox.',
                         topofthestairs='Get up and head out of your room like a normal person.',
                         continuetoignoremom='Continue to ignore mom.')
    story['continuetoignoremom'] = Page('Your mom stomps into your room. Like a whirlwind, she grabs up your gaming system, your laptop, and the extension cord to power all your electronics. She says, "I will trade you all these for the darn mail! Now go!" She stomps out of the room with her armload of stuff.',
                         backtosleep='Roll over and go back to sleep. You will get your stuff later.',
                         fallingdeath='Wake up just slightly and head out the window towards the mailbox far below.',
                         topofthestairs='Realize you want your stuff, get up, and head out towards the stairs finally.')
    story['backtosleep'] = Page('Ah, sweet sleep! You really do like the peaceful state of dreaming. You fly for a little bit, once right over your own mailbox. You fly towards the trees when you feel something hard and heavy hit you in the rear! Whack! Hey, that hurt! This is a crappy dream! Whack! Oh wait, this is not a dream, it is your dad waking you up with a paddle! Whack!',
                         fallingdeath='Ahhhh! Jump up and dive out the window!',
                         livingroom='Eeeek! Jump up and run through the hallway and down the stairs!')
    story['fallingdeath'] = Page('Really? Did you think you were superman? Guess what? You aint. You cannot fly. In fact, you just fell to your death. Sorry about that.')
    story['callyourmomforhelp'] = Page('"Mooooooooommmmmmm!" You cry like a little girl for help. Maybe you are a little girl, in which case that actually makes sense. Either way, your mom sticks her head out of the back room, looks at you and the dog and laughs. "Psst! Here, Buttercup!" The dog turns and looks at your mom, then quickly pads off after her. The way down the stairs is now clear.',
                         livingroom='Head down the stairs and to the living room.',)
    story['livingroom'] = Page('You are standing in the living room at the bottom of the stairs.',
                         headoutthefrontdoor='Head out the front door.',
                         thekitchen='Walk away from the mailbox and into the kitchen for a snack.',
                         thegarage='Go into the garage.')
    story['snarlingdogkillsyou'] = Page('You feint to the left. The dog starts left. You run right, heading down the stairs. As you start to pass the snarling dog, you feel its teeth get a grip on your ankle. Just as the pain registers, you start to turn. Then you realize that you are running down stairs! You are not sure what part of your body hits the ground first as you and the dog tumble down the stairs, his teeth still locked on your leg. Before you reach the bottom, everything goes dark. Sorry, you did not get the mail today.')
    story['headoutthefrontdoor'] = Page('You open the door and step outside. As you squint your eyes in the bright sunlight, you head the door close and latch behind you...',
                         thefrontporch='Look around the front porch.',)
    story['thekitchen'] = Page('You are in the kitchen. It is shopping day, so there is no food around for you to grab. You wonder if there might be any cookies in the mail today.',
                         backyard='Head out the back door, into the back yard.',
                         livingroom='Go to the living room.')
    story['thegarage'] = Page('This is the garage, nowhere near the mailbox. Like most garages (except the ones in the movies), this garage is full of junk. It has got so much junk in it, you cannot get to the garage door. Instead, you have to head into the house, or out one of the small doors from the garage.',
                         livingroom='Go back into the house.',
                         backyard='Head out the back door, into the back yard.',
                         sideyard='Go out the "small" door to the side yard.')
    story['thefrontporch'] = Page('You are standing on your front porch. The mailbox is not far away, just 50 yards or so. You squint when you look at it, but then suddenly something blocks the sun. Tim the bully stands between you and the mailbox. He looks like he wants to beat you up...',
                         beatentoapulp='The only way to beat a bully is to stand up to him! Attack him before he attacks you!',
                         runforthemailbox='Sure he is big, but he is slow, you think. Run past him for the mailbox!',
                         yellformom='Yell for mom.',
                         sideyard='Run away from the bully (and the mailbox).')
    story['beatentoapulp'] = Page('You stand like you have seen them in the movies. You start to dodge and weave, thinking that will help. As you start to move towards him, you are thinking about taking a shot with your left hand when something that feels like a massive hammer slams into the right side of your face. Before you can really realize how much that hurts, another hammer slams into the left side of your face. You think you heard something crack. Hey, when did the sun get over there? And why does everything look so fuzzy? My, is that a... big boot? Sorry, the bully beat you to a pulp. No mail for you today.')
    story['runforthemailbox'] = Page('It seems that Tim is not as slow as he looks. When you try to run past him, he quickly and easily steps in your way!',
                         thefrontporch='You are still on the porch.')
    story['yellformom'] = Page('mom yells back, "Shut up and get the mail already!"',
                         thefrontporch='You are still on the porch.')
    story['sideyard'] = Page('This is the side yard. You are next to your house (nowhere near the mailbox). You can see a nice tree growing in your neighbours yard, but you have to climb over a fence to get there.',
                         thefrontporch='Move towards the mailbox and onto your own front porch.',
                         neighboursyard='That fence cannot stop me! Head to the neighbours yard.',
                         backyard='Since the mailbox is out front, lets head to the back yard.')
    story['topofthestairs'] = Page('Outside your room, there are stairs that lead down to the living room. Strangely enough, there is a rather large, snarling dog sitting on the stairs. It looks at you and growls, baring its teeth.',
                         backtosleep='Forget this - Going to my room.',
                         snarlingdogkillsyou='Run past the snarling dog.',
                         callyourmomforhelp='Call your mom For help',
                        brothersroom='Go down the hallway to your brothers room.')

    story['backyard'] = Page('You are now behind your house. There is no sign that there has ever been a mailbox here.',
                         sideyard='Go around your house (towards the mailbox), and to the side yard.',
                         thegarage='You have had enough sunlight for one day, head into the garage.',
                         thekitchen='Go for the back door to the house.',
                         inthewoods='Wander away and into the woods behind your house.')
    story['brothersroom'] = Page('Your brothers room is a mess - that is no surprise. It smells like old, moldly gym socks. You look up when you hear a tapping on the window, only to realize the sound is from the tree that grows right outside his window.',
                         topofthestairs='Exit this smelly place, back to the stairs!',
                         inatree='Head out this window.')
    story['inatree'] = Page('You are in a tree outside your brothers room. You can see the mailbox just a short distance away, up by the street',
                         brothersroom='Head back into your brothers window.',
                         neighboursyard='Climb down the tree.')
    story['neighboursyard'] = Page('You find yourself in your neighbours yard (they live close by). You are standing at the bottom of a large tree that looks quite easy to climb. Oh, and the neighbours yard is fenced in. Why? Because they have a large, vicious rabbit that lives here. In fact, that is him, right over there, running towards you!',
                         inatree='Climb up that tree as fast as you can.',
                         viciousrabbitattack='Stand your ground! The rabbit is not that big!',
                         inthewoods='Run away! Run as fast as you can!')
    story['viciousrabbitattack'] = Page('Oh sure, just a little bunny. But look at the fangs, man! Too late, the vorpal rabbit has decapitated you. Sorry about that, the mail will have to wait for someone else to get it.')
    story['inthewoods'] = Page('You made it through the woods. You can see a mailbox! Sorry, now that you pay attention, you realise it is not your mailbox - that is the street behind your house.',
                         northblock='Take a right and head north.',
                         southblock='Take a left and head south.')
    story['northblock'] = Page('You are north a block from the back side of your house, far from the mailbox. There is a parade going on here with circus animals and people all around. You know that your mailbox (and house) are to the right, but you see a policeman nearby, watching the parade. You know that "the law" says you should walk on the left side of the street, but to do that, you need to cross the street...',
                         crossthestreet='Cross the street',
                         walkonthewrongside='Walk on the Wrong Side',
                         waitfortheparade='Wait for the parade',inthewoods='Head back south, into the woods behind your house.',)
    story['crossthestreet'] = Page('You wait for a marching band to pass, and then you make a run for it. Sadly, you did not check to see what was coming down the street next. It was the elephants. And no, not the slow elephants. There is a loud trumpeting sound, then you are squashed beneath the large feet of a grey elephant. The elephant is not getting your mail for you, either.')
    story['walkonthewrongside'] = Page('You are casually strolling along, half-watching the parade, but walking on the wrong side of the street. A policeman sees you and yells at you, "Hey! You there! Stop!" He starts running towards you!',
                         stopandwait='Stop and Wait',
                         northyourstreet='Run away from him and get lost in the crowd.')
    story['stopandwait'] = Page('You stop and wait for the policeman. He slams into you and throws you on the ground. When you try and stand back up, he pulls his taser out and 50,000 volts are slammed through you. Wow, that hurts! The policeman knees you in the back and pulls your shoulder out of your socket as he puts the cuffs on you. You try and mention your mailbox, but he sprays mace in your face. You cough and sputter as he throws you in the back of his police car. Maybe if you get out on bail you can get the mail.')
    story['waitfortheparade'] = Page('It is a long parade. There are animals and marching bands. There are fire trucks and cheerleaders. Hey look, there is some tractor floats coming your way now.',
                         northblock='Just a long parade. Nothing to do here.')
    story['southblock'] = Page('You are standing at the end of the road, a block away from your house. As you start to head for your own street, you hear the wail of sirens and the squealing of tires. A car chase! Right here in your own neighbourhood!',
                         inthewoods='Go back up the street, away from the car chase and your mailbox.',
                         carcrash='Keep watching the car chase and head towards your own street.')
    story['carcrash'] = Page('You walk down the sidewalk. You hear more tires squealing and the sirens get louder. You reach your street and start heading towards your mailbox. Just then, a police car turns the corner, sliding sideways. Another car slams into the police car, and the vehicle rolls over and crushes you. The last thing you see as everything goes dark is your mailbox, just out of your reach.')
    story['northyourstreet'] = Page('You are at the north end of your street. You think you can see your mailbox sitting in front of your house to the south.',
                         constructionsite='Head south, down your street, towards your mailbox.',
                         ablockaway='Continue east to the next block over.')
    story['northdeadend'] = Page('You are at the end of yet another dead end in this suburban paradise that is your neighbourhood. You really should be looking to get to your mailbox before sunset.',
                         ablockaway='Head back south.')
    story['ablockaway'] = Page('You are a block away from your house, and nowhere near your mailbox.',
                         ablockawaydeadend='Go south, down the next street over from your street.',
                         northyourstreet='Head west, towards your street.',
                         northdeadend='Go north, almost the opposite direction from your mailbox.')
    story['ablockawaydeadend'] = Page('Welcome to the east block dead end. Not much to see here, other than the perfectly manicured lawns. Oh, and an open sewer hole near the side of the road.',
                         ablockaway='Head north to another street.',
                         mainsewers='Go down into the sewers.')
    story['constructionsite'] = Page('There is a large construction site here on your street. The sidewalk on your side of the street is under construction and there are large holes in the ground and heavy equipment working here.',
                         northyourstreet='Go back up the street, away from your mailbox.',
                         constructionpit='Walk through the construction site, towards your mailbox.',
                         followthesidewalkdetoursigns='Follow the sidewalk detour signs.')
    story['constructionpit'] = Page('You step around the orange barrier and into the site. You step over some heavy equipment and step in some mud. As you step away, your foot slips and you slide into some wet cement. You fall on the ground and slide into a large constructiion pit. You hit your head on the way down and land in a pile of dynamite. Just as you are starting to wake up, you hear, "Fire in the Hole" as the dynamite explodes... You are not sure if your own mailbox was destroyed in the blast, but you know you are not getting any mail today.')
    story['followthesidewalkdetoursigns'] = Page('You are walking along the detoured sidewalk and you can see your house and mailbox across the street. You can see a bully standing on your front porch as well. The detour continues both north and south from here.',
                         constructionpit='Head towards your mailbox, through the construction site.',
                         tauntthebully='Taunt the Bully from across the street.',
                         southblock='Follow the construction detour south.',
                         constructionsite='Follow the construction detour north.',)
    story['tauntthebully'] = Page('You stick your tongue out at the bully. Then you turn around and moon him. Strangely enough, he actually sees you and starts running towards you. He skillfully dodges the mud, wet concrete, and a pit. He is suddenly standing right next to you. He smiles and punches you in the face. The mailbox across the street is the last thing you see as your vision fades and you realize that you  will not collect any mal today...')
    story['mainsewers'] = Page('You are at the bottom of the main sewer line. Disgusting.',
                         asmallsewer='Head north, deeper into the sewers.',
                         asmellysewer='Head south, towards a stronger sewer stink.',
                         awetsewer='Head east, towards a wetter sewer.',
                         asewerpit='Head west, towards an echoing sewer.',
                         ablockawaydeadend='Climb the ladder up and out of the sewers.',)
    story['asmallsewer'] = Page('This is a much smaller sewer. You have to bend down to fit through this area.',
                         mainsewers='Head south, towards a larger sewer space.',
                         alittlesewer='Head north, deeper into the sewers.')
    story['alittlesewer'] = Page('You have to crawl at this point to continue through the sewers. This place is nasty.',
                         asmallsewer='Head south, towards a larger sewer space.',
                         atinysewer='Head north, deeper into the sewers.')
    story['atinysewer'] = Page('It is hard to breathe here because of the stink. The sewers continue north, but you are going to have to crawl to be able to fit there...',
                         sewerdeadend='Crawl north, deeper into the sewers.',
                         alittlesewer='Head south, towards a larger sewer space.')
    story['sewerdeadend'] = Page('You are crawling on your belly here and getting sewer goop all down your shirt. The sewer continues to get smaller and smaller until you simply cannot go any further.',
                         atinysewer='Crawl back to the south.')
    story['asmellysewer'] = Page('This section of the sewer smells, somehow much worse than other areas.',
                         mainsewers='Head north, away from the smelliest part of the sewer.',
                         astinkysewer='Go east, to see if you can find the source of the stink.')
    story['astinkysewer'] = Page('Wow. It really stinks here. You have never smelled a sewer that was this horrible.',
                         awetsewer='Head north, away from the serious stink.',
                         asmellysewer='Go west, where it is not quite as stinky.')
    story['awetsewer'] = Page('This area of the sewer is very wet. You do not want to know why.',
                         mainsewers='Go west, towards a dryer section of sewer.',
                         arunningsewer='Go east, where you can hear running water.',
                         astinkysewer='Head south, where it smells a little worse.')
    story['arunningsewer'] = Page('There is flowing sewage here. It smells. It smells bad. The flowing sewage heads off to the north.',
                         aslipperysewer='Head north, to see where the sewage is going.',
                         awetsewer='Head west, away from the flowing sewage.')
    story['aslipperysewer'] = Page('There is more sewage here. There is flowing sewage with some rather horrid large chunks. This is really getting nasty. The flow is flowing downhill, away from you. It is getting very slippery with all the raw sewage sliding around here.',
                         arunningsewer='Head south, away from the flowing sewage.',
                         slidingdeath='Continue to follow the slippery sewage north.')
    story['slidingdeath'] = Page('You continue to head north and the sewer gets more and more slippery. You slip and fall and the sewage starts shoving you along. You start gaining speed and something soft and wet smacks you in the back of the head. It is pitch dark by now, so you could not see what it was if you wanted to. You start sliding up and down the sides of the sewer as the passage gets steeper. Suddenly you find yourself falling through space... In the darkness, you have no idea what is going on, or when it will end. You feel and hear the splash as you land in more sewage. You quickly go under the surface and are completely immersed in the sewage. You cannot tell which way is up. Your lungs are bursting, but you cannot even imagine opening your mouth. You struggle and swim around, but you bump into nothing but walls. Finally your lungs can take no more and you attempt to take a breath. You breathe in nothing but sewage. Thankfully, you do not last long before you pass out... Sorry, there will be no mail-getting for you today!')
    story['asewerpit'] = Page('There is a large sewer pit here. There is stuff floating in the sewage. It is pretty nasty. If you jump or dive in, you are pretty sure you will nott be able to get back up to where you are now.',
                         mainsewers='Go east.',
                         swimmingthroughsewage='Jump right in and try to swim across the sewage!',
                         sewerdeath='Dive in and search for a secret passage at the bottom.')
    story['swimmingthroughsewage'] = Page('You jump right in and try and avoid the larger chunks floating around. This is nasty. After swimming for a minute, you see an area that opens up to a dry area of sewer and you can see light filtering in through an opening above!',
                         adrysewer='Pull yourself out of the sewage and onto the open space.')
    story['adrysewer'] = Page('You are standing at a rather dry area of the sewer. There is a ladder that leads up to the street here.',
                         themailbox='Climb the ladder up and out of the sewers.')
    story['themailbox'] = Page('Yes, really. You climb out of the sewer and find yourself standing right in front of your mailbox! You win! Oh sure, you might have a few cuts and bruises, and you really stink after swimming through that sewage, but you have made it to the mailbox! Hooray! You open the mailbox... and find that it is empty. I guess you did not get any mail today anyway...')
    story['sewerdeath'] = Page('Really? Why would you do that? Okay... You dive in and plow right through some semi-soft sewage "stuff."" When you get under the surface you realize how horrible this idea could be. You cannot see anything. You reach around in the darkness. You find nasty sewage stuff. Suddenly you realize you do not know which way is up. Without thinking, you open your eyes. Yeah, that did not help at all. You are floating around in raw sewage, under the surface, lost... You are going to die, but this death is just too nasty for me to describe! Your mom is going to have to find someone else to get your mail today (and every other day, too, apparently')
    return story

# Class for the "book"
class Book:
    # All "books" have an intro, outro, copyright page and they all have to have pages
    # "self.__root" : current page
    def __init__(self, introduction, copyright, outro):
        self.__introduction = introduction
        self.__copyright = copyright
        self.__outro = outro
        self.__pages = {}
        self.__root = None
    # Set page based on user's choice
    def __setitem__(self, key, value):
        self.__pages[key] = value
        if self.__root is None:
            self.__root = key
    # Method to loop through - main function in a way
    def read(self):
        print(self.__introduction)
        # print (self.__copyright)
        current_page = self.__pages[self.__root]
        while True:
            next_page = current_page.activate()
            current_page = self.__pages.get(next_page)
            if not current_page:
                playagain()
                break
            # time.sleep(2)
        print(self.__outro)

# Class for the "pages" of each "book"
class Page:
    # Each page has a description and choices
    def __init__(self, description, **choices):
        self.__description = description
        self.__choices = choices
    # "Activate" a page which is practically, printing the description and the choices available
    def activate(self):
        print(self.__description)
        targets = []
        for index, (key, value) in enumerate(self.__choices.items(), 1):
            print('{}. {}'.format(index, value))
            targets.append(key)
        return self.__get_choice(targets)
    # Used @staticmethod - behaves like a plain function but has link to this class
    @staticmethod
    def __get_choice(targets):
        while targets:
            try:
                return targets[int(input('>>> ')) - 1]
            except EOFError:
                return
            except (ValueError, IndexError):
                print('Please select an available option.')
# Function to ask user if they want to play again
def playagain():
    while True:
        try:
            replay = input("Do you want to play again? ").lower()
        except ValueError:
            print("Sorry, Invalid Entry")
            continue
        if replay in ("yes","y","true","t"):
            main()
            return()
        elif replay in ("no","n","false","f"):
            return
        else:
            print("Invalid entry, Please enter yes or no")
# Call main loop if script isn't being imported as a module
if __name__ == '__main__':
    main()
