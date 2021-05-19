import network_model as nm


# Algorithm 1: Packet segmentation.
def initialization(L, R_o, delta_o):
    packets = [L]
    LLim = 5000
    while (True):
        if L > LLim:
            L %= LLim
            omega_o = nm.getOptOmegao(L)
            D = L * omega_o * R_o / delta_o
            packets.append(L)
        else:
            break
    omega_o = nm.getOptOmegao(L)
    omega_c = 1 - omega_o
    D = L * omega_o * R_o / delta_o
    return omega_o, omega_c, D, len(packets)


# Algorithm 2: AUV communicates with GNs.
def auv_walk(auv, GNL):
    for gn in GNL:
        auv.x = gn.x
        auv.y = gn.y
        auv.z = gn.z + nm.STAY_DISTANCE
        dis = nm.get_distance(auv, gn)
        gn.communicate_acoustic(dis)
        gn.communicate_optical(dis)

    # for x in x_axis:
    #     for y in y_axis:
    #         for gn in Gateway_Node_List:
    #             auv.x = x
    #             auv.y = y
    #             # Let AUV.z = Height/2 to satisfy the demand of
    #             # the traditional lawn mower path of AUV and reduce time complexity.
    #             dis = get_distance(auv, gn)
    #             gn.communicate_acoustic(dis)
    #             gn.communicate_optical(dis)
    #             count += 1
