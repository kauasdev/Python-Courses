withdraw_value = int(input("How much do you want to withdraw: "))

bills_50 = bills_20 = bills_10 = bills_1 = 0

bills_50 = withdraw_value // 50
withdraw_value -= (bills_50 * 50)
bills_20 = withdraw_value // 20
withdraw_value -= (bills_20 * 20)
bills_10 = withdraw_value // 10
withdraw_value -= (bills_10 * 20)
bills_1 = withdraw_value // 1

print(f"{'='*25}")
if bills_50 > 0:
    print(f"Total of {bills_50} $50 bills")
if bills_20 > 0:
    print(f"Total of {bills_20} $20 bills")
if bills_10 > 0:
    print(f"Total of {bills_10} $10 bills")
if bills_1 > 0:
    print(f"Total of {bills_1} $1 bills")
