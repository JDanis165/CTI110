# Getting input for gas mileage efficiency.
gas_efficiency = float(input())
# Getting input for gas price.
gas_cost = float(input())
# Determining the prices per mile.
per_mile = gas_cost / gas_efficiency
twenty_mile = per_mile * 20
sevenfiv_mile = per_mile * 75
fivhun_mile = per_mile * 500
# Printing Conclusions
print(f'{twenty_mile:.2f} {sevenfiv_mile:.2f} {fivhun_mile:.2f}')