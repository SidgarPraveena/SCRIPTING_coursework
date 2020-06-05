lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele) 

visited = [0]*n


j=0
while(j<n):
    if lst[j]!= -1:
        #print(lst[j])
        visited[j]=1
    else:
        if lst[j+1]!= -1:
            #print(lst[j+1])
            visited[j+1]=1
            j+=1
    j=2*j+1
    
j=0
while(j<n):
    if lst[j]!= -1:
        #print(lst[j])
        visited[j]=1
    else:
        if lst[j-1]!= -1:
            #print(lst[j-1])
            visited[j-1]=1
            j-=1
    j=2*j+2

j=0
while(j<n):
    if (2*j+1 < n and lst[2*j+1] == -1) and (2*j+2 < n and lst[2*j+2] == -1):
        visited[j]=1
    elif 2*j+1>=n:
        visited[j]=1
    j+=1
    
sum=lst[0]
for i in range(len(visited)):
    if visited[i] == 1 and lst[i]!=-1:
        #print(lst[i],end='')
        sum+=lst[i]
print(sum+lst[0])
