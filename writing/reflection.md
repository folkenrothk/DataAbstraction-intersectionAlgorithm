# Intersection Algorithms

## Kate Folkenroth 

## Program Output

### Use eight fenced code blocks to provide output from eight different runs of `intersection` with different inputs

*Do not run the program with the `--display` option when conducting experiments!*

*Whenever possible, please use the same "small" and "large" inputs for both the List-based and Tuple-based algorithms.*

*Document and justify your choice for the `number` and `maximum` variables.*

After running each command four times, below are the run times averaged. Outputs displayed are the fourth run of the experiments.

I used the same inputs for the ListSingle and TupleSingle algorithms. The small input was with the size as 50000 and 50 as the maximum possible value. The large input was size 100000 and a maximum of 100.

The ListDouble and TupleDouble used smaller inputs in comparison to the ListSingle and TupleSingle algorithms. The doubles used the size of 1000 and a maximum of 25 as the small input. The large input in comparison was a size of 3000 and a maximum of 100. 

I chose to separate the single and double algorithms so that I could use larger inputs in my experiments. I also wanted to try the varying maximums and sizes so I varied them between inputs while all actual parameters the between the paired algorithms.

**Summary of the runs for the List-based algorithms:**

Summary of the runs for the ListSingle algorithm:
  * Small = `poetry run intersection --number 50000 --maximum 50 --profile --approach ListSingle`
    - R1: 0.086
    - R2: 0.067
    - R3: 0.066
    - R4: 0.056
    Average Runtime: 0.06875
  * Large =  `poetry run intersection --number 100000 --maximum 100 --profile --approach ListSingle`
    - R1: 0.177
    - R2: 0.156
    - R3: 0.141
    - R4: 0.185
    Average Runtime: 0.16475
Summary of the runs for the ListDouble algorithm:
  * Small = `poetry run intersection --number 1000 --maximum 25 --profile --approach ListDouble`
    - R1: 0.121
    - R2: 0.065
    - R3: 0.049
    - R4: 0.081
    Average Runtime: 0.079
  * Large = `poetry run intersection --number 3000 --maximum 100 --profile --approach ListDouble` 
    - R1: 0.954
    - R2: 0.574
    - R3: 0.380
    - R4: 0.619
    Average Runtime: 0.63175

**Summary of the runs for the Tuple-based algorithms:**

Summary of the runs for the TupleSingle algorithm:
  * Small = `poetry run intersection --number 50000 --maximum 50 --profile --approach TupleSingle`
    - R1: 3.815
    - R2: 3.577
    - R3: 3.718
    - R4: 4.407
    Average Runtime: 3.87925      
  * Large = `poetry run intersection --number 100000 --maximum 100 --profile --approach TupleSingle`
    - R1: 8.726
    - R2: 9.861
    - R3: 9.335
    - R4: 9.817
    Average Runtime: 9.43475
Summary of the runs for the TupleDouble algorithm:
  * Small = `poetry run intersection --number 1000 --maximum 25 --profile --approach TupleDouble`
    - R1: 1.881
    - R2: 1.902
    - R3: 1.842
    - R4: 1.958
    Average Runtime: 1.89575
  * Large = `poetry run intersection --number 3000 --maximum 100 --profile --approach TupleDouble`
    - R1: 9.827
    - R2: 9.544
    - R3: 9.855
    - R4: 9.786
    Average Runtime: 9.753

#### Two outputs from running the `ListSingle` algorithm with different inputs
Run 1: ListSingle with a small input
    `poetry run intersection --number 50000 --maximum 50 --profile --approach ListSingle`

```
🔬 Here's profiling data from computing an intersection with random datacontainers of 50000!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 18:53:00  Samples:  63   
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.056     CPU time: 0.062/   _/                      v4.0.3

Program: intersection --number 50000 --maximum 50 --profile --approach ListSingle

0.063 intersection  intersection\main.py:111
└─ 0.063 compute_intersection_list_single  intersection\main.py:75      
   ├─ 0.057 [self]
   └─ 0.006 list.append  <built-in>:0
         [2 frames hidden]  <built-in>
```

Run 2: ListSingle with a large input
    `poetry run intersection --number 100000 --maximum 100 --profile --approach ListSingle`
    
```
🔬 Here's profiling data from computing an intersection with random 
data containers of 100000!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 15:17:54  Samples:  188 
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.185     CPU time: 0.188
/   _/                      v4.0.3

Program: intersection --number 100000 --maximum 100 --profile --approach ListSingle

0.189 intersection  intersection\main.py:111
└─ 0.187 compute_intersection_list_single  intersection\main.py:75     
   ├─ 0.173 [self]
   └─ 0.014 list.append  <built-in>:0
         [2 frames hidden]  <built-in>
```

#### Two outputs from running the `ListDouble` algorithm with different inputs

Run 1: ListDouble with a small input
    ` poetry run intersection --number 1000 --maximum 25 --profile --approach ListDouble`

