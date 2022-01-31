#Luis Carrillo
#Quick and Dirty Calculator in Python


running = True #Condition for while loop

result = 0.0 #Default value before any input

while running:
    print("""
          Select an operation:
          [a] Addition
          [s] Subtraction
          [d] Division
          [f] Multiplication
          [c] Clear
          [x] Exit
          """)
    
    print(result)
    
    choice = input() 
    
    match choice: #Python version of switch statement
        case "a": #Addition
            x = float(input("Enter 1st number:"))
            y = float(input("Enter 2nd number:"))
            result = x + y
        case "s": #Subtraction
            x = float(input("Enter 1st number:"))
            y = float(input("Enter 2nd number:"))
            result = x - y
        case "d": #Division
            x = float(input("Enter 1st number:"))
            y = float(input("Enter 2nd number:"))
            result = x / y
        case "f": #Multiplication
            x = float(input("Enter 1st number:"))
            y = float(input("Enter 2nd number:"))
            result = x * y
        case "c": #Clear
            result = 0.0
        case "x": #Exit
            print("Goodbye!")
            running = False #While loop ends, ending program
        case _: #Catch-all for any other input
            print("Error: Invalid Input")