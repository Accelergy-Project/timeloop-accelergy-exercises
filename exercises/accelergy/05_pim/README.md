Exercise 4
==========

## Overview

This exercise runs a energy/area reference table generation on a processing-in-memory based, more specifically memristor-based,
architecture that is described with user-defined compound components.

## Steps

To run the exercise, we need to provide 3 inputs to the Accelergy:
- An architecture description.
- A compound component description.

Since processing-in-memory based architecture is based on emerging technology, 
the current CACTI and conventional CMOS are not able to perform energy estimations. 
We add a set of PIM-related estimation tables by adding a new root to the table based plug-in.

Please add the provided PIM estimation tables using the command

  ```
  accelergyTables -r <path to this repo>/PIM_estimation_tables
  ```

We have provided the `.yaml` files in the input folder. To run this exercise, type: 

```
    accelergy input/ -o output/ 
```

This generates the following output in folder `output/`
- The received input files and the important evaluation progress are reported on `stdout`.
- The energy reference tables (ERTs) (pJ/action) for the components in the architecture `ERT.yaml`.
- The energy reference table summary for the components in the architecture `ERT_summary.yaml`.
- The area reference tables (ERTs) (umm^2/component) for the components in the architecture `ART.yaml`(note that the DRAM area is a place holder as it is not on-chip).
- The area reference table summary for the components in the architecture `ART_summary.yaml`.
- The flattened architecture that describes the class and attributes of the components in
the architecture is saved to `flattened_architectue.yaml`.
- The estimation (pJ) for the primitive components in the design are saved in `energy_stimation.yaml`.


## Observations

- Note that the `input/architecture.yaml` is much more complicated than the previous examples. The architecture contains three main parts, 2 global buffers, 4 NoCs for different data types, and the 168 PEs, each contain 3 local buffers and a MAC unit.
- The compound components can be specified separately to avoid long and tedious compound component descriptions. Examine the files, what is the relationship between different compound components? Are they dependent or independent? 
- Can you find the necessary components related to analog/digital conversions?
- Is this the only way to define the architecture and compound components?
- What will the architecture description look like if we use primitive components to describe the architecture?
- Examine the `output/ERT.yaml`, which component has the most energy consuming actions?
- Examine the `output/ERT.yaml` and `output/ART.yaml`, 
is memristor-based MAC more energy and area efficient comparing to conventional digital MACs?


## Takeaways
- Compound components can be defined with more hierarchies, 
i.e., the subcomponent of a compound component can also be a compound component.
- Architectures with emerging technology can result in very different energy distributions across various components.
- Architecture and compound components are closed related, we can have various ways of defining them.