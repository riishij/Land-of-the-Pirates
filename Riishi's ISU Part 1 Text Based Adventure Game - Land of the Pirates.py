#-------------------------------------------------------------------------------
# Name: Riishi Jeevakumar
# Program Name: Lost in the land of Pirates: A choose your story adventure game
#-------------------------------------------------------------------------------
#start of game
#outputs introduction to game
print"--------------------------------------------------------------------------------------------------"
print"Welcome to the Land of the Pirates!"
print" "
import time
time.sleep(3)
print"During the game, you will receive points by selecting the most suitable option!"
print" "
import time
time.sleep(3)
print"You must be alive by the end of the game. "
print " "
import time
time.sleep(3)
print"Once you complete the game, you will be ranked based on the total amount of points you've earned!"
print " "
import time
time.sleep(3)
print"Good luck and break a leg! ARGHHH!"
print"--------------------------------------------------------------------------------------------------"

x=1
while x==1:
    #variables set for user's name, total points and health
    name=raw_input("Enter Your Name")
    totalPoints=0
    health=100
    health=int(health)

    #location of user's starting point
    print "Location: Jeevan Industries "
    print "Year: 2100"
    print ""

    #Delay and display storyline
    import time
    time.sleep(4)
    print name +", you are a famous scientist who has invented the first ever Time Machine!"
    print" "

    maleFriend=raw_input("Enter the name of your male friend")

    #Delay and display storyline
    import time
    time.sleep(4)
    print "One day, you and " + maleFriend + " arrive at Jeevan Laboratories to see your wonderful invention."
    print""

    #Delay and display storyline
    import time
    time.sleep(4)
    print "However, when you try to test the time machine, it doesn't turn on. "
    print""

    #Delay and display storyline
    import time
    time.sleep(4)
    print name +", you decide to go inside the time machine to see what is wrong. "
    print""

    #Delay and display storyline
    import time
    time.sleep(4)
    print "Once you go inside, you hear the door behind you close! "
    print""

    #Delay and display storyline
    import time
    time.sleep(4)
    print"BEEP! BEEP! BEEP!"
    print""

    #Delay and display storyline
    import time
    time.sleep(4)
    print name + ", you turn around to see how the door got closed and once you do, you see your friend tampering with the time machine's controls. "
    print""

    #Delay and display storyline
    import time
    time.sleep(4)
    print "You ask " + maleFriend + " to help you, but suddenly he takes off his mask!"
    print""

    #Delay and display storyline
    import time
    time.sleep(4)
    print "You realize that he's your arch-nemesis, Kuta Raja, but's it's too late as the time machine activates!"
    print""

    #Delay and display storyline
    import time
    time.sleep(4)
    print"BOOM!"
    print""

    #Delay and display storyline
    import time
    time.sleep(2)
    print"You go unconscious..."

    #Delay and display storyline
    import time
    time.sleep(2)
    print"(Loses 20 health)"
    #user loses 20 health
    health= health-20

    #Delay and display storyline
    import time
    time.sleep(2)
    #Display remaining health
    print"Total health remaining= " + str(health)
    print""

    #Delay and display storyline
    import time
    time.sleep(3)
    #new user location
    print "Location: Isle of Blood"
    print "Year: 1679"

    #Delay and display storyline
    import time
    time.sleep(3)
    print "Splash! Woosh! Chrip! "
    print name + ", after going unconscious, you go back 421 years in time and wake up the Isle of Blood, a land full of pirates!"

    #Delay and display storyline
    import time
    time.sleep(4)
    print" "
    print "You cannot believe how hot it is as you decide to take off your lab coat."

    #Delay and display storyline
    import time
    time.sleep(4)
    print" "
    print"Once you do, you try to open the time machine, but it doesn't budge!"

    #Delay and display storyline
    import time
    time.sleep(4)
#FIRST PART (ASKING USER TO SELECT AN OPTION)
#Display options
    print name + ", what do you want to do?"
    print" "
    print"1. Take a break to find some food"
    print"2. Try to break open the time machine using a rock"
    print"3. Go into the town to get some help"
    #Asks user question, uses try and except to safeguard the program from crashing
    question1=raw_input("Enter which option you would like to pick(1, 2, or 3)")

    while x==1:
        try :

            question1 = int(question1)
            if question1 >=1 and question1 <=3:
                break
            else:
                print "Invalid input!"
            question1=raw_input("Enter which option you would like to pick(1, 2, or 3)")
        except:
            print "Invalid input!"
            question1=raw_input("Enter which option you would like to pick(1, 2, or 3)")

    #If user chooses option 1, display storyline
    if (question1==1):
        print" "
        print name + ", you go into the nearby forest."
        print" "

    #Delay and display storyline
        import time
        time.sleep(4)
        print "When you do, a lion comes out from a bush and jumps towards you!"
        print" "

    #Delay and display storyline
        import time
        time.sleep(4)
        print "You try to scream for help but no can hear you!"
        print"  "

    #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", you have nothing to protect yourself from the lion as you took off your lab coat before entering the forest!"
        print" "

    #Delay and display storyline
        import time
        time.sleep(4)
        print"ROAR! CRUNCH!"
        print"  "

    #Delay and display storyline
        import time
        time.sleep(2)
    #User is dead
        print name.upper() + ", YOU ARE DEAD!"
        print"  "
        time.sleep(2)
    #health variable set to 0
        print"(Loses 80 health)"
        health=0
        time.sleep(2)
    #Outputs health
        print"------------------------------------------------------------------------------------"
        print name + ", you have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"

        #Asks the user if they want to restart the game or end the game
        while x==1:
            endGameOption=raw_input("Enter R to restart the game or Enter E to Exit the game")
            if (endGameOption=="R" or endGameOption=="r"):
                print"You have restarted the game"
                print" "
                print"-------------------------------------------------------------------------------"
                break

            elif(endGameOption=="E" or endGameOption=="e"):
                print"Game Over"
                print str(name)+" ,you ended with "+str(health)+" health" +" and with "+str(totalPoints)+" points"
                print"Make better decisions next time!"
                x=0
                #game is done

            else:
                print "Invalid Input"


    if(question1==2):
        #If user chooses option 2, display storyline
        print" "
        print name + ", when you try to open the machine, it breaks as the rock damages it greatly."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "You then lie in the sand and find a mysterious letter."
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        totalPoints=int(totalPoints)
        totalPoints=totalPoints+1
        #Displays points
        print"-----------------------------------------------------------------------------------------"
        print name + ", you have "+str(totalPoints)+" point(s) right now"
        print"-----------------------------------------------------------------------------------------"
        print" "
        break



    if(question1==3):
        #If user chooses option 3, display storyline
        import time
        time.sleep(4)
        print name + ", you decide to walk to the nearby town, Cooksville."
        print" "

        import time
        time.sleep(4)
        print "Once you arrive at Cooksville, you try to enter the town, but the inlanders think that you are an enemy."
        print " "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "You then decide to run back to the time machine."
        print" "
