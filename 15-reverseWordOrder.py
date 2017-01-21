def reverseWordOrder(n: str):
    return " ".join(list(n.split())[::-1])


myStr = "My name is Khalid"
print(reverseWordOrder(myStr))
