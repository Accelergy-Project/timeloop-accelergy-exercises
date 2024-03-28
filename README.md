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

##  Related reading
 - [Timeloop/Accelergy documentation](https://timeloop.csail.mit.edu/)
 - [Timeloop/Accelergy tutorial](http://accelergy.mit.edu/tutorial.html)
 - [SparseLoop tutorial](https://accelergy.mit.edu/sparse_tutorial.html)
 - [eyeriss-like design](https://people.csail.mit.edu/emer/papers/2017.01.jssc.eyeriss_design.pdf)
 - [simba-like architecture](https://people.eecs.berkeley.edu/~ysshao/assets/papers/shao2019-micro.pdf)
