a = [1,2,3,4,5] 

print("GROW ARRAY TO FIVE (1->5)")
for i in reversed(range(len(a))):
	if i == 0:
		print(a)
	else:
		print(a[:-i])

print("\n\nSHRINK ARRAY TO 1 (5->1)")
for i in range(len(a)):
	if i == 0:
		print(a)
	else:
		print(a[:-i])

print("\n\nSHRINK ARRAY TO FIVE (1->5)")
for i in range(len(a)):
	if i == 0:
		print(a)
	else:
		print(a[i:])

print("GROW ARRAY TO FIVE (1->5)")
for i in reversed(range(len(a))):
	if i == 0:
		print(a)
	else:
		print(a[i:])