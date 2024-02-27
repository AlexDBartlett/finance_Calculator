'''
start
1. import math module
2. User should be able to choose a type of caculation
3. ask the user to enter a type of calculation using the given statement:

"investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed:"

4. Capitalisation should not affect how this runs. i.e  'Bond', 'bond', 'BOND' should all work.
5. if the user chose bond then ask for the following;
    - What is the value of the house
    - What is your interest rate?
    - How many months do you plan to repay?
6. Calculate the result using this formula: repayment = (i * P)/(1 - (1 + i)**(-n))
7. Print the result

8. If the user chose investment then ask for the following:
    - Ask the user how much money they are depoisiting
    - Ask the user the intereste rate as a percentage. (no percentage sign)
    - Ask the user the number of years they plan to invest.
    - Ask the user if they want "simple" or "Compound" interest and store as a variable called interest
    
9. If the user chose simple then calculate using the folowing formula: A = P * (1+r*t). Then print the result
10. If the user chose compound then calculate using the folowing formula: A = P * math.pow((1+r),t). Then print the result.

11. If the user did not enter either investement or bond in the beginning loop back to start and give error.
end
'''

import math

while True:
    
    # print the provided intro statement before asking the user for input
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond - to calculate the amount you'll have to pay on a home loan")

    # Ask the user whether they want an investment or a bond
    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:")

    # convert the user's choice to lowercase so it doesn't matter which casing they typed as input
    convert_choice = choice.lower()

    # If the user asked for a bond then do the following steps
    if convert_choice == 'bond':
        
        # Ask the user for the value of the house
        P = float(input("What is the value of the house?"))
        
        # Ask the user for their interest rate
        i = float(input("What is your interest rate?")) / 100 
        
        # Ask the user how many months they plan to repay
        n = int(input("How many months do you plan to repay?"))
        
        # Calculate the repayment figure using the values provided
        repayment = (i * P) / (1 - (1 + i)**(-n))
        
        # Print the result
        print(f"The monthly repayment amount for your bond is: £{repayment:.2f}")
        
    # If the user asked for an investment, then do the following steps
    elif convert_choice == 'investment':
        
        # Ask the user how much money they are depoisiting
        P = float(input("How much are you depositing?"))

        # Ask the user the intereste rate as a percentage. (no percentage sign)
        r = float(input("What is your interest rate?")) / 100

        # Ask the user the number of years they plan to invest
        t = int(input("How many years are you investing?"))
        
        #ask if they want "simple" or "Compound" interest
        interest = input("Do you want simple or compound interest?") 
        
        # Convert interest input to lowercase to avoid casing issues
        converted_interest = interest.lower()

        # Simple interest route - if the user asked for an investment and interest =  'simple', do the following formula ' A = P *(1 + r*t)'
        if converted_interest == 'simple':
            A = P * (1 + r * t)
            print(f"The final amount after {t} years with simple interest is {A:.2f}")
        
        # Compound interest route - if the user asked for an investment and interest = 'compound', do the following formula 'A = P math.pow((1+r),t)'   
        elif converted_interest == 'compound':
            A = P * math.pow(( 1 + r), t)
            print(f"The final amount after {t} years with compound interest is {A:.2f}") 

    # If the user did not enter either 'bond' or 'investment then print the below and loop to start      
    else:
        print("Please enter either investment or bond.")
        

    
