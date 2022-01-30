
#Calculator Python Project

#Functions for Opertations
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b
def multiply(a,b):
    return a*b

#Main Function
def main():
#while loop to continue asking user for calculations until user decides to quit
 while True:
    #User input for type of operation 
    selection = int(input('Press 1 for addition, 2 for subtraction, 3 for division , 4 for multiplication, 5 to quit\n'))
    
    
   
    #if statements for each option
    if selection == 1:
     x= float(input('Enter a number\n'))
     y= float(input('Enter a second number\n'))
     print(x, "+" , y , "=", add(x,y))

    elif selection == 2:
     x= float(input('Enter a number\n'))
     y= float(input('Enter a second number\n'))
     print(x, "-" , y , "=", subtract(x,y))

    elif selection == 3:
     x= float(input('Enter a number\n'))
     y= float(input('Enter a second number\n'))
     print(x, "/" , y , "=", divide(x,y))

    elif selection == 4:
     x= float(input('Enter a number\n'))
     y= float(input('Enter a second number\n'))
     print(x, "*" , y , "=", multiply(x,y))

    elif selection ==5:
        print('Program has ended')
        break
        
    #Error Message if incorrect selection is made
    else:
     print('invalid selection')
    
#call to main function
if __name__ == "__main__":
    main()
