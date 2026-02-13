def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] > last[1]:
            merged.append(current)
        else:
            last[1] = max(last[1], current[1])
    return merged

s = input().strip()
if not s: 
    intervals = []
else:
    intervals = list(map(lambda x: list(map(int, x.split())), s.split(',')))
print(intervals)

print(merge_intervals(intervals))

