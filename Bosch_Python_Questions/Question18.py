while(1):
    a = float(input("Enter the first Number: "))
    b = float(input("Enter the second Number: "))
    print("\n","Please select from the below Options")
    n = int(input("Press 1 for ADD | Press 2 for SUB | Press 3 for MUL | Press 4 for DIV"))
    match n:
        case 1:
            print("\n")
            print("Sum of the Values: ",a+b)
        case 2:
            print("\n")
            print("Diff of the Values: ",a-b)
        case 3:
            print("\n")
            print("Multiplication of Values: ",a*b)
        case 4:
            print("\n")
            print("Division of the Values: ",a/b)
        case _:
            print("\n")
            print("Oops!! You given wrong input So Run the program again hahaha")
            print("\n")
            break
    
    
    