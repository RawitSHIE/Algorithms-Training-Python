"""[Rerun Exam Week 2] Plagiarism"""
def main():
    """Plagiarism"""
    text = list(input().lower())
    time = 0
    while 1:
        pas = list(input().lower())
        if pas == text:
            print("System Unlocked")
            break
        elif time == 19:
            print("System Locked Down")
            break
        elif len(pas) == len(text):
            like = 0
            for i in range(len(text)):
                if pas[i] == text[i]:
                    like += 1
            print("Likeness =" ,like)
        else:
            print("Entry Denied")
        time += 1
main()
