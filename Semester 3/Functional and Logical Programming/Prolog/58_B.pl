% B. Given a linear list of numbers, write a SWI-Prolog program
%  that replaces every sequence of
% consecutive equal numbers with the sum of the sequence.
%  This process must be repeated until there
% are no consecutive equal elements in the list.
%
%  For example, for the list [1, 2 , 1, 1, 4, 5, 6, 7, 7, 7, 3
% 3, 3, 3, 3, 3, 3, 10], the result will be [1, 8, 5, 6, 42, 10].

% mathematical models:
% replaceEqual(l1l2...ln) =
%    { [], if L is empty
%    { l1 oplus replaceEqual(l2...ln), if l1 != l2
%    { sum(l1+l2+...+li) oplus replaceEqual(l(i+1)...ln), if l1=...=li

% sum_while_equal(l1l2...ln) =
%    { 0, if L is empty
%    { l1, if l1 != l2 (count it still, it was equal until here)
%    and even if it was not equal.. doesn't matter, we count it
%    even if it's single, like 1 2 3 , get 1
%    because in the above function this will never happen
%    but it respects the definition
%    { l1 + sum_while_equal(l2...ln), if l1 = l2

% count_equal(l1l2...ln) =
%    { 1 + count_equal(l2...ln), if l1 = l2)
%    { 1, if l1 != l2
%    {0, if L is empty


% replaceEqual(L: list, R: list); (i, o), (o, i), (i, i) - deterministic
% (o, o) - non-deterministic
% sum_while_equal(L: list, R: integer, Index: integer);
% (i, i, o), (i, o, o), (i, i, i), (i, i, o) - deterministic;
% (o, i, i), (o, i, o), (o, o, o), (o,o,i) - non-deterministic

sum_while_equal([], 0, 0):-!. % 0 if the list is empty
sum_while_equal([H1, H2|_], H1, 1):- % H1 if H1 != H2
    H1 =\= H2, !.
sum_while_equal([H|T], R, C):-
    % it didn't stop above, just sum
    sum_while_equal(T, Raux, Caux), % sum recursively the rest
    R is H+Raux,
    C is 1+Caux.


replaceEqual([_| T], R, C):-
    C > 0, !, % C > 0, decrement it
    Cnew is C-1,
    replaceEqual(T, R, Cnew). % if C > 0 basically keep doing this
replaceEqual([], [], _):-!. % L is empty, return empty list
replaceEqual([H1, H2|T], [HR|TR], _):-
    H1 =\= H2, !, % do not try the other way if they're not equal
    HR is H1,
    replaceEqual([H2|T], TR, 0).
replaceEqual( [H1, H2, H3|T], [HR|TR], _):-
    H1 == H2, !,
    sum_while_equal([H1, H2, H3|T], HR, CC), % sum all the equal ones into HR
    % now I need another function to COUNT the equal ones
    % and basically SKIP that many after H1
    % just get it in sum_while_equal...
    replaceEqual([H1, H2, H3|T], TR, CC).
replaceEqual([H], [H], _). % if the list is not empty
% but it has a single element, so cannot compare

% math model: has_consecutive_numbers(l1l2...ln) =
% { true, if l1 = l2
% { has_consecutive_numbers(l2...ln), if l1 != l2
% { false, if L is empty

has_consecutive_numbers([H1, H2|_]):-
    H1 == H2, !. % true
has_consecutive_numbers([_|T]):-
    has_consecutive_numbers(T).

% mathematical model: replace_equal(L) =
%  { replaceEqual(L)
replace_equal(L, R):-
    has_consecutive_numbers(L), !,
    replaceEqual(L, Raux, 0),
    replace_equal(Raux, R). % AGAIN, because it HAD conseucitve numbers
replace_equal(L, L):-!. % no consecutive numbers




