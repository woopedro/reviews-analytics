data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 
		if count % 3 == 0:
			print(len(data))
print(data)
print('檔案讀取完了，總共有', len(data), '筆資料')
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 50:
		new.append(d)
print('一共有', len(new), '筆留言長度小於50')

nose = []
for d in data:
	if '鼻' in d:
		nose.append(d)
print('一共有', len(nose),'筆留言提到鼻')