```
🔬 Here's profiling data from computing an intersection with random datacontainers of 1000!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 16:18:18  Samples:  73   
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.081     CPU time: 0.094/   _/                      v4.0.3

Program: intersection --number 1000 --maximum 25 --profile --approach ListDouble

0.074 intersection  intersection\main.py:111
└─ 0.074 compute_intersection_list_double  intersection\main.py:61      
   ├─ 0.069 [self]
   └─ 0.005 list.append  <built-in>:0
         [2 frames hidden]  <built-in>  
```

Run 2: ListDouble with a large input
    `poetry run intersection --number 3000 --maximum 100 --profile --approach ListDouble`

```
🔬 Here's profiling data from computing an intersection with random datacontainers of 3000!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 16:20:46  Samples:  613  
 /_//_/// /_\ / //_// / //_'/ //     Duration: 0.619     CPU time: 0.594/   _/                      v4.0.3

Program: intersection --number 3000 --maximum 100 --profile --approach ListDouble

0.619 intersection  intersection\main.py:111
└─ 0.618 compute_intersection_list_double  intersection\main.py:61      
   ├─ 0.601 [self]
   └─ 0.017 list.append  <built-in>:0
         [2 frames hidden]  <built-in>
```


#### Two outputs from running the `TupleSingle` algorithm with different inputs

Run 1: TupleSingle with a small input
    `poetry run intersection --number 50000 --maximum 50  --profile --approach TupleSingle`

```
🔬 Here's profiling data from computing an intersection with random datacontainers of 50000!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 16:36:49  Samples:  1    
 /_//_/// /_\ / //_// / //_'/ //     Duration: 4.407     CPU time: 4.219/   _/                      v4.0.3

Program: intersection --number 50000 --maximum 50 --profile --approach TupleSingle

4.412 intersection  intersection\main.py:111
└─ 4.412 compute_intersection_tuple_single  intersection\main.py:100  
```

Run 2: TupleSingle with a large input
    `poetry run intersection --number 100000 --maximum 100 --profile --approach TupleSingle`

```
🔬 Here's profiling data from computing an intersection with random 
data containers of 100000!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 15:28:50  Samples:  1   
 /_//_/// /_\ / //_// / //_'/ //     Duration: 9.817     CPU time: 9.812
/   _/                      v4.0.3

Program: intersection --number 100000 --maximum 100 --profile --approach TupleSingle

9.816 intersection  intersection\main.py:111
└─ 9.816 compute_intersection_tuple_single  intersection\main.py:100 
```


#### Two outputs from running the `TupleDouble` algorithm with different inputs

Run 1: TupleDouble with a small input
    `poetry run intersection --number 1000 --maximum 25 --profile --approach TupleDouble`
   
```
🔬 Here's profiling data from computing an intersection with random datacontainers of 1000!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 16:02:37  Samples:  1    
 /_//_/// /_\ / //_// / //_'/ //     Duration: 1.958     CPU time: 1.953/   _/                      v4.0.3

Program: intersection --number 1000 --maximum 25 --profile --approach TupleDouble

1.959 intersection  intersection\main.py:111
└─ 1.959 compute_intersection_tuple_double  intersection\main.py:88     

```

Run 2: TupleDouble with a large input
    `poetry run intersection --number 3000 --maximum 100 --profile --approach TupleDouble`
    
```
🔬 Here's profiling data from computing an intersection with random datacontainers of 3000!

  _     ._   __/__   _ _  _  _ _/_   Recorded: 16:00:35  Samples:  1    
 /_//_/// /_\ / //_// / //_'/ //     Duration: 9.786     CPU time: 9.734/   _/                      v4.0.3

Program: intersection --number 3000 --maximum 100 --profile --approach TupleDouble

9.786 intersection  intersection\main.py:111
└─ 9.786 compute_intersection_tuple_double  intersection\main.py:88  
```

## Performance Analysis

Provide three paragraphs that explain **which** algorithm is fastest, by **how much** it is faster, and **how you knew** that the it was faster, referencing the data in the aforementioned command outputs to support your response. 

- *Is intersection faster with a list or a tuple?* 
- *Is intersection faster with a double-for-loop or a single-for-loop?*
- *Overall, what is the fastest approach for computing the intersection?*

(*Make sure that your responses explain WHY certain algorithms are faster!*)


For intersection, lists tended to be faster than tuples. This was easy to see in the direct comparisons I ran between ListSingle and TupleSingle as well as with ListDouble and TupleDouble. Using the averages of the experiments, the ListSingle is about 98% faster than the TupleSingle for both the small and large inputs. The ListDouble was about 96% faster with the smaller input and then 93.5% faster with the larger input than the TupleDouble. I knew it was faster as I chose my inputs based off of the runtimes spent by the tuple algorithms rather than basing it off of the lists. Code wise, it makes sense that the tuples took longer as they are immutable while lists are mutable. This means that the tuple had to be remade everytime it needed to change and add another value while lists could just append.

