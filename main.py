import operator
from option_parameters import *

x_axis = range(Range)
y_axis = range(Range)
auv = AUV(0, 0)
np.random.seed(9999)
a = np.random.randint(0, Range, size=[NODE_NUMBER, 2])
Gateway_Node_List = []
for _ in a:
    gn = GatewayNode(_[0], _[1])
    Gateway_Node_List.append(gn)
    
cmpfun = operator.attrgetter('x')
Gateway_Node_List.sort(key=cmpfun, reverse=False)


def initializetion(L,R_o,delta_o)
    packets = [L]
    LLim = 5000
    while(True):
        if L>Llim:
            L %= Llim
            omega_o = 0.97
            D = L*omega_o*R_o/delta_o
            packets.append(L)
        else:break
    omega_o = 0.97
    omega_c = 1-omega_o
    D = L*omega_o*R_o/delta_o
    return (omega_o,omega_c,D,len(packets))

if __name__ == "__main__":
    initialization(L,Llim=5000,R-o,delta_o)
    count = 0
    for x in x_axis:
        for y in y_axis:
            for gn in Gateway_Node_List:
                auv.x = x
                auv.y = y
                auv.z = DISTANCE_OPT
                gn.communicate_acoustic(auv)
                gn.communicate_optical(auv, DISTANCE)
                count += 1

    total = 0 # total energy consumption
    #print(omega_o)
    #print(L)
    #print(R_o)
    #print(delta_o)
    print("optimum distance=", DISTANCE_OPT*1000, 'm')
    print("input distance =", DISTANCE*1000, "m")
    for gn in Gateway_Node_List:
        total += gn.energy_consumption
    print("total consumption=", total, 'J')
