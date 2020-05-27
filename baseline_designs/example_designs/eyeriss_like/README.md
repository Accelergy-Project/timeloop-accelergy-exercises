Eyeriss-Like Architecture
----------------------------
This folder contains an architecture based on the Eyeriss design description proposed
[here](https://people.csail.mit.edu/emer/papers/2017.01.jssc.eyeriss_design.pdf).

Q&As:
----------------------------
1. Why is the technology different?

   Since the open-sourced energy estimation plug-ins have the most flexible support
    for the 45nm components, we changed the technology to 45nm.
    
2. What is the usage of the "DummyBuffer"?

   DummyBuffer is place-holder memory block that helps timeloop to correctly model 
   the row stationary mappings. With the insertion of the Dummybuffer, we can map 
   M dimension to both the rows of the PE and cols of PE -- otherwise, timeloop can 
   only map the model dimensions to either the rows or columns of the PE array.
   
3. Doe this design perform exactly as the Eyeriss design in the paper?
    
   For many cases, it does. However, since timeloop's mapper is not as flexible as a manually 
   generated mapping, sometimes, it does not produce the exact results as shown in the paper.
   The main limitation is that timeloop considers the factors of a dimension, e.g., 4 is a factor 
   of 256, when it performs mapping space explorations. Therefore, when using a non-divisible factor 
   result in better mappings, timeloop is not able to find it. However, padding the workload dimensions 
   will solve these types of problems.
   
4. How long do the Timeloop simulations take?
  
   Depending on your workload, the simulation takes various amount of time to finish. Generally, they should 
   converge within 30 mins. You can manually stop the exploration when you see things are converging by 
   pressing `ctrl + C`. They sometimes will take much longer to automaticaly stop as we set the converging cretiria to be pretty high to avoid early-stop with subooptimal mappings. Use you own
   judgement.
   



