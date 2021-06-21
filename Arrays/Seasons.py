seasons=['WINTER','SPRING','SUMMER','AUTUM']
season=0
T=[2,3,5,-5,-10,-15,10,14,]
group_count=len(T)//4
max_amp=0
s=-1
for part in range(0,len(T),group_count):
    print(f'T[{part}:{group_count}+{part}-1]')
    minimum = min(T[part:group_count+part-1])
    maximum = max(T[part:group_count+part-1])
    amp=maximum-minimum
    if max_amp < amp:
        max_amp=amp
    s=s+1


print('max_amp:',max_amp,'Seasons:',seasons[s])




