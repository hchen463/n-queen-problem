# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:48:50 2020

We use hill climbing algorithm with random initial state to solve
the n-queen problem.

@author: Hongxu Chen
"""

import random




# Return all successor of a given state with given static point.
def succ(state, static_x, static_y):
    # Return an empty list when there is no queen in the static point
    if(state[static_x]!=static_y):
        return []
    # list to store all the successor
    successor = []
    for i in range(len(state)):
        # find the successor when we are not searching at the static column
        if i != static_x:
            # Move the queen downside as a successor when the queen
            # is not at the top
            if state[i]-1 != -1:
                new_state = state.copy()
                new_state[i] = state[i]-1
                successor.append(new_state)
            # Move the queen upside as a successor when the queen
            # is not at the bottom
            if state[i]+1 != len(state):
                new_state = state.copy()
                new_state[i] = state[i]+1
                successor.append(new_state)
    # Sort all successor
    successor.sort()
    return successor


# Return the value of a given state
def f(state):
    number = 0
    # List to mark if a queen will be attacked or not
    counted = [1]*len(state)
    for i in range(len(state)):
        # Find all the queens that will be attacked in horizon or diagonal
        for j in range(i+1,len(state)):
            # If a queen is in the same or diagonal position, mark as 0.
            if state[j] == state[i] or state[j] == state[i] + (j-i) \
                or state[j] == state[i] - (j-i):
                       counted[i] = 0
                       counted[j] = 0
    # Count the number of 0 is the list
    for i in range(len(counted)):
        if counted[i] == 0:
            number = number+1
    return number
                

    
# Return the next state from all the successor
def choose_next(curr, static_x, static_y):
    # Return none if there is no queen in the static point
    if curr[static_x] != static_y:
        return None
    successor = succ(curr, static_x, static_y)
    # Include the current state in the list of the successor
    successor.append(curr)
    # Sort all the successor
    successor.sort()
    next = successor[0]
    min = f(successor[0])
    # Find the state such that has the min value.
    for suc in successor:
        new_f = f(suc)
        if new_f<min:
            next = suc
            min = new_f
    return next
    

# Return the goal state from a given intial state,
# print the path if pri=True, do not print if pri=False.
def n_queens_print(initial_state, static_x, static_y, pri):
    # Initialize two pointers to denote the previous and current state.
    prev = initial_state
    curr = choose_next(prev, static_x, static_y)
    # Initialize two values to denote the value of previous and current state.
    curr_f = f(curr)
    pre_f = f(initial_state)
    # Keep finding the next state while two continguous state 
    # do not have the same value.
    while curr_f < pre_f:
        if pri:
            print(str(prev) + " - f=" + str(pre_f))
        prev = curr
        curr = choose_next(curr, static_x, static_y)
        pre_f = curr_f
        curr_f = f(curr)
    # Print only one state if the value is 0.
    if curr_f == 0:
        if pri:
            print(str(prev) + " - f=" + str(pre_f))
        return prev
    # Print two states  if the value is not 0, which means
    # we encounter two states with the same value.
    if pri:
        print(str(prev) + " - f=" + str(pre_f))
        print(str(curr) + " - f=" + str(curr_f))
    return curr



# Call previous method with pri=True to print the path.
def n_queens(initial_state, static_x, static_y):
    return n_queens_print(initial_state, static_x, static_y, True)
    


    
# Randomly select k initial state and return the optimal value.
def n_queens_restart(n, k, static_x, static_y):
    random.seed(1) 
    # List to store all the optimal state
    goal = []
    min = n
    # Select k many initial states
    for i in range(k):
        # Generate random initial states except for the static point
        initial = [1]*n
        for j in range(n):
            if j == static_x:
                initial[j] = static_y
            else:
                initial[j] = random.randint(0,n-1)
        # Get optimal state using the n_queens_print method without printing
        new_goal = n_queens_print(initial, static_x, static_y, False)
        new_f = f(new_goal)
        # Empty the list if the current value is strictly less than
        # the previous min, and insert the current state into the list
        if new_f < min:
            min = new_f
            goal = []
            goal.append(new_goal)
        # Insert the state into the list when current value is the same as min.
        elif new_f == min:
            goal.append(new_goal)
        # Break if we min value is 0, which means we find the state.
        if min == 0:
            break;
    # Sort the state list and print them.
    goal.sort()
    for state in goal:
        print(str(state) + " - f=" + str(f(state)))
        

