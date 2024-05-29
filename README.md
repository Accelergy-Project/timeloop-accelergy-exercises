Fibertree/Timeloop/Accelergy Tutorial Exercises
======================================

This repository contains a set of exercises and baseline designs to explore Fibertrees, Timeloop, and Accelergy.
Please find the respective directories and more detailed descriptions under `workspace` folder.

## Using Docker

We provide a docker with built-in tools for you to get started

- Make a copy of the provided template docker compose file: `cp docker-compose.yaml.template docker-compose.yaml`
- Examine the instructions in `docker-compose.yaml` to setup the docker correctly, e.g., setup the correct `UID` and `GID`.
- Pull the newest docker image: `docker-compose pull`
- Run docker: `docker-compose up`. You should see the docker being setup.
- This docker uses Jupyter notebooks, and you will see an URL once the docker is up. Please copy and paste the URL
to a web browser of your choice to access the workspace. 

##### Notes (if notebook URL does not work)
- Option1: in your `docker-compose.yaml` file, uncomment the last line under `environment` to disable token and try again
- Option2: try the 192.168.X.X host with the same token as shown in the output (X.X can be obtained by `hostname -I`)
- Option3: if you have access to docker GUI app (e.g., Kitematic for docker temrinal), try open the web page there with the token


## Native Installation

Please find the instructions for native installations of the tools needed [here](https://timeloop.csail.mit.edu/installation)

## Related reading
 - [Timeloop/Accelergy documentation](https://timeloop.csail.mit.edu/)
 - [Timeloop/Accelergy tutorial](http://accelergy.mit.edu/tutorial.html)
 - [SparseLoop tutorial](https://accelergy.mit.edu/sparse_tutorial.html)
 - [eyeriss-like design](https://people.csail.mit.edu/emer/papers/2017.01.jssc.eyeriss_design.pdf)
 - [simba-like architecture](https://people.eecs.berkeley.edu/~ysshao/assets/papers/shao2019-micro.pdf)

## Citation
Please cite the following:

- A. Parashar, P. Raina, Y. S. Shao, Y.-H. Chen, V. A. Ying, A. Mukkara, R. Venkatesan, B. Khailany, S. W. Keckler, and J. Emer, “Timeloop: A systematic approach to DNN accelerator evaluation,” in 2019 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS), 2019, pp. 304–315.
- M. Horeni, P. Taheri, P. Tsai, A. Parashar, J. Emer, and S. Joshi, “Ruby: Improving hardware efficiency for tensor algebra accelerators through imperfect factorization,” in 2022 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS), 2022, pp. 254–266.
- Y. N. Wu, P.-A. Tsai, A. Parashar, V. Sze, and J. S. Emer, “Sparseloop: An analytical, energy-focused design space exploration methodology for sparse tensor accelerators,” in 2021 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS), 2021, pp. 232–234.
- Y. N. Wu, J. S. Emer, and V. Sze, “Accelergy: An architecture-level energy estimation methodology for accelerator designs,” in 2019 IEEE/ACM International Conference on Computer-Aided Design (ICCAD), 2019, pp. 1–8.
- T. Andrulis, J. S. Emer, and V. Sze, “CiMLoop: A flexible, accurate, and fast compute-in-memory modeling tool,” in 2024 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS), 2024.

Or use the following BibTeX:

```BibTeX
@inproceedings{timeloop,
  author      = {Parashar, Angshuman and Raina, Priyanka and Shao, Yakun Sophia and  Chen, Yu-Hsin and Ying, Victor A and Mukkara, Anurag and Venkatesan, Rangharajan and Khailany, Brucek and Keckler, Stephen W and Emer, Joel},
  booktitle   = {2019 IEEE international symposium on performance analysis of systems and software (ISPASS)}, pages={304--315}, year={2019},
  title       = {Timeloop: A systematic approach to dnn accelerator evaluation},
  year        = {2019},
}
@inproceedings{ruby,
  author      = {M. Horeni and P. Taheri and P. Tsai and A. Parashar and J. Emer and S. Joshi},
  booktitle   = {2022 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS)},
  title       = {Ruby: Improving Hardware Efficiency for Tensor Algebra Accelerators Through Imperfect Factorization},
  year        = {2022},
}
@inproceedings{sparseloop,
  author      = {Wu, Yannan N. and Tsai, Po-An, and Parashar, Angshuman and Sze, Vivienne and Emer, Joel S.},
  booktitle   = {{ ACM/IEEE International Symposium on Microarchitecture (MICRO)}},
  title       = {{Sparseloop: An Analytical Approach To Sparse Tensor Accelerator Modeling }},
  year        = {{2022}}
}
@inproceedings{accelergy,
  author      = {Wu, Yannan Nellie and Emer, Joel S and Sze, Vivienne},
  booktitle   = {2019 IEEE/ACM International Conference on Computer-Aided Design (ICCAD)},
  title       = {Accelergy: An architecture-level energy estimation methodology for accelerator designs},
  year        = {2019},
}
@inproceedings{cimloop,
  author      = {Andrulis, Tanner and Emer, Joel S. and Sze, Vivienne},
  booktitle   = {2024 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS)}, 
  title       = {{CiMLoop}: A Flexible, Accurate, and Fast Compute-In-Memory Modeling Tool}, 
  year        = {2024},
}
```
