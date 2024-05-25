% isnumber(X) is true if X is a isnumber

isnumber(0).
isnumber(s(X)) :- isnumber(X).

% plus(X,Y,Z) is true if X + Y = Z

plus(0,X,X) :- isnumber(X).
plus(s(X),Y,s(Z)) :- plus(X,Y,Z).

% minus(X,Y,Z) is true if X - Y =Z

minus(X,0,X) :- isnumber(X).
minus(s(X),s(Y),Z) :- minus(X,Y,Z).

% times(X,Y,Z) is true if X * Y = Z

times(X,0,0) :- isnumber(X).
times(X,s(Y),Z) :- times(X,Y,Z1), plus(X,Z1,Z).

% pow(X,Y,Z) is true if X^Y = Z

pow(X,0,s(0)) :- isnumber(X).
pow(X,s(Y),Z) :- pow(X,Y,Z1), times(X,Z1,Z).

% even(N) is true if N is even.
even(0).
even(s(N)) :- odd(N).

% odd(N) is true if N is odd.
odd(s(0)).
odd(s(N)) :- even(N).

% div2(N, D) :- plus(D, D, N).

div2(N, D) :- times(D,s(s(0)),N).

log(X,B,N) :- pow(B, N, X).

fib(0, 0) :- true.
fib(s(0), s(0)) :- true.
fib(X, Y) :-
    minus(Y, X, Z),
    fib(Z, X).

% power(X,0,_) :- s(0).
% power(X,s(0),_) :- X.
% power(X,N,Y) :- even(N),

power(_, 0, 1) :- s(0).
power(X, N, Y) :-
    N1 is N // s(s(0)),
    power(X, N1, Y1),
    (even(N) ->
        Y is Y1 * Y1;
        Y is X * Y1 * Y1
    ).

% a2b = (a2)b and a2b+1 = a · a2b

% Example queries:
% Isnumbers are represented as successors of 0. For example, 2 is s(s(0)).
% 2+2=4 is plus(s(s(0)), s(s(0)), s(s(s(s(0)))))
% 3*2=? is times(s(s(s(0))), s(s(0)), X)
