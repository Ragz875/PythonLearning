# hash table implementation with chaining example
class HashTable():
    def __init__(self,size):
        print(' Init HashTable invoked')
        self.size=size
        self.arr=[[] for i in range(self.size)]
        print(' HashTable is initialized with length:', len(self.arr), ' HashTable status', self.arr)

    # grouping chaining based on length of the key
    def get_hash_ind(self,key):
        return len(key) % self.size

    def insert_item(self,key,val):
        print('insert method called')
        h_ind=self.get_hash_ind(key)
        found=False
        # this loop is to check if there is a any key,val already present at the hash_index
        # if so replace it and mark as found
        for ind,key_val_set in enumerate(self.arr[h_ind]):
            print('ind,key_val_set:', ind,key_val_set)
            if key_val_set[0]==key : #and len(key_val_set)==2:
                self.arr[h_ind][ind]=(key,val)
                found=True
                break
        if not found:
#            print('in not found')
            self.arr[h_ind].append((key,val))

    def print_hash(self):
        for ind,ele in enumerate(self.arr):
            print(ind,':', ele)

    def delete_item(self,key):
        h_ind=self.get_hash_ind(key)
        del_flag=0
        for ind, set in enumerate(self.arr[h_ind]):
            if set[0]==key:
                #self.arr[h_ind].remove(set)
                del self.arr[h_ind][ind]
                del_flag=1
                break
        if del_flag:
            print('element ', set, 'removed')
        else:
            print('element not found')


ht=HashTable(5)
ht.insert_item('rag',111) # insert
ht.insert_item('rags',222) # insert
ht.insert_item('rag',1111) # append
ht.insert_item('raj',1111) # append
ht.insert_item('rajs',333) # append
ht.insert_item('raghu',333) # insert
ht.insert_item('ragh1',333) # append
ht.insert_item('ragh2',333) # append
ht.print_hash()