#RANDOM EVENT NUMBER 1
#Random generator determines outcome of user
        print"While running, you suddenly see a flash of lighting strike a tree as it comes crashing down towards you!"
        from random import randint
        num = randint (1,10)
        if num !=1 or num!=3 or num!=5 or num!=7 or num!=9:
            print "However, you were able to successfully dodge the tree as you went back to the time machine where you found a letter in the sand."
            totalPoints=int(totalPoints)
            totalPoints=totalPoints+1
            #Displays points
            import time
            time.sleep(4)
            print"-----------------------------------------------------------------------------------------"
            print name + ", you have "+str(totalPoints)+" point(s) right now"
            print"-----------------------------------------------------------------------------------------"
            print" "
            break

        else:
            print name + ", you have no time to react as the tree crushes your body!"
            #Delay and display storyline
            import time
            time.sleep(2)
            #User is dead
            print name.upper() + ", YOU ARE DEAD!"
            print"  "
            time.sleep(2)
            #health variable set to 0
            health=0
            time.sleep(2)
            #Outputs health
            print"------------------------------------------------------------------------------------"
            print name + ", you have "+ str(health)+" health right now"
            print"------------------------------------------------------------------------------------"

            #Asks the user if they want to restart the game or end the game
            while x==1:
                endGameOption=raw_input("Enter R to restart the game or Enter E to Exit the game")
                if (endGameOption=="R" or endGameOption=="r"):
                    print"You have restarted the game"
                    print" "
                    print"-------------------------------------------------------------------------------"
                    break

                elif(endGameOption=="E" or endGameOption=="e"):
                    print"Game Over"
                    print str(name)+" ,you ended with "+str(health)+" health" +" and with "+str(totalPoints)+" points"
                    print"Make better decisions next time!"
                    x=0
                    #game is done

                else:
                    print"Invalid Input"




while x==1:
    #Delay and display storyline
    import time
    time.sleep(4)
    print name + ", after finding the letter, you decide to take a rest and open it tomorrow."
    print " "

    #Delay and display storyline
    import time
    time.sleep(4)
    print "The next day, you open the letter."
    print " "

    #Delay and display storyline
    import time
    time.sleep(4)
    print "Inside the letter, it contains a message that says 'If you want to return home, head north to Banterville for your next clue.' "
    print " "

    #Delay and display storyline
    import time
    time.sleep(4)
    print "However, you have no idea where Banterville is, but suddenly you see a small house."
    print " "

    #Delay and display storyline
    import time
    time.sleep(4)
    print name + ", you aren't sure what's in the house."
    print " "

    #Delay and display storyline
    import time
    time.sleep(4)
#SECOND PART (ASKING USER TO SELECT AN OPTION)
#Display options
    print "What do you want to do?"
    print" "
    print"1. Head to the house"
    print"2. Ignore the house"
    print"3. Take a break and head into the ocean"
    #Asks user question, uses try and except to safeguard the program from crashing
    question2=raw_input("Enter which option you would like to pick(1, 2, or 3)")

    while x==1:
        try :

            question2 = int(question2)
            if question2 >=1 and question2 <=3:
                break
            else:
                print "Invalid input!"
                question2=raw_input("Enter which option you would like to pick(1, 2, or 3)")
        except:
            print "Invalid input!"
            question2=raw_input("Enter which option you would like to pick(1, 2, or 3)")

    if (question2==1):
        #if user selects option 1, display storyline
        print" "
        print name + ", you head to the house."
        print" "

    #Delay and display storyline
        import time
        time.sleep(4)
        print "When you enter the house, you notice a old man on the ground."
        print" "


    #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", you try to not disturb him, but suddenly he wakes up!"
        print" "

     #Delay and display storyline
        import time
        time.sleep(4)
        print "When he sees you, he notices your injuries and heals you with a Pecha Berry, a berry that heals your health!"
        print" "
        time.sleep(4)
        health=health+10
     #Display health
        print"------------------------------------------------------------------------------------"
        print name + ", you have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"

    #Delay and display storyline
        import time
        time.sleep(4)
        print "He then introduces himself as a priest."
        print" "

    #variable created to allow user to enter the name of the priest
        priest=raw_input("Enter the name of the priest")

    #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", you show your letter to " + priest + "."
        print" "

    #Delay and display storyline
        import time
        time.sleep(4)
        print "Once the priest reads the letter, he tells you that you are the chosen one and hands you a map!"
        print" "

    #Delay and display storyline
        import time
        time.sleep(4)
        print "You then thank " + priest + " and begin your journey to Banterville."
        print" "
        break

        totalPoints=int(totalPoints)
        totalPoints=totalPoints+2
        #Displays points
        print"-----------------------------------------------------------------------------------------"
        print name + ", you have "+str(totalPoints)+" point(s) right now"
        print"-----------------------------------------------------------------------------------------"
        print" "

    if(question2==2):
        #if user selects option 2, display storyline
        print" "
        print name + ", you ignore the house and begin your journey."
        print" "

    #Delay and display storyline
        import time
        time.sleep(4)
        print "While you are walking, a inlander comes to you and hits you with a whip!"
        print""
        print"(Loses 20 health)"
        health= health-20
    #Display health
        print"------------------------------------------------------------------------------------"
        print name + ", you have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"

    #Delay and display storyline
        import time
        time.sleep(4)
        print "While the inlander hits you, you notice a map hanging from the inlander's pocket!"
        print" "

    #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", you then hear something coming from the house!"
        print" "

     #Delay and display storyline
        import time
        time.sleep(4)
        print "Priest: ARGHHHHH! WHO WOKE ME UP!"
        print" "

     #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", the inlander gets distracted from this as you are able to push him onto the ground and snatch the map!"
        print" "


    #Delay and display storyline
        import time
        time.sleep(4)
        print "The inlander then runs away."
        print" "

    #Delay and display storyline
        import time
        time.sleep(4)
        print "The man who was at the house comes towards you and introduces himself as a priest."
        print" "

        priest=raw_input("Enter the name of the priest")

    #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", you show your letter to " + priest + "."
        print" "

    #Delay and display storyline
        import time
        time.sleep(4)
        print "Once the priest reads the letter, he tells you that you are the chosen one!"
        print" "

    #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", you then thank " + priest + " and continue your journey to Banterville."
        print" "
        break

        totalPoints=int(totalPoints)
        totalPoints=totalPoints+1
        #Displays points
        print"-----------------------------------------------------------------------------------------"
        print name + ", you have "+str(totalPoints)+" point(s) right now"
        print"-----------------------------------------------------------------------------------------"
        print" "

    if(question2==3):
        #if user selects option 3, display storyline
        print" "
        print name + ", you go into the ocean to swim and relax."
        print" "

    #Delay and display storyline
        import time
        time.sleep(4)
        print "When you do, you notice something shiny and swim to it."
        print" "

    #Delay and display storyline
        import time
        time.sleep(4)
        print "Once you get close to the object, you notice a Great White Shark coming towards you!"
        print"  "

    #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", you try to swim away, but the shark crunches you into bits!"
        print" "

    #Delay and display storyline
        import time
        time.sleep(2)
        print"CRUNCH!"
        print"  "

    #Delay and display storyline
        import time
        time.sleep(2)
    #user has died
        print name.upper() + ", YOU ARE DEAD!"
        print"  "
    #health variable set to 0
        health=0
        time.sleep(2)
    #Display health
        print"------------------------------------------------------------------------------------"
        print name + ", you have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"

        #Asks the user if they want to restart the game or end the game
        while x==1:
            endGameOption=raw_input("Enter R to restart the game or Enter E to Exit the game")
            if (endGameOption=="R" or endGameOption=="r"):
                print"You have restarted the game"
                print" "
                print"-------------------------------------------------------------------------------"
                break

            elif(endGameOption=="E" or endGameOption=="e"):
                print"Game Over"
                print str(name)+" ,you ended with "+str(health)+" health" +" and with "+str(totalPoints)+" points"
                print"Make better decisions next time!"
                x=0
                #game is done

            else:
                print "Invalid Input"

