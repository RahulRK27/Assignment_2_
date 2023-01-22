def last(lst):
    return lst[-1]
def sort(lst):
    return sorted(lst,key=last)
lst = [(2,5),(1,2),(4,4),(2,3),(2,1)]
print("sorted")
print(sort(lst))
