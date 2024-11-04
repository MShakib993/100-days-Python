word = "Donkey"
with open("q4/file.txt") as f:
    content =  f.read()
contentNew = content.replace(word , "####")
with open("q4/file.txt","w") as f:
    f.write(contentNew)


