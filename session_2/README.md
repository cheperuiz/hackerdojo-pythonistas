# Session 2
## Summary

Our goal this session is to be able to run a pre-trained machine learning model from a python script. For that, we need to re-visit some of the fundamental building blocks in the Python ecosystem to understand how they work, how they interact with each other and some of the *Gotchas* that might caught you off guard.

## Prerequisites

You should have a python-friendly setup already installed and configured in your system. For simplicity, I recommend VS Code.
If this is your first time developing with python, follow the steps below:

- Install `Python 3.8+` in your system (I recommend the latest stable version, `Python 3.10`). If you are not sure how to do this, follow the steps at the [Official Documentation](https://wiki.python.org/moin/BeginnersGuide/Download).

- Install and configure [VS Code](https://code.visualstudio.com) (or any other IDE) for python development, including `black` as a code formatter.
    - [Python in visual studio](https://code.visualstudio.com/docs/languages/python).
    - About [Black](https://black.readthedocs.io/en/stable/) formatter and why its awesome.
- Have a virtual environment already configured as an interpreter for your project.
    - For this, you can try completing all the steps from [Session 1](../session_1/README.md).


## Overview of the building blocks

Among the multiple programming languages and paradigms that exists, there is one thing that is always present: The ability to group related things togehter.
This is necessary because, as humans, grouping things together and treating them as a single unit allows us to think more about the problem we are trying to solve, and think less about the details of whats actually happening underneath.

As a languange that aims for simplicity, Python allows programmers to group things together with great flexibility. In order to understand how this works, we need to know (at least partially) how Python is built, what happens when I run my script with `python my_script.py` and how programs written in Python are usually structured.

Some of the concepts we will glance over are:

- Types and built-in types.
- Variables, scopes and lifetimes.
- Loops and comprehensions.
- Functions.
- Classes and magic *dunder* methods (double underscore methods).
- Modules, packages and the import system.
- A few, very useful, *advanced-ish* concepts (context managers, decorators, iterators/generators)

Depending on the type of a variable, it will behave differently when used in combination with the different operators that exist in python. You can take a look at al the operators available here:

## Built-in types and what you can do with them

The set of built-in types in python is fairly limited but very useful. You can use those types to solve any computing problem you might face. It is my opinion that knowing the details around these types can be very beneficial and save you time (like, a lot...) in the future.

There are a few more types available, and you may find an interesting read at the [Official Documentation](https://docs.python.org/3.10/library/stdtypes.html#), but for now, let's take a look at the ones I've been using more:

- Boolean (`bool`)
- Integer (`int`)
- Floating point (`float`) and Decimal (`decimal.Decimal`)
- List (`list`)
- Tuple (`tuple`)
- Set (`set`)
- Dict (`dict`)
- String (`str`)

Please take a look at the [Session 2 Notebook](./Session_2.ipynb) to take a look at interesting things we can do with each type.

## Scopes and lifetimes

In computer science `scope` refers to the places from where a certain symbol is available (visible). In Python there are three main scopes that we care about:

- Global (please, please, please... don't use this one)
- Global to a module/package (Try to avoid)
- Local (whenever possible, use this.)

The lifecycle of a symbol is called `lifetime`. In python, the lifetime of a symbol will be the same as the `context` that contains it. In other words, when the context is over, making the object out of scope, it will end its lifecycle (ie. a local variable defined inside a function ceases to exist as the funcion ends).

## Loops

There are two main constructs to create loops in python: `while` and `for`
Both of them can be useful in certain conditions, although I find myself almost never using a `while` loops.
A `while` loop should be used when we are expecting a certain condition to change, whereas a `for` loop is mainly used to iterate over collections. In Python, the `for` construct is more like a `foreach` in other languages.

One of my favorite constructs in python are list comprehensions (and dict, set comprehensions as well). It is a special syntax that allow you to write a loop that builds a list in a single line. So, something that looks like this:

```
alphabet = 'abcdefghijklmnopwrstuvwxyz'

first_ten = []
for a in alphabet[:10]:
    first_ten.append(a)
```
Becomes:

```
alphabet = 'abcdefghijklmnopwrstuvwxyz'
first_ten = [c for c in alphabet[:10]]
```

And you can even use constraints to build your new list, so this:

```
alphabet = 'abcdefghijklmnopqrstuvwxyz'
odd_index = []
for i,c in enumerate(alphabet):
    if i % 2 != 0:
        odd_index.append(c)
```

becomes:

```
alphabet = 'abcdefghijklmnopqrstuvwxyz'
odd_index = [c for i,c in enumerate(alphabet) if i % 2 != 0]
```

## Functions

A function is a block of code that we can group together so that we can execute that same block multiple times during the execution of our program. We already looked at the basic syntax for defining functions in [Session 1](../session_1/README.md) but let's try to look a little deeper into it:

```
def my_function(a, b, c=0, d=0):
    return (a+c) * (b + d)
```

In `my_function` I have defined a few parameters:

- `a` and `b` are *positional* arguments, and they are mandatory.
- `c` and `d` are `keyword` arguments and have a default value defined. Passing a value for `c` and `d` is optional and, depending on which values I choose to pass, there are several ways to call `my_function`:

```
my_function(1,2)
my_function(1,2,3)
my_function(1,2,c=3)
my_function(1,2,3,4)
my_function(a=1,b=2,c=3,d=4)
my_function(1,2,d=4)
```
All the previous statements are valid function calls, and they all do different things. Note that I can use kewyword syntax for positional arguments but after that, all arguments MUST be keyword arguments. For example, this would throw an error:

```
my_func(a=1, 2)
```

### Pitfalls: Mutable types as default values (don't do it)

## Classes

A class allow us to define our own types. The syntax is very simple and similar to other languages. It allows us to group together several related functions and data. Some people like OOP, others prefer using only functions. The good thing is that Python allows you to use one or the other (or both) whenever you want.

For this section, take a look at the [notebook](./Session_2.ipynb).

## Modules and the import system

The import system is a Python component that allows us to package (and publish) fractions of our code. A module is the next level of grouping after functions and classes


## Bonus: Context Managers, Generators, Decorators

A brief summary of these very useful concepts.

## Putting it all together: Inferencing library using Intel's OpenVINO

## Thanks to Intel

These sessions are sponsored by [Intel](https://www.intel.com). Take a look at this post about [How to put your Python skills to work](https://medium.com/intel-tech/how-to-put-your-python-skills-to-work-in-ai-3c581b916a41).

You will learn about the [Edge AI Certification](https://www.intel.com/content/www/us/en/developer/tools/devcloud/edge/learn/certification.html?utm_campaign=python_campaign_q322&utm_source=Medium&utm_medium=Blog&utm_content=python_blog&utm_term=edge_ai_cert) and the [30-Day AI Dev Challenge](https://devchallenge.intel.com/na_30_start?utm_campaign=python_campaign_q322&utm_source=Medium&utm_medium=Blog&utm_content=python_blog&utm_term=5_reasons_header)

Consider joining the challenge!