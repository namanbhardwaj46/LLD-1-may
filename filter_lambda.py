from functools import reduce
from symbol import return_stmt

mul = lambda x,y: x*y

print(mul(2,3))

is_even = lambda x: x%2==0

print(is_even(3))
print(is_even(2))

#  maps:

square = lambda x: x*x

nums = [1, 2, 3, 4, 5]

# for idx, i in enumerate(nums):
#     nums[idx] = nums[idx]*nums[idx]
#
# print(nums)


result = list(map(lambda x: x*x, nums))

print(result)


z = ["karan", "naman", "abc", "xyz"]


print(list( map(lambda x: "Mr." + x, z) ))


listMultiply = [1,2,3,4,5]
n= 3
result = list(map(lambda x: x*n, listMultiply))

print(result)


listMultiply = [1,2,3,4,5]
list2Multiply = [2]

l1 = lambda x,y: x*y

result = list(map(l1, listMultiply, list2Multiply))

print(result)

# filters...

nums = [1,2,3,4,5]

even = list(filter( lambda x: x%2==0, nums))

print(even)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


primes = list(filter(lambda num: num>1 and
                                 all(num%i!=0
                                     for i in
                                     range(2, int(num**0.5)+1)), nums))

print(primes)


#  REDUCE:

val=[1,2,100,3,4,5]

x = 15
for y in val:
    x += y
print(x)

sum_nums = reduce(lambda x,y: x+y, val)

print(sum_nums)



max_num = reduce(lambda x,y: max(x,y), val)
print(max_num)




# LAMBDA: small expression methods
# MAP: apply a function to each item in an iterable
# FILTER: filter items in an iterable based on a condition
# REDUCE: apply a function cumulatively to the items of an iterable to get a single value


zz=  ["a", "b", "c", "d", "e"]

print("abcde")


z= lambda *args: sum(args)

print(z(1, 2, 3, 4, 5))  # Output: 15

dixt_person = [{

    "name": "John",
    "age": 30,
    "city": "New York"
}, {
    "name": "Jane",
    "age": 25,
    "city": "Los Angeles"
},
    {
        "name": "zak",
        "age": 20,
        "city": "Los Angeles"
    }
]

filet_even_age = list(filter(lambda x: x['age'] >20, dixt_person))

print(filet_even_age)


# IS EVEN

#  double


#  filter and double

def is_even(num):
    return num % 2 == 0

is_evev = lambda num: num % 2 == 0


def double(num):
    return num * 2


def filter_and_double_even_numbers(numbers):


    filtered_numbers = filter(is_even, numbers)

     return list(map(double, filtered_numbers))

filter_and_double_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
