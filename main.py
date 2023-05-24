import os
import Controller


def mainMenu():
    while True:
        os.system('cls')
        print("Music concert ticket booking manager program")
        print("1. Event manager")
        print("2. Customer manager")
        print("3. Database manager")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            eventManager()
        elif choice == "2":
            customerManager()
        elif choice == "3":
            databaseManager()
        elif choice == "4":
            print("Thank you for using our program!")
            break
        else:
            print("Invalid choice, please try again.")
            input("Enter any key to continue ")


def eventManager():
    while True:
        os.system('cls')
        print("Event manager")
        print("1. View all events")
        print("2. Search event")
        print("3. Add new event")
        print("4. Delete event")
        print("5. Update event")
        print("6. Main menu")
        choice = input("Enter your choice: ")
        os.system('cls')
        if choice == "1":
            Controller.eventManagerController.viewAllEvents()
        elif choice == "2":
            Controller.eventManagerController.searchEvent()
        elif choice == "3":
            Controller.eventManagerController.addNewEvent()
        elif choice == "4":
            Controller.eventManagerController.deleteEvent()
        elif choice == "5":
            Controller.eventManagerController.updateEvent()
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")


def customerManager():
    while True:
        os.system('cls')
        print("Customer manager")
        print("1. View all customers")
        print("2. Search customer")
        print("3. Add new customer")
        print("4. Delete customer")
        print("5. Update customer")
        print("6. Main menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            Controller.customerManagerController.viewAllCustomers()
        elif choice == "2":
            Controller.customerManagerController.searchCustomer()
        elif choice == "3":
            Controller.customerManagerController.addNewCustomer()
        elif choice == "4":
            Controller.customerManagerController.deleteCustomer()
        elif choice == "5":
            Controller.customerManagerController.updateCustomer()
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")
            input("Enter any key to continue ")


def tableManager():
    while True:
        os.system('cls')
        print("Table manager")
        print("1. View all tables")
        print("2. Show columns of table")
        print("3. Create new table")
        print("4. Delete table")
        print("5. Update table")
        print("6. Back to database manager menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            Controller.databaseManagerController.viewAllTables()
        elif choice == "2":
            Controller.databaseManagerController.showColumnsOfTable()
        elif choice == "3":
            Controller.databaseManagerController.createNewTable()
        elif choice == "4":
            Controller.databaseManagerController.deleteTable()
        elif choice == "5":
            Controller.databaseManagerController.updateTable()
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")


def triggerManager():
    while True:
        os.system('cls')
        print("Trigger manager")
        print("1. View all triggers")
        print("2. Create new trigger")
        print("3. Delete trigger")
        print("4. Back to database manager menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            Controller.databaseManagerController.viewAllTriggers()
        elif choice == "2":
            Controller.databaseManagerController.createNewTrigger()
        elif choice == "3":
            Controller.databaseManagerController.deleteTrigger()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")


def functionManager():
    while True:
        os.system('cls')
        print("Function manager")
        print("1. View all functions")
        print("2. Create new function")
        print("3. Delete function")
        print("4. Back to database manager menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            Controller.databaseManagerController.viewAllFunctions()
        elif choice == "2":
            Controller.databaseManagerController.createNewFunction()
        elif choice == "3":
            Controller.databaseManagerController.deleteFunction()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")
            input("Enter any key to continue ")


def procedureManager():
    while True:
        os.system('cls')
        print("Procedure manager")
        print("1. View all procedures")
        print("2. Create new procedure")
        print("3. Delete procedure")
        print("4. Back to database manager menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            Controller.databaseManagerController.viewAllProcedures()
        elif choice == "2":
            Controller.databaseManagerController.createNewProcedure()
        elif choice == "3":
            Controller.databaseManagerController.deleteProcedure()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")


def executeCommand():
    while True:
        os.system('cls')
        print("Execute a command")
        print("1. Enter a command")
        print("2. Back to database manager menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            Controller.databaseManagerController.executeCommand()
        elif choice == "2":
            break
        else:
            print("Invalid choice, please try again.")
            input("Enter any key to continue ")


def databaseManager():
    while True:
        os.system('cls')
        print("Database manager")
        print("1. Table manager")
        print("2. Trigger manager")
        print("3. Function manager")
        print("4. Procedure manager")
        print("5. Execute a command")
        print("6. Main menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            tableManager()
        elif choice == "2":
            triggerManager()
        elif choice == "3":
            functionManager()
        elif choice == "4":
            procedureManager()
        elif choice == "5":
            executeCommand()
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")


class main:
    mainMenu()
