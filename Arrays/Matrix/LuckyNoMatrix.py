"""Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row
and maximum in its column.
Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]"""


class LuckyNoMatrix:
    def luckyNumbers(self,mat):
        min_row = [min(row) for row in mat]
        max_row=[]
        for row in zip(*mat):
            max_row.append(max(row))
        #return list(set(min_row) & set(max_row))
        return [i for i in min_row if i in max_row]
if __name__ == '__main__' :
    print('Main has started :')
    martices = [
                [[3, 7, 8], [9, 11, 13], [15, 16, 17]],
                [[1,10,4,2],[9,3,8,7],[15,16,17,12]],
                [[7,8],[1,2]]
                ]
    obj = LuckyNoMatrix()
    for mat in martices:
        print(mat, ':', obj.luckyNumbers(mat))