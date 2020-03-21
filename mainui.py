from add import add_f
from train import train_f
from detectdyna import detectdyna_f
from export import export_f
from addimg_dev import add_from_file

while(True):
    print("1.Add a new student")
    print("2.Recognize in real-time")
    print("3.Train the model")
    print("4.Export as spreadsheet")
    choice = int(input())
    if(choice == 1):
        print("\n")
        print("1.Add from file")
        print("2.Add from camera feed")
        option = int(input())
        if (option == 1):
            print("\n")
            add_from_file()
        elif (option == 2):
            print("\n")
            add_f()
        else:
            print("\nInvalid choice")
            break
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

