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
(defun inorder (tree)
  (cond 
    ((null tree) nil)
    (t (append 
        (inorder (left tree)) (list (car tree)) (inorder (right tree)) 
      )
    )
  )
)

(print (left '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) ))
(print (right '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) ))
(print (inorder '(a 2 b 2 c 1 i 0 f 1 g 0 d 2 e 0 h 0) ))
(print (inorder '(a 2 b 2 () ))