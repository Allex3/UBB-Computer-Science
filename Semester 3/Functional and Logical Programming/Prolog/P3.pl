% (o, i) - non-deterministic
candidate(E, [E|_]). % take E
candidate(E, [_|T]):- % don't take E
	candidate(E, T).

% (i, o), (i, i) - deterministic
get_xes([], 0). % base condition
get_xes([H|T], Xes):-
    get_xes(T, Xesaux),
    H == "X",!, % if H is X, count Xes
    Xes is Xesaux+1.
get_xes([H|T], Xes):-
    get_xes(T, Xesaux),
    \+ H == "X", !,
    Xes is Xesaux. % don't increment it

% (o, i) - non-deterministic (N = number of games)
predictions(R, N):-
    candidate(E, [1,2,"X"]),
    get_xes([E],Xes),
    predictions_aux([E], N, 1, Xes, R). % Col will be placed in R

% predictions_aux(Col: list, N: int, Len: int, Xes: int, R: list)
% (i, i, i, i, o) - non-deterministic
predictions_aux(Col, N, N, _, Col):- % matches R to Col, when Length = N games
    !,final(Col). % verify the final conditions
predictions_aux([H|T], N, Len, Xes, R):-
    candidate(E, [1,2,"X"]),
    constraints(E, N, Len, Xes), % if E passes constraints add it to Col
    get_xes([E, H|T], Xes1), % get the new number of Xes
    Len1 is Len+1,
    predictions_aux([E, H|T], N, Len1, Xes1, R).

% constraints(E: list, N: int, Len: int, Xes: int)
% (i, i, i, i) - deterministic
constraints(E, N, Len, Xes):-
    Len < N,
    E == "X", !, % if E is X, there has to be <2 Xes; ! = check only this pred.
    Xes < 2.
constraints(E, N ,Len, _):-
    Len < N,
    E =\= "X". % if E is NOT x, Xes don't matter

% (i) - deterministic, true only if at the end of the list there is 1 or x
final([1]).
final(["X"]).
final([_|T]):-
    final(T).
