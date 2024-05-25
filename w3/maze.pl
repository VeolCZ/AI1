connected(i, m).
connected(n, m).
connected(n, o).
connected(p, l).
connected(l, h).
connected(h, d).
connected(d, c).
connected(c, g).
connected(g, k).
connected(k, j).
connected(j, f).
connected(f, b).
connected(b, a).
connected(f, e).

path(A, B) :-
    connected(A, B);
    connected(B, A);
    (   connected(A, X),
        path(X, B));
    (   connected(B, X),
        path(X, A)).