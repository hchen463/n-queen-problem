# n-queen-problem
We apply the hill climbing algorithm with random initial state to find the optimal state to the n-queen problem,
that is, a state such no queen is attacking any other queen on the chessboard.

We use a function f to compute the value of a given state. The value of a state is defined as the number of queens that will be attacked.

In the file, n_queens_restart(n, k, static_x, static_y) print the optimal state, here n is the size of the chessboard, 
k is the number of random initial state, static_x and static_y is the position of the static point.

If we do not find the optimal state with value 0, we will print all the states with minimum value.
