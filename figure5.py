from network_model import *
from algorithms import *

if __name__ == "__main__":
    initialization(L, R_o, delta_o)
    count = 0
    omega_o = getOptOmegao(L)
    omega_c = 1 - omega_o
    # AUV starts moving.
    auv_walk(auv, Gateway_Node_List)
    total = 0  # total energy consumption
    STAY_DISTANCE_OPT = omega_o * L * R_o / delta_o
    print("optimum stay distance=", STAY_DISTANCE_OPT * 1000, 'm')
    print("input stay distance =", STAY_DISTANCE * 1000, "m")
    for gn in Gateway_Node_List:
        total += gn.energy_consumption
        break
    print("Data amount=", L, 'bit   ', "total consumption=", total, 'J')
