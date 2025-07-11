data = [47, 92, 35, 64, 23, 89, 91, 17, 56, 78, 34, 66, 23, 45, 89, 90, 21, 62, 47, 35, 80, 70, 29, 60, 33]
def describeData(data):
    n = len(data)
    mean = sum(data)/n

    rankData = sorted(data)
    if n % 2 == 1:  # odd number
        median  = rankData[n//2]
    else:  # even number
        median = (rankData[n//2] + rankData[n//2-1])/ 2

    count = {}
    for times in data:
        count.setdefault(times, 0)
        count[times] += 1
    maxCount = max(count.values())
    mode = []
    for k, v in count.items():
        if v == maxCount:
            mode.append(k)


    variation = 0
    for ms in data:
        variation += (ms - mean)**2/ n
    standardDeviation = variation**0.5

    return {'mean': mean,
            'median': median,
            'mode': mode,
            'standard deviation': standardDeviation}

print(describeData(data))