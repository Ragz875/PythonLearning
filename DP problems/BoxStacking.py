#Given N boxes [(L1,W1,H1),(L2,W2,H2)..(Ln,Wn,Hn)] where box i has length Li , width Wi and height Hi
# find the tallest possible stack. Box(Li, Wi, Hi) can be on top of box (Lj, Wj, Hj) if Li < Lj , Wi < Wj
#Example : [(2,3,3),(2,2,4),(4,4,2)] ans: max height 6 [(4,4,2), (2,2,4)]
# Example2: [(1,5,4),(1,2,2),(2,3,2),(2,4,1),(3,6,2),(4,5,3)]

def tallestStack(boxes):
    print('before:', boxes)
    # sort the boxes in ascending order of its length
    boxes.sort(key=lambda x:x[0])
    print('After:', boxes)
    # keep all the heights in dictionary
    for box in boxes:   print(box)
    heights={box:box[2] for box in boxes}
    print(heights)

    for i in range(1,len(boxes)):
        box=boxes[i]
        S=[boxes[j] for j in range(i) if canBeStacked(boxes[j],box)]
        print(S)
        # adding current box height + all its previous boxes height , maintaining height at all
        # sub problems
        heights[box]=box[2]+max([heights[box] for box in S],default=0)
    print(heights)
        # select max height out of all sub problems height
    return max(heights.values(),default=0)
def canBeStacked(top,bottom):
    return top[0] < bottom[0] and top[1] < bottom[1]

if __name__=='__main__':
    print('main started')
    arr=[(1,2,2),(2,3,2),(2,4,1),(3,6,2),(4,5,3),(1,5,4)]
    arr=[(2,3,3),(2,2,4),(4,4,2)]
    print(tallestStack(arr))