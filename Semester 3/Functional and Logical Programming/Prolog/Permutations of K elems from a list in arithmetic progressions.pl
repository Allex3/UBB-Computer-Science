% List with distinct integer elements is given
% Generate all subsets with k elements in  arithmetic progression
% (basically the ratio between each two consecutive elements should stay
% the same), like l2-l1 = l3-l2 = ... = ln-l_{n-1}

% recursive models:
% candidate(E, l1l2...ln) = 1. l1 if L not empty, 2. candidate(l2...ln)

% candidate(E: int, L: list) - generate a candiate from a list
% for the airthmetic progression we need two candidates tho
% so call this function two times, check if the elements are distinct
% and get their ratio, and continue with them, these are A1 and A2
candidate(E, [E|_]).
candidate(E, [_|T]):-
    candidate(E, T).

% arithmeticprog_aux(L: list, K: int R: result list,
% Ratio: ratio for arithm prog., Length (<K, until K, will match at the end)
% LCol: collector list, will match to R at the end
% (i, i, o, i, i, i) - non-deterministic
arithmeticprog_aux(_, K, LCol, _, K, LCol). % match R to LCol when Length=K
arithmeticprog_aux(L, K, R, Ratio, Length, [H|T]):-
    candidate(E, L), % will return false if list empty, don't have to check that
    constraints(Length, K, Ratio, E, [H|T]),
    L1 is Length+1,
    arithmeticprog_aux(L, K, R, Ratio, L1, [E, H|T]). % add E to LCol, E to Sum

% our constraints: H-E = Ratio (ratio defined in main predicate from first two elems)
% E is NOT already a member of LCol, Length < K, so define it as such:
% constraints(Length: int, K: int, Ratio: int, E: int, LCol: list of col.)
% (i, i, i, i, i) - determinisitc
constraints(Length, K, Ratio, E, [H|T]):-
    Length < K,
    R1 is E-H,
    R1 == Ratio,
    \+ member(E, [H|T]).

% member(E: int, L: list), (i, i) - deterministic, (i, o) - det. i think
member(E, [E|_]):-!. % return from here
member(E, [_| T]):-
	member(E, T).

arithmeticprog(L, K, R):-
    K>1, % cannot do anything if K<=1
    candidate(E1, L),
    candidate(E2, L),
    E1 \== E2,
    Ratio is E2 - E1,
    % will generate in invese order: An...A2 A1
    arithmeticprog_aux(L, K, R, Ratio, 2, [E2, E1]).