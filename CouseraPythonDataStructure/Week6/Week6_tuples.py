#Week6_tuples.py

#looks like
x = ('aa','bb','cc')
for i in x:
	print(i)


# immutable like string

# more efficient than list

# Assignment:
(x,y) = (4,'fred')

# With dictionary
#item() method returns a list of (key, value) Week6_tuples
d = dict()
d['csev'] = 2
d['cwen'] = 3
for (k,v) in d.items():
	print(k,v)

# Compare
(1,2,3) < (2,3,4)
# 从左到右比较，只要有比右边小的 停止比较， return True

# Sort
d = {'a':10,'b':1,'c':20}
d.items()
#sorted by key orders
sorted(d.items()) 
#sorted by values order
tmp = list()
for k,v in d.items():
	tmp.appends((v,k))
print(tmp)
tmp = sorted(tmp, reverse=True)# from high to low

# Shorter version>> list comprehension
print(sorted([(v,k) for k,v in c.items()]))




