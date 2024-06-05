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

%iso(X) :- x=0
iso(X) :- X is 0.

%power(X, Y, Z) is true if X^Y = Z
power(X,0,s(0)) :- isnumber(X).
power(X,s(Y),Z) :- odd(s(Y)), power(X, Y, W), times(X, W, Z).
power(X, Y, Z) :- even(Y), times(X, X, M), plus(N, N, Y), pow(M, N, Z).

% a2b = (a2)b and a2b+1 = a · a2b

len([],0).
len([H|T],N) :- len(T,N1), N is N1+1.

%Membership
member(X, []) :- false.
member(X, [H|T]):- X is H; member(X, T).

%Concationation
concat(X,[], X).
concat([T|B], [T|A], X) :- concat(B, A, X).

%Reverse
reverse([], []).
reverse([X|T], R) :- reverse(T, NewR), concat(R, NewR, [X]).

%Palindrome
palindrome(L) :- reverse(L, L).
