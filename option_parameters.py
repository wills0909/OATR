R_o = 2.25*100000
delta_o = 10000000000
from network_model import *
# You can change these parameters
# ==========================================================
# It is assumed that GNs and SNs are randomly deployed in the 2 km × 2 km × 1.6 km cubic
# underwater area and the depth is chosen at random between 50 m and 200 m. Monte Carlo 
# method is conducted and 50 GNs are set up in the experiment.
NODE_NUMBER = 50  # number of gateway node

Range = 2000   # cube 2000x2000x1600
height =1600

omega_c = 0.03  # you can change it as you want, notice omega_c+omega_o = 1
omega_o = 0.97
L = 1000   # L is the data amount(bit)
DATASIZE_OPTICAL = omega_o * L # bit
DATASIZE_ACOUSTIC = omega_c * L # bit

# optimum distance of optical communication
DISTANCE_OPT = omega_o * L * R_o / delta_o

# Not optimum distance,AUV communicates with GN when their distance equals DISTANCE
DISTANCE = 50e-03  # Km

# ==========================================================
# You can change these parameters.
