from add import add_f
from train import train_f
from detectdyna import detectdyna_f
from export import export_f

while(True):
    print("1.Add a new student")
    print("2.Recognize in real-time")
    print("3.Train the model")
    print("4.Export as spreadsheet")
    choice = int(input())
    if(choice == 1):
        print("\n")
        add_f()
    elif(choice == 2):
        print("\n")
        detectdyna_f()
    elif(choice == 3):
        print("\n")
        train_f()
    elif(choice == 4):
        print("\n")
        export_f()
    else:
        print("\nInvalid choice")
        break

