; HOW do i get the level? Add as when adding nv, BUT decrement when you reach 0
; basically you go B 2 -> 1, C 1 -> 2, I 0 -> call with 1 now,
; because we reached a leaf so come back

(defun left_inorder(tree nv ne) 
  (cond
((null tree) nil)
((= nv (+ 1 ne)) nil) ; reached the end (the number of added vertices besides root = ne)
    ; and the number of real vertices is that +1 = + root, so we have all now  

    (t (cons (car tree)
        (cons (cadr tree)
          (left_inorder (cddr tree) (+ 1 nv) (+ (cadr tree) ne))
        )
      )
    )
  )
)

(defun left (tree)
  (left_inorder (cddr tree) 0 0)
)


(defun right_inorder (tree nv ne)
  (cond 
    ((null tree) nil)
    ((= nv (+ 1 ne)) tree) ; end of left subtree
    ; but since its the END of the left subtree => return subtree, that is the right
    (t
    ; at the semi-last call it will be the node BEFORE the right tree
          (right_inorder (cddr tree) (+ 1 nv) (+ (cadr tree) ne))
          
        
        
      
    )
  )
)

(defun right (tree)
  (right_inorder (cddr tree) 0 0)
)

; left + root + right
(defun inorder (tree lev)
  (cond 
  ; finished the tree, but before this it was NOT null, so level-1 is the real one
    ((null tree) (- lev 1))
    (t (max ; get maximum level instead of appending lists
        (inorder (left tree) (+ 1 lev))  (inorder (right tree) (1+ lev)) 
      )
    )
  )
)

; the level = how deep we are in the inorder traversal 
; basically, at the first call it's level 0, when we call it again we go right or left
; and going right/left means going DOWN
; so as long as the tree is NOT null, we can increment the level
(setq LEV 0)
(print (inorder '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) LEV))