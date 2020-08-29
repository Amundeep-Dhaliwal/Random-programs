import sqlite3, re

def add_bond(entryList):
    with conn: # context manager to automatically commit the INSERT
        c.execute("INSERT INTO OrderCache VALUES (:OrderID, :BondID, :Direction, :Quantity)", 
        {'OrderID':entryList[0], 'BondID': entryList[1], 'Direction':entryList[2], 'Quantity': entryList[3]})

def remove_bond(orderID):
    with conn: 
        c.execute("DELETE from OrderCache WHERE OrderID = :OrderID", {'OrderID': orderID})

def view_all_bonds(returnBondID = False, returnOrderID= False):
    c.execute("SELECT * FROM OrderCache") # SELECT statements do not need to be committed
    transactions = c.fetchall()
    if returnBondID:
        return {entry[1] for entry in transactions}
    elif returnOrderID:
        return {entry[0] for entry in transactions}
    else:
        return transactions

def print_bonds(listBonds):
    print('\nOrder ID     Bond ID     Direction   Quantity')
    for entry in listBonds:
        print(entry[0], '        ', entry[1], '        ', entry[2], '    ', entry[3])
    print('\n')

def view_bondID(bondID):
    c.execute("SELECT * FROM OrderCache WHERE BondID = :BondID", {'BondID':bondID}) # SELECT statements do not need to be committed
    return c.fetchall()

def view_bonds_by_quant(quant):
    c.execute("SELECT * FROM OrderCache WHERE Quantity > :Quantity", {'Quantity':quant}) # SELECT statements do not need to be committed
    return c.fetchall()

def view_all_directions():
    c.execute("SELECT * FROM OrderCache WHERE Direction = :B", {'B': '\'B\''})
    BBonds = c.fetchall()
    boughtBonds = 0
    numBought = len(BBonds)
    for bought in BBonds:
        boughtBonds += bought[3]
    
    c.execute("SELECT * FROM OrderCache WHERE Direction = :S", {'S': '\'S\''})
    SBonds = c.fetchall() 
    soldBonds = 0
    numSold = len(SBonds)
    for sold in SBonds:
        soldBonds += sold[3]
    return f'\nThe number of bought bond(s) is {numBought} with a total value of {boughtBonds}\n\
The number of sold bond(s) is {numSold}, with the total value of {soldBonds}\n\
The difference between the quantities of sold and bought bonds is {boughtBonds-soldBonds}.\n'

def main():
    print('\nWelcome to the Sovereign bonds platform.\nThis platform can be used to add/manage bonds.\n')
    while True:
        userInput = ''
        while userInput not in {'add', 'cancel', 'view', 'exit'}: 
            userInput = input('Please enter a valid operation (add/cancel/view/exit): ')
        
        if userInput == 'add':
            numAdd = ''
            while not re.match(r'\d+', numAdd):
                numAdd = input('Please enter the number of additions you wish to make: ')
            
            for _ in range(int(numAdd)):
                entry = '' 
                while not re.match(r'ID\d+\s\w{5}\s\'(B|S)\'\s\d+', entry):
                    entry = input('Please enter the order ID, bond ID, direction(B/S) and quantity all seperated by spaces: ')
                add_bond(entry.split())
            
            print('Entries successfully added.')
        
        elif userInput == 'view':
            currBonds = view_all_bonds()
            if len(currBonds)==0:
                print('No bonds to show.')
                continue
            else:
                print_bonds(currBonds)
            
            
            print('\n\nYou can also perform the following queries:\n\
-A specific bond ID\n\
-All the entries that have traded above a given quantity\n\
-Total number of buy/sell transactions and their difference')
            viewInput = '' 
            while viewInput not in {'exit','bond ID', 'quantity', 'total'}:
                viewInput = input('\nPlease enter one of the options (bond ID, quantity, total, exit): ')
            
            if viewInput == 'exit':
                continue

            elif viewInput == 'bond ID':
                allNames = view_all_bonds(returnBondID=True)
                bondInput = ''
                while bondInput not in allNames:
                    bondInput = input('Please enter the bond name: ')
                
                listOfBonds = view_bondID(bondInput)
                print_bonds(listOfBonds)
            
            elif viewInput == 'quantity':
                while True: 
                    try:
                        userQuantity = int(input('Please enter the quantity: '))
                    except:
                        continue
                    else:
                        break
                biggerQuant = view_bonds_by_quant(userQuantity)
                print_bonds(biggerQuant)
            
            elif viewInput == 'total':
                print(view_all_directions())
            
        elif userInput == 'cancel':
            currBonds = view_all_bonds()
            if len(currBonds)==0:
                print('No bonds to cancel.')
                continue
            else:
                print_bonds(currBonds)
            
            orderIDs = view_all_bonds(returnOrderID=True)
            cancelInput = ''
            while cancelInput not in orderIDs:
                cancelInput = input('Please enter the order ID that you would like to cancel: ')
            remove_bond(cancelInput)
            print('Bond successfully cancelled.')
        
        else: 
            break

    
    
    print('\nThank you for using this system.')


if __name__ == '__main__':
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute("""CREATE TABLE OrderCache (
                OrderID text, 
                BondID text, 
                Direction text,
                Quantity integer
                )""")
    main()
    conn.close()