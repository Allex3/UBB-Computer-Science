input - string
print
list -> .append, .pop, .pop(index); len(list)

for element in iterable
	for i in range(len(list))
	reverse order: 
		for i in range(len(list)-1, -1, -1)
		for i in range(1, len(list)+1) (from 1 to len(list)):
			but work with list[-i]
for number in range()
	range(5) = 0, 1, 2, 3, 4; range(5, 10) = 5, 6, 7, 8, 9;
	range(8, 2, -2) ->8, 6, 4; range(2, 7, 2) -> 2, 4, 6


basic types are mutable
containers (list, dictionary, map) are IMmutable

First assignment:
	for each file (p1, p2, p3 representing a problem set)
	have atleast 1 function 
	make user understand app (user-friendly input and output)
	user interaction SEPARATED from the function that calculates stuff
	DON'T use global variables

		def isPrime(...):
			....
			
		def func(...):
			..... calculates stuff
			...
		user interaction (outside of function)
	DON'T use global variables

