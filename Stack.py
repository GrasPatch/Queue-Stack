import os
 
stakataka = []

stakataka.append(69)
stakataka.append(420)
stakataka.append(13)
stakataka.append(64)
stakataka.append('Dylan')
stakataka.append('Hannah')
stakataka.append('Noah')

def menu(stakataka):
    choice = input("Would you like to Pop, Push, Peek, Print, or Bugger off?")
    if choice.lower() == 'pop':
        Pop(stakataka)
    elif choice.lower() == 'push':
        Push(stakataka)
    elif choice.lower() == 'peek':
        Peek(stakataka)
    elif choice.lower() == 'print':
        for i in range (0, len(stakataka)):
                print(stakataka[len(stakataka)-i-1])
        menu(stakataka)
    elif choice.lower() == 'bugger off':
        print("Fine then")
        os.system('shutdown -s')       
    else:
        print("Stoopid")
        menu(stakataka)
    
def Pop(stakataka):
    stakataka.pop()
    menu(stakataka)
    
def Push(stakataka):
    inp = input("What would you like to push?")
    stakataka.append(inp)
    menu(stakataka)
    
def Peek(stakataka):
    length = len(stakataka)
    print(stakataka[length-1])
    menu(stakataka)

menu(stakataka)
