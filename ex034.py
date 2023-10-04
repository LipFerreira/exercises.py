salary = float(input("What is the employee's salary? "))
if salary <= 1250:
    new_salary = salary + (salary * 15/100)
else:
    new_salary = salary + (salary * 10/100)
print('Someone who used to earn ${:.2f} now earns ${:.2f}.'.format(
    salary, new_salary))
