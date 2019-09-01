from colorama import init, Fore, Back, Style
init(convert=True)

def main():

        print(Fore.LIGHTMAGENTA_EX + "~ PLEASE NOTE THIS GAME IS A WORK IN PROGRESS ~" + (Style.RESET_ALL)) 
        print("Please enter your first name" + Fore.LIGHTGREEN_EX) 
        firstname = input()
        print((Style.RESET_ALL) + "Please enter you last name" + Fore.LIGHTGREEN_EX)
        lastname = input()
        
        print(Fore.LIGHTMAGENTA_EX + "~ YOU MUST ANSWER THESE QUESTIONS IN LOWER CASE ~" + (Style.RESET_ALL))
        print("Why hello " + firstname + " today is day one of your life as a human, you have to get some food from the shopping center ")
        print("so you need to go to the shopping center but what way do you want to do it:" + Fore.LIGHTGREEN_EX + " (A)" + (Style.RESET_ALL) + " car," + Fore.LIGHTGREEN_EX + " (B) " + (Style.RESET_ALL) + "bike or" + Fore.LIGHTGREEN_EX + " (C)" + (Style.RESET_ALL) + " walk" + Fore.LIGHTGREEN_EX)
        
        answer1 = input()
        if answer1 == "a": print((Style.RESET_ALL) + "so you got in your car, turned on the engine buckled your seatbelt and then realised you could'nt drive..." + " FAIL PLEASE TYPE RESTART" + Fore.RED)
        if answer1 == "b": print((Style.RESET_ALL) + "you go outside hop onto your bike and break you leg becasue it was a stupid idea to try to get onto your bike by hopping..." + " FAIL PLEASE TYPE RESTART" + Fore.RED)
        if answer1 == "c": print((Style.RESET_ALL) + "so you go outside and do the one thing that you know how to do... walk, you arive at the shopping center five minutes later" + " so your there but what shop should you go to either" + Fore.LIGHTGREEN_EX +" (A)" + (Style.RESET_ALL) + " Toys R Us or" + Fore.LIGHTGREEN_EX + " (B)" + (Style.RESET_ALL) + " Target" + Fore.LIGHTGREEN_EX)
        else: print((Style.RESET_ALL) + "FAIL PLEASE TYPE RESTART " + Fore.RED)
        
        answer2 = input()
        if answer2 == "a": print((Style.RESET_ALL) + "ha good one... wait you really thought Toys R Us still existed... ok then... " + " FAIL PLEASE TYPE RESTART" + Fore.RED)
        if answer2 == "b": print((Style.RESET_ALL) + "you walk inside and nearly get shot by an archer and wonder what you should buy," + Fore.LIGHTGREEN_EX + " (A)" + (Style.RESET_ALL) + " Pringles," + Fore.LIGHTGREEN_EX + " (B)"  + (Style.RESET_ALL) + " Orange Juice or" + Fore.LIGHTGREEN_EX +" (C)"  + (Style.RESET_ALL) + " some good ol Coffee Beans " + Fore.LIGHTGREEN_EX)
        else: print((Style.RESET_ALL) + "FAIL PLEASE TYPE RESTART " + Fore.RED)
        if answer2 == "restart":
            main()
        
        answer3 = input()
        if answer3 == "a": print((Style.RESET_ALL) + "half way to the cash register you realise you hand cant even fit in a pringle can..." + " FAIL PLEASE TYPE RESTART" + Fore.RED)
        if answer3 == "b": print((Style.RESET_ALL) + "nah its to good to be true..." + " FAIL PLEASE TYPE RESTART" + Fore.RED)
        if answer3 == "c": print((Style.RESET_ALL) + "duh its the name of the game why werent you supposed to get this" + " you walk over to the cashier with your coffee beans in hand " + " Cashier: so whats the name " + " You: the names" + " " + firstname +" "+ firstname +" "+ lastname + " Cashier: uhhh that will be $4.50 " +  "you leave you realise do you want to go home or not:" + Fore.LIGHTGREEN_EX + " (A)" + (Style.RESET_ALL) + " go home or" + Fore.LIGHTGREEN_EX + " (B)" + (Style.RESET_ALL) + " dont go home" + Fore.LIGHTGREEN_EX)
        else: print((Style.RESET_ALL) + "FAIL PLEASE TYPE RESTART " + Fore.RED)
        if answer3 == "restart":
            main()
        
        answer4 = input()
        if answer4 == "a": print((Style.RESET_ALL) + "easy enough... you sleep happy that night" + Fore.CYAN +" DAY TWO" + (Style.RESET_ALL) + " You wake up to remember its your first day of work at McDonalds what do you wear" + Fore.LIGHTGREEN_EX + " (A)" + (Style.RESET_ALL) + " a tuxedo," + Fore.LIGHTGREEN_EX + " (B)" + (Style.RESET_ALL) + " your Ronald McDonald suit or"  + Fore.LIGHTGREEN_EX + " (C)" + (Style.RESET_ALL) + " nothing" + Fore.LIGHTGREEN_EX)
        if answer4 == "b": print((Style.RESET_ALL) + "ummm i dont know what to say except you are really dumb..." + " FAIL PLEASE TYPE RESTART" + Fore.RED)
        else: print((Style.RESET_ALL) + "FAIL PLEASE TYPE RESTART " + Fore.RED)
        if answer4 == "restart":
            main()
        
        answer5 = input()
        if answer5 == "a": print((Style.RESET_ALL) + "you put your closest thing to a tuxedo on and that is your penguin suit... you arive at work and immediately get told to leave" + " FAIL PLEASE TYPE RESTART" + Fore.RED)
        if answer5 == "b": print((Style.RESET_ALL) + "its sad but you have to wear it... you arrive at work ten minutes later because of you fricken suit " + " your there but what do you do" + Fore.LIGHTGREEN_EX + " (A)" + (Style.RESET_ALL) + " go over and talk to the children or" + Fore.LIGHTGREEN_EX + " (B)" + (Style.RESET_ALL) + " just go talk to your friend" + Fore.LIGHTGREEN_EX)
        if answer5 == "c": print((Style.RESET_ALL) + "well thats not gonna work is it you idiot..." + " FAIL PLEASE TYPE RESTART" + Fore.RED)
        else: print((Style.RESET_ALL) + "FAIL PLEASE TYPE RESTART " + Fore.RED)
        if answer5 == "restart":
            main()
        
        answer6 = input()
        if answer6 == "a": print((Style.RESET_ALL) + "you go and say hi to one of the children they start crying..." + " FAIL PLEASE TYPE RESTART" + Fore.RED)
        if answer6 == "b": print((Style.RESET_ALL) + "you go over to your friend and ask how hes doing " + "Nonexistent Friend: uhh im pretty good how bout you?" + " how are you are feeling" + Fore.LIGHTGREEN_EX + " (A)" + (Style.RESET_ALL) + " like an epic gamer" + Fore.LIGHTGREEN_EX + " (B)" + (Style.RESET_ALL) + " noice or" + Fore.LIGHTGREEN_EX + " (C)" + (Style.RESET_ALL) + " depressed" + Fore.LIGHTGREEN_EX)
        else: print((Style.RESET_ALL) + "FAIL PLEASE TYPE RESTART " + Fore.RED)
        if answer6 == "restart":
            main()
        
        answer7 = input()
        if answer7 == "a": print((Style.RESET_ALL) + "you say you feel like an epic gamer... Nonexistent Friend proceeds to throw himself out the window..." + "what do you do" + Fore.LIGHTGREEN_EX + " (A)" + (Style.RESET_ALL) + " jump after him or" + Fore.LIGHTGREEN_EX + " (B)" + (Style.RESET_ALL)+ " do nothing" + Fore.LIGHTGREEN_EX)
        if answer7 == "b": print((Style.RESET_ALL) + "you say you feel pretty noice " + "Nonexistent Friend walks outside, proceeds to face palm and gets hit by a car... he died" + " FAIL PLEASE TYPE RESTART " + Fore.RED)
        if answer7 == "c": print((Style.RESET_ALL) + "you say you feel pretty down... nobody cares about your feelings ):" + " FAIL PLEASE TYPE RESTART")
        else: print((Style.RESET_ALL) + "FAIL PLEASE TYPE RESTART " + Fore.RED)
        if answer7 == "restart":
            main()
        
        answer8 = input()
        if answer8 == "a": print((Style.RESET_ALL) + " you try and jump after him but alas jumping while sitting in a chair doesnt work and you hurt your legs..." + " FAIL PLEASE TYPE RESTART" + Fore.RED)
        if answer8 == "b": print((Style.RESET_ALL) + " well this isnt helping is it" + " you get bored of seeing your friend bleeding out so you either " + Fore.LIGHTGREEN_EX + " (A)" + (Style.RESET_ALL) + " go home or" + Fore.LIGHTGREEN_EX + " (B)" + (Style.RESET_ALL) + " go to the park" + Fore.LIGHTGREEN_EX)
        else: print((Style.RESET_ALL) + "FAIL PLEASE TYPE RESTART " + Fore.RED)
        if answer8 == "restart":
            main()
        
        answer9 = input 
        if answer9 == "a": print((Style.RESET_ALL) + "you go home to watch some netflix... and before you know it is midnight" + + Fore.CYAN + "DAY THREE" + (Style.RESET_ALL) + "make next day")
        if answer9 == "b": print((Style.RESET_ALL) + " you have a walk to the park and see a dog you go to pet it..." + " it turns out it was actually a very hairy midget" + " FAIL PLEASE TYPE RESTART" + Fore.RED)
        else: print((Style.RESET_ALL) + "FAIL PLEASE TYPE RESTART " + Fore.RED)
        if answer9 == "restart":
            main()
        
        answer10 = input()
        if answer10 == "x": print("")
        if answer10 == "restart":
            main()
main()