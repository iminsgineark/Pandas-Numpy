# q1 - Method 1
def is_prime(num):
    if num <= 1:
        return False  # 1 and below are not prime
    for i in range(2, int(num ** 1 / 2) + 1):
        if num % i == 0:
            return False  # found a factor, not prime
    return True  # no factors found, prime


number = int(input("Enter The Number \n"))
print(is_prime(number))

# q1 - Method 2
Number = int(input("Enter a number:"))
if Number > 1:
    for i in range(2, Number // 2):
        if (Number % i) == 0:
            print(Number, "is not a prime number")
            break
    else:
        print(Number, "is a prime number")

# Q2


def DiscountPriceCalculation(price, discount):
    discount = price * (discount / 100)
    discounted_price = price - discount
    return discounted_price


CostPrice = int(input("Enter The CP\n"))
Discount = int(input("Enter The Discount\n"))
print("Final Price After Discount Is : ", DiscountPriceCalculation(CostPrice, Discount))

# Q3


def CurrencyConverter(amount, CurrencyType):
    if CurrencyType == 'USD':
        return amount * 82.74
    elif CurrencyType == 'EUR':
        return amount * 87.54
    elif CurrencyType == 'INR':
        return amount
    else:
        return None


Currency = int(input("Enter The Currency\n"))
Currency_Type = input("Enter The CurrencyType\n")
print(CurrencyConverter(Currency, Currency_Type))

# Q4


def TotalBill(billAmount, tip):
    tipAmount = billAmount * (tip / 100)
    Total = billAmount + tipAmount
    return Total


BillAmount = int(input("Enter The Bill Amount\n"))
Tip = int(input("Enter The Tip \n"))
print(TotalBill(BillAmount, Tip))

# Q5


def FinalGrade(score, weights):
    total_weighted_score = 0
    total_weight = 0
    for i in range(len(score)):
        total_weighted_score += score[i] * weights[i]
        total_weight += weights[i]
    final_grade = total_weighted_score / total_weight
    return final_grade


Score = [76.5, 90.2, 89.5]
Weight = [0.3, 0.5, 0.4]
print(FinalGrade(Score, Weight))