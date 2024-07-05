def perform_operation(num1, num2, operation):
        if operation=="add":
           return num1+num2
        elif operation=="subtract":
            return num1-num2
        elif operation=="multiply":
            return num1*num2
        elif operation=="divide":
             while num2==0:
                  print("num2 should be different from zero")
                  return 
             return num1/num2
        else:
            print("Enter valid operations")
    