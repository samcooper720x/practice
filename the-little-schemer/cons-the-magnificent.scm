(define insertR
  (lambda (new old lat)
    (cond
      ((null? lat) '())
      (else
        (cond
          ((eq? (car lat) old) (cons old (cons new (cdr lat))))
          (else
            (cons (car lat) (insertR new old (cdr lat)))))))))

(insertR 'topping 'fudge '(ice cream with fudge for desert))

(define insertL
  (lambda (new old lat)
    (cond
      ((null? lat) '())
      (else
        (cond
          ((eq? (car lat) old) (cons new lat))
          (else
            (cons (car lat) (insertL new old (cdr lat)))))))))

(insertL 'topping 'fudge '(ice cream with fudge for desert))

(define subst
  (lambda (new old lat)
    (cond
      ((null? lat) '())
      (else
        (cond
          ((eq? (car lat) old) (cons new (cdr lat)))
          (else
            (cons (car lat) (subst new old (cdr lat)))))))))

(subst 'topping 'fudge '(ice cream with fudge for desert))

(define subst2
  (lambda (new o1 o2 lat)
    (cond
      ((null? lat) '())
      (else
        (cond
          ((or (eq? (car lat) o1) (eq? (car lat) o2)) (cons new (cdr lat)))
          (else 
            (cons (car lat) (subst2 new o1 o2 (cdr lat)))))))))

(subst2 'vanilla 'chocolate 'banana '(banana ice cream with chocolate topping))

; Define helpers
(define atom?
 (lambda (x)
    (and (not (pair? x)) (not (null? x)))))

(define lat?
  (lambda (l)
    (cond
      ((null? l) #t)
      ((atom? (car l)) (lat? (cdr l)))
      (else #f))))

