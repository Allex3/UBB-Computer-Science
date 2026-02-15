(defvar arb)
(setq arb '(a (b () (f)) (d (e () (k)) (l))))
(print arb)

; find the path from the root to a given node 
; use the auxiliary function to see if an element is part of a V1 tree, non-linear lists
(defun tree_member (E tree)
  (cond
    ((null tree) nil) ; nop, cooked
    ((equalp E (car tree)) T)
    (T (OR (tree_member E (cadr tree)) (tree_member E (caddr tree)))) ; find it anywhere left right
  )
)

(defun cale (E tree) ; tree: root left right
  (cond 
    ((null tree) nil)
    ((equalp E (car tree)) (list E)) ; list only of E
    ((tree_member E (cadr tree)) (cons (car tree) (cale E (cadr tree)))) ; E is in l2, the left tree
    ((tree_member E (caddr tree)) (cons (car tree) (cale E (caddr tree))))
    (T nil)
  )
)

(print (cale 'f arb))