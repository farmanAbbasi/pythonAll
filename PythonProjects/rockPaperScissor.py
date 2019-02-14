from random import randint

def RPS(pc,cc):
    while(1):
        player=input('rock(r), paper(p) or scissor(s) ?')
     
        chosen=randint(1,3)
        if(chosen==1):
            computer='r'
        elif(chosen==2):
            computer='p'
        else:
            computer='s'
        print(player,'vs',computer)
        
        if((player=='r' and computer=='s') or (player=='s'and computer=='p') or (player=='p' and computer=='r')):
            print("Player wins!")
            pc+=1
            print("Player = ",pc,"Computer = ",cc)
        elif(player==computer):
            print("Draw")
        else:
            print("Computer wins!!!!")
            cc+=1
            print("Player = ",pc,"Computer = ",cc)
   

RPS(0,0)    
    
    

