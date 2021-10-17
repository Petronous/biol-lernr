qs = open("questions.txt", mode = 'w', encoding = "utf-8")
ans= open("answers.txt", mode = 'w', encoding = "utf-8")


with open("text.txt", encoding = "utf-8") as t:
    an = ""
    for line in t:
        if line[:2] == "..":
            qs.write(line[2:])
            an += '.\n'
            if an != "": ans.write(an); an = ""
        else:
            an += line
    if an != "": ans.write(an)

qs.close()
ans.close()
