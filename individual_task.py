#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Определить результат выполнения операций над множествами.
#Считать элементы множества строками. Проверить результаты вручную.
# X=(A∪B)∩D; Y=(¬A∩D)∪(C/B)
# A={a,b,g,k,m,p}; B={b,e,f,l,r}; C={k,l,w,x}; D={e,j,o,p,q,u,v}

if __name__ == "__main__":
    A = set('abgkmp')
    B = set('beflr')
    C = set('klwx')
    D = set('ejopquv')
    U = set('abgkmpbeflrklwxejopquv')

    X = (A.union(B)).intersection(D)
    Y = ((U.difference(A)).intersection(D)).union(C.difference(B))

    print(X, Y)

