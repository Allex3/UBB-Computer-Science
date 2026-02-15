% mathematical models: (start with these maybe it helps LMAO)

% rearrange_aux(a1a2...an, b1b2...bm) =
% { [a1], [b1] U rearrange_aux(a2...an,b2...bm), if a1 >= b1
% { [b1], [a1] U rearrange_aux(....), if a1 < b1
% { [], [], if both lists are empty
% { [A, []], if B is empty (put in at the greater list)
% { [B, []], if A is empty (B is greater)

% to achieve the above function we use reverse
% to actually start from the beginning
% rearrange(A, B) = rearrange_aux(reverse(A), reverse(B))

% rearrange_lists(a1a2...an, b1b2...bm) =
% { rearrange_lists(A, b2...bm), if a1 is a list, b1 is not a list
% { rearrange_lists(a2...an, B), if b1 is a list, a1 is not a list
% basically go until both are sublists (we know we have the same number
% of sublists, we just need to match them
% { rearrange_lists(a2...an, b2...bm), if a1 and b1 are NOT lists
% { [][], if A OR B are empty (not AND, oops)
% { rearrange(a1, b1) U rearrange_lists(a2...an, b2...bm), if a1 and b1 are lists

% rearrange_aux(A: list, B: list, RG: list, RS: list)
% (i, i, o, o) - deterministic, basically a sort of merging,
% interclasare
rearrange_aux([],[], [], []):-!. % both empty
rearrange_aux([],B,B,[]):-!. % A is empty, B is greater
rearrange_aux(A, [], A, []):-!. % DO NOT RETURN FALSE PLEASE
rearrange_aux([HA|TA], [HB|TB] , [HG|TG], [HS|TS]):-
    HA >= HB, !, % do not try the other case
    HG is HA, % greater digit
    HS is HB, % smaller digit
    rearrange_aux(TA, TB, TG, TS).
rearrange_aux([HA|TA], [HB|TB] , [HG|TG], [HS|TS]):-
    % the other case basically
    HG is HB,
    HS is HA,
    rearrange_aux(TA, TB, TG, TS).

% rearrange(A: list, B: list, RG: list, RS: list)
% ( i, i, o, o) - det.
rearrange(A, B, RG, RS):-
    reverse(A, RevA),
    reverse(B, RevB),
    rearrange_aux(RevA, RevB, RGaux, RSaux),
    reverse(RGaux, RG),
    reverse(RSaux, RS).


% rearrange_lists(A: list, B: list, RG: list, RS: list)
% (i, i, o, o) - deterministic
% keep in mind here RG and RS will be lists of lists
rearrange_lists([], [], [], []):-!. % both lists empty
rearrange_lists([HA|TA], [HB|TB], RG, RS):-
    is_list(HA),
    \+ is_list(HB), !, %only HA list, dont check the others
    rearrange_lists([HA|TA], TB, RG, RS).
rearrange_lists([HA|TA], [HB|TB], RG, RS):-
    \+ is_list(HA),
    is_list(HB), !, %only HB list, dont check the others
    rearrange_lists(TA, [HB|TB], RG, RS).
rearrange_lists([HA|TA], [HB|TB], RG, RS):-
    \+ is_list(HA),
    \+ is_list(HB), !, % neither list
    rearrange_lists(TA, TB, RG, RS).
rearrange_lists([HA|TA], [HB|TB], [HG|TG], [HS|TS]):-
    is_list(HA),
    is_list(HB), !, % both lists
    rearrange(HA, HB, HG, HS), % finally rearrange them
    rearrange_lists(TA, TB, TG, TS).
% FORGOT TWO CASESSS FUCKK, when oneo fthem is empty
% since we have the SAME number of sublists in both of them
% if one is empty, we already tackleda ll of them as per the above
% predicate, so it can just be discarded, same as the both empty case
rearrange_lists([], _, [], []):-!.
rearrange_lists(_, [], [], []):-!.
