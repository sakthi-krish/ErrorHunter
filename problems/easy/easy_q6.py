# Print Numbers from 1 to N: Write a program to print numbers from 1 to a given number N using a while loop.
 
n=int(input("enter the number:")) 
i = 1
while i <=n:
    print(i)
    i+= 1
 
def print_numbers(num):
    i = 1
 
    while i <=num:
        print(i)
 
        i += 1   
        

if __name__ == "__main__":
    num = int(input("Enter the Number :"))
    res = print_numbers(num)
 
        
 