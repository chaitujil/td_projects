import os

os.mkdir("telugudata")
a = {"2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"}
for i in a:
    os.mkdir("telugudata/" + i)
b = {"andhrapradesh", "business", "editorial", "entertainment", "freshnews", "nation", "navya", "special", "sports",
     "telangana"}
for i in a:
    for j in b:
        os.mkdir("telugudata/" + i + "/" + j)
