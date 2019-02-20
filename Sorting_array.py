
def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < pivot:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i + 1:])
        first_part.append(x[i])
        return first_part + second_part


def getArray(arr):
    return (quicksort(arr))

blob_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def checkblob_Pink(distance, angle, coorx, temp_x):
    if 130 < distance < 210:
        if 0 < angle < 35:
            blob_array[0] = distance  # blob 1
    if 145 < distance < 189:
        if 50 < angle < 90:
            if temp_x < coorx:
                if blob_array[0] != 0:
                    temp_x = 0
                if temp_x == 0:
                    blob_array[1] = distance  # blob 2
                else:
                    if blob_array[1] < distance:
                        blob_array[2] = distance
                    else:
                        blob_array[2] = blob_array[1]
                        blob_array[1] = distance
    if 189 < distance < 210:
        if (70 < angle < 85) | (-70 > angle > -90):
            if blob_array[2] == 0:
                blob_array[2] = distance  # blob 3
    if 210 < distance < 260:
        if (80 < angle < 90) | (-70 > angle > -90):
            if blob_array[3] == 0:
                blob_array[3] = distance  # blob 4
    elif 150 < distance < 260:
        if -50 > angle > -90:
            if blob_array[4] == 0:
                blob_array[4] = distance  # blob 5

uppery = [0,0,0,0]
lowery = [0,0,0,0]
def checkblob_Blue(middleY, coorY, distance, angle):
    if (0 < angle < 61) & (0 < distance < 60):
        blob_array[5] = distance
    else:
        if coorY > middleY:
            if (blob_array[1] == 0) & (uppery[0] == 0):
                uppery[0] = distance
            elif (blob_array[2] == 0) & (uppery[1] == 0):
                if uppery[0] != 0:
                    if uppery[0] > distance:
                        uppery[1] = distance
                    else:
                        uppery[1] = uppery[0]
                        uppery[0] = distance
                else:
                    uppery[1] = distance
            elif (blob_array[3] == 0) & (uppery[2] == 0):
                uppery[2] = distance
                if ((uppery[0] == 0)& (uppery[1] != 0)) & (uppery[1] < distance):
                        uppery[2] = uppery[1]
                        uppery[1] = distance
                elif ((uppery[0] != 0) & (uppery[1] == 0)) & (uppery[0] < distance):
                        uppery[2] = uppery[0]
                        uppery[0] = distance
                else:
                    if uppery[0] < distance:
                        uppery[2] = uppery[1]
                        uppery[1] = uppery[0]
                        uppery[0] = distance
                    elif uppery[1] < distance:
                        uppery[2] = uppery[1]
                        uppery[1] = distance
            elif (blob_array[4] == 0) & (uppery[3] == 0):
                uppery[3] = distance
                if uppery[2] < distance:
                    uppery[3] = uppery[2]
                    uppery[2] = distance
                    if uppery[1] < uppery[2]:
                        temp = uppery[2]
                        uppery[2] = uppery[1]
                        uppery[1] = temp
                        if uppery[0] < uppery[1]:
                            temp = uppery[1]
                            uppery[1] = uppery[0]
                            uppery[0] = temp
                elif uppery[1] < distance:
                    uppery[3] = uppery[2]
                    uppery[2] = uppery[1]
                    uppery[1] = distance
                    if uppery[0] < uppery[1]:
                        temp = uppery[1]
                        uppery[1] = uppery[0]
                        uppery[0] = temp
                elif uppery[0] < distance:
                    uppery[3] = uppery[2]
                    uppery[2] = uppery[1]
                    uppery[1] = uppery[0]
                    uppery[0] = distance

            blob_array[6] = uppery[0]
            blob_array[8] = uppery[1]
            blob_array[10] = uppery[2]
            blob_array[12] = uppery[3]

        elif coorY < middleY:
            if (blob_array[1] == 0) & (lowery[0] == 0):
                lowery[0] = distance
            elif (blob_array[2] == 0) & (lowery[1] == 0):
                lowery[1] = distance
                if lowery[0] != 0:
                    if lowery[0] > distance:
                        lowery[1] = distance
                    else:
                        lowery[1] = lowery[0]
                        lowery[0] = distance
                else:
                    lowery[1] = distance
            elif (blob_array[3] == 0) & (lowery[2] == 0):
                lowery[2] = distance
                if ((lowery[0] == 0)& (lowery[1] != 0)) & (lowery[1] < distance):
                        lowery[2] = lowery[1]
                        lowery[1] = distance
                elif ((lowery[0] != 0) & (lowery[1] == 0)) & (lowery[0] < distance):
                        lowery[2] = lowery[0]
                        lowery[0] = distance
                else:
                    if lowery[0] < distance:
                        lowery[2] = lowery[1]
                        lowery[1] = lowery[0]
                        lowery[0] = distance
                    elif lowery[1] < distance:
                        lowery[2] = lowery[1]
                        lowery[1] = distance
            elif (blob_array[4] == 0) & (lowery[3] == 0):
                lowery[3] = distance
                if lowery[2] < distance:
                    lowery[3] = lowery[2]
                    lowery[2] = distance
                    if lowery[1] < lowery[2]:
                        temp = lowery[2]
                        lowery[2] = lowery[1]
                        lowery[1] = temp
                        if lowery[0] < lowery[1]:
                            temp = lowery[1]
                            lowery[1] = lowery[0]
                            lowery[0] = temp
                elif lowery[1] < distance:
                    lowery[3] = lowery[2]
                    lowery[2] = lowery[1]
                    lowery[1] = distance
                    if lowery[0] < lowery[1]:
                        temp = uppery[1]
                        lowery[1] = lowery[0]
                        lowery[0] = temp
                elif lowery[0] < distance:
                    lowery[3] = lowery[2]
                    lowery[2] = lowery[1]
                    lowery[1] = lowery[0]
                    lowery[0] = distance

            blob_array[7] = lowery[0]
            blob_array[9] = lowery[1]
            blob_array[11] = lowery[2]
            blob_array[13] = lowery[3]

        elif coorY == middleY:
            blob_array[5] = distance  # blob 6

def print_blob_array():
    print blob_array
    import NeuralNetwork
    NeuralNetwork.main()

