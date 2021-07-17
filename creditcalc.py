import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--payment')
parser.add_argument('--periods')
parser.add_argument('--interest')

args = parser.parse_args()

cal_type = args.type
principal = args.principal
payment = args.payment
periods = args.periods
interest = args.interest

if cal_type not in ["annuity", "diff"]:
    print("Incorrect parameters.")
    exit()

if cal_type == "diff":
    if principal and periods and interest and (not payment) and int(principal) >= 0 and int(periods) >= 0 \
            and float(interest) >= 0:
        principal = int(principal)
        periods = int(periods)
        interest = float(interest) / (100 * 12)

        total_payment = 0
        for i in range(1, periods + 1):
            D = math.ceil((principal / periods) + interest * (principal - principal * (i - 1) / periods))
            total_payment += D
            print(f"Month {i}: payment is {D}")

        print(f"\nOverpayment = {abs(principal - total_payment)}")
    else:
        print("Incorrect parameters.")
elif cal_type == "annuity":
    if principal and periods and interest and (not payment) and int(principal) >= 0 and int(periods) >= 0 \
            and float(interest) >= 0:
        loan_principle = int(principal)
        periods = int(periods)
        loan_interest = float(interest)

        i = loan_interest / (12 * 100)

        annuity = math.ceil(loan_principle * i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1))

        print(f"Your annuity payment = {annuity}!")
        print(f"Overpayment = {abs(loan_principle - annuity * periods)}")
    if principal and payment and interest and (not periods) and int(principal) >= 0 and int(payment) >= 0 \
            and float(interest) >= 0:
        loan_principle = int(principal)
        monthly_payment = int(payment)
        loan_interest = float(interest)

        i = loan_interest / (12 * 100)
        n = math.ceil(math.log(monthly_payment / (monthly_payment - i * loan_principle), i + 1))

        n_years = math.floor(n / 12) if n > 12 else 0
        n_months = n - math.floor(n / 12) * 12

        year_string = f"{n_years} year{'s' if n_years > 1 else ''}" if n_years > 0 else ""
        month_string = f"{n_months} month{'s' if n_months > 1 else ''}" if n_months > 0 else ""

        duration_string = f"{year_string} {'and' if n_years + n_months > 0 else ''} {month_string}"

        print(f"It will take {year_string} to repay this loan!")
        print(f"Overpayment = {abs(loan_principle - monthly_payment * n)}")
    if periods and payment and interest and (not principal) and int(periods) >= 0 and int(payment) >= 0 \
            and float(interest) >= 0:
        annuity = int(payment)
        periods = int(periods)
        loan_interest = float(interest)

        i = loan_interest / (12 * 100)
        loan_principle = round(annuity / (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1)))

        print(f"Your loan principal = {loan_principle}!")
        print(f"Overpayment = {abs(loan_principle - periods * annuity)}!")
    else:
        print("Incorrect parameters.")
