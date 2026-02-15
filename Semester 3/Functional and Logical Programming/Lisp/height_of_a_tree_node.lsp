; height of a node in a tree..
; (a (b (g)) (c (d (e)) (f))) , e -> 0, v -> -1, g -> 0, c -> 2
; basically how many edges from a leaf to itself I think


; get_distance_to_deepest_leaf(tree, N) = 
; { N, if tree is an atom
; { MAX(append(get_distance_to_deepest_leaf(tree_i, N+1))), otherwise
; where tree_i is each node/subtree (element) of the tree we are currently in
(DEFUN get_distance_to_deepest_leaf (TREE N)
(cond
  ((ATOM TREE) N)
  (T (APPLY #'MAX (MAPCAR #'(LAMBDA (X) (get_distance_to_deepest_leaf X (+ 1 N))) TREE  )))
)
)

; height_tree_aux(tree, N, E) =
; { N, if tree=E
; { nil, if tree is empty
; { OR(append(height_tree_aux(tree_i, N, E))), where tree_i, is every element in the list tree
(DEFUN height_tree_aux (TREE E ITS_SUBTREE)
(cond
; START FROM -1, because this being its subtree, it will get to 0 only when going through
; its elements, so this way E will be at 0 , and the leaf will be at the 
; from E to leaf, so its height
  ((EQUAL TREE E) (get_distance_to_deepest_leaf ITS_SUBTREE -1)) ; basically go in the subtree of E
  ((ATOM TREE) NIL)
  ((NULL TREE) NIL)
  (T (SOME #'(LAMBDA (X) (height_tree_aux X E TREE)) TREE) ) 
  ; TREE is the subtree of each node/subtree we go in basically
)
)

(PRINT (height_tree_aux '(a (b (g)) (c (d (e)) (f))) 'a NIL))
