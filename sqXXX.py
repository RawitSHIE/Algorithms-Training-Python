"""
judge : seqence XXX
pair : Rawit & Aof
date: 5/10/2560
"""
def main():
    """the energy"""
    colum = int(input())
    seq = int(input())

    for i in range(colum):
        string = ""
        for j in range(colum):

            if i == j or i == 0 or i == colum-1 \
            or j == 0 or j == colum-1 or i == colum-1-j:
                string += "*"

            else:
                string += " "

        string += " "

        print(string * seq)
main()
