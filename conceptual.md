### Conceptual Exercises

__What is Big O Notation?__  
  Big O notation is representation of time and space complexity, or a mathematical analysis of how time and space increase as input size increases.  
  
__What is the call stack?__  
  The call stack is how execution context is kept track of. When a function is called, its execution context is placed on the stack and is removed from the stack when the function returns.
  
__What is a base case?__  
  A base case is a condition that, when reached, will not recurse. When using recursion, a base case is what prevents infinite recursion.
  
__What is the difference between time and space complexity?__  
  Time complexity is the number of operations that are required as an input size gets larger. Space complexity is the amount of memory that is required as an input size gets larger.
  
__What are some advantages/disadvantages to using Linked Lists versus arrays?__  
  Advantages to linked lists versus arrays include insertion and shifting. Disadvantages to linked lists versus arrays include lookup by index.

__What is the difference between a tree and a graph?__  
  A tree has a root node and is not cyclical. A graph does not have a root node and can cyclical.
  
__What is the difference between a binary search tree and binary tree?__  
  A binary search tree and binary tree both require that nodes have 0, 1, or 2 children only, but a binary search tree requires that a node must have a left child with a value less than it and a right child with a value greater than it (a binary search tree is order left to right).

__What are graphs used for?__  
  Graphs are used to model networks. They are used in social networks and maps.
  
__What are trees used for?__  
  Trees are used to model hierarchies, sorted data, or searchable data.
  
__What are linked lists used for?__  
  Linked lists are used when the limitations of arrays add complexity to a solution. Use cases include queues and priority queues, where insert and shifting are important but lookup is not.
  
__What is a stack? Where and how are they used?__  
  A stack is a data stucture that follows FILO (First in last out) rules. A stack can only be pushed to or popped from.
  
__What is a queue? Where and how are they used?__  
  A queue is a data structure that follow FIFO (first in first out) rules. A queue can only be enqueued to and dequeued from.
  
__What is an adjacency list?__  
  An adjacency list is a list of nodes that are adjacent to the node in question.
  
__What is an adjacency matrix?__  
  An adjacency matrix is a 2D list that represents the connections of nodes. It works like a lookup table.

__Explain conceptually how BFS in a graph works__  
  BFS (breadth first search) will exhaustively search each rank before progressing to children.

__Explain conceptually how DFS in a graph works__  
  DFS (depth first search) will exhastively search all children before progressing to siblings in each rank.
  

### Algorithm Design
  
  
__How would you build a system that stores and manages the hierarchy of an organization.__  
  Build an n-ary tree that represents each member of the organization. The root node will be the highest ranking officer, and the children will be the people supervised or managed by that person.

__Build the functionality to allow for undo and redo. Think of this feature like what you’ve used in a text editor or word processor.__  
  Using a stack, store previous changes in an undo stack. As a user uses the _undo_ feature pop a previous change from the undo stack and push it to a redo stack. If a user uses the _redo_ feature pop from the redo stack and push to the undo stack.


__If you were building a game of Snake, what would be an optimal data structure for the snake?__  
  A stack could be used to represent the snake. Segments need to be added to the end of the snake, but they never will need to be inserted or looked up.

__Write a system that accepts a string of HTML and validates it.__  
  Using a stack we can check that the HTML is balanced (all open tags are closed) by pushing to a stack when an open tag is found and popping when a closed tag is reached until the previous open tag is found. If the end is reached and the stack is not empty, the HTML is not balanced.

__A numeric array of length N is given. We need to design a function that finds all positive numbers in the array that have their opposites (a number that when added results in 0) as well.__  
  Using a hash table a frequency counter can be made to do lookups. If a number is found, it's opposite is looked up. If an opposite is found, the positive number is pushed to an array

__Build a game of tug of war. You should be able to add players to both teams.__  
  Using two arrays a new player can be added by pushing to the array. The array with a larger sum wins.

__You’re building the system at McDonalds for managing your order.__  
  A priority queue can be used to enqueue orders that need to be made. Another queue can be used to hold orders that are completed but are pending being picked up by the customer. These can be dequeued when a customer picks up their order.

__Design a simple calculator that can handle addition, subtraction, multiplication and division.__  
  Start pushing each character in the string to a stack, ignoring whitespace. Whenever an arithmetic operator is reached, the following item is evaluated with the previous and added to an accumulator. If the following item is a parenthesis, then continue pushing to the stack until a closed parenthesis is found. At that point, start popping from the stack evaluating each pair of values with the operator in between them and added to an accumulator.  __REFACTOR THIS, IT WILL NOT HANDLE PEMDAS__

__Build a game of Rock paper scissors. How could you build a system that scales to hundreds of option options (Spock, Lizard, fire, water, etc.)__  
  Using a directional graph we can create a network of what beats what. By looking at the adjacency list or matrix, it can be determined which option wins.  
  _rock -> scissors_  
  _scissors -> paper_  
  _paper -> rock_  

__You need to design a system that can schedule tasks at different times.__  


__Now that you have designed the scheduler, a number of the tasks need to wait for some -her tasks to complete prior to running themselves. How would this change your system?__  


__Merge k sorted arrays, Given k sorted arrays of size n each, merge them and print the sorted output.__  


__Given a map of the United States, and N number of colors, figure out all the ways each -ate can be colored as long as no two bordering states have the same color.__  


__Given a chessboard of N*N, how many different ways can you arrange the board so that N number of queens can be placed without attacking each other vertically, horizontally or diagonally.__  


__Design the pseudocode for a Minesweeper game__  


__Design a game of battleship, how would you lay out the board?__  


__Create a system that allows for scheduling events on a calendar for available dates.__  



