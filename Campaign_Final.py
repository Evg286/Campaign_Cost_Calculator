from time import sleep

print("Welcome to your campaign budget wizard!")
sleep(1)

budget = int(input("\nEnter your budget: \n"))

print("\nRunning a campaign on facebook costs 100 ILS per day. \nRunning a campaign on instagram costs 50 ILS per day.")
sleep(1)

facebook = int(input("\nEnter the number of days you would like to run your facebook campaign: "))
instagram = int(input("Enter the number of days you would like to run your instagram campaign: "))
sleep(1)

summary = (facebook*100) + (instagram*50)

short = (summary*1.17) - (budget)

print("\nYour total campaign cost is " + str("%.2f" % (summary*1.17)) + " ILS, VAT included.")


if budget >= (summary*1.17):
    print ("\nSuccess")
else:
    print ("\nInsufficient Funds. Please add " + str("%.2f" % (short) + " ILS."))




