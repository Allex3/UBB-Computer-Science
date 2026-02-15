% a. Replace all occurrences of an element from a list with another element e.
% b. For a heterogeneous list, formed from integer numbers and list of numbers,
% define a predicate to determine the maximum number of the list,
% and then to replace this value in sublists with the maximum value of sublist.
% Eg.: [1, [2, 5, 7], 4, 5, [1, 4], 3, [1, 3, 5, 8, 5, 4], 5, [5, 9, 1], 2] =>
% [1, [2, 7, 7], 4, 5, [1, 4], 3, [1, 3, 8, 8, 8, 4], 5, [9, 9, 1], 2]

% a) mathematical model:
% replace(l1l2...ln, E, R) = 
% 	[], 				if L is empty
% 	R + l2...ln, 		if l1 = E
%	replace(l2...ln),   otherwise
% predicate: replace(L: list, E: element, R: element, Res: list) ??
% (i, i, i, o), (i, o, i, i), (i, i, o, i), (o, i, i, i), (i, o, o, i) - deterministic
replace([], _, _, []):-!. % map TR to an empty set, otherwise it's a list there or_
replace([H|T], E, R, [HR|TR]):-
    H == E,
    !, % it is useless to test the other one
    HR is R,
    replace(T, E, R, TR).
replace([H|T], E, R, [HR|TR]):-
    H \== E,
    !,
    HR is H,
    replace(T, E, R, TR).
    
% b, the maximum number is NOT in a list, only by itself, a number
% after finding that, we replace it in each integer sub-list

% find_max(L: list, M: int) - find max M in a list of ints and sublists of ints
% mathematical model: find_max(l1l2...ln) = 
% 	-999, if list is empty
%	l1, if l1 is an integer and its greater than the current maximum M
%	find_max(l2...ln), if l1 is a sublist of integers OR l1 <= M
find_max([], M):- M is -999,!. % match M to -999
find_max([H|T], Max):-
    is_list(H),
    find_max(T, Max). % do nothing to a list
find_max([H|T], Max):-
    find_max(T, Max),
    \+ is_list(H), 
    H =< Max,!. % to return true if Max doesn't change
find_max([H|T], H):- % H 
    find_max(T, Max), % first go to set the Max at the deepest level
    \+ is_list(H), % not a sublist
    H > Max, !.

% replace_max_impl(L: list, Res: List)
% mathematical model: replace_max_impl(l1l2...ln) = 
% 	replace_max_impl(l2...ln), if l1 is an integer (do nothing)
% 	replace(l1, find_max(l1), Max) + l2...ln, if l1 is a sublist of integers
replace_max_impl([], [], _):-!.
replace_max_impl([H|T], [HR|TR], Max):-
    integer(H), !,
    HR is H,
    replace_max_impl(T, TR, Max).
replace_max_impl([H|T], [HR|TR], Max):-
    is_list(H),
    find_max(H, LocalMax), %localMax is the max in the sublist
    replace(H, Max, LocalMax, HR), %replace global max with local max in H
    % HR is ResAux, % if above in replace() we put ResAux instead of HR 
    % this will NOT WROK!!!
    replace_max_impl(T, TR, Max). % go forward to replace the rest
% replace_max(L: list, Res: List)
% mathematical model: replace_max(l1l2...ln) =
% 	replace_max_impl(l1l2...ln, find_max(l1l2...ln))
% (i, o) - deterministic
replace_max(L, Res):-
    find_max(L, Max),
    replace_max_impl(L, Res, Max).