while x==1:
    #Delay and display storyline
    import time
    time.sleep(4)
    print name + ", while walking to Banterville, you fall into a hole."

    #Delay and display storyline
    import time
    time.sleep(2)
    print "One of these options will randomly select your outcome."

    #Delay and display storyline
    import time
    time.sleep(4)
#RANDOM EVENT NUMBER 2
#Random generator determines user's outcome
#Display options
    print"1. You jump over the hole and proceed with your journey."
    print"2. You fall into the hole."
    print"3. The priest saves you and gives you a potion which revives your health."
    from random import randint
    random2 = randint (1,4)

    if (random2==1):
        #If random option 1 is selected , delay and display storyline
        import time
        time.sleep(4)
        print"The Pirate Gods are determining the outcome..."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print"The Pirate Gods decided that you will jump over the hole without sustaining any injuries and proceed with your journey! "
        print" "

        totalPoints=int(totalPoints)
        totalPoints=totalPoints+1
        #Displays points
        print"-----------------------------------------------------------------------------------------"
        print name + ", you have "+str(totalPoints)+" point(s) right now"
        print"-----------------------------------------------------------------------------------------"
        print" "
        break

    if (random2==2):
        #if random option 2 is selected , delay and display storyline
        import time
        time.sleep(4)
        print"The Pirate Gods are determining the outcome..."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print"The Pirate Gods decided that you will fall in the hole and injure your foot greatly! "
        print" "
        print"(Loses 20 health)"
        health= health-20
        #Display health
        print"------------------------------------------------------------------------------------"
        print name + ", you have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"

        #Delay and display storyline
        import time
        time.sleep(4)
        print"However, you are able to get out of the hole using all of your strength as you continue your journey."
        print" "
        break

    if (random2==3):
        #if random option 3 is selected, delay and display storyline
        import time
        time.sleep(4)
        print"The Pirate Gods are determining the outcome..."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print"The Pirate Gods decided that " + priest+ " saves you from falling in the hole and gives you a potion which revives your health!"
        print" "
        print" "
        print"(Gains 5 health)"
        health= health+5
        #display health
        print"------------------------------------------------------------------------------------"
        print name + ", you have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"

        #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", you thank " + priest + " and continue your journey."
        print" "

        totalPoints=int(totalPoints)
        totalPoints=totalPoints+1
        #Displays points
        print"-----------------------------------------------------------------------------------------"
        print name + ", you have "+str(totalPoints)+" point(s) right now"
        print"-----------------------------------------------------------------------------------------"
        print" "
        break

while x==1:
    #Delay and display storyline
    import time
    time.sleep(4)
    print name + ", once you get to Banterville, you ask the townsfolk about the next clue. "
    print " "

    #Delay and display storyline
    import time
    time.sleep(4)
    print "No one knows what you are talking about and you think of leaving the town. "
    print " "

    #Delay and display storyline
    import time
    time.sleep(4)
    print "However, a little girl comes to you as she tries to communicate with you.  "
    print " "

    #Delay and display storyline
    import time
    time.sleep(4)
    print name + ", you realize that she is deaf, but you notice something unusual with the girl.   "
    print " "

    #Delay and display storyline
    import time
    time.sleep(4)
