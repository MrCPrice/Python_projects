import my_maths

old_answer = 0
old = False
active = True

while active == True:
    result = 0
    if old == True:
        a = old_answer
    else:
        a = input("Please enter a number: ")

    sym = input("Please enter one following symbols (+,-,*,/,^) or q (to quit) or cls (to clear old answer): ")
    
    if sym == "cls":
        old = False
        print("Answer has been cleared!")
    elif sym == "q":
        active = False
        print("Goodbye!")
        break
    else:
        old = True
   
    b = input("Please enter another number: ")

    if sym == "+":
        result = my_maths.add_A_B(a,b)
    elif sym == "-":
        result = my_maths.minus_A_B(a,b)
    elif sym == "*":
        result = my_maths.times_A_B(a,b)
    elif sym == "/":
        result = my_maths.devide_A_B(a, b)
    elif sym == "^":
        result = my_maths.power_A_B(a,b)
        
    print("Here is your answer: " + str(result))
    old_answer = result
