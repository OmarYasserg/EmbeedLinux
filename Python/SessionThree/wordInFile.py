with open("ex.txt", "r") as f:
    content_to_read = f.read()
    print(f.tell())
    print(len(content_to_read))