#THIRD PART (ASKING USER TO SELECT AN OPTION)
#Display options
    print name + ", what do you want to do?"
    print" "
    print"1. Ignore the girl and leave the town"
    print"2. Run away"
    print"3. Show her the letter"
    #Asks user question, uses try and except to safeguard the program from crashing
    question3=raw_input("Enter which option you would like to pick(1, 2, or 3)")

    while x==1:
        try :

            question3 = int(question3)
            if question3 >=1 and question3 <=3:
                break
            else:
                print "Invalid input!"
                question3=raw_input("Enter which option you would like to pick(1, 2, or 3)")
        except:
            print "Invalid input!"
            question3=raw_input("Enter which option you would like to pick(1, 2, or 3)")

    if (question3==1):
        #If option 1 is selected, display storyline
        print" "
        print name + ", when you leave the town, you encounter a wildfire and burn to death! "
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        #user is dead
        print name.upper() + ", YOU ARE DEAD!"
        print"  "
        #health variable set to 0
        health=0
        time.sleep(2)
        #display health
        print"------------------------------------------------------------------------------------"
        print name + ", you have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"

        #Asks the user if they want to restart the game or end the game
        while x==1:
            endGameOption=raw_input("Enter R to restart the game or Enter E to Exit the game")
            if (endGameOption=="R" or endGameOption=="r"):
                print"You have restarted the game"
                print" "
                print"-------------------------------------------------------------------------------"
                break

            elif(endGameOption=="E" or endGameOption=="e"):
                print"Game Over"
                print str(name)+" ,you ended with "+str(health)+" health" +" and with "+str(totalPoints)+" points"
                print"Make better decisions next time!"
                x=0
                #game is done

            else:
                print "Invalid Input"

    if (question3==2):
        #If option 2 is selected, display storyline
        print" "
        print name + ", you decide to run away from Banterville after you notice something unusual about the girl."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print
        print "While you are running away, the girl gets mad at you and slams you on the ground using her mind control skills! "
        print" "
        #user loses health
        print"(Loses 30 health)"
        health= health-30
        #display health
        print"------------------------------------------------------------------------------------"
        print name + ", you have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"

        #Delay and display storyline
        import time
        time.sleep(4)
        print
        print name + ", you try to apologize, but the girl isn't having it as she kills you instantly by tossing you in the sky and smashing your head onto the ground! "
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        #user is dead
        print name.upper() + ", YOU ARE DEAD!"
        print"  "
        #health variable set to 0
        health=0
        time.sleep(4)
        #display health
        print"------------------------------------------------------------------------------------"
        print name + ", you have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"

        #Asks the user if they want to restart the game or end the game
        while x==1:
            endGameOption=raw_input("Enter R to restart the game or Enter E to Exit the game")
            if (endGameOption=="R" or endGameOption=="r"):
                print"You have restarted the game"
                print" "
                print"-------------------------------------------------------------------------------"
                break

            elif(endGameOption=="E" or endGameOption=="e"):
                print"Game Over"
                print str(name)+" ,you ended with "+str(health)+" health" +" and with "+str(totalPoints)+" points"
                print"Make better decisions next time!"
                x=0
                #game is done

            else:
                print "Invalid Input"

    if (question3==3):
        #if option 3 is selected, display storyline
        print" "
        print name + ", you decide to show the letter to the girl."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "After you show the letter, you communicate with her in sign language!"
        print " "

        #user enters name of girl for new variable
        girl=raw_input("Enter the name of the girl")

        #Delay and display storyline
        import time
        time.sleep(4)
        print "The girl introduces herself as " + girl + " and hands you the next clue."
        print " "

        totalPoints=int(totalPoints)
        totalPoints=totalPoints+1
        #Displays points
        print"-----------------------------------------------------------------------------------------"
        print name + ", you have "+str(totalPoints)+" point(s) right now"
        print"-----------------------------------------------------------------------------------------"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print girl + " then asks you if she can join you on your adventure. "
        print " "

        #Delay and display storyline
        import time
        time.sleep(4)
#FOURTH PART (ASKING USER TO SELECT AN OPTION)
#Display options
        print name + ", what do you want to do?"
        print" "
        print"1. Allow her to join you"
        print"2. Tell her to stay in the town"
        print"3. Tell her to run off and get help"
        #Asks user question, uses try and except to safeguard the program from crashing
        question4=raw_input("Enter which option you would like to pick(1, 2, or 3)")

        while x==1:
            try :
                question4 = int(question4)
                if question4 >=1 and question4 <=3:
                    break
                else:
                    print "Invalid input!"
                question4=raw_input("Enter which option you would like to pick(1, 2, or 3)")
            except:
                print "Invalid input!"
                question4=raw_input("Enter which option you would like to pick(1, 2, or 3)")


        if (question4==1):
            #if user selects option 1, display storyline
             print" "
             print name + ", you decide to let " + girl + " join you"
             print" "
             totalPoints=int(totalPoints)
             totalPoints=totalPoints+1
             #Displays points
             print"-----------------------------------------------------------------------------------------"
             print name + ", you have "+str(totalPoints)+" point(s) right now"
             print"-----------------------------------------------------------------------------------------"
             print" "
             break

        if (question4==2):
            #if user selects option 2, display storyline
            print" "
            print name + ", you tell " + girl + " to stay in town because she is pretty young."

            #Delay and display storyline
            import time
            time.sleep(4)
            print girl + " cries because she can't come with you and runs behind a bush. "
            print " "

            #Delay and display storyline
            import time
            time.sleep(4)
            print "You run to the bush to apologize to  " + girl + ",but suddenly, a vine from the ground grabs your foot and throws you onto the ground!"
            print " "

            print" "
            print"(Loses 10 health)"
            health= health-10
            #display health
            print"------------------------------------------------------------------------------------"
            print name + ", you have "+ str(health)+" health right now"
            print"------------------------------------------------------------------------------------"

            #Delay and display storyline
            import time
            time.sleep(4)
            print ""
            print name + ", after you get up from the ground, more vines grab you and suffocate you."


            #Delay and display storyline
            import time
            time.sleep(4)
            print ""
            print girl + " then comes out of the bush as her eyes are pitch black"
            print girl + " is using her mind control tactics to control the vines"

            #Delay and display storyline
            import time
            time.sleep(4)
            print ""
            print name + ", after you realize what's going on, you apologize to " + girl + " and tell her that she can come with you in sign language."


            #Delay and display storyline
            import time
            time.sleep(4)
            print ""
            print girl + "'s eyes return to normal as the vines disappear. "
            print girl + " then tells you that she is sorry for what she did. "

            #Delay and display storyline
            import time
            time.sleep(4)
            print ""
            print name + ", you forgive " + girl + " as you continue your journey with your new accomplice."
            print ""
            totalPoints=int(totalPoints)
            totalPoints=totalPoints+2
            #Displays points
            print"-----------------------------------------------------------------------------------------"
            print name + ", you have "+str(totalPoints)+" point(s) right now"
            print"-----------------------------------------------------------------------------------------"
            print" "
            break

    if (question4==3):
            #if option 3 is selected, display storyline
            print" "
            print name + ", you tell " + girl + " to run off and get help."
            print" "

            #Delay and display storyline
            import time
            time.sleep(4)
            print ""
            print "After " + girl + " runs off, you decide to ditch her and continue your journey."

            #Delay and display storyline
            import time
            time.sleep(4)
            print ""
            print "However, the " + girl + " sees you and uses her mind control tactics to block the gates of the town."

            #Delay and display storyline
            import time
            time.sleep(2)
            print ""
            print "BOOM!"
            print name.upper() + ", YOU ARE TRAPPED!"

            #Delay and display storyline
            import time
            time.sleep(3)
            print ""
            print "You try to apologize to " + girl + ",but she doesn't care as you lied to her!"

            #Delay and display storyline
            import time
            time.sleep(4)
            print ""
            print girl + "'s eyes go pitch black as she uses her mind control tactics once again to throw a huge rock at you!"


            #Delay and display storyline
            import time
            time.sleep(2)
            #user is dead
            print name.upper() + ", YOU ARE DEAD!"
            print"  "
            #health variable set to 0
            health=0
            time.sleep(2)
            #display health
            print"------------------------------------------------------------------------------------"
            print name + ", you have "+ str(health)+" health right now"
            print"------------------------------------------------------------------------------------"

            #Asks the user if they want to restart the game or end the game
            while x==1:
                endGameOption=raw_input("Enter R to restart the game or Enter E to Exit the game")
            if (endGameOption=="R" or endGameOption=="r"):
                print"You have restarted the game"
                print" "
                print"-------------------------------------------------------------------------------"
                break

            elif(endGameOption=="E" or endGameOption=="e"):
                print"Game Over"
                print str(name)+" ,you ended with "+str(health)+" health" +" and with "+str(totalPoints)+" points"
                print"Make better decisions next time!"
                x=0
                #game is done

            else:
                print "Invalid Input"

