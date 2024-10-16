# Search and Sort console menu program
# 1 - Generate a list of random numbers - The user chooses the length of the list
#       (numbers from 0-1000)
#       print the list after generated
#       only use the list generated at option 1
# 2 - search
# 3 - sort 1
# 4 - sort 2
# 5 - Exit
# --------
# Choose option
# (have option to display menu, or display it everytime, organize the menu however)
# if use other than 1 without a list display an empty list or a message
# searching is done in a sorted list, so first sort the list
#   So after you generate the list and the user chooses search without sorting
#   Make the user sort the list first (MAKE SURE THE LIST IS SORTED BEFORE SEARCHING)


#Code a visualisation of the sorting algorithm
#   Show the list at intermediary steps in the console, depending on the algorithm
#   (For example, a swap of elements is a step, or in a mergesort a merge is a step, etc.)
#   DO NOT display all the intermediary steps
#       Let the user decide how many steps they want to see
#        If the user chooses 3, display every THIRD step, etc.
#EXAMPLE:
#   Number of steps: 4
#   Unsorted list: [..]
#   Step 4: [...]
#   Step 8: [...]
#   .....
#   Sortedlist(step 9): [...]

#Implement each algorithm in a separate function
# Each function has 2 params:
#   search(list, number you look for)
#   sort(list, number of steps)

#No global vars

#My algorithms to implement:
#   binary search recursive version
#   permutation sort
#   shell sort