
# cost of items

cost_of_wheat = 25
cost_of_rice = 12

# quantitie of items
qty_of_wheat = 30
qty_of_rice = 50

# selling price
sp_of_wheat = cost_of_wheat * qty_of_wheat
sp_of_rice = cost_of_rice * qty_of_rice

Total_sp = sp_of_wheat + sp_of_rice
print("Total SP:", Total_sp)

# SUBSIDIY calculation

subsidy_amount = (Total_sp * 20)/100  #PEMDAS
print("Subsidy amt:", subsidy_amount)

Billable = Total_sp - subsidy_amount
print("Billable amt:", Billable)


#PEMDAS  - OPERATOR PRECEDENCE SEQUENCE