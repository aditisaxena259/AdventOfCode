file= open("p1.txt",'r')
listl=[]
listr=[]
for line in file:
    left,right=map(int,line.strip().split())
    listl.append(left)
    listr.append(right)
def func():
    listl.sort()
    listr.sort()
    sum=0
    for i,j in zip(listl,listr):
        sum+=abs(i-j)
    print(sum)
func()
def func2():
    sum2=0
    newl=[]
    for i in listl:
        ct=i*listr.count(i)
        if i in newl:
            ct+=ct
        newl.append(i)
        sum2+=ct
    print(sum2)
func2()