Exercise 0
==========

## Overview

This exercise runs a 1D convolution on a toy architecture with a single PE consisting of a small register and a scalar MACC unit.

## Steps

To run the exercise, we need to provide 3 inputs to the Timeloop model:
- An architecture.
- A problem.
- A mapping.

We have provided a separate `.yaml` file for each of these inputs. To run the exercise, type:

```
    timeloop-model *.yaml
```

This generates the following outputs:
- Overall performance (in terms of hardware utilization fraction) and energy efficiency (in terms of pJ/MACC) are reported on `stdout`.
- Detailed statistics are saved to `timeloop-model.stats.txt`.
- A pretty-printed form of the mapping is saved to `timeloop-model.map.txt`.

## Observations

- Look at the structure of the `timeloop-model.stats.txt` file.
  - It is divided into sections, one for each Arithmetic and Storage level in the hardware topology.
  - Each section reports the level's specs (which may be user-defined, derived or default), followed by statistics from the model's execution of the mapping.
  - Some statistics are separated out into sub-sections for each data-space (such as Weights, Inputs, etc.)
  - By convention, statistics for a network connecting an outer storage level to an inner storage level are reported as part of the outer level's statistics.
  - In these exercises, some statistics are reported as 0 because we are using a simple technology model for the tutorial.
- The only storage level is `Buffer`, which both acts as the backing store for all operand and result data-spaces, as well as the sole operand source and result destination for each arithmetic operation.
- Note that tiles of "Outputs" are actually partial sums. Accesses to partial sums inside buffers are Read-Modify-Update operations. Look at the number of reads and updates of Outputs at the Buffer. Are they equal?
