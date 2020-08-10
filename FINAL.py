
import time
import random

health = 100
rope = False
shard = False

def health_checker():
  global health
  while health <=0:
     print("Oh dear you were slain or captured")
     tryagain = input("Would you like to try again? (Y/N)")
     if tryagain.upper() == "Y":
       health = 100  
       start_game()
     elif tryagain.upper() == "N": 
        print("thanks for playing!")
        end_game()   
        break      
  else:
      print("you health was reduced to {}".format(health))

def start_game():
    print("Its been so long since you have seen the sun...")
    time.sleep(2)
    print("Drifting in and out of consciousness... trapped in this rotten cell for a crime you did not commit")
    time.sleep(2)
    print("The enemy has heavily reduced your spirit and your memories are not what they were")
    time.sleep(2)
    print("But it slowly comes back to you... you are the prince Elith hailing from the kingdom Wessex and if you stay here any longer, you will die soon...")
    time.sleep(2)
    print("In the narrow slits of the tiny window in your cell, a piece of paper flutters onto the ground, it is signed 'C' ")
    time.sleep(2)
    response = input("My friend, for too long you have wasted away in this cell, Are you ready to escape this wretched place? (Y/N) ")
    if response.upper() == "Y" or response.upper() == "YES":
        print("Let us press forward then!")
        act_one()
    elif response.upper() == "N" or response.upper() == "NO":
        print("Then you will spend the rest of your life in this cell...")
    else:
        print("Try again, I didn't recognise that.")
        start_game()


def act_one():
    choice = input("You must decide which method of escape to choose,  search the cell for a weapon?(A) or jump through the window(B)") 
    if choice.upper() == "A":
     act_one_A()
    elif choice.upper() == "B":
       act_one_B() 
    else:
     print("Did not understand command, choose again")
     act_one()
    

def act_one_B():
    
    choice= input("You decide to escape out through the prison window, do you decide to take the rope to aid in your escape? (Y/N)")
    global rope
    if choice.upper() == "Y":
        rope = True
        act_one_BB()
    elif choice.upper()== "N":
        rope = False
        act_one_BB()
    else:
        print("Did not understand command, please choose again")  
        act_one_B()     


       

def act_one_A():
    global shard
    global health
    print("You frantically search the room for a weapon, the room is very empty...") 
    time.sleep(2)
    print("You trace your fingers across the walls... you hear a faint humming noise from the corner of a wall")
    time.sleep(2)
    print("The wall is in poor condition in this corner and is starting to crumble...")
    time.sleep(2)
    print("after much digging the sound of the humming gets louder until you see a small metal shard jut out from the corner")
    anotherchoice = input("Take the metal shard? (Y/N)")
    if anotherchoice.upper() == "Y":
     print("as you try to extract the blade you cut yourself slightly... ouch!")
     time.sleep(2)
     health -= 5
     if health <= 0:
      health_checker()
      time.sleep(2)
     elif health>0:
      health_checker()
      time.sleep(2)   
      shard = True
      act_one_AA()
    elif anotherchoice.upper() =="N":
        print("since you decided you have no use for this metal shard, you discard it and opt for plan B")
        time.sleep(2)
        shard = False
        act_one_B()  
    else:  
        print("Did not understand command, choose again")
        act_one() 


def act_one_AA():
    global health
    print("With the shard now in your possession wait for the right time to act")
    time.sleep(2)
    command = input("you must decide: do you attempt to pick the lock and sneak out of the cell (A) or do you wait for a guard to approach and subdue him (B) (A/B)")
    time.sleep(2)
    if command.upper()=="A":
       pick_lock()
    elif command.upper()=="B":
        attack_guard()
    else:
     print("Did not understand command, choose again")
     act_one_AA()
    
def end_game():
    print("you ended the game")

def pick_lock():
    randy = random.randint(0,100)
    if randy >=0 and randy <= 40:
     print("you attempt to pick the lock...")
     time.sleep(3)
     print("success! you slip through the door in the middle of the night and must now chose to turn to the door on the right or turn left")
     time.sleep(1)
     level_two_A()
     time.sleep(2)
    elif randy>=41 and randy<=100:
     print("you're attempts at picking the lock failed... maybe now its time to wait for a guard to distract and dispatch")
     time.sleep(3)   
     attack_guard()

    

