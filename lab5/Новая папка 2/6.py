import re

with open("/Users/kydyrtabyngalyyev/Desktop/ll6588/lab5/Новая папка 2/row.txt", "r", encoding="utf-8") as row:
    file = row.read()
a = re.sub(r"[ ,.]", ":", file)
for i in a:
    print(i, end=" ")