while x==1:
    #Delay and display storyline
    import time
    time.sleep(4)
    print name + ", after you allow " + girl + " to join you, you head onto the Picanugan Forest. "
    print " "

    #Delay and display storyline
    import time
    time.sleep(4)
    print "As you come to the edge of the forest, there is a fork in the pathway. "
    print " "

    #Delay and display storyline
    import time
    time.sleep(4)
    print name + ", to the right of the pathway, you see a strange looking house and to the left of the forest, you see the pathway disappear over a tall hill. "
    print " "

    #Delay and display storyline
    import time
    time.sleep(4)
    print "You aren't sure which pathway to take."
    print " "

    #Delay and display storyline
    import time
    time.sleep(4)
#FIFTH PART (ASKING USER TO SELECT AN OPTION)
#Display options
    print name + ", what do you want to do?"
    print" "
    print"1. Stay in the forest and camp out for the night"
    print"2. Head onto the left pathway"
    print"3. Head onto the right pathway"
    #Asks user question, uses try and except to safeguard the program from crashing
    question5=raw_input("Enter which option you would like to pick(1, 2, or 3)")

    while x==1:
        try :
            question5 = int(question5)
            if question5 >=1 and question5 <=3:
                break
            else:
                print "Invalid input!"
            question5=raw_input("Enter which option you would like to pick(1, 2, or 3)")
        except:
            print "Invalid input!"
            question5=raw_input("Enter which option you would like to pick(1, 2, or 3)")

    if (question5==1):
        #if user selects option 1, display storyline
        print" "
        print name + ", you and " + girl + " decide to stay in the forest and camp out for the night."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "The next day, when you wake up, you noticed that " + girl + " has disappeared!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "However, you finally notice her on the fork of the pathway as she is in combat with someone."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "When you get closer, you couldn't believe your eyes!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "IT WAS YOUR ARCH-NEMESIS, KUTA RAJA!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "Once you realize Kuta Raja is here, you try to join the fight."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "However, Kuta Raja is able to kill " + girl + " in a couple of seconds and soon he notices you!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", you do not have anything to protect yourself with as he fires a bullet at you!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        print "BOOM!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        print "The bullet goes through your head and pierces your skull!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        #user is dead
        print name.upper() + ", YOU ARE DEAD!"
        print"  "
        #health variable set to 0
        health=0
        time.sleep(2)
        #display health
        print"------------------------------------------------------------------------------------"
        print name + ", you have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"

        #Asks the user if they want to restart the game or end the game
        while x==1:
            endGameOption=raw_input("Enter R to restart the game or Enter E to Exit the game")
            if (endGameOption=="R" or endGameOption=="r"):
                print"You have restarted the game"
                print" "
                print"-------------------------------------------------------------------------------"
                break

            elif(endGameOption=="E" or endGameOption=="e"):
                print"Game Over"
                print str(name)+" ,you ended with "+str(health)+" health" +" and with "+str(totalPoints)+" points"
                print"Make better decisions next time!"
                x=0
                #game is done

            else:
                print "Invalid Input"

    if (question5==2):
        #if user selects option 2, display storyline
        print" "
        print name + ", you and " + girl + " decide to go onto the left pathway."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "While walking to the strange house, you hear dreadfull sounds."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "BOO! SQUEAK! CAW! AH!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", once you arrive at the house, " + girl + " tells you that she wants to go inside first."
        print" "


        #Delay and display storyline
        import time
        time.sleep(4)
        print "You let " + girl + " inside the home, but after 10 minutes, she doesn't come outside!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", you get scared so you decide to go inside the house."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "The first thing you see is " + girl + "'s body on the ground drenched by blood!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", you become traumatized by what you saw and suddenly, someone hits you from behind!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "You check to see who hit you and you couldn't believe your eyes!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "IT WAS YOUR ARCH-NEMESIS, KUTA RAJA!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "You get up and ask Kuta Raja what he is doing here."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "Kuta Raja: I'm finishing you right here and now! ARGHH!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        print "BOOM!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        print name + ", a bullet goes through your head and pierces your skull!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        #user is dead
        print name.upper() + ", YOU ARE DEAD!"
        print"  "
        #health variable set to 0
        health=0
        time.sleep(2)
        #display health
        print"------------------------------------------------------------------------------------"
        print name + ", you have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"

        #Asks the user if they want to restart the game or end the game
        while x==1:
            endGameOption=raw_input("Enter R to restart the game or Enter E to Exit the game")
            if (endGameOption=="R" or endGameOption=="r"):
                print"You have restarted the game"
                print" "
                print"-------------------------------------------------------------------------------"
                break

            elif(endGameOption=="E" or endGameOption=="e"):
                print"Game Over"
                print str(name)+" ,you ended with "+str(health)+" health" +" and with "+str(totalPoints)+" points"
                print"Make better decisions next time!"
                x=0
                #game is done

            else:
                print "Invalid Input"

    if (question5==3):
        #if user selects option 3, display storyline
        print" "
        print name + ", you and " + girl + " decide to go onto the right pathway."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "After going over the hill, you notice " + priest + " standing at the bottom of the hill."
        print " "

        #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", he comes up to you and gives you one of three things:"
        print " "
        import time
        time.sleep(4)