def attack_guard():
    global health
    time.sleep(2)
    print("you call the guard over, he is not pleased... his eyes widen as he sees the weapon in your hand but is too slow to react")
    time.sleep(1)
    print("you dispatch him, but in the melee you lose some health")
    time.sleep(2)
    health -= 20
    if health <= 0:
      time.sleep(2)
      health_checker()
    elif health>0:
      time.sleep(2)
      health_checker()
      time.sleep(2)
      print("using the guards keys you unlock the door and continue with your mission")   
      level_two_A()



def act_one_BB():
    global health
    global rope
   
    if rope == True:
      time.sleep(2)
      print("you make your way down the outer prison wall safely with rope in hand, taking a small amount of damage from the jump to the floor below") 
      health = health - 5
      if health <= 0:
         health_checker()
         time.sleep(2)
      elif health>0:
         health_checker() 
      level_two_B()
    elif rope == False:
      time.sleep(2)
      print("you jump out the window with no safety, taking heavy damage")
      health = health - 30
      if health <= 0:
         health_checker()
         time.sleep(2)
      elif health>0:
         health_checker()
         level_two_B()
      
       
       

     

def level_two_B():
    global health
    print("as you land into the terrace below, you hear a dog barking in the distance!")
    time.sleep(1)
    response = input("do you A tend to your wounds? or B do you run into a nearby ally (A/B).")

    if response.upper() == "A":
     time.sleep(2)
     print("you fixed up your leg but the dog catches you and you lose health fighting off and destroying the dog.")
     time.sleep(1)
    
     health = health - 10
     if health <= 0:
        health_checker()
     elif health>0:
       time.sleep(2)
       health_checker()
       time.sleep(2)
       print("you make your way to the town square and assimilate with the crowd... you hear lots of cheering and singing in the distance")
       time.sleep(2)
       feasting_hall()

    
    elif response.upper() == "B":
     print("you run into a nearby ally, and promptly pass out from fatigue...")
     time.sleep(3)
     print ("you wake up some time later, with most of your injuries tended to by a stranger whilst you were unconcsious...")
     time.sleep(2)
     health+= 20
     print(" you feel reinvigorated... your health has been boosted, it is now  {}".format(health))
     time.sleep(1)
     print("nearby you hear lots of shouting and singing, it appears some kind of festival is being celebrated by your captors")
     time.sleep(2)
     feasting_hall()

    else:
        print("Did not understand command, choose again") 
        level_two_B()


   
     

def left_path_A():  
    global health
    
    time.sleep(1)
    response = input("Which do you choose? (L/R) ")
    if response.upper() == "R":
       time.sleep(2)
       print(" you climb down the trapdoor into the nasty sewers, eventually leading to more tunnels which leads you outside into the courtyard")
       time.sleep(2)
       print("the noxious fumes make you woozy and you feel a little unwell")
       health -= 5
       time.sleep(2)
       health_checker()
       time.sleep(1)
       print("nearby you hear lots of shouting and singing, it appears some kind of festival is being celebrated by your captors")
       time.sleep(3)
       feasting_hall()
       
    elif response.upper() == "L":
        print("you decide to approach the door to the right, you smell smoke but proceed regardless... whats the worst that could happen?")
        time.sleep(1)
        print("as you push past the door, you are greeted by a giant fire breating dragon, who proceeds to burn you to a crisp.")
        time.sleep(1)
        health = health - 20000
        if health <= 0:
          health_checker()
        elif health>0:
         health_checker()
    else:
        print("Did not understand command, choose again")
        left_path_A()     
      

def level_two_A():
    time.sleep(2)
    print("The door to your left is warm and smoky... you are enticed by the warmth, having been snared in a very cold cell for so long")
    time.sleep(2)
    print("The path to the right leads to a trapdoor into an underground sewer system, a very smelly affair but probably will get you safe quicker...")
    time.sleep(2)
    left_path_A()






def feasting_hall():
    global health
    print("You make your way towards the town square and head for the large Feasting Hall")
    time.sleep(2)
    print("There are three guards guarding the entrance to the hall")
    time.sleep(2)
    print("There's no way to pass without being spotted")
    time.sleep(2)
    response = input("Do you fight your way through and incite a riot(A) or set fire to the wall hangings to create a distraction(B) (A/B) ")
    if response.upper() == "A":
        time.sleep(2)
        print("You fight your way through, creating a massive brawl... allowing you to slip inside the feasting hall")
        time.sleep(2)
        health = health - 25
        if health <= 0:
         health_checker()
        elif health>0:
         health_checker()
        
        corridor()
        
    elif response.upper() == "B":
        print("Your fire distraction worked perfectly")
        time.sleep(1)
        print("You take 0 damage")
        time.sleep(2)
        corridor()
    else: 
        print("Did not understand command, choose again")
        feasting_hall()
         

