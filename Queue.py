import random
import tkinter as tk

def queue():
    Queue = [random.randint(1, 10) for i in range (10)]
    while True:
        choice = input("""
    ~~~Make your choice~~~
1)Enqueue
2)Dequeue
3)Peek
4)Exit
""")
        if choice == "1" or choice == "Enqueue":
            Add = input("What would you like to enqueue?")
            Queue.append(Add)

        elif choice == "2" or choice == "Dequeue":
            if len(Queue) == 0:
                print("Queue empty")
            else:
                del Queue[0]

        elif choice == "3" or choice == "Peek":
            if len(Queue) == 0:
                print("Queue empty")
            else:
                print(Queue[0])
                
        elif choice == "4" or choice == "Exit":
            break
        
        elif choice == "I wish for eventual greatness":
            print("It is done")
            main()

        else:
            print("How are you this dense, pick one of the FOUR options")

def main():
    root = tk.Tk()
    root.title("Libra Image")

    # Load image named "Libra.gif" from the same folder
    img = tk.PhotoImage(file="Libra.gif")

    # Display it
    label = tk.Label(root, image=img)
    label.pack()

    # Keep a reference so the image doesn't disappear
    label.image = img

    root.mainloop()

    
queue()
