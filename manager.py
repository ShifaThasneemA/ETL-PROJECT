from matplotlib import pyplot as plt
class hr:
    def __init__(self,dbname):
        self.dbname=dbname
        import pandas as pd
        import pymysql
        data = pymysql.connect(user='root', password='', host="localhost", database="hr")
        cursor = data.cursor()
        sql = "select * from"+" "+self.dbname;
        global result
        result = pd.read_sql(sql, data)
        print("success")
    def datashow(self):
        try:
            print(result)
        except:
            print("error")


    def bargraph(self,a,b):

        try:
            plt.bar(result[a],result[b])
            plt.show()
        except:
            print("error")
    def linegraph(self,a,b):
        try:
            plt.plot(result[a],result[b])
            plt.show()
        except:
            print("error")
    def piechart(self,a):
        try:
            plt.pie(result[a])
            plt.show()
        except:
            print("error")
    def histplot(self,a):
        try:
            plt.hist(result[a])
            plt.show()
        except:
            print("error")

    def scatterplot(self,a,b):
        try:
            plt.scatter(result[a],result[b])
            plt.show()
        except:
            print("error")

name=input("enter your tablename:")
hr1=hr(dbname=f"{name}")
hr1.datashow()
print("column name:")
j = 1
for i in result.columns:
    print(j, i)
    j = j + 1

opt=int(input("""1.bargraph 2.linegraph 3.piechart 4.histplot 5.scatterplot"""))
if opt == 1:
    j = 1
    for i in result.columns:
        print(j, i)
        j = j + 1

    x=int(input("enter x value:"))
    if x==1:
        a=result.columns[0]
    elif x==2:
        a=result.columns[1]
    elif x==3:
        a=result.columns[2]
    elif x==4:
        a=result.columns[3]
    elif x==5:
        a=result.columns[4]
    elif x==6:
        a=result.columns[5]
    elif x==7:
        a=result.columns[6]
    elif x==8:
        a=result.columns[7]
    elif x==9:
        a=result.columns[8]
    elif x==10:
        a=result.columns[9]
    elif x==11:
        a=result.columns[10]
    elif x==12:
        a=result.columns[11]
    elif x==13:
        a=result.columns[12]
    elif x==14:
        a=result.columns[13]
    elif x==15:
        a=result.columns[14]
    else:
        print("error")
    y = int(input("enter your y:"))
    if y==1:
        b=result.columns[0]
    elif y==2:
        b=result.columns[1]
    elif y==3:
        b=result.columns[2]
    elif y==4:
        b=result.column[3]
    elif y==5:
        b=result.column[4]
    elif y==6:
        b=result.column[5]
    elif y==7:
        b=result.columns[6]
    elif y==8:
        b=result.columns[7]
    elif y==9:
        b=result.columns[8]
    elif y==10:
        b=result.columns[9]
    elif y==11:
        b=result.columns[10]
    elif y==12:
        b=result.columns[11]
    elif y==13:
        b=result.columns[12]
    elif y==14:
        b=result.columns[13]
    elif y==15:
        b=result.columns[14]
    hr1.bargraph(a,b)
elif opt == 2:
    j = 1
    for i in result.columns:
        print(j, i)
        j = j + 1

    x =int(input("enter x value:"))
    if x == 1:
        a = result.columns[0]
    elif x == 2:
        a = result.columns[1]
    elif x == 3:
        a = result.columns[2]
    elif x == 4:
        a = result.columns[3]
    elif x == 5:
        a = result.columns[4]
    elif x == 6:
        a = result.columns[5]
    elif x == 7:
        a = result.columns[6]
    elif x == 8:
        a = result.columns[7]
    elif x == 9:
        a = result.columns[8]
    elif x == 10:
        a = result.columns[9]
    elif x == 11:
        a = result.columns[10]
    elif x == 12:
        a = result.columns[11]
    elif x == 13:
        a = result.columns[12]
    elif x == 14:
        a = result.columns[13]
    elif x == 15:
        a = result.columns[14]
    else:
        print("error")
    y = int(input("enter your y:"))
    if y == 1:
        b = result.columns[0]
    elif y == 2:
        b = result.columns[1]
    elif y == 3:
        b = result.columns[2]
    elif y == 4:
        b = result.columns[3]
    elif y == 5:
        b = result.columns[4]
    elif y == 6:
        b = result.columns[5]
    elif y == 7:
        b = result.columns[6]
    elif y == 8:
        b = result.columns[7]
    elif y == 9:
        b = result.columns[8]
    elif y == 10:
        b = result.columns[9]
    elif y == 11:
        b = result.columns[10]
    elif y == 12:
        b = result.columns[11]
    elif y == 13:
        b = result.columns[12]
    elif y == 14:
        b = result.columns[13]
    elif y == 15:
        b = result.columns[14]

    hr1.linegraph(a,b)
elif opt == 3:
    a=input("enter x value:")
    hr1.piechart(a)
elif opt == 4:
    a = input("enter x value:")
    hr1.histplot(a)
elif opt == 5:
    a = input("enter x value:")
    b = input("enter y value:")
    hr1.scatterplot(a,b)
else:
    print("not available")

