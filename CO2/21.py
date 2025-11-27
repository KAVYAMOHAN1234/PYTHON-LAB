def modifyList(lst):
    lst.append(10)
    print("inside function:",lst)
numbers=[1,2,3]
modifyList(numbers)
print("outside function:", numbers)
