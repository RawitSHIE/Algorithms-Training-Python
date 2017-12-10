"""
pair-programming
VerticalHistogram
60070081
"""
 
def histro():
    """sorted alpha"""
    str_lst = [i for i in input()]
    str_dic = {}
    for i in str_lst:
        if i not in str_dic:
            str_dic[i] = str_lst.count(i)
    key_lst = sorted(str_dic.keys(), key=lambda x: ord(x) if ord(x) > 90 else ord(x)+100)
    max_val = max(str_dic.values())
    for i in range(max_val, 0, -1):
        string = "%03d " % i
        for j in key_lst:
            string += "* " if str_dic[j] >= i else '  '
        print(string)
    print('    ' + ' '.join(key_lst))
histro()
