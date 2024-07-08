x={7,6,5,5,7}; #set
print(x)
print(type(x));
x.add(1);
x.remove(5);
print(x)

for i in x: #looping
    print(i);

#unordered
#unchangeable
#duplicates not allowed
a={1,2,3,5}
x.update(a); #union
print(x)
# x.clear();
# print(x)
x.pop()
print(x)

a1={1,2,3}
a2={2,3,4}

a3=a1.union(a2) #union
print(a1.union(a2))
print(a3)

print(a1.intersection(a2)) #intersect