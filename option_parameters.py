R_o = 2.25*100000
delta_o = 10000000000
from network_model import *
# You can change these parameters
# ==========================================================

NODE_NUMBER = 20  # number of gateway node
Range = 300   # network range 500 * 500 * 500
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