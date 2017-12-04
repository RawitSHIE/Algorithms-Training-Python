"""
60070081
"""
def main():
    """sorting point"""
    listed = []
    time = int(input())
    for j in range(time):
        dicted = {}
        for _ in range(int(input())):
            text = input().split(" ")
            dicted[text[1]] = text[0]
        sorted_dic = sorted(dicted.keys())
        string = ""
        for i in sorted_dic:
            string += str(dicted[i])
            string += " "
            string += str(i)
        listed += [string]s
    for i in listed:
        print(i)
main()
