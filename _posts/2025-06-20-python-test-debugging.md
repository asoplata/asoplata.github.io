---
title: 'Python debugging inside testing'
date: 2025-06-20
permalink: /posts/2025/06/python-test-debugging
tags:
  - python
  - testing
  - debugging
---

# Table of Contents:

- [Preamble and helpful links](#preamble-and-helpful-links)
- [`pdb`: the Python debugger](#pdb-the-python-debugger)
- [Enhancing `pdb`](#enhancing-pdb)
- [Invoking `pytest`](#invoking-pytest)
- [Using `pdb` with `pytest`](#using-pdb-with-pytest)

------

# Preamble and helpful links

Firstly, here's some sites elsewhere on the web that cover the same / similar things:
- <https://seleniumbase.com/the-ultimate-pytest-debugging-guide-2021/>
- <https://docs.pytest.org/en/6.2.x/usage.html#dropping-to-pdb-python-debugger-on-failures>
- [`pytest` itself](https://docs.pytest.org/en/stable/)
- [`pdb` itself](https://docs.python.org/3/library/pdb.html#module-pdb)

Let's start by making the following assumptions:
- You're working on a Python codebase, and this codebase uses a test suite based on the [pytest](https://docs.pytest.org/en/stable/) testing framework.
- You're relatively new to both software testing and Python debugging in general.
- You have checked out the code, started adding a new feature, and have run the tests. However, the tests have broken, and in a *complex* and non-obvious way.

You may be asking: **How can I get started inspecting or debugging what the issue is?** Let's answer that.

------

# `pdb`: the Python debugger

First, let's ignore testing (`pytest`) for a moment and discuss debugging.

Many code development programs (often called Integrated Development Environments (IDEs)) include their own integrated features for debugging Python code: for VS Code [see here](https://code.visualstudio.com/docs/python/debugging), for PyCharm [see here](https://www.jetbrains.com/help/pycharm/part-1-debugging-python-code.html), and for Spyder [see here](https://docs.spyder-ide.org/5/panes/debugging.html), etc. These can be easy or difficult to use, depending on the choice of IDE, how complex your Python installation environment is, how you've setup your tests, etc.

One thing you can *always* rely on is that Python also includes *its own* support for debugging inside every Python install; this is called `pdb`, and you can find the docs here <https://docs.python.org/3/library/pdb.html#module-pdb>. Even if you mainly program in an aforementioned IDE, you can always open a command line, activate your Python environment, and then use `pdb` to debug your code. This includes using it on remote servers, wherever your code is installed (such as over `ssh`)!

The most common way to use `pdb` for debugging is to insert the following function call into your code, anywhere. Note that this is one of the few built-in functions which are *always* available ([see here](https://docs.python.org/3/library/functions.html#breakpoint)), and therefore you do not need to import anything for it (assuming you're using Python 3.7 or later)!

```python
breakpoint()
```

Let's start using a real example. Let's say you are trying to make changes to [`hnn_core`](https://hnn.brown.edu)'s `Network` class ([here](https://github.com/jonescompneurolab/hnn-core/blob/master/hnn_core/network.py)). Let's also say that you have built your own little run script that you've been using for testing and using your changes to `Network`, based off of our [firing pattern example code here](https://github.com/jonescompneurolab/hnn-core/blob/master/examples/howto/plot_firing_pattern.py). *Then* let's say that you want to inspect certain attributes in an instantiated `Network` object, just to confirm that your changes have been applied. Let's look at the code from lines 22-29 of `hnn-core/examples/howto/plot_firing_pattern.py`: <https://github.com/jonescompneurolab/hnn-core/blob/master/examples/howto/plot_firing_pattern.py#L22-L29>:

```python
###############################################################################
# Now let's build the network. We have used the same weights as in the
# :ref:`evoked example <sphx_glr_auto_examples_plot_simulate_evoked.py>`.
import matplotlib.pyplot as plt

net = jones_2009_model()

###############################################################################
```

I want to inspect what this `Network` object looks like after it's created, but before the drives are added, and one way I can do this is by adding `breakpoint()` into this file, changing the code to look like this:

```python
###############################################################################
# Now let's build the network. We have used the same weights as in the
# :ref:`evoked example <sphx_glr_auto_examples_plot_simulate_evoked.py>`.
import matplotlib.pyplot as plt

net = jones_2009_model()

breakpoint()

###############################################################################
```

Next, I run the file like normal:

```
python plot_firing_pattern.py
```

Instead of the usual output, instead I'm "dropped" into "`pdb` debugger console" that looks like the following:

```
> /Users/austinsoplata/rep/brn/hnn-core/examples/howto/plot_firing_pattern.py(29)<module>()
-> breakpoint()
(Pdb)
```

The program is now waiting on your input; this is similar to, but a little different from, a regular Python console or IPython console. The debugger has run the code up until `breakpoint()`, but not the code afterwards.

From here, you can do a lot of things, and those are shown by sending the command `h` to the debugger console (which is short for `help`):

```
> /Users/austinsoplata/rep/brn/hnn-core/examples/howto/plot_firing_pattern.py(29)<module>()
-> breakpoint()
(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    cl         disable     ignore    n        return  u          where
a      clear      display     interact  next     retval  unalias
alias  commands   down        j         p        run     undisplay
args   condition  enable      jump      pp       rv      unt
b      cont       exceptions  l         q        s       until
break  continue   exit        list      quit     source  up
bt     d          h           ll        r        step    w
c      debug      help        longlist  restart  tbreak  whatis

Miscellaneous help topics:
==========================
exec  pdb

(Pdb)
```

`h` prints out the help menu, including all the commands that you can run inside the debugger console. Again, think of the debugger console as a slightly different version of the "console" you get when you run `python` by itself. This is very powerful, and I don't have time to explain everything, but I will review some of the most common commands. See the list of websites at the beginning of this post for helpful explanations of all the commands.

`l` (short for `list`) shows us which line of code the debugger is currently stopped at, using a little arrow:

```
(Pdb) l
 24     # :ref:`evoked example <sphx_glr_auto_examples_plot_simulate_evoked.py>`.
 25     import matplotlib.pyplot as plt
 26
 27     net = jones_2009_model()
 28
 29  -> breakpoint()
 30
 31     ###############################################################################
 32     # ``net`` does not have any driving inputs and only defines the local network
 33     # connectivity. Let us go ahead and first add a distal evoked drive.
 34     # We need to define the AMPA and NMDA weights for the connections. An
```

If you also use an IDE, this is analogous to when you click and add a breakpoint to a specific line, then run your IDE's debugger, and then your IDE highlights and stops at that line.

The function `dir()` (notice the parens) will print out all the names in our namespace, including any variables we have:

```
(Pdb) dir()
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__pdb_convenience_variables', '__spec__', 'hnn_core', 'jones_2009_model', 'net', 'op', 'plt', 'read_spikes', 'simulate_dipole', 'tempfile']
```

Recall that we were interested in our `Network` object. Similarly to a `python` or `ipython` console, we can type out the name of a variable to print out its value:

```
(Pdb) net
<Network | 35 L2_basket cells
100 L2_pyramidal cells
35 L5_basket cells
100 L5_pyramidal cells>
```

We can also inspect nested attributes or methods of an object in the console as well:

```
(Pdb) net.connectivity[1]
L2_pyramidal -> L2_pyramidal
cell counts: 100 srcs, 100 targets
connection probability: 1.0
loc: 'proximal'; receptor: 'ampa'
weight: 0.0005; delay: 1.0; lamtha: 3.0
```

This could then be where you inspect to make sure that your code changes have had their desired effect.

Now, let's say we want to continue through the `plot_firing_pattern.py` file, but ONLY to the point after the first `net.add_evoked_drive(...)` function is run. There are many ways to do this but here are two:

You can use the command `n` in the debugger to advance to the "`next`" line:

```
(Pdb) n
> /Users/austinsoplata/rep/brn/hnn-core/examples/howto/plot_firing_pattern.py(38)<module>()
-> weights_ampa_d1 = {'L2_basket': 0.006562, 'L2_pyramidal': 7e-6,
(Pdb) l
 33     # connectivity. Let us go ahead and first add a distal evoked drive.
 34     # We need to define the AMPA and NMDA weights for the connections. An
 35     # "evoked drive" defines inputs that are normally distributed with a certain
 36     # mean and standard deviation.
 37
 38  -> weights_ampa_d1 = {'L2_basket': 0.006562, 'L2_pyramidal': 7e-6,
 39                        'L5_pyramidal': 0.142300}
 40     weights_nmda_d1 = {'L2_basket': 0.019482, 'L2_pyramidal': 0.004317,
 41                        'L5_pyramidal': 0.080074}
 42     synaptic_delays_d1 = {'L2_basket': 0.1, 'L2_pyramidal': 0.1,
 43                           'L5_pyramidal': 0.1}
```

See how the arrow shown after `l` indicates that the program is now at line 38. Let's run `n` a few more times, then see where we end up:

```
(Pdb) n
> /Users/austinsoplata/rep/brn/hnn-core/examples/howto/plot_firing_pattern.py(39)<module>()
-> 'L5_pyramidal': 0.142300}
(Pdb) n
> /Users/austinsoplata/rep/brn/hnn-core/examples/howto/plot_firing_pattern.py(38)<module>()
-> weights_ampa_d1 = {'L2_basket': 0.006562, 'L2_pyramidal': 7e-6,
(Pdb) l
 33     # connectivity. Let us go ahead and first add a distal evoked drive.
 34     # We need to define the AMPA and NMDA weights for the connections. An
 35     # "evoked drive" defines inputs that are normally distributed with a certain
 36     # mean and standard deviation.
 37
 38  -> weights_ampa_d1 = {'L2_basket': 0.006562, 'L2_pyramidal': 7e-6,
 39                        'L5_pyramidal': 0.142300}
 40     weights_nmda_d1 = {'L2_basket': 0.019482, 'L2_pyramidal': 0.004317,
 41                        'L5_pyramidal': 0.080074}
 42     synaptic_delays_d1 = {'L2_basket': 0.1, 'L2_pyramidal': 0.1,
 43                           'L5_pyramidal': 0.1}
```

Huh???? We just ran the "run next line" command several times, but we're still at line 38! What gives? Well, as it turns out, debuggers frequently do this for any command that spans multiple lines. They proceed through each line of the multiline command before "finishing" at the first line of the command. Only then do they proceed to the next "real" line of code. If we type `n` again, we will see that the program will not go to line 39, but instead end up at line 40 (the beginning of the next "real" command):

```
(Pdb) n
> /Users/austinsoplata/rep/brn/hnn-core/examples/howto/plot_firing_pattern.py(40)<module>()
-> weights_nmda_d1 = {'L2_basket': 0.019482, 'L2_pyramidal': 0.004317,
(Pdb) l
 35     # "evoked drive" defines inputs that are normally distributed with a certain
 36     # mean and standard deviation.
 37
 38     weights_ampa_d1 = {'L2_basket': 0.006562, 'L2_pyramidal': 7e-6,
 39                        'L5_pyramidal': 0.142300}
 40  -> weights_nmda_d1 = {'L2_basket': 0.019482, 'L2_pyramidal': 0.004317,
 41                        'L5_pyramidal': 0.080074}
 42     synaptic_delays_d1 = {'L2_basket': 0.1, 'L2_pyramidal': 0.1,
 43                           'L5_pyramidal': 0.1}
 44     net.add_evoked_drive(
 45         'evdist1', mu=63.53, sigma=3.85, numspikes=1, weights_ampa=weights_ampa_d1,
```

As expected, now we're at the next `weights...` setting line.

However, as we said before, where we really want to be is after the `net.add_evoked_drive(...` call. Another faster way to get there is the following: let's set a new, additional breakpoint from inside the debugger itself (the command `b`) at a later line (line 54):

```
(Pdb) b 54
Breakpoint 1 at /Users/austinsoplata/rep/brn/hnn-core/examples/howto/plot_firing_pattern.py:54
```

Then, we can use `c` to `continue` the program until the next breakpoint (or until the end of the program, whichever comes first):

```
(Pdb) c
> /Users/austinsoplata/rep/brn/hnn-core/examples/howto/plot_firing_pattern.py(54)<module>()
-> weights_ampa_p1 = {'L2_basket': 0.08831, 'L2_pyramidal': 0.01525,
(Pdb) l
 49     ###############################################################################
 50     # The reason it is called an "evoked drive" is it can be used to simulate
 51     # waveforms resembling evoked responses. Here, we show how to do it with two
 52     # proximal drives which drive current up the dendrite and one distal drive
 53     # which drives current down the dendrite producing the negative deflection.
 54 B-> weights_ampa_p1 = {'L2_basket': 0.08831, 'L2_pyramidal': 0.01525,
 55                        'L5_basket': 0.19934, 'L5_pyramidal': 0.00865}
 56     synaptic_delays_prox = {'L2_basket': 0.1, 'L2_pyramidal': 0.1,
 57                             'L5_basket': 1., 'L5_pyramidal': 1.}
 58
 59     # all NMDA weights are zero; pass None explicitly
```

To be clear, when a program being debugged arrives at a line with a breakpoint like line 54 above, you can think of the breakpoint as "up to, but not including" the line. In other words, *line 54 has not been executed yet*, but all the code before it has. We can confirm this by testing if `weight_ampa_p1` has been created:

```
(Pdb) weights_ampa_p1
*** NameError: name 'weights_ampa_p1' is not defined
```

The final thing I will review for typical `pdb` usage is that, just like a regular `python` or `ipython` console, you can re-define variables in the middle of the program being executed. For example, we can do the following, which will eventually break our program:

```
(Pdb) net = ['asdf']
(Pdb) net
['asdf']
```

In the middle of the program, we have changed `net` from a valid `Network` object to one that is a list with a silly string in it. If we use `c` to continue the program, it will try to run the program to the end (since there are no more breakpoints), but our program will break the next time that we use `net`, since `net` has been significantly changed:

```
(Pdb) c
Traceback (most recent call last):
  File "/Users/austinsoplata/rep/brn/hnn-core/examples/howto/plot_firing_pattern.py", line 60, in <module>
    net.add_evoked_drive(
    ^^^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'add_evoked_drive'
```

Speaking of `pdb` in general, there are other ways to invoke `pdb`, as mentioned in its [documentation](https://docs.python.org/3/library/pdb.html#module-pdb), but `breakpoint()` is probably the most frequent and easy. For example, we could start our program already inside the debugger without any pre-established breakpoints using.

```
python -m pdb plot_firing_pattern.py
```

------

# Enhancing `pdb`

There are at least several attempts to make `pdb` and related usage more user-friendly, convenient, and powerful, including both:

- `pdbpp`: <https://github.com/pdbpp/pdbpp>, my personal favorite, which is very configurable and provides things like syntax highlighting, better tab completion, "sticky mode", and seems to work in-place with `pytest` support. You can install it with `pip install pdbpp`. It specifically advertises itself as a "drop-in replacement", meaning that **it will take the place of your regular `pdb` usage by default** (which is very convenient).
- `ipdb`: <https://github.com/gotcha/ipdb>

------

# Invoking `pytest`

"Okay Austin", you say, "that's great but you've gotten off-topic from `pytest`" Correct. Let's do the converse: let's ignore `pdb` for now and only discuss how to control execution of our tests.

Most uses of `pytest` testing framework involve running the command `pytest`, followed specifically by the files where your tests are located, followed by options, such as [shown here](https://github.com/jonescompneurolab/hnn-core/blob/e80b546747e0468c5a8fdecdac3aac9b9ae80070/Makefile#L61) and pasted below:

```
pytest ./hnn_core/tests/ -m "uses_mpi"
```

This command is assumed to be running from the top-level directory of where your <https://github.com/jonescompneurolab/hnn-core> source code is located (i.e. inside `hnn-core`, *not* inside its sub-directory `hnn_core`). Let's ignore the `-m "uses_mpi` part of the `pytest` call.

You could run *all* of our tests by using the following from the command line, and from inside `hnn-core`:

```
pytest ./hnn_core/tests/
```

This runs all of the tests inside the `hnn-core/hnn_core/tests` directory.

However, let's say that you're only interested in a single one of the test files. You could run only the tests in that specific file by passing only that filename in the invocation (instead of the directory), using the following:

```
pytest ./hnn_core/tests/test_network.py
```

Let's go further, and say you're only interested in one *specific* test from that file. You can actually run only that specific test through the command-line as well! For example, let's say I only want to run the test called `test_network_models()` ([code here](https://github.com/jonescompneurolab/hnn-core/blob/master/hnn_core/tests/test_network.py#L94)) inside the file mentioned above. I would then add `::<function_name>` to the end of my command from above, as shown below:

```
pytest ./hnn_core/tests/test_network.py::test_network_models
```

If you run the above, then as part of the `pytest` output, you should see `collected 1 item` followed by the filename, followed by the test status. This enables you to examine or re-run any specific test without having to re-run the entire test suite!

-----

# Using `pdb` with `pytest`

Finally, it's time to combine our knowledge. Fortunately, `pytest` has built-in and convenient `pdb` support! All you have to do is add the `--pdb` option to your `pytest` invocation. [See docs here](https://docs.pytest.org/en/6.2.x/usage.html#dropping-to-pdb-python-debugger-on-failures).

The shortest way to get started to use the following from the command line:

```
pytest --pdb
```

However, as before, let's provide a better, more real example. Let's say I make a local change to `hnn_core/tests/test_network.py::test_network_models` ([see here](https://github.com/jonescompneurolab/hnn-core/blob/master/hnn_core/tests/test_network.py#L97)), where I change line 97 from this:

```python
    net_law = law_2021_model()
```

to this:

```python
    net_law = list()
```

When I next run my function-specific test, this will fail:

```
pytest ./hnn_core/tests/test_network.py::test_network_models
```

What are we to do? Simply add `--pdb` to the end of our command!

```
pytest ./hnn_core/tests/test_network.py::test_network_models --pdb
```

When (and WHERE) the test fails, instead of just reporting a failed test, `pytest` will "drop" us down into a `pdb` debug console like before, but *exactly where the test fails*:

```
(hc13) {15:08}~/rep/brn/hnn-core:master ✗ ➭ pytest ./hnn_core/tests/test_network.py::test_network_models --pdb
================================================================================================ test session starts =================================================================================================
platform darwin -- Python 3.13.2, pytest-8.4.0, pluggy-1.6.0
rootdir: /Users/austinsoplata/rep/brn/hnn-core
configfile: pytest.ini
plugins: xdist-3.7.0, anyio-4.9.0, cov-6.2.1
collected 1 item

hnn_core/tests/test_network.py F
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> traceback >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def test_network_models():
        """ "Test instantiations of the network object"""
        # Make sure critical biophysics for Law model are updated
        net_law = list()
        # instantiate drive events for NetworkBuilder
>       net_law._instantiate_drives(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
            tstop=net_law._params["tstop"], n_trials=net_law._params["N_trials"]
        )
E       AttributeError: 'list' object has no attribute '_instantiate_drives'

hnn_core/tests/test_network.py:99: AttributeError
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> entering PDB >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB post_mortem (IO-capturing turned off) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
> /Users/austinsoplata/rep/brn/hnn-core/hnn_core/tests/test_network.py(99)test_network_models()
-> net_law._instantiate_drives(
(Pdb)
```

This is awesome! We can now examine what the state of all the variables are when the tests fail. However, if we try to use `c` to `continue` the program in our `pdb` session, we'll just get the same output as before.

Another way that `pytest` supports `pdb` is with `breakpoint()` insertion like normal Python code. Let's go inside our `test_network.py` file, and reverse the line 97 change. Then, let's add a `breakpoint()` after it, such that our lines 97 and 98 look like:

```python
97    net_law = law_2021_model()
98    breakpoint()
```

Now, let's try to get to our breakpoint using the `pytest` invocation from above:

```
pytest ./hnn_core/tests/test_network.py::test_network_models --pdb
```

We get a `pdb` debug console, same as before:

```
(hc13) {15:26}~/rep/brn/hnn-core:master ✗ ➭ pytest ./hnn_core/tests/test_network.py::test_network_models
================================================================================================ test session starts =================================================================================================
platform darwin -- Python 3.13.2, pytest-8.4.0, pluggy-1.6.0
rootdir: /Users/austinsoplata/rep/brn/hnn-core
configfile: pytest.ini
plugins: xdist-3.7.0, anyio-4.9.0, cov-6.2.1
collected 1 item

hnn_core/tests/test_network.py
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB set_trace (IO-capturing turned off) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
> /Users/austinsoplata/rep/brn/hnn-core/hnn_core/tests/test_network.py(98)test_network_models()
-> breakpoint()
(Pdb) l
 93
 94     def test_network_models():
 95         """ "Test instantiations of the network object"""
 96         # Make sure critical biophysics for Law model are updated
 97         net_law = law_2021_model()
 98  ->     breakpoint()
 99         # instantiate drive events for NetworkBuilder
100         net_law._instantiate_drives(
101             tstop=net_law._params["tstop"], n_trials=net_law._params["N_trials"]
102         )
103
(Pdb)
```

Thus, we can use `breakpoint()` to investigate our test code just like we can use it for normal code. Note that the `--pdb` option isn't strictly necessary in this instance (we've explicitly provided a `breakpoint()`), but anytime you are debugging tests, it is good to have it.

If you want to get to a `pdb` debug console at the beginning of the test, rather than waiting until things break, you can pass `--trace` to `pytest` instead of `--pdb`: [see here in the `pytest` docs](https://docs.pytest.org/en/6.2.x/usage.html#dropping-to-pdb-python-debugger-at-the-start-of-a-test).

In my personal experience, debugging stand-alone scripts or code using IDE debuggers tends to be pretty straightforward, but debugging `pytest` calls from an IDE tend to be *much* harder to configure and get working. If you are trying to debug `pytest` tests specifically, you may find it easier to use these above `pdb`-based methods instead of your IDE. They'll also work everywhere.

Note: whenever you are debugging your tests, it is recommended to *not* run independent tests in parallel, such as what we do by default using `-n auto` in our default `pytest` calls here <https://github.com/jonescompneurolab/hnn-core/blob/master/Makefile#L60> (`-n auto` is provided by `pytest-xdist`, not regular `pytest`). If you insert a `breakpoint()` or try to invoke a `pdb` debug console session for tests that are running fully parallel, you may get multiple cores entering a debug console session simultaneously, and the input/output may be garbled. Instead, it is recommended to 1. only run the most specific tests you can at a time (such as a single function or file), and 2. run them without the `-n auto` arguments, so that all tests are run serially.

