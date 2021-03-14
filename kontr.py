import math
import random
import matplotlib.pyplot as plt
datafirst = [[
"0.25",
"0.15",
"0.5",
"0.58",
"0.5",
"0.615",
"0.61",
"0.62",
"0.62",
"0.28",
"0.56",
"0.32",
"0.22",
"0.39",
"0.43",
"0.49",
"0.4",
"0.39",
],[
"79",
"73",
"102",
"65",
"102",
"59",
"29",
"145",
"148",
"103",
"56",
"56",
"60",
"71",
"37",
"67",
"40",
"23"
],[
"7",
"7",
"5",
"5",
"5",
"5",
"5",
"5",
"5",
"7",
"5",
"6",
"6",
"5",
"5",
"5",
"6",
"5"
]]
number = 18
data = [[0.1 for y in range(number)] for x in range(3)]
for i in range (0,3):
    for k in range (0,number):
        data[i][k] = float(datafirst[i][k])
for i in range (0,number):
    data[0][i] = data[0][i]*100
k = 15

resnum = 0
index = [0.0 for y in range(k)] # index that defines how good is the K
results = [[[-1.0 for y in range(number)] for x in range(3)] for z in range (k+1)] # dots for every cluster
for z in range(1,k+1):
    best = 0.0
    curnum = z + 1
    checker = 1
    clusters = [[0 for y in range(2)] for x in range(curnum)]  # x, y of cluster center
    for s in range (50):
        tempx = 100.0 / curnum
        tempy = 120.0 / curnum
        nowx = 0.0
        nowy = 0.0
        for t in range(0, curnum):
            nowx = nowx + tempx
            nowy = nowy + tempy
            clusters[t][0] = random.uniform(nowx - tempx, nowx)
            print(clusters[t][0])
            clusters[t][1] = random.uniform(nowy - tempy, nowy)
            print(clusters[t][1])
        for u in range (0,curnum):
            print("Clusters:" + str(curnum) + " Current cluster: " + str(u))
            print("x: " + str(clusters[u][0]) + "y: " + str(clusters[u][1]))
        resdistance = [[0.1 for y in range(number)] for x in range(2)]  # distance to closest cluster, closest cluster
        for i in range(0, number):
            resdistance[1][i] = -1
        while (checker == 1):
            for u in range(0, curnum):
                print("Inside")
                print("Clusters:" + str(curnum) + " Current cluster: " + str(u))
                print("x: " + str(clusters[u][0]) + "y: " + str(clusters[u][1]))
            checker = 0
            distance = [[0.1 for y in range(number)] for x in range(curnum)]  # distance to every cluster center
            for t in range(0, curnum):
                for i in range(0, number):
                    distance[t][i] = math.sqrt(
                        abs(clusters[t][0] - (data[0][i])) * abs(clusters[t][0] - (data[0][i])) + abs(
                            clusters[t][1] - data[1][i]) * abs(clusters[t][1] - data[1][i]))
            min = 10000.0

            # for t in range (0,curnum):
            #     for i in range (0, number):
            #         if distance[t][i] < min:
            #             resdistance[0][i] = distance[t][i]
            #             resdistance[1][i] = t
            #             min = resdistance[0][i]
            for t in range(0, number):
                min = 10000.0
                temp = resdistance[1][t]
                for i in range(0, curnum):
                    if distance[i][t] < min:
                        resdistance[0][t] = distance[i][t]
                        resdistance[1][t] = i
                        min = resdistance[0][t]
                if temp != resdistance[1][t]:
                    checker = 1
                    print("YES")
                else:
                    print("NO")
            for i in range(0, curnum):
                counter = 0.0
                tempx = 0
                tempy = 0
                for x in range(0, number):
                    if resdistance[1][x] == i:
                        tempx = tempx + data[0][x]
                        tempy = tempy + data[1][x]
                        counter = counter + 1
                if counter != 0:
                    tempx = tempx / counter
                    tempy = tempy / counter
                    clusters[i][0] = tempx
                    clusters[i][1] = tempy
                else:
                    print("counter == 0")
        indexresult = 0.0
        for i in range(0, curnum):
            innercounter = 0
            inner = 0.0
            for x in range(0, number):
                min = 100000.0
                if resdistance[1][x] == i:
                    for y in range(0, number):
                        if resdistance[1][y] == resdistance[1][x] and y != x:
                            innercounter = innercounter + 1
                            inner = inner + math.sqrt(
                                abs(data[0][y] - (data[0][x])) * abs(data[0][y] - (data[0][x])) + abs(
                                    data[1][y] - data[1][x]) * abs(data[1][y] - data[1][x]))
                    tempmin = 10000.0
                    for y in range(0, curnum):
                        dist = math.sqrt(abs(clusters[y][0] - (data[0][x])) * abs(clusters[y][0] - (data[0][x])) + abs(
                            clusters[y][1] - data[1][x]) * abs(clusters[y][1] - data[1][x]))
                        if dist < tempmin:
                            tempmin = dist
                    if tempmin < min:
                        min = tempmin
            if innercounter != 0:
                inner = inner / innercounter
                temp = 0.0
                if inner > min:
                    temp = inner
                else:
                    temp = min
                indexresult = indexresult + ((min - inner) / (temp))
            else:
                indexresult = 0.0
                s = s - 1
        indexresult = indexresult / curnum
        print("Index: " + str(indexresult))
        if best < indexresult:
            best = indexresult
            for i in range(0, number):
                results[z][0][i] = data[0][i]
                results[z][1][i] = data[1][i]
                results[z][2][i] = resdistance[1][i]
    index[z - 1] = best
