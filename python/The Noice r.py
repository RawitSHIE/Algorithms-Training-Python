"""The Noice"""
def main():
    """condition"""
    num_a = float(input())
    num_b = float(input())
    if num_a%2 == 0:
        num_c = float(input())
        if num_b == num_c:
            print("My heart goes Sha la la lal la\nclap clap clap")
        elif num_b > 0:
            print("My heart will go on and on\nuh hmm ummm")
        elif num_b < 0:
            print("My heart goes Sha la la la Just for you")
    elif num_a%2 == 1 and num_b%2 == 0:
        print("What's in your head!! In your head!!")
    elif num_a%2 == 1 and num_b%2 == 1:
        print("What's in your head!! Zombie Zombie!\nZombie ei ei eh oh!")
main()
