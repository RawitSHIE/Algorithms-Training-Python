"""[Rerun Exam Week 2] My money"""
def main():
    """banking"""
    name = input()
    account = 0
    while 1:
        command = input().lower()
        if command == "deposit":
            account += int(input())
        elif command == "withdraw":
            account -= int(input())
        elif command == "delete":
            account = 0
        elif command == "stop":
            break
    print(name, account, sep=" : ")
main()
