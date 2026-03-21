# using with statement use for file so not need to close method write

with open("c.txt") as f:
    text = f.read()
print(text)