for i in range (0,k):
    print(index[i])
for i in range (1,k+1):
    uo = ""
    for j in range(0,number):
        uo = uo + " " + str(results[i][2][j])
    print(uo)
colors = ["green", "yellow", "red", "blue", "orange", "purple", "white", "pink", "brown", "tomato", "c", "lime", "deeppink"]

# distance = [[0.1 for y in range(18)] for x in range(2)]
# for i in range (0,18):
#     distance[0][i] = math.sqrt(abs(x-(data[0][i]))*abs(x-(data[0][i])) + abs(y - data[1][i])*abs(y - data[1][i]))
#     print("x: " + str(data[0][i]))
#     print("y: " + str(data[1][i]))
#     print("dis: " + str(distance[0][i]))
#     distance[1][i] = data[2][i]
#     print(data[2][i])
#     print(distance[0][i])


fig, ax = plt.subplots()
numbers = [0]*k
for i in range (0,k):
    numbers[i] = i + 1

ax.scatter(numbers, index, c = 'lime')

ax.set_facecolor('black')
reser = "Silhouette index \n The best option would be to use "
temper = 0.0
tempi = 0
for i in range (0,k):
    if index[i] > temper:
        temper = index[i]
        tempi = tempi + 1
reser = reser + str(tempi) + " clusters!"
ax.set_title(reser)
tempi = tempi - 1
fig.set_figwidth(7)
fig.set_figheight(7)


fig1, ax1 = plt.subplots()

for k in range(0, number):
    ax1.scatter(results[tempi][0][k], results[tempi][1][k], c=colors[int(results[tempi][2][k])])


ax1.set_facecolor('black')
ax1.set_title('The best clustering!')

fig1.set_figwidth(7)
fig1.set_figheight(7)

plt.show()


# num1 = 0
# num2 = 0
# num3 = 0
# x1 = [0]*18
# x2 = [0]*18
# x3 = [0]*18
# y1 = [0]*18
# y2 = [0]*18
# y3 = [0]*18
# for i in range (0,18):
#     if (data[2][i] == 5.0):
#         x1[num1] = data[0][i]
#         y1[num1] = data[1][i]
#         num1 = num1 + 1
#     else:
#         if data[2][i] == 6.0:
#             x2[num2] = data[0][i]
#             y2[num2] = data[1][i]
#             num2 = num2 + 1
#         else:
#             x3[num3] = data[0][i]
#             y3[num3] = data[1][i]
#             num3 = num3 + 1
# x1res = [0]*num1
# y1res = [0]*num1
# for i in range (0, num1):
#     x1res[i] = x1[i]
#     y1res[i] = y1[i]
# x2res = [0]*num2
# y2res = [0]*num2
# for i in range (0, num2):
#     x2res[i] = x2[i]
#     y2res[i] = y2[i]
# x3res = [0]*num3
# y3res = [0]*num3
# for i in range (0, num3):
#     x3res[i] = x3[i]
#     y3res[i] = y3[i]
# print("Type the new volatile acidity: ")
# x = 100*float(input())
# print("Type the new total sulfur dioxide: ")
# y = float(input())

# print("Type k: ")
# k = int(input())
# min = 1000000.0
# marks = [0]*k
# prev = -1.0
# for j in range (0,k):
#     for i in range(0, 18):
#         if distance[0][i] < min and distance[0][i] > prev:
#             print("hi")
#             print(j)
#             print("new min:")
#             print(distance[0][i])
#             min = distance[0][i]
#             marks[j] = distance[1][i]
#     prev = min
#     min = 1000000.0



# resmarks = [0]*3
# for i in range (0,k):
#     if marks[i] == 5.0:
#         resmarks[0] = resmarks[0] + 1
#     else:
#         if marks[i] == 6.0:
#             resmarks[1] = resmarks[1] + 1
#         else:
#             resmarks[2] = resmarks[2] + 1
#     print(marks[i])
# max = 0
# thei = -1
# for i in range (0,3):
#     print(resmarks[i])
#     if resmarks[i] > max:
#         max = resmarks[i]
#         thei = i
#

