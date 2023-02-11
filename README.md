# CMPS 2200  Recitation 02

**Name (Team Member 1):** Tyler Simms  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.


## Setup
- Make sure you have a Github account.
- Login to Github.
- Login to repl.it, using "sign in with github"
- Click on the assignment link sent through canvas and accept the assignment.
- Click on your personal github repository for the assignment.
- Click on the "Work in Repl.it" button. This will launch an instance of `repl.it` initialized with the code from your repository.
- You'll work with a partner to complete this recitation. To do so, we'll break you into Zoom rooms. You will be able to code together in the same `repl.it` instance. You can choose whose repl.it instance you will share. This person will click the "Share" button in their repl.it instance and email the lab partner.

## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest main.py` will run all tests
  + `pytest main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Version Control" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

When $f(n) = 1$, the asymptotic behavior is O(n). When $f(n) = n$, the asymptotic behavior is O(n^2). When $f(n) = \log n$, the asymptotic behavior is O(nlogn). My derivations match the trends in the chart below. The chart from left to right is $f(n) = 1$, $f(n) = n$, and $f(n) = \log n$.


|     n |   W_1 |    W_2 |   W_3 |
|-------|-------|--------|-------|
|    10 |    15 |     36 |     8 |
|    20 |    31 |     92 |    16 |
|    50 |    63 |    276 |    32 |
|   100 |   127 |    652 |    64 |
|  1000 |  1023 |   9120 |   512 |
|  5000 |  8191 |  61728 |  4096 |
| 10000 | 16383 | 133456 |  8192 |

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

|     n |       W_1 |   W_2 |    W_3 |
|-------|-----------|-------|--------|
|    10 |       174 |    15 |     36 |
|    20 |       748 |    31 |     92 |
|    50 |      4790 |    63 |    276 |
|   100 |     19580 |   127 |    652 |
|  1000 |   1990744 |  1023 |   9120 |
|  5000 |  49957880 |  8191 |  61728 |
| 10000 | 199915760 | 16383 | 133456 |

This comparison was done using a = 2 and b = 2. The work increases very quickly when $c > \log_b a$, as seen in the W_1 column. The work increases much slower when $c < \log_b a$, relative to when $c > \log_b a$, as seen in the W_2 column. I modified the 'compare_work' function to also print the work when $c = \log_b a$. When $c = \log_b a$, the work increases faster than when $c < \log_b a$ but not as fast as when $c > \log_b a$, as seen in the W_3 column.

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

The asymptotic expressions for the span are the same as those of the work for the recurrences from problem 4. The table below confirms this.

|     n |   W_1 |    W_2 |   W_3 |
|-------|-------|--------|-------|
|    10 |    15 |     36 |     8 |
|    20 |    31 |     92 |    16 |
|    50 |    63 |    276 |    32 |
|   100 |   127 |    652 |    64 |
|  1000 |  1023 |   9120 |   512 |
|  5000 |  8191 |  61728 |  4096 |
| 10000 | 16383 | 133456 |  8192 |
