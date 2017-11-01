"""
judge : Fizz &Buzz
pair : Rawit & Aof
date: 5/10/2560
"""
def main():
    """3 or 5 or 15"""
    for i in range(1, int(input())+1):
        if i%15 == 0:
            print("Fizz Buzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
main()
