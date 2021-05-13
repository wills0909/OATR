from option_parameters import *


# this code is to calculate the optimum omega_o
def get_opt(o):

    part1 = (6 * o * o * math.pow(L, 3) * math.pow(R_o, 2) * pi * (1 - math.cos(theta_0)) * P_l
             * math.exp(Klambda * o * L * R_o / delta_o / math.cos(theta))) \
            / (math.pow(delta_o, 3) / eta_t / eta_r / A_r / math.cos(theta))

    part2 = (2 * Klambda * math.pow(o, 3) * math.pow(L, 4) * math.pow(R_o, 3) * pi * (1 - math.cos(theta_0)) * P_l
             * math.exp(Klambda * o * L * R_o / delta_o / math.cos(theta))) \
            / math.pow(delta_o, 4)/eta_t / eta_r / A_r / math.cos(theta) / math.cos(theta)
    part3 = L * E_elec - (k + 1) * L * P_i * math.pow((1 - o) * L * R_c / delta_c, k) * math.pow(alpha_f, (
            1 - o) * L * R_c / delta_c)
    part4 = L * P_i * math.pow((1 - o) * L * R_c / delta_c, k + 1) \
            * math.pow(alpha_f, (1 - o) * L * R_c / delta_c) * math.log(alpha_f)

    return part1 + part2 + part3 - part4


root_list = np.arange(0.8, 1, 0.001)
tmp = []
for r in root_list:
    t = abs(get_opt(r) - 0)
    #print(t)
    tmp.append(t)

index = 0
num = tmp[0]
for i in range(len(tmp)):
    if tmp[i] < num:
        num = tmp[i]
        index = i
# print(index)
print(root_list[index])
