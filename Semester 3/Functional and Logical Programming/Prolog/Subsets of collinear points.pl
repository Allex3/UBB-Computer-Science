% A set of n points in a plan (represented using its coordinates)
%  are given. Write a predicate to determine 
% all subsets of collinear points.
% n points are collinear if the slopes between all the points are equal

% so first get two candidate points from the set, get their slope
% (just as the ratio for the arithmetic progression example)
% then when trying to add a new point ,check it's slope with all the
% existing points from the current subset, it has to be equal

candidate(P, [P|_]).
candidate(P, [_|T]):- 
    candidate(P, T).

% collinear_aux (L: list, Slope: int, R, LCol: collector list)
% R gets matched to LCol each time we find another collinear point (another subset)
collinear_aux(_, _, LCol, LCol). % match every time
collinear_aux(L, Slope, R, LCol):-
    candidate(P, L),
    constraints(P, LCol, Slope),
    collinear_aux(L, Slope, R, [P, LCol]).
                
% the constraints we have: P to be collinear to those in LCol
% is a subSET so points not repeating => get them in order by X coord
constraints([X, Y], [[HX,HY] | T], Slope):-
    X =< HX,
    Y =< HY,
    \+ member([X, Y], [[HX, HY]|T]),
    check_collin([X, Y], [[HX, HY]|T], Slope).   

member(P, [P|_]):-!.
member(P, [_|T]):-
    member(P, T).

check_collin([_, _], [], _).
check_collin([X, Y], [[X, _]|T], inf):-
    % X = HX => line parallel to Oy, slope = infinity
    % will not enter if Slope != Inf, so they're not colinear
    check_collin([X, Y], T, inf).
check_collin([X, Y], [[HX, HY]|T], Slope):-
    Slope \== inf,
    Slope1 is (Y-HY)/(X-HX),
    Slope1 == Slope,
    check_collin([X, Y], T, Slope).

% collinear(L: list, R: result)
% recursive model: collinear(L) = all subsets of collinear points
collinear(L, R):-
    candidate([X1, Y1], L),
    candidate([X2,Y2], L),
    X1 < X2,
    Y1 < Y2,
    Slope is (Y2-Y1)/(X2-X1),
    collinear_aux(L, Slope, R, [[X1, Y1], [X2, Y2]]).
collinear(L, R):-
    candidate([X1, Y1], L),
    candidate([X2,Y2], L),
    X1 == X2,
    Y1 < Y2,
    collinear_aux(L, inf, R, [[X1, Y1], [X2, Y2]]).