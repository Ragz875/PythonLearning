class TimeMap:
    def __init__(self):
        self.dic={}

    def set(self, key, val, timestamp):
        print('set')
        if key not in self.dic:
            self.dic[key]=[(timestamp,val)]
        else:
            self.dic[key].append((timestamp,val))

    def get(self, key, timestamp) :
        print(f'key :{key} , timestamp : {timestamp}')
        if key not in self.dic:
            return ''


        for i in range(len(self.dic[key])-1,-1,-1):
            time, val = self.dic[key][i]
            print(time,val)
            if time <=timestamp :
                return val

    def display(self):
        for key,value in self.dic.items():
            print(key,value)


if __name__=='__main__' :
    t=TimeMap()
    t.set('11','aa',1)
    t.set('11', 'aaa', 10)
    t.set('22','bb', 2)
    t.set('22', 'bbb', 20)
    t.set('33','cc', 3)
    t.display()
    print(t.get('11',10))
    print(t.get('22',30))