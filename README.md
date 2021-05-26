# OATR——《Optimum Data Transmission Allocation in Multimodal Communication of Underwater Sensor Networks》

####  This letter investigates the optimum data transmission allocation in the underwater MC. Considering the fundamental MC tradeoff, the MC energy efficiency model is established and formulated as a mixed integer nonlinear programming problem with the provable convex optimization properties. Simulation results validate the effectiveness of this letter.

#### Simulation setup
The simulations employ the experimental platform
developed using Python. GNs and SNs
are randomly deployed in the 2 km × 2 km × 1.6 km cubic
area and the depth is chosen at random between
50 m and 200 m. The AC transmission rate is set to 10
Kbps, and the OC transmission rate is set to 10 Gbps. AUV
traverses through the underwater environment following the
traditional lawn mower path. Suppose the time for AUV to traverse all GNs in
the network is T. Llim is set to 5000 bits. The other main
parameters are shown in Table below. 

![Other main parameters](https://images.gitee.com/uploads/images/2021/0526/152705_e67b3bc4_9091576.png "屏幕截图.png")

#### File description

1.  The network model is created using the  **network_model.py** that contains the settings for all our main parameters, which you can change manually.
2.  The  **get_optimum_omega.py** is used to calculate the $ω_o$, a parameter whose value is related to the total amount of data $L$.
3.  In this letter, two algorithms are proposed and we implement them in  **algorithms.py**.
4.  The  **figure2.py**, **figure3.py**, **figure4.py**, and **figure5.py** are used to generate the data of figure 2 to figure 5, respectively.

#### How to use?

1.  Before experimenting, make sure your development environment is ** Anaconda+Pycharm**.
2.  Create an empty python project in the IDE and configure the interpreter as Anaconda.
3.  Copy all the files of this project into the new project you just created.
4.  Running the **figure2.py**, **figure3.py**, **figure4.py**, and **figure5.py** yields the data in Figures 2 to 5, and running the **get_optimum_omega.py** will give you $ω_o$. 

