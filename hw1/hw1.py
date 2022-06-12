price = float(input("Enter the purchase price: "))
headers = ["Month", "Starting Balance", "Interest to Pay", "Principal to Pay", "Payment", "Ending Balance"]
yc = 1
interest = 0
princ = 0
payment = 0
dp = price*0.1
sbal = price-dp
ebal = 0
table = []
table.append(headers)
while(sbal>0):
	#print("one")
	interest = 0.01*sbal
	payment = (price-dp)*0.05
	princ = payment-interest 
	ebal = sbal-princ
	if(ebal<0):
		ebal = 0
	temp = ["{:10}".format(str(yc)), "{:10}".format("{:.2f}".format(sbal, "0.2f")), "{:10}".format("{:.2f}".format(interest, "0.2f")), "{:10}".format("{:.2f}".format(princ, "0.2f")), "{:10}".format("{:.2f}".format(payment, "0.2f")), "{:10}".format("{:.2f}".format(ebal, "0.2f"))]
	table.append(temp)
	sbal = ebal
	yc+=1

count = 1
for row in table:
	if(count == 1):
		print(" ".join(row))
	else:
		print("".join(row))
	count+=1
