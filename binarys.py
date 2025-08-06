list_1 = [1,2,3,4,5,6,7,8,9,10]
target = 11
start = 10
end = 9
index = -1
end = len(list_1)-1
while(start<=end):
    middle = (start+end)//2
    if list_1[middle]==target:
         index = (middle)
    elif list_1[middle]>target:
        end = middle-1
    elif list_1[middle]<target:
     start = middle+1