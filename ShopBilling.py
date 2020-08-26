sum = 0
while(True):
    userinput = input("Enter price or q to quit: \n")
    if(userinput!='q'):
        sum = sum + int(userinput)
        print(f"Your order total so far is {sum}.")

    else:
        print('')
        print(f"Your Bill Total is {sum}.")
        break
    