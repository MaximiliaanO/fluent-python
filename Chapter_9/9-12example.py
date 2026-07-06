def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total, count, total / count
    
    return averager

average = make_averager()
total, count, averg = average(10)
print("Total:", str(total), "Count:", str(count), "Average:", str(averg), sep="\t")
total, count, averg = average(10)
print("Total:", str(total), "Count:", str(count), "Average:", str(averg), sep="\t")
total, count, averg = average(15)
print("Total:", str(total), "Count:", str(count), "Average:", str(averg), sep="\t")