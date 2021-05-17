from option_parameters import *

# This file is to figure out the relationship between total energy consumption with Ratio of acoustic and optical
# You can change Node number, Data amount:L and the ratio.
Node_number = 50  # 30, 35, 40, 45, 50
L = 2000
DATASIZE_OPTICAL = 1800  # Fig.4b OATR
AOC = 2000  # Fig.4b AOC
AAC = 0  # Fig.4b AAC
import math

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
# These is the setup of our simulation.Don't change this parameters please!!!
# ================================================================


# define a function of total consumption
def total(l,optical_data):
    """
    :param l: data size
    :param optical_data: data optical
    :return: total consumption
    """

    L = l
    omega_o = optical_data/L
    omega_c = 1 - omega_o
    exponential = math.exp(Klambda * optical_data * R_o / delta_o /math.cos(theta))


    fraction1 = 2 * math.pow(optical_data, 3) * math.pow(R_o, 2) * pi * (1 - math.cos(theta_0)) * P_l \
                / math.pow(delta_o, 3) /eta_t / eta_r / A_r / math.cos(theta)

    energy_optical = exponential * fraction1 + optical_data * E_elec

    fraction2 = omega_c * L * R_c / delta_c

    energy_acoustic = omega_c * L * P_i * math.pow(fraction2, k) * math.pow(alpha_f, fraction2) #+ L*P_r

    return energy_optical + energy_acoustic

print("="*20)
print("Fig.2")
print("="*20)
print("only acoustic")
print("one node energy consumption(J),data amount=1000,1500,2000,2500,3000,3500,4000,4500,5000")
print(total(1000, 0))
print(total(1500, 0))
print(total(2000, 0))
print(total(2500, 0))
print(total(3000, 0))
print(total(3500, 0))
print(total(4000, 0))
print(total(4500, 0))
print(total(5000, 0))



print("only optical")
print("one node energy consumption(J),data amount=1000,1500,2000,2500,3000,3500,4000,4500,5000")
print(total(1000, 1000))
print(total(1500, 1500))
print(total(2000, 2000))
print(total(2500, 2500))
print(total(3000, 3000))
print(total(3500, 3500))
print(total(4000, 4000))
print(total(4500, 4500))
print(total(5000, 5000))


print("="*20)
print("Fig.4a")
print("="*20)
print("when omega=optimum ratio")
print("one node energy consumption(J),data amount=1000,1500,2000,2500,3000,3500,4000,4500,5000")
print(total(1000, 970))
print(total(1500, 1460))
print(total(2000, 1941))
print(total(2500, 2422))
print(total(3000, 2900))
print(total(3500, 3378))
print(total(4000, 3854))
print(total(4500, 4329))
print(total(5000, 4803))



print("="*20)
print("OATR = 9:1")
print(total(1000, 900))
print(total(1500, 1350))
print(total(2000, 1800))
print(total(2500, 2250))
print(total(3000, 2700))
print(total(3500, 3150))
print(total(4000, 3600))
print(total(4500, 4050))
print(total(5000, 4500))

print("="*20)
print("Fig.4b")
print("="*20)
total_consumption = 0
for _ in range(Node_number):
    total_consumption += total(L,DATASIZE_OPTICAL)
print('OATR consumption:',total_consumption,'Node numbers:',Node_number)
total_consumption = 0
for _ in range(Node_number):
    total_consumption += total(L,AOC)
print('AOC consumption:',total_consumption,'Node numbers:',Node_number)  
total_consumption = 0
for _ in range(Node_number):
    total_consumption += total(L,AAC)  
print('AAC consumption:',total_consumption,'Node numbers:',Node_number)
