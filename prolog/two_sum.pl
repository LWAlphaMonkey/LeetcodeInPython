list_with_index(List, Res) :-
    list_with_index(List, 0, Res).

list_with_index([], _, []).

list_with_index([H|T], N, [num(H, N)|Res]) :-
    N1 is N + 1,
    list_with_index(T, N1, Res).

select(H, [H|T], T).
select(X, [H|T], [H|Res]) :-
    select(X, T, Res).

two_sum(List, Target, [M1, M2]):-
    list_with_index(List, NewList),
    select(num(E1, M1), NewList, _),
    select(num(E2, M2), NewList, _),
    Target is E1 + E2,
    M1 \= M2,
    !.
