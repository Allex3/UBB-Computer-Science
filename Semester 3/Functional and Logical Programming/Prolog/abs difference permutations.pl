% Given two natural values n (n> 2) and v (v nonzero),
% a Prolog predicate is required which returns the 
% permutations of the elements 1, 2 ...., n with the property that 
% any two consecutive elements have the difference in absolute 
% value greater than or equal to v.

candidate(N, N). % bound E to N
candidate(N, E):-
    N>1,
    N1 is N-1, % permutations, so go to n-1
    candidate(N1, E).

%permutations
% (i, i, o) - non-deterministic, backtracking
permutations(N, V, L):-
    candidate(N, E), 
    permutations_aux(N, V, L, 1, [E]).
    
    
%permutations_aux (N: int, V:int, L: output list,
%length: current result length,
% LCollectors: collects the element of the permutations   
% Stops when Lcollectors is of N length (cuz permutations
% (i, i, o, i, i) - non-deterministic
permutations_aux(N, _, Col, N, Col):-!. % match LRes to LCollectors
permutations_aux(N, V, LRes, Length, [H|T]):-
    candidate(N, E), % choose another candidate
    constraints(N, V, Length, E, H, [H|T]),
	L1 is Length+1,
	permutations_aux(N, V, LRes, L1, [E, H|T]).
        
member(E, [E|_]):-!. % true if E is part of the list we got to
member(E, [_|T]):-
    member(E, T). % each the next element

% constraints(N: int, V:int, length: int, ENew: int, HRes, LCollectors: list)
% (i,i, i, i, i, i) - deterministic
% checks for constraints if we can continue generating a permutation
% from there parameters: length < N, |E-H| >=V (the others are checked
% already since we check each when we add...)
% then if E is member of the list already
constraints(_, V, _, ENew, HRes, LCol):-
    % Len < N, % no need to check for this, because when Len = n
    % it will basically return with cut from permutations_aux
    abs(HRes-ENew) >= V,
    \+ member(ENew, LCol). % (i, i)
