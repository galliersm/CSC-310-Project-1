# CSC-310-Project-1
Implementation of a postfix expression evaluator and the Radix Sort algorithm

## Overview
Both of these programs are part of an assignment given in my data structures course, CSC 310. These programs make use
of data structures we have recently been covering, namely Stacks and Queues. Throughout this project you will find a
clear understanding of these basic data structures as well as cleanly written and heavily commented code.

### Radix Sort
This program is an implementation of the Radix Sort algorithm; a counting based sorting algorithm that uses the queue
data structure to sort a list of positive integers.

#### How it Works
My implementation of the Radix Sort algorithm uses an inherited and modified version of a basic queue ADT. This 
modified queue class includes a counter used to determine when all numbers from a previous intermediate sort have been
processed. The Radix Sort algorithm itself is implemented as a class. On init, it creates a list of 10 queues that it
can use for each sorting request.

The sorting process is handled by a method. The method starts by initializing some 
tracking/accumulator variables, enqueueing all list variables into the queue with index "0", and setting the queue's 
remaining attribute to the number of items.

Then, the method will perform sorting operations on a specific number's 
place, moving from right to left (i.e. ones, tens, hundreds, etc.) until none of the numbers being sorted have a 
digit at the number place being processed. When this occurs, all numbers will be in the queue of index "0" again, but
this time will be fully sorted.

For each number's place being sorted, the algorithm will loop through each of the 10 queues, de-queueing and 
processing each remaining number from the previous iteration of the same loop. When processing a number, the method 
extracts the digit of the number's place being processed and the places the number in the queue having an index 
matching the digit just extracted. This repeated process of sorting numbers based on a digit's place in increasing 
significance is the core of how the Radix Sort algorithm works.

Finally, after the current digit's place being evaluated has exceeded any number in the list, all numbers are sorted 
and in the queue of index "0". Then all numbers are de-queued and placed back into the list in non-decreasing order. 
The list object is then returned and the method is complete.

A user menu is included for ease of use and testing.

### Postfix Evaluator
This program is a simple postfix (or RPN) notation evaluator. It works by using a stack ADT to track the results of 
broken up operations done on numbers. It is assumed that all numbers in expressions are single digit numbers.

#### How it Works
The postfix evaluator was also implemented using a class as a way of organizing the components of the project. For 
evaluating operators in the expression, a dictionary of keys of the four compatible operators ('*', '/', '+', '-') 
and values of imported functions that can evaluate each operator is included. Upon instantiation, the class creates 
a stack attribute to be used in the evaluation method.

The evaluation method starts by iterating over each character in the given expression from beginning to end, ignoring 
whitespace. If it encounters a number it is pushed to the stack. If it encounters an operator, it pops the last two
numbers off the stack in reverse order, i.e. second number is first one popped off and first is second popped off and
saves them. Then it calls one of the aforementioned operator dictionary methods based on the specific operator. The 
result is obtained and then pushed onto the stack.

After processing each character, the only number on the stack is the result. It is popped and returned.

A user menu is included for ease of testing.