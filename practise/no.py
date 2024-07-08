# print("hi");
x=5;
print(type(x));

x=[5,6]; #list
print(type(x));
print(x[-1]) #reverse
print(x[-2])
x=[1,2,-1,1]
print(x[0:3]); #printing 
x[1]=5; #mutable
print(x);
x[0:3]=[-2,0,1];
print(x);
x.append("k"); #append
print(x);

x.insert(len(x),2); #insert
print(x); 
x.remove("k"); #remove
print(x);

del x[1]; #delete
print(x);
#x.clear(); #clear
x.insert(0,5);
print(x);
x.sort(); #sorting (asc)

print(x);

y=[0,1,4,-1,0]
y.sort(reverse=True); #sorting (desc)
print(y)
y.sort()
print(y);
y.reverse(); #reverse
print(y);