The single-for-loop is faster than the double-for-loop. Though it is not directly recorded above, I had tried to use the same inputs from the single-for-loop testing as with the double-for-loops. I chose to switch to smaller inputs for the double-for-loops because of the drastic difference in durations. Looking at the numbers above, the small input for ListSingle ran for about the same time as the small input for ListDouble (only about 0.011 of a differnce). Looking at how similar the runtimes, I can compare the inputs between the two. For the ListSingle, the inputs were a size of 50000 and a maximum of 50 while the ListDouble only had a size of 1000 and a maximum of 25. This difference between the inputs is large. Shows that the single-for-loop is faster since it was able to use larger inputs and complete it in about the same time as the double-for-loop. This makes sense with the code since the double-for-loop does as it is labeled, it uses two for loops in its code. Iterating takes time and the single-for-loop only needs to do it once.

Overall, the fastest approach for computing intersection is ListSingle. From the comments above, this algorithm utilizes both the faster iteration structure, a single-for-loop, and data container, lists. I knew this from my ability to use the largest input with this algorithm along with combining these optimal pieces. The time for a size of 100000 and a maximum value of 100 was still computed under a second with this approach. I aborted the testing of this input with the double-for-loops when the duration went over a few minutes as it was obvious those loops would be much slower. 


## Source Code

### Describe in detail how the completed source code works

#### A class that defines the four algorithmic options for running the experiment

```
class IntersectionApproach(str, Enum):
    """Define the name for the approach for performing intersection of structured types."""

    list_single = "ListSingle"
    tuple_single = "TupleSingle"
    list_double = "ListDouble"
    tuple_double = "TupleDouble"
```
This class called `IntersectionApproach` is what defines the four options for this experiment. It takes in strings and Enum. Enum is imported from enumeration. This class is used in the CLI to pick which function to use based on what is specified in the command after the `--approach`. 

#### A function signature that defines the command-line interface for `intersection`

```
@cli.command()
def intersection(
    number: int = typer.Option(5),
    maximum: int = typer.Option(25),
    profile: bool = typer.Option(False),
    display: bool = typer.Option(False),
    approach: IntersectionApproach = IntersectionApproach.tuple_single,
) -> None:
```
This code block displays the function signature for the CLI for intersection. This is seen because of the first two lines showing the `cli.command()` and defining the function `intersection`. This signature has the parameters of number, maximum, profile, display, and approach. Number and maximum are integers. The defaults are set as 5 and 25 respectively. Profile and display are booleans. Both of these are set to false as default. Approach is a string that needs to match the strings listed in the class IntersectionApproach. 
This outputs none.


#### A function that can generate a data container with random values in it

```
def generate_random_container(
    size: int, maximum: int, make_tuple: bool = False
) -> Union[List[int], Tuple[int, ...]]:
    """Generate a random list defined by the size and with no number bigger than maximum."""
    # generate a list of random values
    randomList = []
    # the size of the list must be defined by the size parameter
    # the contents of the list cannot have a number bigger than the number stored in maximum
    for num in range(0, size):
        num = random.randint(0, maximum)
        randomList.append(num)
    # if the make_tuple parameter is True, then return a tuple instead of a list
    if make_tuple is True:
        return tuple(randomList)
    else:
        return randomList
```
This code block shows the source code for generating a container of random integers. It has three parameters: size, maximum, and make_tuple. Size and maximum are integers. Size is used to restrict how many numbers are in our list. Maximum is used to restrict how large the numbers inside the list can be. Make_tuple is a boolean, set to false as default, which makes our list of random integers a tuple. This function can output a list or a tuple of integers at of any length (determined by the parameter given).

Line by line, the code segment starts with the declaration of the function which list the parameters, types, and outputs. The code first creates an empty list. Then within the range of zero to size, the code generates a random integer from 0 to maximum for the variable num. This is then added to the list with the append statement until the length of the list is the same as size. The if statement looks at the boolean of whether to make this list a tuple. If make_tuple is true, the output is a tuple of integers. If not, it returns the list as a list.

### What was the greatest challenge that you faced when completing this assignment?

My greatest challenge with this assignment was working on this with in-laboratory instruction. I feel as though I can successfully now say that I was able to complete the lab, just with more effort and time involved. I much prefer being in class so I can absorb the questions asked my peers and the collective problem solving completed at the lab tables as we work through the code. I was able to replicate some of this as I did discuss my coding challenges with my collegues. 

### Leveraging your response to the previous question, how did you overcome the challenge?

Paired with this difficulty of making up work was the actual coding error I made. As I was creating lists, I was accidently not creating an empty list. Mine were storing the characters "Any" and "..." as I was using the same syntax within the function as the type annotation in the declaration of a function. I realized this mistake by comparing code with peers and referencing online resources in conjunction to our class textbook. This has improved my understanding of lists and data containers as a whole as well as Python syntax.
