"""strip"""
def main():
    """<p>"""
    text = input()
    if text.startswith("<p>") and text.endswith("</p>"):
        pos = len(text)-4
        textst = text[3:pos]
        print("%100s" %textst)
    else:
        print("%100s" %text)
main()
