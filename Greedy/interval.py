intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]
intervals.sort(k=lambda x:(x[1],x[0])
c=0
v=[]
e=-1
for i in intervals:
  if e<i[0]:
    e=i[1]
    c+=1
    v.append(i)
print(c)#maximum 
print(v) # non conflicting pairs
print(len(intervals)-c)  #minimum
