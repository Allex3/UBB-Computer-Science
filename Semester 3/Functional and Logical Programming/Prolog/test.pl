% mathematical model:
% odd_count(l1l2...ln) =
%    0, if L is empty (base case)
%    odd_count(l2...ln), if l1 is an even number
%    1 + odd_count(l2...ln), if l1 is an odd number
%    odd_count(l1) + odd_count(l2...ln), if l2 is a list of numbers

% odd_count(L: list, R: int), R is the result
% (i, o), (i, i) - deterministic
odd_count([], 0):-!. % match empty list to 0 odd numbers
odd_count([H|T], R):- % H is an EVEN number
    number(H),
    Parity is H mod 2,
    Parity == 0, !, % do not check the other parity or it will return false
    odd_count(T, R).
odd_count([H|T], R):-
    number(H), % H is number, go deeper and R will be that count IF H is odd
    Parity is H mod 2,
    Parity == 1, !, % otherwise it will return false when checking if its a list
    odd_count(T, Raux),
    R is Raux +1.
odd_count([H|T], R):-
    is_list(H), % H is a list, just run odd_count on it, and that result is added to the deeper result of odd_count of our list
    odd_count(H, Hcount),
    odd_count(T, Raux), % as above, get the remaining odd count
    R is Raux+Hcount. % as above, but instead of 1 we add the count of odd numbers in the list H

