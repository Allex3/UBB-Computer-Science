% permutations 1 ... N
% having the property that the absolute value of the difference between
% 2 consecutive values from the permutation is >=2

% candidate(N) =
% 1. N, if N > 0
% 2. candidate(N-1), if N > 1

% mymember(E, l1l2...ln) =
% { false, if L is empty
% { true, if l1 = E
% { mymember(E, l2...ln)

% constraints(A, B, Len, N) = (check constraints when adding a new
% number)
% { true, if abs(A-B) >= 2  AND Len <= K
% { false, otherwise

% permutations_aux(N, Len, Col) =
% 1. Col, if N = Len ( all constraints achieved until here)
% 2. permutations_aux(N, Len, candidate(N) + col), if constraints(first
% element of col and candidate(N))

% permutations(N) = permutations_aux(N, 1, [candidate(N)])

% candidate(E: int, N: int)
% (o, i) - non-deterministic, (i, i), (i, o),(o,o)- deterministic
candidate(E, E). % E = N
candidate(E, N):-
    N > 1,
    N1 is N-1,
    candidate(E, N1).

% mymember(E: int, L: list)
% (i, i) -det., (o, i) - non-det.
mymember(E, [E|_]).
mymember(E, [_|T]):-
    mymember(E,T).

% constraints(A: int, B:int, Len: int, N:int)
% ( i, i, i, i) - deterministic
constraints(A, B, Len, N):-
    M is abs(A-B),
    M >= 2,
    Len =< N.

% permutations_aux(N: int, Len: int, Col: list, R:list)
% (i, i, i, o) - non-deterministic
permutations_aux(N, N, R, R). % match R to Col, when N=Len
permutations_aux(N, Len, [H|T], R):-
    candidate(E, N),
    \+ mymember(E, [H|T]),
    Len1 is Len+1,
    constraints(E, H, Len1, N),
    permutations_aux(N, Len1, [E, H|T], R).

% permutations(N: int, R: list)
% (i, o) - deterministic
permutations(N, R):-
    candidate(E, N),
    permutations_aux(N, 1, [E], R).


% main_pred(N) = permutations(N)
main_pred_c(N, R):-
    bagof(Raux, permutations(N, Raux), R).
