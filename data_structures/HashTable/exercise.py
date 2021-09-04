count = {}
with open('poem.txt', 'r') as f:
    for line in f:
        for word in line.split():
            if word in count:
                count[word] += 1
            else:
                count[word] = 1 

print(count)
