"""
date : 21/09/2560
pair pro: Rawit & Supakit
judge : HelloWorldComeBack
"""
def main():
    """is ไทย"""
    text = input()
    for i in text.lower():
        if i in "abcdefghijklmnopqrstuvwsyz":
            alp = True
        else:
            alp = False
            break
    if alp:
        print("Hello %s." %text)
    else:
        print("สวัสดี %s" %text)
main()
