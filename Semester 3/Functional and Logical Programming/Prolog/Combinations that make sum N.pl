% Consider a set of non-null natural numbers 
% represented as a list. Determine all the possibilities to write a 
% number N as a sum of elements from this list.
% (I will assume the numbers are unique or I go insane)

% recursive models:
% candidate(E, l1l2...ln) = 1. l1 if L not empty, 2. candidate(l2...ln)

% candidate(E: int, L: list) - generate a candiate from a list
% (o, i) - non-deterministic (can also be (i, i) - deterministic ehehe
candidate(E, [E|_]).
candidate(E, [_|T]):-
    candidate(E, T).

% permutations_aux(N: int, L: list, R: result list, 
% S: part of the sum towards N of L elements made of the candidate now
% LCol: collector list, will match to R at the end
% (i, i, o, i, i) - non-deterministic
permutations_aux(N, _, LCol, N, LCol). % when N=S we match LCol to R
permutations_aux(N, L, R, S, [H|T]):-
    candidate(E, L), % will return false if list empty, don't have to check that
    constraints(N, E, S, H),
  	S1 is S+E,
    permutations_aux(N, L, R, S1, [E, H|T]). % add E to LCol, E to Sum

% we have the following constraints to check: S+E <= N
% if E is member of LCol already, that's all I think
% constraints (N: int, E:int, S: int, H: head of LCol)
% (i, i, i, i) - deterministic
constraints(N, E, S, H):-
    (S+E) =< N,
    E < H. % check this so we add in increasing order
    % so that for example 2 3 for N=5 and 3 2 don't repeat
    % \+ member(E, [H|T]). % the above condition renders this useless

member(E, [E|_]):-!. % it is part of the list, don't go further, return true
member(E, [_|T]):-
    member(E, T).

% permutations(N, l1l2...ln) =
% 1. permutations_aux(N, L, E=candidate(L), E)
% permutations(N: int, L: list, R: result list),
% write N as a sum of elements from L
% (i, i, o) - non-deterministic backtracking
permutations(N, L, R):-
    candidate(E, L),
    permutations_aux(N, L, R, E, [E]).