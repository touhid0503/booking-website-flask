x=5,6; #tuple
print(type(x));

x=(-1,2);
print(x[-2])
#same as list

#converting
print(type(x))
y=list(x);
print(type(x))
print(type(y))

y.insert(1,"l");
x=tuple(y);
print(x);
#tuple immutable
print(x.index("l"))