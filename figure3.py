# This file is to figure out the relationship between total energy consumption with Ratio of acoustic and optical
# You can change Node number, Data amount:L and the ratio.

from get_optimum_omega import *
import math


# define a function of total consumption
def totalConsumption(DataAmout, OpticaRatio):
    dis1 = OpticaRatio * DataAmout * R_o / delta_o
    dis2 = (1 - OpticaRatio) * DataAmout * R_c / delta_c
    exponential = math.exp(Klambda * dis1 / math.cos(theta))
    dividend = 2 * math.pow(OpticaRatio * DataAmout, 3) * math.pow(R_o, 2) * pi * (1 - math.cos(theta_0)) * P_l
    divisor = math.pow(delta_o, 3) * eta_t * eta_r * A_r * math.cos(theta)
    fraction1 = dividend / divisor
    energy_acoustic = (1 - OpticaRatio) * DataAmout * P_i * math.pow(dis2, k) * math.pow(alpha_f, dis2)
    return exponential * fraction1 + OpticaRatio * DataAmout * E_elec + energy_acoustic


if __name__ == "__main__":
    V = [1000, 2000, 3000, 4000, 5000]  # V can be 1000 or 2000 or 3000 or 4000 or 5000
    print("Here is the energy consumption vs. data amount of fig.3, V equals 1000 or 2000 or 3000 or 4000 or 5000.")
    print("=" * 20)
    for v in V:
        print("Data amount=", v, 'bit')
        print(totalConsumption(DataAmout=v, OpticaRatio=0.85))
        print(totalConsumption(DataAmout=v, OpticaRatio=0.9))
        print(totalConsumption(DataAmout=v, OpticaRatio=0.95))
        print(totalConsumption(DataAmout=v, OpticaRatio=1))
