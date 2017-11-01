"""
pair proggramming
judge : classify
date : 19/10/60
"""
def main():
    """no dict"""
    name = []
    num = []
    data = []
    lock = ""
    while 1:
        text = input()
        if text.isalpha():
            break
        data.append(text[:4])
    data = sorted(data)
    for i in data:
        if i not in name:
            name.append(i)
            num.append(1)
        else:
            num[name.index(i)] += 1
    for i in range(len(num)):
        if name[i][:2] != lock:
            print(name[i][:2], int(name[i][2:4]), num[i])
            lock = name[i][:2]
        else:
            print("--", int(name[i][2:4]), num[i])
main()
