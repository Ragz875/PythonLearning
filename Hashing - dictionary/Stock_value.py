def add(key,new_value):
    global min_value
    global max_value
    if len(dic)==0:
        min_value=new_value
        max_value=new_value
    else:
        if new_value > min_value:
            max_value=new_value
        else:
            min_value=new_value
    if key not in dic:
        dic[key]=new_value

def update(key,new_value):
    global min_value
    global max_value

    if new_value < min_value:
        min_value=new_value

    if new_value > max_value:
        max_value = new_value

    if key in dic:
        dic[key]=new_value

def delete(key):
    global min_value
    global max_value

    if len(dic) > 0:
        del_value=dic[key]

        if del_value < min_value:
            min_value=del_value
        if del_value > max_value:
            max_value = del_value
        del dic[key]

    if len(dic)==0:
        min_value,max_value=0,0

    if len(dic)==1:
        val=list(dic.values())[0]
        min_value,max_value=val,val

def min_dic():
    global min_value
    return min_value

def max_dic():
    global max_value
    return max_value

dic={}
min_value=0
max_value=0
add('time1',10)
add('time2',20)
add('time3',50)
print(dic, min_value,max_value)

update('time1',5)
update('time2',100)
print(dic, min_value,max_value)

delete('time1')
delete('time2')
print(dic, min_value,max_value)

print(min_dic(), max_dic())
delete('time3')
print(dic, min_value,max_value)

