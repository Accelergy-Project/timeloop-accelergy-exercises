Exercise 6
==========

## Overview

In this exercise, we present a set of detailed architecture and constraints specifications used to describe the Eyeriss accelerator architecture. The constraints include directives to model the _Row Stationary_ dataflow. We use a 7-deep loop nest representing a full Convolutional Neural Network layer as the input problem. We run the mapper on an example instance of the layer shape to find an optimal mapping on the Eyeriss architecture and derive performance, energy and other statistics from the execution.

## Steps and Observations

Take a look at the YAML files describing the problem, architecture, mapspace constraints and mapper configuration.
* The problem should be fairly straightforward to understand, but note the use of a new directive called `coefficients`, which are used to set up the _stride_ and _dilation_ parameters used in index calculation.
* The architecture spec is more complex, but the hierarchical structure is just a logical extension of the topologies we have looked at in prior examples.
* The mapspace constraints may look daunting, but they follow the same rules as the constraints in the previous exercise and set up factor, permutation and bypass constraints for each temporal and spatial tiling level in the architecture.
* The mapper configuration contains a new flag called `live-status`. This triggers an ncurses-based UI screen that allows you to track the activity of all mapper threads.

To run the exercise, type:
```
timeloop-mapper prob/cnn-layer.prob.yaml    \
                arch/eyeriss-256-arch.yaml  \
                mapper/mapper.yaml          \
                constraints/cnn-layer-eyeriss-256-rs.constraints.yaml
```

The status screen shows the following per-thread statistics:
* Total mappings visited.
* Invalid mappings rejected (because of capacity violations or spatial fanout violations).
* Valid mappings modeled.
* Consecutive invalid mappings rejected.
* Sub-optimal valid mappings evaluated since the last update of the optimal mapping.
* Stats for the optimal mapping seen thus far.

As usual, you can use Ctrl+C to gracefully terminate the mapper.

There are no suggested incremental steps or expected observations for this exercise at this time. We will have a combined Timeloop+Accelergy lab exercise based on this architecture after the Accelergy presentation.
