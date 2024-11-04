words = ["Horse","Animal","Donkey"]
with open("q5/file.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("q5/file.txt","w") as f:
    f.write(content)