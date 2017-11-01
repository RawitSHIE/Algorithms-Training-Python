"""doc str"""
def main():
    """def main"""
    text = input()
    if text.lower() == (text[::-1]).lower():
        print(text, "is Palindrome.")
    else:
        print("This is not Palindrome")
main()
