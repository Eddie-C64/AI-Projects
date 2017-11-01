# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?
A: *The constraint given to us in the naked twins problem is: 1. a unit must have 2 possible values 2. if there is another unit among its peers that have the same possibilities then it is a naked twin 3. if there is a pair of naked twins then those possibilities must be removed as possible values for all other peers Using these constraints we can build our function to satisfy these constraints. In the order listed above we could start building our naked_twins function. First thing I did was grab all the units that have only 2 possible values (length of 2). From there we can move on to the next constraint, which would be to grab all the units that have a naked twin pair by checking if the possible values are the same among their peers. Lastly, we would remove these possibilities as possibilities for the rest of the units in their respective peers. Handling the constraints lead us to our solution.*

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?
A: *For the diagonal Sudoku problem we are adding one more constraint to our program. We already have existing constraints from Sudoku itself that are very similar to diagonal Sudoku. Since the Unit_list is already accomplishing the constraints from Sudoku and in order to satisfy the diagonal Sudoku problem we can add the values that are needed to be satisfied to unit_list. Doing this will cause our problem to attempt to satisfy this constraint as well.*

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_value` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login) for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

