print('Welcome to learn with quiz')

player = input('do you want to play a game?')

if player.lower() !='yes':
    quit()
    
print('lets play the game') 
score=0   

question = input('in rainbow how many colours will be there?')
if question.lower() == 'seven':
    print('correct')
    score+=1

else:
    print('incorrect')

question = input('how many days do you have in a week?')
if question.lower() == 'seven':
    print('correct') 
    score+=1

else:
    print('incorrect')

question = input('who is the king of forest?')
if question.lower() == 'lion':
    print('correct')  
    score+=1

else:
    print('incorrect')

question = input('tamil actor who has acted in moive plays police role his name was & moive name is singam?')
if question.lower() == 'durai singam':
    print('correct') 
    score+=1                

else:
    print('incorrect')

question = input('who is the father of nation in india ?')
if question.lower() == 'gandhi':
    print('correct') 
    score+=1 

else:
    print('incorrect')

print("your score"+ str(score))    

