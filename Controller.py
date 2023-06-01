import connectDB


class eventManagerController:

    @classmethod
    def viewAllEvents(cls):
        connectDB.eventManagerDB.viewAllEvents()
        input("Enter any key to continue ")

    @classmethod
    def addNewEvent(cls):
        connectDB.eventManagerDB.addNewEvent()
        input("Enter any key to continue ")

    @classmethod
    def deleteEvent(cls):
        connectDB.eventManagerDB.deleteEvent()
        input("Enter any key to continue ")

    @classmethod
    def updateEvent(cls):
        connectDB.eventManagerDB.updateEvent()
        input("Enter any key to continue ")

    @classmethod
    def searchEvent(cls):
        connectDB.eventManagerDB.searchEvent()
        input("Enter any key to continue ")


class customerManagerController:
    @classmethod
    def viewAllCustomers(cls):
        connectDB.customerManagerDB.viewAllCustomers()
        input("Enter any key to continue ")

    @classmethod
    def addNewCustomer(cls):
        connectDB.customerManagerDB.addNewCustomer()
        input("Enter any key to continue ")

    @classmethod
    def deleteCustomer(cls):
        connectDB.customerManagerDB.deleteCustomer()
        input("Enter any key to continue ")

    @classmethod
    def updateCustomer(cls):
        connectDB.customerManagerDB.updateCustomer()
        input("Enter any key to continue ")

    @classmethod
    def searchCustomer(cls):
        connectDB.customerManagerDB.searchCustomer()
        input("Enter any key to continue ")


class databaseManagerController:

    @classmethod
    def executeCommand(cls):
        connectDB.databaseManagerDB.executeCommand()
        input("Enter any key to continue ")

    @classmethod
    def viewAllTables(cls):
        connectDB.databaseManagerDB.viewAllTables()
        input("Enter any key to continue ")

    @classmethod
    def createNewTable(cls):
        connectDB.databaseManagerDB.createNewTable()
        input("Enter any key to continue ")

    @classmethod
    def deleteTable(cls):
        connectDB.databaseManagerDB.deleteTable()
        input("Enter any key to continue ")

    @classmethod
    def updateTable(cls):
        connectDB.databaseManagerDB.updateTable()
        input("Enter any key to continue ")

    @classmethod
    def viewAllTriggers(cls):
        connectDB.databaseManagerDB.viewAllTriggers()
        input("Enter any key to continue ")

    @classmethod
    def createNewTrigger(cls):
        connectDB.databaseManagerDB.createNewTrigger()
        input("Enter any key to continue ")

    @classmethod
    def deleteTrigger(cls):
        connectDB.databaseManagerDB.deleteTrigger()
        input("Enter any key to continue ")

    @classmethod
    def updateTrigger(cls):
        pass

    @classmethod
    def viewAllFunctions(cls):
        connectDB.databaseManagerDB.viewAllFunctions()
        input("Enter any key to continue ")

    @classmethod
    def createNewFunction(cls):
        connectDB.databaseManagerDB.createNewFunction()
        input("Enter any key to continue ")

    @classmethod
    def deleteFunction(cls):
        connectDB.databaseManagerDB.deleteFunction()
        input("Enter any key to continue ")

    @classmethod
    def updateFunction(cls):
        connectDB.databaseManagerDB.updateFunction()
        input("Enter any key to continue ")

    @classmethod
    def viewAllProcedures(cls):
        connectDB.databaseManagerDB.viewAllProcedures()
        input("Enter any key to continue ")

    @classmethod
    def createNewProcedure(cls):
        connectDB.databaseManagerDB.createNewProcedure()
        input("Enter any key to continue ")

    @classmethod
    def deleteProcedure(cls):
        connectDB.databaseManagerDB.deleteProcedure()
        input("Enter any key to continue ")

    @classmethod
    def showColumnsOfTable(cls):
        connectDB.databaseManagerDB.showColumnsOfTable()
        input("Enter any key to continue ")

    @classmethod
    def runProcedure(cls):
        connectDB.databaseManagerDB.runProcedure()
        input("Enter any key to continue ")

    @classmethod
    def runFunction(cls):
        connectDB.databaseManagerDB.runFunction()
        input("Enter any key to continue ")
