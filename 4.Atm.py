
bankUser ={
    'kumar':{
    'postion':'silver',
    'limit':2000,
    'workingAtmCard':True,
    'cardPin':1234,
    'currentBalance':35000
    },
    'ravi':{
    'postion':'gold',
    'limit':3000,
    'workingAtmCard':True,
    'cardPin':1235,
    'currentBalance':55000
    },
    'bharathi':{
    'postion':'platinum',
    'limit':5000,
    'cardPin':1236,
    'workingAtmCard':True,
    'currentBalance':95000
    }
}



def WithdrawalAmount(withdrawal,user):
    if ((withdrawal % 1000 == 500) or (withdrawal % 1000 == 0)) :
        if(withdrawal <= user['currentBalance']):
            if(withdrawal <= user['limit']):
                user['currentBalance'] = user['currentBalance'] - withdrawal
                print('withdrawal successfully')
                print('Balance:',user['currentBalance'])
            else:
                print('Your per day you limit is:',user['limit'])

        else:
            print('Insufficient balance')
    else:
        print('Withdrawal minimum 500')
     

def AmountProcessing(user):
    print('Choose the option')
    atmOption = int(input(' 1.Balance \n 2.Deposit \n 3.Withdrawal \n 4.Statement \n :'))
    if atmOption == 1: 
        print('Account current balance is:' ,user['currentBalance'])
    elif atmOption == 2:
        print('Please you deposite 500 cash only')
        depositeAmount = int(input('Please enter the cash:'))
        if ((depositeAmount % 1000 == 500) or (depositeAmount % 1000 == 0) ) :
            user['currentBalance'] = user['currentBalance'] + depositeAmount
            print('Deposite successfully')
            print('Balance:',user['currentBalance'])
        else:

            print('The machine not accept the :',depositeAmount % 1000)
            print('Minimum deposite 500')

    elif atmOption == 3:

        withdrawal = int(input(' 1.1000 \n 2.2000 \n 3.4000 \n 4.others \n :'))
        if(withdrawal <= 3): 
            if(withdrawal <= user['currentBalance']):
                user['currentBalance'] = user['currentBalance'] - withdrawal
                print('withdrawal successfully')
                print('Balance:',user['currentBalance'])
            else:
                print('Insufficient balance')
        elif(withdrawal == 4):
            withdrawal = int(input('Enter the amount:'))
            WithdrawalAmount(withdrawal,user)
        else:
            print('The atm machine not accept this option please enter the correct option')

    elif atmOption == 4:
        print(
        ' position:',user['postion'],
        '\n limit:',user['limit'],
        '\n Card status:',user['workingAtmCard'],
        '\n Card pin:',user['cardPin'],
        '\n Current balance:',user['currentBalance']
        )
    
    else:
        print('The atm machine not accept this option please enter the correct option')

    
    exit()
    

def AtmMachine():
    atmMachile = 'y'
    userUseAccount = 0
    while atmMachile != 'n':

        userUseAccount = userUseAccount + 1

        insertCard = input('Please insert your card:') # name
        atmPin = int(input('Please enter your pin:'))  # int number
        if insertCard in bankUser:
            if atmPin == bankUser[insertCard]['cardPin']:
                if(bankUser[insertCard]['workingAtmCard']):
                    AmountProcessing(bankUser[insertCard])
                else:
                    print('Your card is locked please can see your bank')
            else:
                if(userUseAccount != 3):
                    print('Pin number is wrong please correct your pin number')
                else:
                    print('Your card is locked please can see your bank')
                    bankUser[insertCard]['workingAtmCard'] = False
                    atmMachile = 'n'
        else:
            print('User is invalid please check your bank')
            atmMachile = input('click "n" means your translation be cancel')
        

AtmMachine()















