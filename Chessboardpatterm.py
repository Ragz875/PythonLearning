curr=0
prev=1
for i in range(5):
    for j in range(5):
        print(curr, ' ', end='')
        (curr,prev)=(prev,curr)
    print('')

