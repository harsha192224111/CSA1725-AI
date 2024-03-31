% Predicate to solve the Towers of Hanoi problem
hanoi(N) :- move(N, left, center, right).

% Predicate to move N disks from A to B using C as a temporary peg
move(0, _, _, _) :- !.
move(N, A, B, C) :-
    M is N - 1,
    move(M, A, C, B),
    write('Move disk from '), write(A), write(' to '), write(B), nl,
    move(M, C, B, A).
