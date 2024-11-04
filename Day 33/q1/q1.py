with open("q1/file.txt") as f:
    content = f.read()
    if "twinkle" in content:
        print("Twinkle is present")
    else:
        print("not present")
