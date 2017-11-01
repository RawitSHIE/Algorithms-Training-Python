"""
pair programming
Filter
60070092
"""
import json as js
def main():
    """sorted listed"""
    stu_dic = js.loads(input())
    divi = float(input())
    state = True
    sort_id = sorted(stu_dic)
    for i in sort_id:
        if stu_dic[i] >= divi:
            print(i, "%.2f" %stu_dic[i], sep="\t")
            state = False
    if state:
        print("Nope")
main()
