#question 04

test_list = [1, 2, 7, 5, 6, 3, 4, 8]
k = 3
print ("The list : " + str(test_list))
  
count = 0
for i in test_list :
    if i > k :
        count = (k + 1)
        
  
print ("The numbers greater than 3 : " + str(count))