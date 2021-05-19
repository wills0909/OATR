import math
import numpy as np
import operator

# This is the setup of our simulation. Don't change the parameters please!!!
# ==================================================================
theta_0 = 60 # angle
theta = 5
pi = math.pi
R_o = 2.25e05 # 2.25×105km/s
R_c = 1.5  # 1.5km/s
P_l = 30  # 30w
P_i = 0.0002  # 0. 0002w
P_r = 0.000035
Klambda = 0.398  # 0.398
delta_o = 1e10  # 10000000000bps
delta_c = 1e4 # 10000bps
eta_t = 0.9
eta_r = 0.9
A_r = 1.7e-05
E_elec = 1e-08  #
k = 1.5
f = 10  # 10kHz
alpha_f = 1.187029939
# This is the setup of our simulation. Don't change the parameters please!!!
# ================================================================

# You can change these parameters.
# ==========================================================

NODE_NUMBER = 50 # Number of gateway node
Range = 2000   # Network range 2*2*1.6
Height = 1600
L = 4000   # L is the data amount(bit)
omega_o = 0
omega_c = 1-omega_o


DATASIZE_OPTICAL = omega_o * L # bit
DATASIZE_ACOUSTIC = omega_c * L # bit

# Optimum distance of optical communication
STAY_DISTANCE_OPT = omega_o * L * R_o / delta_o

# Not optimum distance, AUV communicates with GN when their distance equals DISTANCE
STAY_DISTANCE = 100e-03  # Km

# ==========================================================
# You can change these parameters.

def total(l,optical_data):
    """
    :param l: data size
    :param optical_data: data optical
    :return: total consumption
    """
    L = l
    omega_o = optical_data/L
    omega_c = 1 - omega_o
    exponential = math.exp(Klambda * omega_o * L * R_o / delta_o / math.cos(theta))
    fraction1 = 2 * math.pow(omega_o * L, 3) * math.pow(R_o, 2) * pi * (1 - math.cos(theta_0)) * P_l / \
                (math.pow(delta_o, 3)*eta_t * eta_r * A_r * math.cos(theta))
    energy_optical = exponential * fraction1 + omega_o * L * E_elec
    print(energy_optical)
    fraction2 = omega_c * L * R_c / delta_c
    energy_acoustic = omega_c * L * P_i * math.pow(fraction2, k) * math.pow(alpha_f, fraction2) #+  L*P_r
    #print(energy_acoustic)
    return energy_optical + energy_acoustic

def optical_consumption(distance):
    # L = l
    # omega_o = optical_data / L
    # omega_c = 1 - omega_o
    omega_o = getOptOmegao(L)
    exponential = math.exp(Klambda * distance / math.cos(theta))
    fraction1 = 2 * math.pow(omega_o * L, 3) * math.pow(R_o, 2) * pi * (1 - math.cos(theta_0)) * P_l / \
                (math.pow(delta_o, 3)*eta_t * eta_r * A_r * math.cos(theta))
    return exponential * fraction1 + omega_o * L * E_elec

def acoustic_consumption(distance):
    #fraction2 = omega_c * L * R_c / delta_c
    omega_o = getOptOmegao(L)
    omega_c = 1 - omega_o
    energy_acoustic = omega_c * L * P_i * math.pow(distance, k) * math.pow(alpha_f, distance) # + L*P_r
    return energy_acoustic

def get_distance(sensor1, sensor2):
    temp = (sensor1.x - sensor2.x) * (sensor1.x - sensor2.x) + (sensor1.y - sensor2.y) * \
           (sensor1.y - sensor2.y) +(sensor1.z - sensor2.z)*(sensor1.z - sensor2.z)
    return math.sqrt(temp)/1000

def partialDerivative(o, data_amount):
    L = data_amount
    part1 = (6 * o * o * math.pow(L, 3) * math.pow(R_o, 2) * pi * (1 - math.cos(theta_0)) * P_l
             * math.exp(Klambda * o * L * R_o / delta_o / math.cos(theta))) \
            / (math.pow(delta_o, 3) / eta_t / eta_r / A_r / math.cos(theta))

    part2 = (2 * Klambda * math.pow(o, 3) * math.pow(L, 4) * math.pow(R_o, 3) * pi * (1 - math.cos(theta_0)) * P_l
             * math.exp(Klambda * o * L * R_o / delta_o / math.cos(theta))) \
            / math.pow(delta_o, 4) / eta_t / eta_r / A_r / math.cos(theta) / math.cos(theta)
    part3 = L * E_elec - (k + 1) * L * P_i * math.pow((1 - o) * L * R_c / delta_c, k) * math.pow(alpha_f, (
            1 - o) * L * R_c / delta_c)
    part4 = L * P_i * math.pow((1 - o) * L * R_c / delta_c, k + 1) \
            * math.pow(alpha_f, (1 - o) * L * R_c / delta_c) * math.log(alpha_f)

    return part1 + part2 + part3 - part4

# This function is to find the optimum optical ratio.
def getOptOmegao(data_amount):
    root_list = np.arange(0.8, 1, 0.001)
    tmp = []
    for r in root_list:
        t = abs(partialDerivative(r, data_amount) - 0)
        # print(t)
        tmp.append(t)

    index = 0
    num = tmp[0]
    for i in range(len(tmp)):
        if tmp[i] < num:
            num = tmp[i]
            index = i
    return root_list[index]

class AUV():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Sensor():
    def __init__(self, x, y,z, gn):
        self.x = x
        self.y = y
        self.z = z
        self.parent_node = gn
    
class GatewayNode():

    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z
        self.id = 0
        self.energy_consumption = 0 
        
    def communicate_acoustic(self, distance):
        # Radius = omega_c * L * R_c / delta_c
        # # print(Radius)
        # if abs(distance*-Radius)*1000 <= 0.01:
        self.energy_consumption += acoustic_consumption(distance)
    
    def communicate_optical(self, distance):
        if abs(distance * 1000 - STAY_DISTANCE * 1000) <= 0.01:
            self.energy_consumption += optical_consumption(STAY_DISTANCE)
# ==========================================================
# Initialization

x_axis = range(Range)
y_axis = range(Range)
z_axis = range(Height)
# print(x_axis)
# print(y_axis)
# print(z_axis)
# Auv initialization
auv = AUV(0, 0, 0)
# Gateway node initialization through Monte carlo simulation.
np.random.seed(9999)
a = np.random.randint(0, Range, size=[NODE_NUMBER, 2])
#print(a)
Gateway_Node_List = []
for _ in a:
    gn = GatewayNode(_[0], _[1], Height/2)
    Gateway_Node_List.append(gn)

cmpfun = operator.attrgetter('x')
Gateway_Node_List.sort(key=cmpfun, reverse=False)

