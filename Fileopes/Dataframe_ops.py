"""
case1: add_list=[[1,'Mapbox, Inc.','50 Beale St., Floor 9','San Francisco, CA 94105'], \
          [2,'The President','1600 Pennsylvania Avenue','Washington, DC 20500'], \
          [3,'Mapbox, Inc.','50 Beale St., Floor 9','San Francisco, CA 94105'] ]
case2: dic={'av':'avenue',  'ave':'avenue', 'cir':'circle'}
add_list=
         [[1,'The President','1600 Pennsylvania Ave','Washington, DC 20500'], \
          [2,'The President','1600 Pennsylvania Avenue','Washington, DC 20500'], \
          [2,'The President','1600 PENNSYLVANIA AV','Washington, DC 20500'] 
          
          ]
"""
#add_list=[[1,'av','ab','ac'],[2,'av','cir','ac'],[3,'ave','bb','bc']]
import re
def formatlist(add_list):
    mod_list=[]
    temp_list=[]
    for i in range(len(add_list)):
        # add id to temp_list
        temp_list.append(add_list[i][0])
        # read each address until end of list
        for add_ele in add_list[i][1:]:
            # address formatting
            # print(add_ele)
            mod_str = ''
            for ele in add_ele.split():
                # print(ele)
                ele1=re.sub(r'[.|,|&]',r'',ele)
                if ele1.casefold() in dic:
                    # print(ele)
                    mod_str += ' ' + dic[ele1.casefold()]
                else:
                    mod_str += ' ' + ele1
                # print(mod_str)
            temp_list.append(mod_str.upper().strip())
            print(mod_str.upper().strip())
        mod_list.append(temp_list)
        temp_list = []
    mod_list1=[]
    for row in mod_list:
        mod_list1.append([row[0],' '.join(row[1:])])
    print('mod_list1:',mod_list1)

    return mod_list1

if __name__=='__main__':
    # ans: [1,11,3,4] [2] [12,13]
    add_list=[[1, 'Mapbox, Inc.','50 Beale St., Floor 9', 'San Francisco, CA 94105'], \
              [11, 'Mapbox, Inc.', '50 Beale St., Floor 9', 'San Francisco, CA 94105'], \
              [2, 'The President', '1600 Pennsylvania Avenue', 'Washington, DC 20500'], \
              [3, 'Mapbox, Inc.','50 Beale St., Floor 9', 'San Francisco, CA 94105'], \
              [4, 'Mapbox, Inc.','50 BEALE St., FLOOR 9', 'San Francisco, CA 94105'], \
              [12, 'Wilson Sonsini Goodrich & Rosati', '139 Townsend St, Suite 150', 'San Francisco, CA 94404'], \
              [13, 'Wilson Sonsini Goodrich & Rosati', '139 Townsend Street, Suite 150', 'San Francisco CA']]
    dic={'av':'avenue',  'ave':'avenue','cir':'circle','plz':'plaza', 'st':'street'}
         #,'st,':'street','ave.':'avenue','st.':'street',}

    print(add_list)
    mod_list1=formatlist(add_list)
    print('modified list:',mod_list1)
    i=0
    j=len(mod_list1)-1
    from fuzzywuzzy import fuzz
    final=[]
    i,j=0,0
    while i < len(mod_list1):
        jrow=[]
        j=0
        while j < len(mod_list1):
            #print(mod_list1[i][1],' vs ', mod_list1[j][1],fuzz.partial_ratio(mod_list1[i][1],mod_list1[j][1]))
            if i!=j and fuzz.partial_ratio(mod_list1[i][1],mod_list1[j][1])==100:
                print(mod_list1[j][0])
            #print(i,j)
            j=j+1
        i=i+1
    print(final)







