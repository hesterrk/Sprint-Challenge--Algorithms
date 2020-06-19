#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is 0(n) because of the single while loop. The number of operations scale with input, the number of 'n' determines the number of while loops that have to be run. For example with n = 2 it runs 2 operations, with n = 4 it runs four operations.


b) The sum statement is 0(1). The for loop is 0(n) as the number of operations increases with the size of the 'n' input (each bigger input, more loops). Because it has a nested while loop, which halves the operations, as each time the input of n increases, j's number doubles each time the loop runs, so it reaches the condition to stop the while loop quicker. So this part is 0(logn). The sum+=1 statement is 0(1) as its always going to do one operation no matter what the 'n' input is.
Overall its a 0(n) * log(n) --> 0(nlogn)


c) The 'if' condition is 0(1). The function is called recursively 'bunnies' times until it reaches base case. Increasing the input also increases the operations aka the number of function calls but at the same rate. 
Overall it's 0(n). 



## Exercise II

--> The first idea is to use a binary search.  
--> We are talking about 'n' floors, which would be the length of our list 
--> Each index in our list is assigned as 'f'
--> We find where the 'f' where no eggs break when thrown off 
--> We assign the start of the list (bottom floor) a 'low' pointer and the end of the list a 'high' pointer(top floor)
--> To do this, we halve our list (n) to work out the middle index of 'n' (halving the sum of our high and low pointers) We then check at this specific index which is our middle floor whether the egg breaks. 
--> If they do can focus on the left side of our list, as it means our middle index floor is too high. We focus on the lower floors half of the list. We re-calculate the high pointer so it points at one below the middle index. Our low pointer stays at the start of the list. We then reculate our middle index so it becomes the floor halfway between the low and new high pointer. We test again whether the egg breaks, if it does, repeat the same process, until we find a floor where the egg does not break and return this index of 'f'. 

--> Alternatively, if the egg doesnt break at the initial calculated middle index, then we can recalculate our search by focusing on the right side(higher floors), adjust the middle index so its one after its current index, and test whether the egg breaks at this new calculated floor. If not, repeat, until you find optimal floor where it doesnt break.

--> The big 0 would be worst-case 0(logn) as input size increases we are halving the operations each time. 
