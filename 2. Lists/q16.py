marks=[9,9.5,7,6,10]
total_sum=0
for mark in marks:
    total_sum += mark

avg=total_sum/len(marks)
print(f'total number: {total_sum}')
print(f'Avg: {avg:.2f}')