#RANDOM EVENT NUMBER 3
#Random generator determines user's outcome
#Display options
        print"1. A suit of armor"
        print"2. A Mersa Berry"
        print"3. A guide dog"
        #Asks user question, uses try and except to safeguard the program from crashing
        from random import randint
        random3 = randint (1,4)

    if (random3==1):
        #If random option 1 is selected , delay and display storyline
        import time
        time.sleep(4)
        print"The Pirate Gods are determining the outcome..."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print"The Pirate Gods decided that you will receive a suit of armor! "
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        print" "
        print"(Gains 50 health)"
        health= health+50
        #display health
        print"------------------------------------------------------------------------------------"
        print name + ", you have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"
        print""

        #Delay and display storyline
        import time
        time.sleep(2)
        print name + ",in addition, " + priest + " gives you the next clue!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        totalPoints=int(totalPoints)
        totalPoints=totalPoints+3
        #Displays points
        print"-----------------------------------------------------------------------------------------"
        print name + ", you have "+str(totalPoints)+" point(s) right now"
        print"-----------------------------------------------------------------------------------------"
        print" "

        #Delay and display storyline
        import time
        time.sleep(3)
        print "You thank " + priest + " for his help and continue your journey."
        print" "
        break

    if (random3==2):
        #If random option 2 is selected , delay and display storyline
        import time
        time.sleep(4)
        print"The Pirate Gods are determining the outcome..."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print"The Pirate Gods decided that you will receive a Mersa Berry! "
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        print name + ", however, " + priest + " accidentally gives you the wrong berry as you get really sick!"
        print" "

        print"(Loses 10 health)"
        health= health-10
        #display health
        print"------------------------------------------------------------------------------------"
        print"You have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"

        #Delay and display storyline
        import time
        time.sleep(2)
        print priest + " apologizes for giving you the wrong berry and hands you the next clue!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        print name + ", you forgive him and thank him for the clue as you continue your journey."
        print" "

        totalPoints=int(totalPoints)
        totalPoints=totalPoints+1
        #Displays points
        print"-----------------------------------------------------------------------------------------"
        print name + ", you have "+str(totalPoints)+" point(s) right now"
        print"-----------------------------------------------------------------------------------------"
        print" "
        break

    if (random3==3):
        #If random option 3 is selected , delay and display storyline
        import time
        time.sleep(4)
        print"The Pirate Gods are determining the outcome..."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print"The Pirate Gods decided that " + priest + " gives you a guide dog!"
        print" "

        #new variable created for user to enter name for dog
        dog=raw_input("Enter the name of the dog")

        #Delay and display storyline
        import time
        time.sleep(2)
        print name + ", you ask " + priest + " why you received a dog."
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        print priest + " tells you that a dog is a man's best friend and hands you the next clue."
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        print "Afterwards, " + priest + " disappears into thin air!"
        print" "

        totalPoints=int(totalPoints)
        totalPoints=totalPoints+1
        #Displays points
        print"-----------------------------------------------------------------------------------------"
        print name + ", you have "+str(totalPoints)+" point(s) right now"
        print"-----------------------------------------------------------------------------------------"
        print" "
        break

while x==1:
    #Delay and display storyline
    import time
    time.sleep(4)
    print name + ", after exiting the Picanugan Forest, you head to Pirate Cove."
    print" "

    #Delay and display storyline
    import time
    time.sleep(4)
    print "Once you arrive at Pirate Cove, you encounter a group of Pirates!"
    print" "

    #Delay and display storyline
    import time
    time.sleep(4)
    print "When the pirates try to attack you, you hear something that is very familar."
    print" "

    #Delay and display storyline
    import time
    time.sleep(4)
    print "STOP!"
    print" "

    #Delay and display storyline
    import time
    time.sleep(4)
    print "The pirates stop their attack and you see your arch-nemesis Kuta Raja at the top of the cove!"
    print" "

    #Delay and display storyline
    import time
    time.sleep(4)
    print name + ", you then have a long conversation with Kuta Raja..."
    print" "

    #Delay and display storyline
    #Dialogue between you and Kuta Raja
    import time
    time.sleep(3)
    print "Kuta Raja: Well, well, well. What do we have here?"
    #Delay and display storyline
    import time
    time.sleep(3)
    print name + ": You bastard! Why are you here!"
    #Delay and display storyline
    import time
    time.sleep(3)
    print "Kuta Raja: Bro, such harsh words."
    #Delay and display storyline
    import time
    time.sleep(3)
    print name + ": Stop calling me bro!"
    #Delay and display storyline
    import time
    time.sleep(3)
    print "Kuta Raja: Ok bro."

    #based on the random option user got in random event #3, user will get a different storyline unique to that option
    if (random3==1 or random3==2):
        #Delay and display storyline
        import time
        time.sleep(3)
        print "While you are talking, you notice " + girl + " sneak in Pirate Cove."
        print" "
        break

    if (random3==3):
        #Delay and display storyline
        import time
        time.sleep(3)
        print "While you are talking, you notice " + girl + " and " + dog + " sneak in Pirate Cove."
        print" "
        break

while x==1:
    #Delay and display storyline
    import time
    time.sleep(3)
    print name + ", you then continue your conversation with Kuta Raja..."
    print" "
    #Delay and display storyline
    import time
    time.sleep(3)
    print name + ": What the heck man!"
    #Delay and display storyline
    import time
    time.sleep(3)
    print "Kuta Raja: I'm only here for one reason...and you know why!"
    #Delay and display storyline
    import time
    time.sleep(3)
    print name + ": Huh, what."
    #Delay and display storyline
    import time
    time.sleep(3)
    print "Kuta Raja: Ugh, I came here to finish you off once in for all!"
    #Delay and display storyline
    import time
    time.sleep(3)
    print name + ": But why did you transport me here."
    #Delay and display storyline
    import time
    time.sleep(3)
    print "Kuta Raja: I want to kill you here so that I will be known as the creator of the time machine in 2100!"
    #Delay and display storyline
    import time
    time.sleep(3)
    print name + ": Shut up! Tell me how I can get out of here!"
    #Delay and display storyline
    import time
    time.sleep(3)
    print "Kuta Raja: There's only one way how you can get out of here, but I have it in my hand right now!"
    #Delay and display storyline
    import time
    time.sleep(3)
    print "(Shows golden key to " + name + ")"
    #Delay and display storyline
    import time
    time.sleep(3)
    print name + ": Give it to me!"
    #Delay and display storyline
    import time
    time.sleep(3)
    print "Kuta Raja: Are you ok? You took my idea of creating the time machine and now I will annihilate you with my pirate army!"

    #Delay and display storyline
    import time
    time.sleep(3)
    print name + ", after the conversation..."
    print" "

    #Delay and display storyline
    import time
    time.sleep(3)
    print "You realize that this is your only chance to get back to the year 2100."
    print" "

    #Delay and display storyline
    import time
    time.sleep(3)
    print "However, you are very nervous as you could lose your life right now."
    print" "
    #Delay and display storyline
    import time
    time.sleep(3)
