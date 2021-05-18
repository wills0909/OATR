from figure3 import *


def opticalConsumption(Data_amount):
    dis = Data_amount * R_o / delta_o
    exponential = math.exp(Klambda * dis / math.cos(theta))
    dividend = 2 * math.pow(Data_amount, 3) * math.pow(R_o, 2) * pi * (1 - math.cos(theta_0)) * P_l
    divisor = math.pow(delta_o, 3) * eta_t * eta_r * A_r * math.cos(theta)
    fraction1 = dividend / divisor
    return exponential * fraction1 + Data_amount * E_elec


def acousticConsumption(Data_amount):
    dis = Data_amount * R_c / delta_c
    energy_acoustic = Data_amount * P_i * math.pow(dis, k) * math.pow(alpha_f, dis)
    return energy_acoustic


Optical_amount = [2000, 4000, 6000, 8000, 10000]
Acoustic_amount = [200, 400, 600, 800]

print("Fig 2(a)")
oec = 0  # optical energy consumption
for o in Optical_amount:
    oec = opticalConsumption(o)
    print('Data amount=', o, 'bit  ', 'Optical energy consumption=', oec, 'J')
print("="*30)
print("Fig 2(b)")
aec = 0  # acoustic energy consumption
for a in Acoustic_amount:
    aec = acousticConsumption(a)
    print('Data amount=', a, 'bit  ', 'Acoustic energy consumption=', aec, 'J')
