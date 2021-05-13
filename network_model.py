import math
import option_parameters
import numpy as np
# These is the setup of our simulation,don't change this parameters!!!

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
# These is the setup of our simulation,don't change this parameters!!!
# ================================================================

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
    exponential = math.exp(Klambda * distance/1000 / math.cos(theta))
    fraction1 = 2 * math.pow(option_parameters.omega_o * option_parameters.L, 3) * math.pow(R_o, 2) * pi * (1 - math.cos(theta_0)) * P_l / \
                (math.pow(delta_o, 3)*eta_t * eta_r * A_r * math.cos(theta))

    return exponential * fraction1 + option_parameters.omega_o * option_parameters.L * E_elec

def acoustic_consumption():

    fraction2 = option_parameters.omega_c * option_parameters.L * R_c / delta_c
    energy_acoustic = option_parameters.omega_c * option_parameters.L * P_i * math.pow(fraction2, k) * math.pow(alpha_f, fraction2) # + L*P_r
    return energy_acoustic

def get_distance(sensor1, sensor2):
    temp = (sensor1.x - sensor2.x) * (sensor1.x - sensor2.x) + (sensor1.y - sensor2.y) * \
           (sensor1.y - sensor2.y) 
    return math.sqrt(temp)

class AUV():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 50

class Sensor():
    def __init__(self, x, y, gn):
        self.x = x
        self.y = y
        self.z = 50
        self.parent_node = gn
    
class GatewayNode():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 50 # let z = 50 to reduce time complexity
        self.id = 0
        self.energy_consumption = 0 
        
    def communicate_acoustic(self,auv):
        dis = get_distance(auv,self)
        Radius = option_parameters.omega_c * option_parameters.L * R_c / delta_c
        if dis<=Radius:
            self.energy_consumption += acoustic_consumption()
    
    def communicate_optical(self,auv,distance):
        if abs(get_distance(auv,self)-distance*1000) < 0.01:
            self.energy_consumption += optical_consumption(distance)

