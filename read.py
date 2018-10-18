data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0: ## % --> 
			print(len(data))
print('file reading has completed!! There are total', len(data), 'records found')


sum_len = 0 
for d in data:
	sum_len = sum_len + len(d)  ## sum_len += len(d)

print('the average length of comment is', sum_len/len(data))


## select records that comments is less than 100 characters
new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('There are total', len(new), 'records that comment is less than 100 characters')
print(new[0])
print(new[1])


