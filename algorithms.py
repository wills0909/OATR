import network_model as nm
import operator


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
    step = 10
    Stay_Range = 150
    cmpfun = operator.attrgetter('y')
    GNL.sort(key=cmpfun, reverse=True)
    # for gn in GNL:
    #     auv.x = gn.x
    #     auv.y = gn.y
    #     # auv.z = gn.z + nm.STAY_DISTANCE*1000
    #     dis = nm.get_distance(auv, gn)
    #     gn.communicate_acoustic(dis)
    #     gn.communicate_optical(dis)

    # The traditional lawn mower path of AUV and reduce time complexity.
    for x in range(0, 2000, step):
        if x % 2 == 0:
            for y in range(0, 2000, step):
                for gn in GNL:
                    if gn.complete == 0:
                        auv.x = x
                        auv.y = y
                        dis = nm.get_distance(auv, gn)
                        if dis <= Stay_Range/1000:
                            gn.communicate_acoustic(dis)
                            gn.communicate_optical(dis)

        else:
            for y in range(2000, 0, -step):
                for gn in GNL:
                    if gn.complete == 0:
                        auv.x = x
                        auv.y = y
                        dis = nm.get_distance(auv, gn)
                        if dis <= Stay_Range/1000:
                            gn.communicate_acoustic(dis)
                            gn.communicate_optical(dis)


