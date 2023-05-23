import Model
import connectDB
class eventManagerController:

    @classmethod
    def viewAllEvents(cls):
        connectDB.eventManagerDB.viewAllEvents()
        print("Enter any key to continue:")
        input()

    @classmethod
    def addNewEvent(cls):
        connectDB.eventManagerDB.addNewEvent()
        print("Enter any key to continue:")
        input()

    @classmethod
    def deleteEvent(cls):
        connectDB.eventManagerDB.deleteEvent()
        print("Enter any key to continue:")
        input()

    @classmethod
    def updateEvent(cls):
        connectDB.eventManagerDB.updateEvent()
        print("Enter any key to continue:")
        input()


class customerManagerController:
    @classmethod
    def viewAllCustomers(cls):
        connectDB.customerManagerDB.viewAllCustomers()
        print("Enter any key to continue:")
        input()

    @classmethod
    def addNewCustomer(cls):
        connectDB.customerManagerDB.addNewCustomer()
        print("Enter any key to continue:")
        input()

    @classmethod
    def deleteCustomer(cls):
        connectDB.customerManagerDB.deleteCustomer()
        print("Enter any key to continue:")
        input()

    @classmethod
    def updateCustomer(cls):
        connectDB.customerManagerDB.updateCustomer()
        print("Enter any key to continue:")
        input()


class databaseManagerController:

    @classmethod
    def executeCommand(cls):
        connectDB.databaseManagerDB.executeCommand()
        print("Enter any key to continue:")
        input()

    @classmethod
    def viewAllTables(cls):
        connectDB.databaseManagerDB.viewAllTables()
        print("Enter any key to continue:")
        input()

    @classmethod
    def createNewTable(cls):
        connectDB.databaseManagerDB.createNewTable()
        print("Enter any key to continue:")
        input()

    @classmethod
    def deleteTable(cls):
        connectDB.databaseManagerDB.deleteTable()
        print("Enter any key to continue:")
        input()

    @classmethod
    def updateTable(cls):
        connectDB.databaseManagerDB.updateTable()
        print("Enter any key to continue:")
        input()

    @classmethod
    def viewAllTriggers(cls):
        connectDB.databaseManagerDB.viewAllTriggers()
        print("Enter any key to continue:")
        input()

    @classmethod
    def createNewTrigger(cls):
        connectDB.databaseManagerDB.createNewTrigger()
        print("Enter any key to continue:")
        input()

    @classmethod
    def deleteTrigger(cls):
        connectDB.databaseManagerDB.deleteTrigger()
        print("Enter any key to continue:")
        input()

    @classmethod
    def updateTrigger(cls):
        pass

    @classmethod
    def viewAllFunctions(cls):
        connectDB.databaseManagerDB.viewAllFunctions()
        print("Enter any key to continue:")
        input()

    @classmethod
    def createNewFunction(cls):
        connectDB.databaseManagerDB.createNewFunction()
        print("Enter any key to continue:")
        input()

    @classmethod
    def deleteFunction(cls):
        connectDB.databaseManagerDB.deleteFunction()
        print("Enter any key to continue:")
        input()

    @classmethod
    def updateFunction(cls):
        connectDB.databaseManagerDB.updateFunction()
        print("Enter any key to continue:")
        input()

    @classmethod
    def viewAllProcedures(cls):
        connectDB.databaseManagerDB.viewAllProcedures()
        print("Enter any key to continue:")
        input()

    @classmethod
    def createNewProcedure(cls):
        connectDB.databaseManagerDB.createNewProcedure()
        print("Enter any key to continue:")
        input()

    @classmethod
    def deleteProcedure(cls):
        connectDB.databaseManagerDB.deleteProcedure()
        print("Enter any key to continue:")
        input()

    @classmethod
    def showColumnsOfTable(cls):
        connectDB.databaseManagerDB.showColumnsOfTable()
        print("Enter any key to continue:")
        input()


