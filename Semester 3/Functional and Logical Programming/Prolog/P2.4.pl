% 4. 
% a. Write a predicate to determine the
% sum of two numbers written in list representation.
% b. For a heterogeneous list, formed from integer numbers and 
% list of digits, write a predicate to compute the 
% sum of all numbers represented as sublists.
% Eg.: [1, [2, 3], 4, 5, [6, 7, 9], 10, 11, [1, 2, 0], 6] => [8, 2, 2].

% little-endian (reversed lists) so we can do add with carry
% a1, b1 = least significant digit
% c = carry from last operation (starts from 0, set to 1 only if a1+b1>9
% sum with carry, mathematical model: sum(a1a2...an, b1b2...bm, c) = 
%	(a1+b1+c)%10 \oplus sum(a2...an, b2...bm, (a1+b1+c)/10)), if A and B are NOT empty
%	(b1+c) \oplus sum([], b2...bm, (b1+c)/10), if A = [] (carry will be only from last op)
%	(a1+c) \oplus sum(a2...an, [], (a1+c)/10)), if B = []
%	[], if A = [] and B = []

% sum(A: list, B:list, C: int, R: list)
% (i, i, i, o), (i, o, i, i), (o, i, i, i), (o, i, o, i) ?
sum_aux([], [], 0, []):-!. %if both are empty and C=1, match to [1], otherwise to []
sum_aux([], [], 1, [1]). % if C=1
sum_aux([HA|TA], [HB|TB], C, [HR|TR]):-
    HR is (HA+HB+C) mod 10, % current digit
    C1 is (HA+HB+C) div 10,
    sum_aux(TA, TB, C1, TR).
sum_aux([], [HB|TB], C, [HR|TR]):-
    HR is (HB+C) mod 10,
    C1 is (HB+C) div 10,
    sum_aux([], TB, C1, TR).
sum_aux([HA|TA], [], C, [HR|TR]):-
    HR is (HA+C) mod 10,
    C1 is (HA+C) div 10,
    sum_aux(TA, [], C1, TR).

sum(A, B, R):-
    reverse(A, RevA),
    reverse(B, RevB),
    sum_aux(RevA, RevB,0, RevR),
    reverse(RevR, R).