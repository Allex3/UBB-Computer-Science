% mathematical/rescursive models:

% candidate(l1l2...ln) =
% 1. l1, if L is not empty
% 2. candidate(l2...ln)

% list_sum(l1l2...ln) =
% { 0, if list is empty
% { l1 + list_sum(l2...ln), otherwise

% constraints(l1l2...ln) =
% { true, if l1+l2+...+ln % 2 = 1, length(L)%2=0, L not empty
% { false, otherwise

% arrangements(L, Col) =
% 1. Col, if constraints(Col) is true
% 2. arrangements(L, candidate(L)+Col)

% (i, i), (o, i) -  deterministic
candidate(E, [E|_]).
candidate(E, [_|T]):-
    candidate(E, T).

list_sum([], 0):-!.
list_sum([H|T], S):-
    list_sum(T, Saux),
    S is H+Saux.

constraints(L, Len):-
    M is Len mod 2,
    M == 0, % even number of elements
    list_sum(L, S), % if list empty sum 0 so false anyway
    MS is S mod 2,
    MS == 1. % odd sum

arrangements(_, R, R, Len):- % match R to Col
    constraints(R, Len). % if the constraints are met..
arrangements(L, Col, R, Len):-
    candidate(E, L),
    \+ candidate(E, Col), % E not a candidate already
    Len1 is Len+1,
    arrangements(L, [E|Col], R, Len1).

% main_pred(L, R) = arrangements(L, [], R, 0)
% (i) - non-deterministic
main_pred(L, R):-
    bagof(Raux, arrangements(L, [], Raux, 0), R).



