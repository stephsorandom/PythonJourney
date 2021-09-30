##using Tuples in for loop
stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]
    for item in stock_prices:
        print(item)
            ==> ('APPL', 200) 
                ('GOOG', 400) 
                ('MSFT', 100)


##Tuple Unpacking
    for ticker,price in stock_prices:
        print(ticker)
            ===> 
                APPL
                GOOG
                MSFT


#list of Tuples with employees. and how many hours they work a month
work_hours = [('Abby',100), ('Billy', 400), ('Cassie',800)]

##Find employee of the year...who has worked the most hours?
##Return the employee name and hours who has the most

def employee_check(work_hours):

    #placeholder variables...one to compare the hours through each iteration...second to store the value of the highest worker
    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max: ##is the current employee hours more than the previous?
            current_max = hours ##if so, set that employee hours as the new current_max
            employee_of_month  ##add that employee name to the empty string placeholder
        else:
            pass
    return (employee_of_month,current_max)