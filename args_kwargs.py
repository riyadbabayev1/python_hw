#---PYTHON HOMEWORK: FUNCTION ARGUMENTS (positional, default, *args, **kwargs)---

#PART 1 — Positional & Default Arguments



LINE = "---------------------------"

#==========================================
#Task 1
#==========================================

def greet_user(name, message="Hello"):
    return f"{message}, {name}!"

print(greet_user("Ali"))
print(greet_user("Riyad", "Welcome"))
print(greet_user("Samir", "Good morning"))

#==========================================
#Task 2
#==========================================

def calculate_power(num, exp=2):
    return num ** exp

print(calculate_power(5))
print(calculate_power(2, 3))
print(calculate_power(10, 0))

#==========================================
#Task 3
#==========================================

def calculate_price_including_tax(price, tax_rate=0.15):
    return price * (1 + tax_rate)

print(calculate_price_including_tax(100))
print(calculate_price_including_tax(200, 0.20))
print(calculate_price_including_tax(50, 0))

#==========================================
#Task 4
#==========================================

def introduct_person(name, age, country="obscure country"):
    return f"Hey it's {name}, I am {age} old and I am from {country}"

print(introduct_person("Riyad", 20))
print(introduct_person("Ali", 22, "Azerbaijan"))
print(introduct_person("Sam", 30, "Turkey"))

#==========================================
#Task 5
#==========================================

def multiply_nums_up_to_three(num1=1, num2=1, num3=1):
    return num1 * num2 * num3

print(multiply_nums_up_to_three())
print(multiply_nums_up_to_three(5))
print(multiply_nums_up_to_three(2, 3, 4))

#==========================================

#PART 2 — Positional & Default Arguments


#==========================================
#Task 6
#==========================================

def process_order(item_name, quantity, discount=0):
    return f"Proceeding order: {item_name}\nQuantity: {quantity}\nDiscount: {discount}"

print(process_order("Pizza", 2))
print(process_order("Burger", 3, 0.10))
print(process_order("Cola", 1, 0))

#==========================================
#Task 7
#==========================================

def store_student_info(name, grade, school=None):
    return {name: [grade, school]}

print(store_student_info("Ali", 95))
print(store_student_info("Riyad", 88, "Oxford"))
print(store_student_info("Sam", 75, "Harvard"))

#==========================================
#Task 8
#==========================================

def calculate_rectangle_area(lentgh, width=None):
    if not width:
        width = lentgh
    return lentgh * width

print(calculate_rectangle_area(5))
print(calculate_rectangle_area(5, 10))
print(calculate_rectangle_area(7, 3))

#==========================================
#Task 9
#==========================================

def include_flag_in_login_func(
        username: str, 
        password: str, 
        remember_me_flag: bool=None
) -> bool:
    if remember_me_flag:
        return username, password
    
print(include_flag_in_login_func("admin", "1234", True))
print(include_flag_in_login_func("user", "pass", False))
print(include_flag_in_login_func("test", "1111"))

#==========================================
#Task 10
#==========================================

def calculate_shipping_cost(price, destination_type=None, express_flag=None):
    if destination_type and express_flag:
        return price * 2

    if destination_type:
        return price * 1.5
    
    if express_flag:
        return price * 1.2

print(calculate_shipping_cost(100))
print(calculate_shipping_cost(100, destination_type=True))
print(calculate_shipping_cost(100, destination_type=True, express_flag=True))

#==========================================
#PART 3 — *args (Variable Positional Arguments)


#==========================================
#Task 11
#==========================================

def sum_any_number_of_nums(*nums):
    return sum(nums)

print(sum_any_number_of_nums(1, 2, 3))
print(sum_any_number_of_nums(10, 20, 30, 40))
print(sum_any_number_of_nums())

#==========================================
#Task 12
#==========================================

def find_maximum_num(*nums):
    return max(nums)

print(find_maximum_num(1, 2, 3))
print(find_maximum_num(100, 55, 78))
print(find_maximum_num(-5, -2, -10))

#==========================================
#Task 13
#==========================================

def concatenate_multiple_strings_into_one(*strings):
    concatenated_str = ""
    for string in strings:
        concatenated_str += string
    return concatenated_str

print(concatenate_multiple_strings_into_one("Hello", "World"))
print(concatenate_multiple_strings_into_one("Py", "thon"))
print(concatenate_multiple_strings_into_one("A", "B", "C"))

#==========================================
#Task 14
#==========================================

def calculate_nums_average(*nums):
    summary = sum(nums)
    quantity = len(nums)
    return summary / quantity

print(calculate_nums_average(10, 20, 30))
print(calculate_nums_average(5, 5, 5, 5))
print(calculate_nums_average(100, 50))

#==========================================
#Task 15
#==========================================

def calculate_even_nums_counter(*nums):
    even_nums_counter = 0
    for num in nums:
        if num % 2 == 0:
            even_nums_counter += 1
    return even_nums_counter

print(calculate_even_nums_counter(1, 2, 3, 4, 5, 6))
print(calculate_even_nums_counter(2, 4, 6, 8))
print(calculate_even_nums_counter(1, 3, 5))

#==========================================
#PART 4 — **kwargs (Keyword Arguments)


#==========================================
#Task 16
#==========================================

def write_all_key_value_pairs(**kwargs):
    print(f"{key} - {value}" for key, value in kwargs.items())

write_all_key_value_pairs(name="Ali", age=20)
write_all_key_value_pairs(city="Baku", country="Azerbaijan")
write_all_key_value_pairs()

#==========================================
#Task 17
#==========================================

def build_user_profile(**info):
    return [f"{key} - {value}" for key, value in info.items()]

print(build_user_profile(name="Ali", age=20))
print(build_user_profile(job="Developer", salary=5000))
print(build_user_profile())

