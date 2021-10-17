qus_processed = open("python_stuff/le_html/qus_processed.txt", mode="w", encoding="UTF-8")

with open("python_stuff/le_html/text.txt", mode="r", encoding="UTF-8") as f:
    categories = []
    for line in list(f):
        if line[:3] in ("﻿Ot","Otá"):
            try:
                if len(categories[-1][-1])==0: categories[-1].pop(); print("pop")
            except:
                print("nuffin'")
            categories.append([])
        elif line.isspace() and (len(categories[-1]) == 0 or len(categories[-1][-1]) != 0):
            categories[-1].append("")
        elif not line.isspace():
            categories[-1][-1] += str(len(categories)) + ". - " + line.replace("\n", "<br>")
    if len(categories[-1][-1])==0: categories[-1].pop(); print("pop")
    for a,cat in enumerate(categories):
        print("---", a)
        for ans in cat:
            print(ans.replace("\n", "\\n"))
    print(len(categories))
    qus_processed.write(str(categories))
    qus_processed.close()
