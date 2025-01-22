

cost_of_rice = 10
cost_of_wheat = 34

qty_of_rice = int(input("Enter qty of rice in kgs: "))
print("Qty of rice:", qty_of_rice)
qty_of_wheat= int(input("Enter qty of wheat in kgs: "))
print("Qty of rice:", qty_of_wheat)

sp_rice = cost_of_rice * qty_of_rice
print("Sp is: ", sp_rice)

sp_wheat = cost_of_wheat* qty_of_wheat
print("Sp is: ", sp_wheat)

total = sp_rice + sp_wheat
print("Total is:", total)