% all subsets of elements of a distinct integer elements list
% in strictly ascending order

% recursive models:
% candidate(E, l1l2...ln) = 1. l1 if L not empty, 2. candidate(l2...ln)

% candidate(E: int, L: list) - generate a candiate from a list
% (o, i) - non-deterministic (can also be (i, i) - deterministic ehehe
candidate(E, [E|_]).
candidate(E, [_|T]):-
    candidate(E, T).

% strascsubsets_aux(L: list, R: result list, LCol
% LCol: collector list, will match to R at the end
% (i, o, i) - non-deterministic
strascsubsets_aux(_, LCol, LCol). % match LCol to R every time
strascsubsets_aux(L, R, [H|T]):-
    candidate(E, L), % will return false if list empty, don't have to check that
    E < H, % elements in strictly ascending order
    strascsubsets_aux(L, R, [E, H|T]). % add E to LCol, E to Sum

strascsubsets(L, R):-
    candidate(E, L),
    strascsubsets_aux(L, R, [E]).