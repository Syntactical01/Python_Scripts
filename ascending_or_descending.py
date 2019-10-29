# Determine if a list is ascending, descending or neither O(n) time in O(1) memory.

import operator
def determine_ordering(lst):
    if len(lst) <= 1:
        return None

    if lst[1] > lst[0]:
        operator_to_use = operator.lt
    elif lst[1] < lst[0]:
        operator_to_use = operator.gt
    else:
        return None
      
    for index in range(1, len(lst)):
        if not operator_to_use(lst[index - 1], lst[index]):
            return None

    return 'descending' operator_to_use is operator.gt else 'ascending'
    

test_cases = [
  [1,2,3,4],
  [4,3,2,1],
  [1,3,2,4]
]
for x in test_cases:
    print(determine_ordering(x))
