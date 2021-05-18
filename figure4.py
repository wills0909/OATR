from figure3 import *

Data_amount = [1000, 2000, 3000, 4000, 5000]
print("Fig 4(a)")
print("This is the energy consumption vs. data amount, when OATR=optimum value.")
for da in Data_amount:
    print(da, 'bit:', totalConsumption(da, getOptOmegao(da)))

print("This is the energy consumption vs. data amount, when OATR = 9:1.")
for da in Data_amount:
    print(da, 'bit:', totalConsumption(da, 0.9))

print("This is the energy consumption vs. data amount, when OATR = 10:0, which is the AOC in figure 4(a).")
for da in Data_amount:
    print(da, 'bit:', totalConsumption(da, 1))

print("=" * 30)
print("Fig 4(b)")
Node_Number = [30, 35, 40, 45, 50]
total_consumption = 0
print("This is the total energy consumption vs. node number, when OATR=optimum value. Let Data amount=1000bit ")
for n in Node_Number:
    for _ in range(n):
        total_consumption += totalConsumption(1000, OpticaRatio=getOptOmegao(1000))
    print('Node number=', n, "Total consumption=", total_consumption)

total_consumption = 0
print("This is the total energy consumption vs. node number, when OATR=10:0, which is the AOC in figure 4(b). "
      "Let Data amount=1000bit ")
for n in Node_Number:
    for _ in range(n):
        total_consumption += totalConsumption(1000, 1)
    print('Node number=', n, "Total consumption=", total_consumption)

total_consumption = 0
print("This is the total energy consumption vs. node number, when OATR=0:10, which is the AAC in figure 4(b). Let "
      "Data amount=1000bit ")
for n in Node_Number:
    for _ in range(n):
        total_consumption += totalConsumption(1000, 0)
    print('Node number=', n, "Total consumption=", total_consumption)