#SIXTH PART (ASKING USER TO SELECT AN OPTION)
#Display options
    print name + ", what do you want to do?"
    print" "
    print"1. Run away"
    print"2. Use your brains to find a strategic way to get the key"
    print"3. Fight the pirates head on"
    #Asks user question, uses try and except to safeguard the program from crashing
    question6=raw_input("Enter which option you would like to pick(1, 2, or 3)")

    while x==1:
        try :

            question6 = int(question6)
            if question6 >=1 and question6 <=3:
                break
            else:
                print "Invalid input!"
            question6=raw_input("Enter which option you would like to pick(1, 2, or 3)")
        except:
            print "Invalid input!"
            question6=raw_input("Enter which option you would like to pick(1, 2, or 3)")

    if (question6==1):
        #if user selects option 1, display storyline
        print""
        print name + ", you decide to run away from Pirate Cove!"
        print""

        #Delay and display storyline
        import time
        time.sleep(4)
        print "Kuta Raja: HA HA HA! SUCH A COWARD!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "Kuta Raja then fires a bullet at you!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        print name + ", the bullet goes through your head and pierces your skull"
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        #user is dead
        print name.upper() + ", YOU ARE DEAD!"
        print"  "
        #health variable set to 0
        health=0
        time.sleep(2)
        #display health
        print"------------------------------------------------------------------------------------"
        print name + ", you have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"

        #Asks the user if they want to restart the game or end the game
        while x==1:
            endGameOption=raw_input("Enter R to restart the game or Enter E to Exit the game")
            if (endGameOption=="R" or endGameOption=="r"):
                print"You have restarted the game"
                print" "
                print"-------------------------------------------------------------------------------"
                break

            elif(endGameOption=="E" or endGameOption=="e"):
                print"Game Over"
                print str(name)+" ,you ended with "+str(health)+" health" +" and with "+str(totalPoints)+" points"
                print"Make better decisions next time!"
                x=0
                #game is done

            else:
                print "Invalid Input"

    if (question6==2):
        #if option 2 is selected, display storyline
        print""
        print name + ", you decide to use your brains to find a strategic way to get the key."
        print""

        #Delay and display storyline
        import time
        time.sleep(4)
        print "However, it's literally impossible for you to get the key as Kuta Raja is at the top of the cove!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", while you are thinking, the pirates charge and trample you with ease!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(2)
        #user is dead
        print name.upper() + ", YOU ARE DEAD!"
        print"  "
        #health variable is set to 0
        health=0
        time.sleep(2)
        #display health
        print"------------------------------------------------------------------------------------"
        print name + ", you have "+ str(health)+" health right now"
        print"------------------------------------------------------------------------------------"

        #Asks the user if they want to restart the game or end the game
        while x==1:
            endGameOption=raw_input("Enter R to restart the game or Enter E to Exit the game")
            if (endGameOption=="R" or endGameOption=="r"):
                print"You have restarted the game"
                print" "
                print"-------------------------------------------------------------------------------"
                break


            elif(endGameOption=="E" or endGameOption=="e"):
                print"Game Over"

                print str(name)+" ,you ended with "+str(health)+" health" +" and with "+str(totalPoints)+" points"
                print"Make better decisions next time!"
                x=0
                #game is done

            else:
                print "Invalid Input"

    if (question6==3):
        #if option 3 is selected, display storyline
        print""
        print name + ", you decide to fight the pirates head on!"
        print""

        #Delay and display storyline
        import time
        time.sleep(4)
        print "You pull out a sword and a gun that you stole from Banterville and injure each pirate member one by one."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "Finally, all that is remaining is you and Kuta Raja!"
        print" "

        import time
        time.sleep(4)
        print "Kuta Raja: How in the world did you do that!"
        import time
        time.sleep(4)
        print name + ": Shut up coward! Let's fight!"

        #Delay and display storyline
        import time
        time.sleep(4)
        print "You and Kuta Raja fight for a very long time..."
        print" "

        #Delay and display storyline
        import time
        time.sleep(3)
        print "Suddenly, you are on the ground and Kuta Raja is about to shoot his gun towards you!"
        print" "
        import time
        time.sleep(3)
        print "Kuta Raja: THIS IS THE END OF YOU! ARGHHH!"

        #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", you close your eyes knowing that fact that you are going to die..."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "The trigger is pulled!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "CRACK! BOOM!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", you think you are dead, but once you open your eyes, you see Kuta Raja wailing on the ground holding his arm."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "You are shocked by the outcome, but you notice your accomplices and a big bulky man at the front of Pirate Cove."
        print" "

        import time
        time.sleep(4)
        print "Captain Cook: HA HA HA. It's about time I got revenge!"

        #Delay and display storyline
        import time
        time.sleep(3)
        print name + ", you take the golden key from Kuta Raja's pocket and kill him afterwards using your gun!"
        print" "
        totalPoints=int(totalPoints)
        totalPoints=totalPoints+2
        #Displays points
        print"-----------------------------------------------------------------------------------------"
        print name + ", you have "+str(totalPoints)+" point(s) right now"
        print"-----------------------------------------------------------------------------------------"
        print" "
        break

while x==1:
    #based on the random option user got in random event #3, user will get a different storyline unique to that option
    if (random3==1 or random3==2):
        #Delay and display storyline
        import time
        time.sleep(4)
        print "Captain Cook comes towards you and introduces himself as the leader of the pirates."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "He tells you that Kuta Raja caged him inside Pirate Cove, but thanks to " + girl + ", he was able to be set free!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "Captain Cook then transports both of you back to Cooksville due to your heroic efforts..."
        print" "
        totalPoints=int(totalPoints)
        totalPoints=totalPoints+5
        #Displays points
        print"-----------------------------------------------------------------------------------------"
        print name + ", you have "+str(totalPoints)+" point(s) right now"
        print"-----------------------------------------------------------------------------------------"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", once you get back to Cooksville, you thank " + girl + " for her services as you hug her tightly."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "Afterwards, " + girl + " goes into " + priest + "'s home and once " + priest + " comes out of his home, you also thank him for his help."
        print" "
        break

    if (random3==3):
        #Delay and display storyline
        import time
        time.sleep(4)
        print "Captain Cook comes towards you and introduces himself as the leader of the pirates."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "He tells you that Kuta Raja caged him inside Pirate Cove, but thanks to " + girl + " and " + dog + ", he was able to be set free!"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "Captain Cook then transports all of you back to Cooksville due to your heroic efforts..."
        print" "
        totalPoints=int(totalPoints)
        totalPoints=totalPoints+5
        #Displays points
        print"-----------------------------------------------------------------------------------------"
        print name + ", you have "+str(totalPoints)+" point(s) right now"
        print"-----------------------------------------------------------------------------------------"
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print name + ", once you get back to Cooksville, you thank " + girl + " and " + dog + " for their services as you hug them tightly."
        print" "

        #Delay and display storyline
        import time
        time.sleep(4)
        print "Afterwards, " + girl + " and " + dog + " both go into " + priest + "'s home and once " + priest + " comes out of his home, you thank him for his help."
        print" "
        break

