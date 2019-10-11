Exercise 5
==========

## Overview

In this exercise, we will use Timeloop's **mapper** to automatically construct and explore the _mapspace_ (i.e., the space of legal mappings) of a problem on an architecture. To keep the mapspace manageable for this tutorial setting, we revert back to the 1D Convolution with Output Channels problem shape and the 3-level temporal architecture from Exercise 3.

## Steps and Observations

Similar to the model, the mapper needs:
* An architecture.
* A problem.

However, unlike the model, the mapper does not need an explicit mapping (it finds those for us). Instead, it needs:
* An optional set of _constraints_ to restrict the mapspace (grouped under the YAML configuration key `mapspace_constraints`).
* A set of options for the mapper application itself, including user-interface glags and directives to guide the search heuristics (grouped under the YAML configuration key `mapper`).

1. Verify that the `arch/3level.arch.yaml` and `prob/conv1d+oc.prob.yaml` are identical to those from Exercise 3.

2. Study the three constraints files in `constraints`:
   1. `conv1d+oc-3level-baked.constraints.yaml`. In this example, we have abused the constraints system to completely "bake" every single variable of the mapspace to reduce it down to a size of 1. In fact, this single remaining mapping is identical to the mapping we used in Exercise 3 (map/conv1d+oc-3level.map.yaml). The syntax is nearly identical, but the semantics are subtly different.
   2. `conv1d+oc-3level-baked.constraints.yaml`: In this example, we lock down all factorizations and permutations in the mapping, but leave bypassing un-specified. This allows the mapper to explore all bypassing options.
      > Be careful about how Bypass directives are treated by the model vs. the mapper. If you don't specify any bypass directives in a mapping, the model assumes they are set to `keep` (i.e., do not bypass). Remember that a mapping cannot have any non-determinism. However, the mapper treats anything left un-specified in the constraints as options to explore in the mapspace. If you want to lock down a specific bypass strategy, you need to create an explicit constraint to restrict the mapper.
   3. `constraints/null.constraints.yaml`: In this example, we remove all constraints and let the mapper explore the complete mapspace.

3. Look at the `mapper/exhaustive.mapper.yaml` file. The directives here instruct the mapper to exhaustively explore the complete mapspace. Observe:
   1. The `optimization-metric` gives the mapper a prioritized list of metrics to compare mappings. In this example, `delay` is the highest priority. If two mappings have the same delay, they will be compared based on `energy`. The set of metrics supported today include `energy`, `delay`, `edp` (energy-delay product), and `last-level-accesses`, but this list can be trivially expanded to _any_ metric that the model generates (as in `stats.txt`) with just a few lines of code.
   2. The mapper can launch multiple threads to speed up the search. It will divide up the mapspace among all threads. If the `num-threads` directive isn't specified, the mapper will query the underlying host for the number of available CPU contexts and use that many threads.



Takeaways
=========
While we used constraints to understand the mapper's behavior in this exercise, in practice constraints are used to represent hardware capabilities (or rather, incapabilities). Many hardware accelerators aren't designed to be flexible enough to execute any pattern of data-movement loop nests that a mapper can throw at them. They are restricted (with good reason) to execute a limited set of alternative shapes of mappings, or _dataflows_. This simplifies the hardware design of networks and internal state machines. Timeloop's constraints language is intended to capture these hardware characteristics. In the next exercise, we will work with a detailed specification of the Eyeriss architecture, which includes both an architecture spec as well as a comprehensive set of constraints, including directives to model the _Row Stationary_ dataflow.
