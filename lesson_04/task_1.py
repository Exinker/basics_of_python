

def calculate_payroll(hours, rate, premium):
    return hours * rate + premium


if __name__ == '__main__':
    import sys

    script_name, *args = sys.argv
    
    hours, rate, premium = [float(item) for item in args]
    payroll = calculate_payroll(hours, rate, premium)

    print(f'payroll: {payroll:.2f}$')
