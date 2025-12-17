stakataka = []

stakataka.append(69)
stakataka.append(420)
stakataka.append(13)
stakataka.append(64)
stakataka.append('Dylan')
stakataka.append('Hannah')
stakataka.append('Noah')

def menu(stakataka):
    choice = input("Would you like to Pop, Push, or Peek?")
    if choice.lower() == 'pop':
        Pop(stakataka)
    elif choice.lower() == 'push':
        Push(stakataka)
    elif choice.lower() == 'peek':
        Peek(stakataka)

def Pop(stakataka):
    stakataka.pop()
    for i in range (0, len(stakataka)):
                print(stakataka[len(stakataka)-i-1])
                
def Push(stakataka):
    inp = input("What would you like to push?")
    stakataka.append(inp)
    for i in range (0, len(stakataka)):
                print(stakataka[len(stakataka)-i-1])
                
def Peek(stakataka):
    print(stakataka[0])

menu(stakataka)
