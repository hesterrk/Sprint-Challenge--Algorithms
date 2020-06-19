#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is 0(n) because of the single while loop. The number of operations scale with input, the number of 'n' determines the number of while loops that have to be run. For example with n = 2 it runs 2 operations, with n = 4 it runs four operations.


b) The sum statement is 0(1). The for loop is 0(n) as the number of operations increases with the size of the 'n' input (each bigger input, more loops). Because it has a nested while loop, which halves the operations, as each time the input of n increases, j's number doubles each time the loop runs, so it reaches the condition to stop the while loop quicker. So this part is 0(logn). The sum+=1 statement is 0(1) as its always going to do one operation no matter what the 'n' input is.
Overall its a 0(n) * log(n) --> 0(nlogn)


c) The 'if' condition is 0(1). The function is called recursively 'bunnies' times until it reaches base case. Increasing the input also increases the operations aka the number of function calls but at the same rate. 
Overall it's 0(n). 






## Exercise II


