def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)

def trailingzeroes(n):
    fact = factorial(n)
    count=0
    while(True):
        if(fact%10!=0):
            break
        count = count+1
        fact=fact//10
        
    return count

if __name__ == "__main__":
    n= int(input("Enter number to find factorial: "))
    print(f"factorial is {factorial(n)}.")
    print(f"trailing zeroes in factorial are {trailingzeroes(n)}.")