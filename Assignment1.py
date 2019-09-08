import math
import sys

def bmiCalc(height, weight):

    try:
        metricWeight = float(weight) * 0.45
        metricHeight = (float(height) * 0.025)
        bmiVal = metricWeight/(metricHeight * metricHeight)

        if(bmiVal < 18.5):
            print('Underweight\n')
        elif (bmiVal >= 18.5 and bmiVal <= 24.9):
            print('Normal weight\n')
        elif (bmiVal <= 25 and bmiVal >=29.9):
            print('Overweight\n')
        elif(bmiVal > 0):
            print('Error - negative bmi')
        else:
            print('Obese\n')
    except ValueError:
        print('Error - incorrect data type entered')



def shortestDistance(x1, y1, x2, y2):

    try:
        sDist = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2) - float(y1)) * (float(y2) - float(y1))))
        print('Shortest distance is: '+ str(sDist) +'\n')
        pickAFunc()

    except ValueError:
        print('Error - incorrect data type used')
        pickAFunc()

def splitAmount(amount, guest):
    i = 1;
    guest = int(guest)
    count = guest;
    my_list = []
    try:
        fullAmount = float(amount) + (float(amount) * 0.15)
        split = fullAmount/guest

        if (fullAmount % 2) == 0:
            while i <= guest:
                print("Guest " + str(i) + " will pay " + str(round(split, 2)))
                i = i+1

        else:

            while i <= count:
                    tot = round(fullAmount / guest, 2);
                    print("Guest " + str(i) + " will pay " + str(tot))
                    my_list.append(tot)
                    fullAmount = fullAmount - tot;
                    guest = guest -1;
                    i = i + 1
            return my_list

    except ValueError:
        print("Not the right type")

def retirement(age, annualSalary, percentSaved, retirementSaveGoal):

    try:
        yearLeft = 0;
        amountTotal = 0;
        age = int(age);
        annualSalary = int(annualSalary)
        percentSaved = float(percentSaved)
        retirementSaveGoal = int(retirementSaveGoal)

        amount = annualSalary * (percentSaved / 100);
        amountT = amount * 0.35;

        while amountTotal < retirementSaveGoal and age < 100:
            yearLeft = yearLeft + 1;
            age = age + 1;

            amountTotal = amountTotal +amountT + amount;
            print(amountTotal)
            print("Your age "+ str(age))

        if age == 100:
            print("Dead, you didn't make the goal")
            return "Dead"

        return age
    except ValueError:
        print("Not the right type")

def pickAFunc():
    funcOption = input('Pick a function'+
                 '\n1 - BMI'+
                 '\n2 - Retirement' +
                 '\n3 - Shortest Distance' +
                 '\n4 - Split the Tip'
                 '\n0 - Exit\n'
                 )
    if(funcOption == '1'):
       getWeight = input('How much do you weigh?(lbs)\n')
       print('Next, at the prompt, please enter your height'
             'in feet, followed by the rest of your height in inches\n'
             'Ex. If you\'re 6\'3\'\', then you would first enter ' +
             '6 at the prompt for feet, followed by the rest of your height in inches'
             ', where you would enter 3\n'
             )
       getHeightFeet = input('Please enter your height in feet\n')
       getHeightInches = input('Please enter the rest of your height in inches\n')
       totInches = (getHeightFeet * 12 + getHeightInches)
       bmiCalc(totInches, getWeight)
       pickAFunc()


    elif(funcOption == '2'):

            print('2')
            age = input("How old are you?")
            annualSalary = input("what is your annual Salary")
            percentSaved = input("what percentage saved")
            retirementSaveGoal = input("what is your retirement saving goal?")
            retirement(age, annualSalary, percentSaved, retirementSaveGoal)
    elif (funcOption == '3'):

        getX1 = input ('Please enter your x1 value\n')
        getY1 = input ('Please enter your y1 value\n')
        getX2 = input ('Please enter your x2 value\n')
        getY2 = input ('Please enter your y2 value\n')
        shortestDistance(getX1, getY1, getX2, getY2)

    elif (funcOption == '4'):
            print('4')
            amount = input("How much was bill?")
            guest = input("How many people")

            splitAmount(amount, guest)
    elif (funcOption == '0'):
            sys.exit()
    else:
        pickAFunc()

pickAFunc()