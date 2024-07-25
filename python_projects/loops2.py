numbers = [1, 2, 3, 4, 5, 6, 7]
while True:
    insert = input("Guess a number: ")
    if insert == "b":
        break
    a = int(insert)
    if a in numbers:
        print("You`re right!")
    else:
        print("You`re wrong. Try again.")
        
    
    
    