def corridor():
    print("You enter a brightly lit corridor, lined with family portraits")
    time.sleep(2)
    print("You enter the first unlocked door")
    time.sleep(2)
    bedroom()
def bedroom():
    global health
    print("You've entered Princess Beyonce's bedroom")
    time.sleep(1)
    print("How do you prevent her from screaming & alerting the guards ? ")
    time.sleep(1)
    time.sleep(2)
    response = input("Do you  (A) subdue her  or  (B) attempt to charm her (A/B) ")
    time.sleep(2)
    if response.upper() == "A":
        print("You've successfully subdued the princess")
        time.sleep(2)
        health = health - 5
        print("you take a small amount of damage in the struggle")
        time.sleep(2)
        if health <= 0:
         health_checker()
        elif health>0:
         health_checker()
        time.sleep(2)
        balcony()
    elif response.upper() == "B":
      print("you attempt to charm the princess...")
      time.sleep(2)
      print("after you finish telling her your tale, she is impressed and shows you her secret passage out of the castle...")
      time.sleep(2)
      ending()
    else: 
       print("Did not understand command, choose again")
       bedroom() 
       
def balcony():
    global health
    print("You exit the room onto a narrow balcony")
    time.sleep(2)
    print("Far below you see a deep pool")
    time.sleep(2)
    response = input(" Do you (A) dive off the balcony into the pool or  make a rope from bed sheets and attempt to climb down to the courtyard (B) (A/B) ")
    if response.upper() == "A":
        time.sleep(2)
        print("Oh no, the pool is full of piranhas & they rip you to shreds")
        health = health - 500
        time.sleep(2)
        if health <= 0:
         time.sleep(2)    
         health_checker()
        elif health>0:
         health_checker()
    elif response.upper() == "B":
        act_four()
    else:
        print("Did not understand command, choose again")
        balcony()    











def act_four():
    global health
    print("You climb down the balcony with ease...You're nearly home and dry.. just the final stretch!")
    time.sleep(2)
    print("A natural wall of trees makes up one of the castles defensive walls, it would seem like this is your only hope of escaping")
    time.sleep(2)
    print("As you run into this woodland area, somehow managing not to be detected by any of the patrol guards, you hear a the distint soft growling of a grizzly bear... ")
    time.sleep(2)
    response = input("Your final choice is before you, do you fight the grizzly bear (A) or run as fast as you can to safety deeper into the woods(B) (A/B)")
    time.sleep(2)
    if response.upper() == "A":
        time.sleep(1)
        print("You decide to be brave and challenge the bear...")
        time.sleep(1)
        health = health - 35
        if health <= 0:
         health_checker()
         time.sleep(2)
        elif health>0:
        
         time.sleep(1)
         print("After a furious battle, you come out heavily bleeding... but still alive.")
         time.sleep(1)
         time.sleep(1)
         health_checker()
         ending() 
    elif response.upper() == "B":
         time.sleep(1)
         time.sleep(1)
         print("A wise decision, fighting a bear in this condition would not have a good outlook...")
         time.sleep(1)
         print("Atlast, you are finally free from capture and make it safely back to your kingdom")
         time.sleep(2)
         ending()
    else:
        print("Did not understand command, choose again")
        act_four()     
         
        
def ending():
 global health
 global rope
 rope == False
 if health >=70:
  print("Well done for making it through to the end, you managed to survive with {} health remaining".format(health))
  time.sleep(2)
  print("Congratulations, you are awarded gold for taking minimal damage!")
 elif health >=40 and health <70:
    print("Well done for making it through to the end, you managed to survive with {} health remaining".format(health))
    time.sleep(2)
    print("Congratulations, you are awarded silver for maintaining moderate health!")
 else:  
    print("Well done for making it through to the end, you managed to survive with {} health remaining".format(health)) 
    time.sleep(2)
    print("Congratulations, you are awarded with bronze for barely surviving!") 



start_game()




