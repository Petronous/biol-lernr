cmnl = open("python_stuff/le_html/comments_processed.html", mode="w", encoding="UTF-8")

with open("python_stuff/le_html/comments.html", mode="r", encoding="UTF-8") as f:
    cmnl_str = f.read().replace("<p ", "\n<p ").replace("c13", "c1").replace("c1 c17", "c1").replace("c3 c17", "c3").replace("c3 c26", "c3")
    cmnl_lst = cmnl_str.split("\n")
    while "" in cmnl_lst:
        cmnl_lst.remove("")

    c1_block = False
    categories = []
    # cmnl_lst_mod = cmnl_lst.copy()
    class_types = {}
    for a,line in enumerate(cmnl_lst):
        cls = line[11:13]
        # if cls not in class_types: class_types[cls] = a
        # else: class_types[cls] = a
        class_types[cls] = 0
        if cls == "14":
            try:
                if len(categories[-1][-1])==0: categories[-1].pop(); print("pop")
            except:
                print("nuffin'")
            categories.append([])
        elif cls == '1"' and (len(categories[-1]) == 0 or len(categories[-1][-1]) != 0): categories[-1].append("")
        elif cls != '1"': categories[-1][-1] += line
    if len(categories[-1][-1])==0: categories[-1].pop(); print("pop")
    print(class_types)
    for a,cat in enumerate(categories):
        print("---", a)
        for ans in cat:
            print(ans)
    print(len(categories))
    cmnl.write(str(categories))
    cmnl.close()
