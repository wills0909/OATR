from network_model import *


# Algorithm 1: Packet segmentation.
def initialization(L, R_o, delta_o):
    packets = [L]
    LLim = 5000
    while (True):
        if L > LLim:
            L %= LLim
            omega_o = getOptOmegao(L)
            D = L * omega_o * R_o / delta_o
            packets.append(L)
        else:
            break
    omega_o = getOptOmegao(L)
    omega_c = 1 - omega_o
    D = L * omega_o * R_o / delta_o
    return omega_o, omega_c, D, len(packets)


if __name__ == "__main__":
    initialization(L, R_o, delta_o)
    count = 0
    # AUV starts moving.
    dis_list = []
    for x in x_axis:
        for y in y_axis:
            for gn in Gateway_Node_List:
                auv.x = x
                auv.y = y
                # Let AUV.z = Height/2 to satisfy the demand of
                # the traditional lawn mower path of AUV and reduce time complexity.
                auv.z = Height/2
                dis = get_distance(auv, gn)
                gn.communicate_acoustic(dis)
                gn.communicate_optical(dis)
                count += 1
    total = 0  # total energy consumption
    print("optimum stay distance=", STAY_DISTANCE_OPT * 1000, 'm')
    print("input stay distance =", STAY_DISTANCE * 1000, "m")
    for gn in Gateway_Node_List:
        total += gn.energy_consumption
    print("total consumption=", total, 'J')
