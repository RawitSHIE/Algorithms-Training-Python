"""[Rerun Exam Week 2] Duplicates"""
def main():
    """Duplicates"""
    num = int(input())
    listed = []
    for  _ in range(num):
        text = input().lower()
        if text in listed:
            print("Yes")
        else:
            listed.append(text)
            print("No")
main()
