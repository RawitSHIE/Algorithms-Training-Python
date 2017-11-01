"""string condition"""
def main():
    """case and str"""
    text = input()
    num = int(input())
    text_sp = text + " "
    print((text_sp)*(num-1) + text)
    print(text, str(num)*num)
    print(text, text[::-1])
    print(text[::-1][:3])
main()
