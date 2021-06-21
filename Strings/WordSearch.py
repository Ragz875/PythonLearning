def dirsearch(grid,row,col,word,dir):
    if word[0] != grid[row][col]:
        return False
# loop trough all directions
    for x,y in dir:
        #print(f'    Direction search {x},{y}')
        flag=True
        rowd= row + x
        cold= col + y
#        print(f'    Direction search {rowd},{cold}')
    # loop through all characters , first char already taken care
        for charind in range(1,len(word)):
            if ( 0 <= rowd < len(grid) and
                    0 <= cold < len(grid[0]) \
                        and grid[rowd][cold] == word[charind]):
                rowd+=x
                cold+=y
                #print('Char : ', word[char], 'Location :', rowd,' ' ,cold, 'len(grid) :',len(grid),'len(grid[0]) :',len(grid[0]))
            else:
                flag=False
                break
    # after all 8 direct search check the flag
        if flag:
            return True
    return False


def patternsearch(grid,word,dir):
    print('in Pattern search')

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if dirsearch(grid,row,col,word,dir):
                print(f'Word : {word} found at location :',row ,' ' ,col)
#    print('called seperate',dirsearch(grid, row, col, word, dir))

if __name__=='__main__' :
    dir=[[-1,0],[1,0],[1,1],[1,-1],[-1,-1],[-1,1],[0,1],[0,-1]]
    print('Your Main starts here')
    grid = ["GEEKSFORGEEKS","GEEKSQUIZGEEK","IDEQAPRACTICE"]
    word='GEEKS'
    patternsearch(grid,word,dir)







