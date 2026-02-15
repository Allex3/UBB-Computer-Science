; (A B 12 (9 D (A F (75 B) D (45 F) 1) 15) C 9)
; gcd of ODD numbers on EVEN levels of this list (superficial level = 1)

; mathematical models:

; explanation: Euclidean algorithm
; my_gcd (a, b) = 
; { my_gcd (b, a), if a < b 
; { my_gcd (b, a%b), if b != 0
; { a, if b = 0
(DEFUN MY_GCD (A B)
(cond
  ((NULL B) A)
  ((< A B) (MY_GCD B A))
  ((NOT (EQUAL B 0)) (MY_GCD B (MOD A B)))
  (T A) ; B = 0 
)
)

; explanation: To find the GCD of more numbers, you find the GCD of the first two numbers,
; then the GCD of that GCD and the next number, then with that and the next, and so on..
; gcd_list(l1l2...ln) = 
; { l1, if L only has one element, and l1 is a numerical ATOM
; { gcd_list(l2...ln), if l1 is NOT a numberical atom (ignore it in the calculations)
; { gcd(l1, gcd_list(l2...ln)), otherwise
(DEFUN GCD_LIST (L)
(cond
  ((NUMBERP L) L)
  ((ATOM L) NIL)
  ((NOT (NUMBERP (CAR L))) (GCD_LIST (CDR L))) ; IGNORE IT
  (T  (MY_GCD (CAR L) (GCD_LIST (CDR L))))
)
)

; get_odd_on_even(l1l2...ln, N) =
; { [], if L is empty
; { l1 + get_odd_on_even(l2...ln, N), if l1 is an odd number AND N%2=0
; { get_odd_on_even(l2...ln, N), if l1 is not an odd number (atom)
; { append(get_odd_on_even(l1, N+1), get_odd_on_even(l2...ln, N)), otherwise
; the last case is when the lement is a list, it si the next level
; append to it the results we get too, basically
(DEFUN get_odd_on_even (L N)
(cond
  ((NULL L) NIL)
  ((AND (AND (NUMBERP (CAR L)) (EQUAL (MOD (CAR L) 2) 1)) (EQUAL (MOD N 2) 0)) (CONS (CAR L) (get_odd_on_even (CDR L) N)))
  ((ATOM (CAR L)) (get_odd_on_even (CDR L) N))
  (T (APPEND (get_odd_on_even (CAR L) (+ 1 N)) (get_odd_on_even (CDR L) N)   ))
)
)

; main_gcd(L) = gcd_list(get_odd_on_even(L, 1))
(DEFUN MAIN_GCD (L)
  (GCD_LIST (get_odd_on_even L 1))
)

(PRINT (GCD_LIST '(A B 12 (9 D (A F (75 B) D (45 F) 1) 15) C 9)))
(PRINT (MAIN_GCD '(A B 12 (9 D (A F (75 B) D (45 F) 1) 15) C 9)))



