try:  
    a = int(input())  
    b = int(input())  
    c = a/b
    print(c)  
except ZeroDivisionError:  
    print("Denominator can't be 0")  
except ValueError:  
    print("Input should be an integer")  
except:  
    print("Something went wrong")
    
    
 """
 if a = 5, b = 0 then zero division error 
 if a = 5, b = "p" then value error
 else another exception 
 """
