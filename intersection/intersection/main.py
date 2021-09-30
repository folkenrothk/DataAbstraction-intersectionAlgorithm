"""Perform primality testing with an exhaustive and efficient approaches."""

from pyinstrument import Profiler  # type: ignore

from typing import Any
from typing import List
from typing import Tuple
from typing import Union

from enum import Enum

import random

import typer

from rich.console import Console

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a Profiler object to support timing program code segments
profiler = Profiler()


class IntersectionApproach(str, Enum):
    """Define the name for the approach for performing intersection of structured types."""

    list_single = "ListSingle"
    tuple_single = "TupleSingle"
    list_double = "ListDouble"
    tuple_double = "TupleDouble"


def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # the provided answer is True
    if answer:
        return "Yes"
    # the provided answer is False
    return "No"


def generate_random_container(
    size: int, maximum: int, make_tuple: bool = False
) -> Union[List[int], Tuple[int, ...]]:
    """Generate a random list defined by the size and with no number bigger than maximum."""
    # TODO: generate a list of random values
    # TODO: the size of the list must be defined by the size parameter
    # TODO: the contents of the list cannot have a number bigger than the number stored in maximum
    # TODO: if the make_tuple parameter is True, then return a tuple instead of a list
    # TODO: delete this placeholder return statement
    return ()

def compute_intersection_list_double(
    input_one: List[Any], input_two: List[Any]
) -> List[Any]:
    """Compute the intersection of two provided lists."""
    # TODO: implement this function in a manner
    # that follows the compute_intersection_tuple_double
    # TODO: this function must use a double for loop
    # TODO: delete this placeholder return statement
    return []


def compute_intersection_list_single(
    input_one: List[Any], input_two: List[Any]
) -> List[Any]:
    """Compute the intersection of two provided lists."""
    # TODO: implement this function in a manner
    # that follows the compute_intersection_tuple_single
    # TODO: this function must use a single for loop and an if statement
    # TODO: delete this placeholder return statement
    return []


def compute_intersection_tuple_double(
    input_one: Tuple[Any, ...], input_two: Tuple[Any, ...]
) -> Tuple[Any, ...]:
    """Compute the intersection of two provided lists."""
    result: Tuple[Any, ...] = ()
    for x in input_one:
        for y in input_two:
            if x == y:
                result += (y,)
    return result


def compute_intersection_tuple_single(
    input_one: Tuple[Any, ...], input_two: Tuple[Any, ...]
) -> Tuple[Any, ...]:
    """Compute the intersection of two provided tuples."""
    result: Tuple[Any, ...] = ()
    for element in input_one:
        if element in input_two:
            result += (element,)
    return result


@cli.command()
def intersection(
    number: int = typer.Option(5),
    maximum: int = typer.Option(25),
    profile: bool = typer.Option(False),
    display: bool = typer.Option(False),
    approach: IntersectionApproach = IntersectionApproach.tuple_single,
) -> None:
    """Compute the intersection of data containers."""
    # create a console for rich text output
    console = Console()
    # create the starting data containers with no contents
    input_one = None
    input_two = None
    # create a starting output variable for the intersection computation
    intersection_output: Union[List[Any], Tuple[Any, ...]]
    # TupleSingle: the intersection algorithm that works on an input list
    if approach.value == IntersectionApproach.tuple_single:
        # generate the two inputs consisting of random values
        input_one = generate_random_container(number, maximum, make_tuple=True)
        input_two = generate_random_container(number, maximum, make_tuple=True)
        # perform profiling on the execution of the intersection algorithm
        if profile:
            profiler.start()
            intersection_output = compute_intersection_tuple_single(
                tuple(input_one), tuple(input_two)
            )
            profiler.stop()
        # do not perform profiling on the intersection algorithm
        else:
            intersection_output = compute_intersection_tuple_single(
                tuple(input_one), tuple(input_two)
            )
    # TupleDouble: use the intersection algorithm that works on an input tuple
    elif approach.value == IntersectionApproach.tuple_double:
        # generate the two tuples of random values
        input_one = generate_random_container(number, maximum, make_tuple=True)
        input_two = generate_random_container(number, maximum, make_tuple=True)
        # perform profiling on the execution of the intersection algorithm
        if profile:
            profiler.start()
            intersection_output = compute_intersection_tuple_double(
                tuple(input_one), tuple(input_two)
            )
            profiler.stop()
        # do not perform profiling on the intersection algorithm
        else:
            intersection_output = compute_intersection_tuple_double(
                tuple(input_one), tuple(input_two)
            )
    # ListSingle: the intersection algorithm that works on an input list
    elif approach.value == IntersectionApproach.list_single:
        # generate the two inputs consisting of random values
        input_one = generate_random_container(number, maximum, make_tuple=False)
        input_two = generate_random_container(number, maximum, make_tuple=False)
        # perform profiling on the execution of the intersection algorithm
        if profile:
            profiler.start()
            intersection_output = compute_intersection_list_single(
                list(input_one), list(input_two)
            )
            profiler.stop()
        # do not perform profiling on the intersection algorithm
        else:
            intersection_output = compute_intersection_list_single(
                list(input_one), list(input_two)
            )
    # ListDouble: use the intersection algorithm that works on an input list
    elif approach.value == IntersectionApproach.list_double:
        # generate the two inputs consisting of random values
        input_one = generate_random_container(number, maximum, make_tuple=False)
        input_two = generate_random_container(number, maximum, make_tuple=False)
        # perform profiling on the execution of the intersection algorithm
        if profile:
            profiler.start()
            intersection_output = compute_intersection_list_double(
                list(input_one), list(input_two)
            )
            profiler.stop()
        # do not perform profiling on the intersection algorithm
        else:
            intersection_output = compute_intersection_list_double(
                list(input_one), list(input_two)
            )
    # display the input sets and the result of running the computation
    if display:
        console.print(
            ":sparkles: Here are the details about the intersection computation!"
        )
        console.print()
        console.print("Performed intersection with:")
        console.print(f"---> the first data container: {input_one}")
        console.print(f"---> the second data container: {input_two}")
        console.print(
            f"Computed the intersection as the data container: {intersection_output}"
        )
    # display the results of the profiling if that option was requested
    if profile:
        console.print()
        console.print(
            f":microscope: Here's profiling data from computing an intersection with random data containers of {number}!"
        )
        profiler.print()
