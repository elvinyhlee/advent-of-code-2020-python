#1
count = 0
with open('day1-data.txt') as f:
    for line in f:
        num = int(line)
        count += (num-num%3)//3 - 2

f.close()
print(count)



#2
count = 0
with open('day1-data.txt') as f:
    for line in f:
        num = int(line)
        num = (num-num%3)//3 - 2
        while num > 0:
            count += num
            num = (num-num%3)//3 - 2

f.close()
print(count)
