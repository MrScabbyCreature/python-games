import random

#converting names to corrosponding numbers
def number(name):
    if name=="Rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="Paper":
        return 2
    elif name=="Lizard":
        return 3
    elif name=="Scissors": 
        return 4

#converting numbers to corrosponding names
def name(number):
   if number==0:
        return "Rock"
   elif number==1:
        return "Spock"
   elif number==2:
        return "Paper"
   elif number==3:
        return "Lizard"
   elif number==4:
        return "Scissor"

def rpsls(player_choice):
    player_throw = number(player_choice)
    computer_throw = random.randrange(0,5)
    result = (player_throw - computer_throw) % 5
    
    print "Player chooses" , name(player_throw)
    print "Computer chooses" , name(computer_throw)

    if result>2:
        print  "Computer wins!"
        
    elif result<3 and result>0:
        print "Player wins!"
            
    else:
        print "Its a Draw!"  
     
    print           
    

rpsls("Rock")
rpsls("Spock")
rpsls("Paper")
rpsls("Lizard")
rpsls("Scissors")

