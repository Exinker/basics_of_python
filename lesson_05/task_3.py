
filename = 'task_3.txt'

payroll = []
with open(filename, 'r') as file:
    for line in file:
        line = line.split()

        payroll.append({
            'name': line[0],
            'gross pay': float(line[1]),
        })
        

output = ', '.join([employer['name'] for employer in payroll if employer['gross pay'] < 20000])
print(f"Employers with gross salary less than 20000$: {output}.")

output = sum([employer['gross pay'] for employer in payroll]) / len(payroll)
print(f"Mean gross salary is {output:.2f}$.")
