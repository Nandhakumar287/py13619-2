n=int(input())
li=list(map(str,input().split()))[:n]
li.sort(key=len)
c=0
for i in range(1,len(li)):
    if(li[0] in li[i]):
        c+=1
if(c==len(li)-1):
    print(li[0])