#==========================================
#Task 18
#==========================================

def format_adress(**info):
    return [f"{key} - {value}" for key, value in info.items()]

print(format_adress(city="Baku", street="Nizami"))
print(format_adress(country="Azerbaijan", zip=1000))
print(format_adress())

#==========================================
#Task 19
#==========================================

def calculate_items_price(**named_items):
    total_price = 0
    for _, price in named_items.items():
        total_price += price
    return total_price

print(calculate_items_price(apple=5, milk=7))
print(calculate_items_price(book=20, pen=3, bag=50))
print(calculate_items_price())

#==========================================
#Task 20
#==========================================

def return_filtered_values(**kwargs):
    CERTAIN_NUM = 0
    value_list = []

    for _, value in kwargs.items():
        if value > CERTAIN_NUM:
            value_list.append(value)

    return value_list

print(return_filtered_values(a=1, b=-5, c=10))
print(return_filtered_values(x=-1, y=-2))
print(return_filtered_values(one=100, two=200))

#==========================================
#PART 5 — Mixed Arguments


#==========================================
#Task 21
#==========================================

def print_args(arg1 = 0, arg2 = 1, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

print_args(1, 2, 3, 4, name="Ali")
print_args()
print_args(10, 20)

#==========================================
#Task 22
#==========================================

def display_shopping(cart_owner, discount=0, **items_and_prices):
    total_price = 0
    items = []

    for item, price in items_and_prices.items():
        total_price += price
        items.append(item)

    total_price = total_price * (1 - discount)

    return {
        "Cart owner": cart_owner,
        "Items": items,
        "Total price": total_price
    }

print(display_shopping(
    "Riyad",
    discount=0.10,
    apple=5,
    banana=3,
    milk=7
))

#==========================================
#Task 23
#==========================================

def student_grades(name, *grades, calculate_average=False, **extra_info):
    print(f"Student Name: {name}")
    
    if grades:
        print("Grades:", grades)
        
        if calculate_average:
            average = sum(grades) / len(grades)
            print(f"Average Grade: {average:.2f}")
    else:
        print("No grades provided.")
    
    if extra_info:
        print("Extra Info:")
        for key, value in extra_info.items():
            print(f"{key}: {value}")

student_grades(
    "Ali",
    85, 90, 78, 92,
    calculate_average=True,
    age=20,
    department="Computer Science"
)

#==========================================
#Task 24
#==========================================


def logging(log_level, *multiple_messages, **metadata):
    log = f"Log level: {log_level}\n"
    print(log + LINE + "\nMessages: ")
    for message in multiple_messages:
        print(f"    {message}")
    print(LINE)
    print("Metadata: ")
    for key, value in metadata.items():
            print(f"    {key}: {value}")

logging("error", "e2eoe2dqw", "dwwdwdww", penis="ronaldo", dick="neymar")

#==========================================
#Task 25
#==========================================

def order_in_restaurant(table_num, *multiple_dishes, tip=None, **extra_charges):
    print(f"Table number: {table_num}\n{LINE}\nDishes:")

    for dish in multiple_dishes:
        print(dish)

    print(LINE)

    if tip:
        print(f"Tip: {tip}")
        print(LINE)

    if extra_charges:
        for key, value in extra_charges.items():
            print(f"{key}: {value}")
        print(LINE)


order_in_restaurant(
    12,
    "Pizza",
    "Cola",
    tip=32,
    service_fee=10
)

#==========================================
#Task 26
#==========================================

def sum_only_num_inputs(*nums):
    num_sum = 0
    for num in nums:
        if type(num) == int or type(num) == float:
            num_sum += num
    return num_sum

print(sum_only_num_inputs(1, 2, "hello", 4.5))
print(sum_only_num_inputs("a", "b", "c"))
print(sum_only_num_inputs(100, 200, 300))

#==========================================
#Task 28
#==========================================

def regulate_positional_args(arg1, arg2, *args):
    return arg1, arg2, args

print(regulate_positional_args(1, 2))
print(regulate_positional_args(1, 2, 3, 4, 5))
print(regulate_positional_args("A", "B", "C"))

#==========================================
#Task 29
#==========================================

def calculating_operations(operation_type, *nums):

    if not nums:
        return 'No numbers'
    
    minus = nums[0]
    multiplication = 1
    division = nums[0]
    
    final_result = 0
    
    if operation_type == '+':
        final_result = sum(nums)
    elif operation_type == '-':
        for num in nums[1:]:
            minus-=num
        final_result = minus
        
    elif operation_type == '*':
        for num in nums:
            multiplication*=num
        final_result = multiplication
    
    elif operation_type == '/':
        try:
            for num in nums[1:]:
                division/=num
            final_result = division
        except ZeroDivisionError:
            print("Сannot be divided by 0!")
            
    else:
        return "Invalid operation!"
        
    return final_result

print(calculating_operations("+", 1, 2, 3, 4))
print(calculating_operations("-", 10, 2, 3))
print(calculating_operations("/", 100, 2, 5))
print(calculating_operations("/", 10, 0))
print(calculating_operations("%", 10, 5))

#==========================================
#Task 30
#==========================================

def display_all_argument_types(arg, *args, kwarg=0, **kwargs):
    try:
        
        total = arg / kwarg
        
        for ar in args:
            total+=ar
            
        for kw in kwargs.values():
            total+=kw
            
        return total
    
    except TypeError:
        return 'Must be numbers!'
    except ZeroDivisionError:
        return "Can't divide by zero"
    
print(display_all_argument_types(5,6,7,8,kwarg=0,bal=2,messi=100))
print(display_all_argument_types(5,6,7,8,kwarg=1,bal=2,messi=100))
print(display_all_argument_types(5,6,"7",8,kwarg=1,bal=2,messi=100))