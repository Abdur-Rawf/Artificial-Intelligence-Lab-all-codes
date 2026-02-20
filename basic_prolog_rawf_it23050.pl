% Basic Prolog (Customized by Rawf, Student ID: it23050)

parent(heron, rawf).
parent(heron, lamia).

% --- Rules: Logic ---
% Sibling Rule: X and Y are siblings if they share the same parent Z,
% and X is distinct from Y.
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.