while x==1:
        #Delay and display storyline
        import time
        time.sleep(3)
        print "However, for some reason, the atmosphere starts to get really hot and you notice a meteor heading towards Cooksville."
        print" "

        import time
        time.sleep(3)
#SEVENTH PART (ASKING USERS TO SELECT AN OPTION)
#Display options
        print name + ", what do you want to do?"
        print" "
        print"1. Head inside the time machine"
        print"2. Face the meteor head on"
        print"3. Create a plan to stop the meteor"
        #Asks user question, uses try and except to safeguard the program from crashing
        question7=raw_input("Enter which option you would like to pick(1, 2, or 3)")

        while x==1:
            try :

                question7 = int(question7)
                if question7 >=1 and question7 <=3:
                    break
                else:
                    print "Invalid input!"
                    question7=raw_input("Enter which option you would like to pick(1, 2, or 3)")
            except:
                print "Invalid input!"
                question7=raw_input("Enter which option you would like to pick(1, 2, or 3)")

        if (question7==1):
            #if option 1 is selected, display storyline
            print""
            print name + ", you decide to head inside the time machine because you don't want to die."
            print""

            #Delay and display storyline
            import time
            time.sleep(4)
            print name + ", you then go ahead 421 years to return to the present..."
            print" "
            #user returns to original location
            print "Location: Jeevan Industries "
            print "Year: 2100"
            totalPoints=int(totalPoints)
            totalPoints=totalPoints+2
            #Displays points
            print"-----------------------------------------------------------------------------------------"
            print"You have "+str(totalPoints)+" point(s) right now"
            print"-----------------------------------------------------------------------------------------"
            print" "
            break

        if (question7==2):
            #if option 2 is selected, display storyline
            print ""
            print name + ", you decide to face the meteor head on!"
            print ""

            #Delay and display storyline
            import time
            time.sleep(4)
            print name + ", you then levitate in the sky and suddenly, you are able to redirect the meteor away from Cooksville!"
            print" "
            totalPoints=int(totalPoints)
            totalPoints=totalPoints+5
            #Displays points
            print"-----------------------------------------------------------------------------------------"
            print name + ", you have "+str(totalPoints)+" point(s) right now"
            print"-----------------------------------------------------------------------------------------"
            print" "

            #Delay and display storyline
            import time
            time.sleep(4)
            print priest + ": THE CHOSEN ONE HAS SAVED US! PRAISE " + name + "!"
            print" "

            #Delay and display storyline
            import time
            time.sleep(4)
            print name  + ": How did I do that just now!"
            print" "

            #Delay and display storyline
            import time
            time.sleep(4)
            print priest + ": You are the chosen one!"
            print" "

            #Delay and display storyline
            import time
            time.sleep(4)
            print name + " Um, thank you! I appreciate the opportunity to experience this, but now I must return home!"
            print" "

            #Delay and display storyline
            import time
            time.sleep(4)
            print priest + ": Bye! Come again soon THE CHOSEN ONE!"
            print" "

            #Delay and display storyline
            import time
            time.sleep(4)
            print name + ", you then go inside the time machine and go ahead 421 years to return to the present..."
            print" "
            #user returns to original location
            print "Location: Jeevan Industries "
            print "Year: 2100"
            totalPoints=int(totalPoints)
            totalPoints=totalPoints+2
            #Displays points
            print"-----------------------------------------------------------------------------------------"
            print name + ", you have "+str(totalPoints)+" point(s) right now"
            print"-----------------------------------------------------------------------------------------"
            print" "
            break

        if (question7==3):
        #if option 3 is selected, display storyline
            print""
            print name + ", you decide to make a plan to stop the meteor."
            print""

            #Delay and display storyline
            import time
            time.sleep(3)
            print "However, it's too late as the meteor hits Cooksville within seconds!"
            print" "

            #Delay and display storyline
            import time
            time.sleep(2)
            #user is dead
            print name.upper() + ", YOU ARE DEAD"
            print"  "
            #health variable set to 0
            health=0
            time.sleep(2)
            #display health
            print"------------------------------------------------------------------------------------"
            print name + ", you have "+ str(health)+" health right now"
            print"------------------------------------------------------------------------------------"

            #Asks the user if they want to restart the game or end the game
            while x==1:
                endGameOption=raw_input("Enter R to restart the game or Enter E to Exit the game")
            if (endGameOption=="R" or endGameOption=="r"):
                print"You have restarted the game"
                print" "
                print"-------------------------------------------------------------------------------"
                break

            elif(endGameOption=="E" or endGameOption=="e"):
                print"Game Over"
                print str(name)+" ,you ended with "+str(health)+" health" +" and with "+str(totalPoints)+" points"
                print"Make better decisions next time!"
                x=0
                #game is done

            else:
                print "Invalid Input"
            endGameOption=raw_input("Enter R to restart the game or Enter E to Exit the game")

while x==1:
    #delay and display conclusion of game
    import time
    time.sleep(4)
    print" CONGRATULATIONS, " + name + "! YOU HAVE FINISHED THE GAME! WOO HOO!"
    print"  "
    time.sleep(4)
    #display total health and points
    print"--------------------------------------------------------------------------------------"
    print"You ended the game with "+ str(health)+" health and with " + str(totalPoints)+ " points!"

    #based on how many points user received in the game, the user will receive a unique message
    if totalPoints >=18:
        print name.upper() + ", YOU ARE A MIGHTY PIRATE! ARGHHHH!"

    elif totalPoints >=12 and totalPoints <=17:
        print name.upper() + ", YOU ARE A SHIP COOK! ARGHHHH!"

    else:
        print name.upper() + ", YOU ARE A PEASANT WATER BOY! ARGHHH!"

    print"--------------------------------------------------------------------------------------"

    #Asks the user if they want to restart the game or end the game
    while x==1:
        endGameOption=raw_input("Enter R to restart the game or Enter E to Exit the game")
        if (endGameOption=="R" or endGameOption=="r"):
            print"You have restarted the game"
            print" "
            print"-------------------------------------------------------------------------------"
            break

        elif(endGameOption=="E" or endGameOption=="e"):
            print "Thanks for playing!"
            print "See you soon!"
            x=0
            #game is done

        else:
            print "Invalid Input"
























































































