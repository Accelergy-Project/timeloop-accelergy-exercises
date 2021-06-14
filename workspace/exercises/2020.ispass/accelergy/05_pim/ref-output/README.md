Exercise 5
==========

## Overview

This exercise runs a energy/area reference table generation on a processing-in-memory based architecture
that is described with user-defined compound components and uses memristor based analog computation.

## Steps

To run the exercise, we need to provide 2 inputs to the Accelergy:
- An architecture description.
- A compound component description.

Since this architecture is based on emerging technologies that cannot be modeled by CACTI and conventional CMOS plug-ins.
We would also like to add an estimation plug-in necessary for processing-in-memory architecture estimations.

Please add the provided PIM estimation tables using the command

  ```
  accelergyTables -r /home/workspace/exercises/accelergy/05_pim/PIM_estimation_tables
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


## Observations

- Note that the `input/architecture.yaml` is much more complicated than the previous examples. The architecture contains three main parts, 2 global buffers, 4 NoCs for different data types, and the 168 PEs, each contain 3 local buffers and a MAC unit.
- The compound components can be specified separately to avoid long and tedious compound component descriptions. Examine the files, what is the relationship between different compound components? Are they dependent or independent? 
- What will the architecture description look like if we use primitive components to describe the architecture?
- Examine the `output/estimation.yaml`, do you see the PE processing the most sparse data have the least energy consumption? Can you tell which components are most relevent to the zero-gating optimization?
- Examine the `output/ERT.yaml`, which component's action is the most energy consuming? Can you infer which component is the most energy consuming part of the design?

## Takeaways
- We can define our own compound components and use them to define the architecture.
- Compound components can have multiple hierarchies.
- Modeling the design using compound components 
  - Reduces the architecture description and action counts complexity 
  - Makes architecture redesigns much faster as no new action counts need to be 
    generated. 
- Designs based on emerging technology can have very different energy distribution across components.
