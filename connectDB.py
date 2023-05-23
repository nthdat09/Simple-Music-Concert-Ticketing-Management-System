import mysql.connector
import Model
db = mysql.connector.connect(
    user = 'mysql-py',
    password = '123456a@b@',
    host = 'localhost',
    database = 'dbms_py'
)
cursor = db.cursor()

class eventManagerDB:
    @classmethod
    def viewAllEvents(cls):
        cursor.execute("SELECT * FROM dbms_py.event")
        result = cursor.fetchall()
        for x in result:
            eventList = []
            for y in x:
                eventList.append(str(y))
            eventModel = Model.event(*eventList)
            Model.event.__str__(eventModel)



    @classmethod
    def addNewEvent(cls):
        print("Enter event ID: ")
        ID = input()
        print("Enter event name: ")
        Name = input()
        print("Enter event date (YYYY-MM-DD): ")
        Date = input()
        print("Enter open time (HH:MM:SS): ")
        Open = input()
        print("Enter end time (HH:MM:SS): ")
        Close = input()
        print("Enter event quantity: ")
        Quantity = input()
        print("Enter event description: ")
        Description = input()

        try:
            cursor.execute("INSERT INTO dbms_py.event VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (ID, Name, 1, 1, Date, Open, Close, Quantity, Description))
            print("Event added successfully!")
            print("Are you sure you want to commit? (Y/N)")
            choice = input()
            if choice == "Y" or choice == "y":
                db.commit()
                print("Commit successfully!")
            else:
                db.rollback()
                print("Commit failed!")
        except Exception as e:
            if e.errno == 1062:
                print("Event added failed! Event ID is duplicated!")
            else:
                print("Event added failed!")

    @classmethod
    def deleteEvent(cls):
        cls.viewAllEvents()
        print("Enter event ID to delete: ")
        eventID = input()
        try:
            cursor.execute("DELETE FROM dbms_py.event WHERE EVT_ID = %s", (eventID,))
            print("Event deleted successfully!")
            db.commit()
        except Exception as e:
            if e.errno == 1451:
                print("Event deleted failed! This event is used in other table!")
            else:
                print("Event deleted failed!")

    @classmethod
    def updateEvent(cls):
        cls.viewAllEvents()
        print("Enter event ID to update: ")
        eventID = input()
        print("What do you want to update?")
        print("1. Event name")
        print("2. Event date")
        print("3. Event open time")
        print("4. Event end time")
        print("5. Event quantity")
        print("6. Event description")
        print("7. All")
        print("8. Cancel")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Enter new event name: ")
            newName = input()
            try:
                cursor.execute("UPDATE dbms_py.event SET EVT_NAME = %s WHERE EVT_ID = %s", (newName, eventID))
                print("Event updated successfully!")

                print("Are you sure you want to commit? (Y/N)")
                choice = input()
                if choice == "Y" or choice == "y":
                    db.commit()
                    print("Commit successfully!")
                else:
                    db.rollback()
                    print("Commit failed!")

            except Exception as e:
                print("Event updated failed!")
                db.rollback()

        elif choice == "2":
            try:
                print("Enter new event date (YYYY-MM-DD): ")
                newDate = input()

                cursor.execute("UPDATE dbms_py.event SET EVT_DATE = %s WHERE EVT_ID = %s", (newDate, eventID))
                print("Event updated successfully!")

                print("Are you sure you want to commit? (Y/N)")
                choice = input()
                if choice == "Y" or choice == "y":
                    db.commit()
                    print("Commit successfully!")
                else:
                    db.rollback()
                    print("Commit failed!")

            except Exception as e:
                print("Event updated failed!")
                db.rollback()

        elif choice == "3":
            try:
                print("Enter new event open time (HH:MM:SS): ")
                newOpen = input()

                cursor.execute("UPDATE dbms_py.event SET EVT_OPEN_TIME = %s WHERE EVT_ID = %s", (newOpen, eventID))
                print("Event updated successfully!")


            except Exception as e:
                print("Event updated failed!")
                db.rollback()
        elif choice == "4":
            try:
                print("Enter new event end time (HH:MM:SS): ")
                newClose = input()
                cursor.execute("UPDATE dbms_py.event SET EVT_END_TIME = %s WHERE EVT_ID = %s", (newClose, eventID))
                print("Event updated successfully!")
                db.commit()
            except Exception as e:
                print("Event updated failed!")
                db.rollback()
        elif choice == "5":
            try:
                print("Enter new event quantity: ")
                newQuantity = input()
                cursor.execute("UPDATE dbms_py.event SET EVT_QUANTITY = %s WHERE EVT_ID = %s", (newQuantity, eventID))
                print("Event updated successfully!")
                db.commit()
            except Exception as e:
                print("Event updated failed!")
                db.rollback()
        elif choice == "6":
            try:
                print("Enter new event description: ")
                newDescription = input()
                cursor.execute("UPDATE dbms_py.event SET EVT_DESCRIPTION = %s WHERE EVT_ID = %s", (newDescription, eventID))
                print("Event updated successfully!")
                db.commit()
            except Exception as e:
                print("Event updated failed!")
                db.rollback()
        elif choice == "7":
            try:
                print("Enter new event name: ")
                newName = input()
                print("Enter new event date (YYYY-MM-DD): ")
                newDate = input()
                print("Enter new event open time (HH:MM:SS): ")
                newOpen = input()
                print("Enter new event end time (HH:MM:SS): ")
                newClose = input()
                print("Enter new event quantity: ")
                newQuantity = input()
                print("Enter new event description: ")
                newDescription = input()
                cursor.execute("UPDATE dbms_py.event SET EVT_NAME = %s, EVT_DATE = %s, EVT_OPEN_TIME = %s, EVT_END_TIME = %s, EVT_QUANTITY = %s, EVT_DESCRIPTION = %s WHERE EVT_ID = %s", (newName, newDate, newOpen, newClose, newQuantity, newDescription, eventID))
                print("Event updated successfully!")
                db.commit()
            except Exception as e:
                print("Event updated failed!")
                db.rollback()
        elif choice == "8":
            print("Update cancelled!")
        else:
            print("Invalid choice!")



class customerManagerDB:
    @classmethod
    def viewAllCustomers(cls):
        cursor.execute("SELECT * FROM dbms_py.customer")
        result = cursor.fetchall()

        for x in result:
            customerList = []
            for y in x:
                customerList.append(str(y))
            customerModel = Model.customer(customerList[0], customerList[1], customerList[2], customerList[3], customerList[4], customerList[5], customerList[6])
            Model.customer.__str__(customerModel)

    @classmethod
    def addNewCustomer(cls):
        print("Enter customer ID: ")
        customerID = input()
        print("Enter customer name: ")
        customerName = input()
        print("Enter customer phone number: ")
        customerPhone = input()
        print("Enter customer email: ")
        customerEmail = input()
        print("Enter customer address: ")
        customerAddress = input()
        print("Enter customer type: ")
        customerType = input()
        print("Enter customer point: ")
        customerPoint = input()
        try:
            cursor.execute("INSERT INTO dbms_py.customer VALUES (%s, %s, %s, %s, %s, %s, %s)", (customerID, customerName, customerPhone, customerEmail, customerAddress, customerType, customerPoint))
            print("Customer added successfully!")
            db.commit()
        except Exception as e:
            if e.errno == 1062:
                print("Customer added failed! Customer ID is duplicated!")
            else:
                print("Customer added failed!")

    @classmethod
    def deleteCustomer(cls):
        cls.viewAllCustomers()
        print("Enter customer ID to delete: ")
        customerID = input()
        try:
            cursor.execute("DELETE FROM dbms_py.customer WHERE CUS_ID = %s", (customerID,))
            print("Customer deleted successfully!")
            db.commit()
        except Exception as e:
            if e.errno == 1451:
                print("Customer deleted failed! This customer has been used in other tables!")
            else:
                print("Customer deleted failed!")

    @classmethod
    def updateCustomer(cls):
        cls.viewAllCustomers()
        print("Enter customer ID to update: ")
        customerID = input()
        print("What do you want to update?")
        print("1. Customer name")
        print("2. Customer phone number")
        print("3. Customer email")
        print("4. Customer address")
        print("5. Customer type")
        print("6. Customer point")
        print("7. All")
        print("8. Cancel")
        print("Enter your choice: ")
        choice = input()
        if choice == '1':
            print("Enter new customer name: ")
            newName = input()
            try:
                cursor.execute("UPDATE dbms_py.customer SET CUS_NAME = %s WHERE CUS_ID = %s", (newName, customerID))
                print("Customer updated successfully!")
                db.commit()
            except Exception as e:
                print("Customer updated failed!")
        elif choice == '2':
            print("Enter new customer phone number: ")
            newPhone = input()
            try:
                cursor.execute("UPDATE dbms_py.customer SET CUS_PHONE_NUMBER = %s WHERE CUS_ID = %s", (newPhone, customerID))
                print("Customer updated successfully!")
                db.commit()
            except Exception as e:
                print("Customer updated failed!")
        elif choice == '3':
            print("Enter new customer email: ")
            newEmail = input()
            try:
                cursor.execute("UPDATE dbms_py.customer SET CUS_EMAIL = %s WHERE CUS_ID = %s", (newEmail, customerID))
                print("Customer updated successfully!")
                db.commit()
            except Exception as e:
                print("Customer updated failed!")
        elif choice == '4':
            print("Enter new customer address: ")
            newAddress = input()
            try:
                cursor.execute("UPDATE dbms_py.customer SET CUS_ADDRESS = %s WHERE CUS_ID = %s", (newAddress, customerID))
                print("Customer updated successfully!")
                db.commit()
            except Exception as e:
                print("Customer updated failed!")
        elif choice == '5':
            print("Enter new customer type: ")
            newType = input()
            try:
                cursor.execute("UPDATE dbms_py.customer SET CUS_TYPE = %s WHERE CUS_ID = %s", (newType, customerID))
                print("Customer updated successfully!")
                db.commit()
            except Exception as e:
                print("Customer updated failed!")
        elif choice == '6':
            print("Enter new customer point: ")
            newPoint = input()
            try:
                cursor.execute("UPDATE dbms_py.customer SET CUS_TOTAL_POINT = %s WHERE CUS_ID = %s", (newPoint, customerID))
                print("Customer updated successfully!")
                db.commit()
            except Exception as e:
                print("Customer updated failed!")
        elif choice == '7':
            print("Enter new customer name: ")
            newName = input()
            print("Enter new customer phone number: ")
            newPhone = input()
            print("Enter new customer email: ")
            newEmail = input()
            print("Enter new customer address: ")
            newAddress = input()
            print("Enter new customer type: ")
            newType = input()
            print("Enter new customer point: ")
            newPoint = input()
            try:
                cursor.execute("UPDATE dbms_py.customer SET CUS_NAME = %s, CUS_PHONE_NUMBER = %s, CUS_EMAIL = %s, CUS_ADDRESS = %s, CUS_TYPE = %s, CUS_TOTAL_POINT = %s WHERE CUS_ID = %s", (newName, newPhone, newEmail, newAddress, newType, newPoint, customerID))
                print("Customer updated successfully!")
                db.commit()
            except Exception as e:
                print("Customer updated failed!")
        elif choice == '8':
            print("Cancel update!")
        else:
            print("Invalid choice!")


class databaseManagerDB:

# Command

    @classmethod
    def executeCommand(cls):
        print("Enter command: ")
        command = input()
        try:
            cursor.execute(command)
            print("Command executed successfully!")
            db.commit()
        except Exception as e:
            print("Command executed failed!")

    @classmethod
    def viewAllTables(cls):
        cursor.execute("SHOW TABLES")
        result = cursor.fetchall()
        for x in result:
            print(x)

# Table

    @classmethod
    def createNewTable(cls):
        print("Enter table name: ")
        tableName = input()
        print("Enter number of columns: ")
        numberOfColumns = input()
        for i in range(int(numberOfColumns)):
            print("Column %d" % (i + 1))
            print("Enter column name: ")
            columnName = input()
            print("Enter column type: ")
            columnType = input()
            print("Enter column length: ")
            columnLength = input()

            try:
                cursor.execute("CREATE TABLE %s (%s %s(%s))" % (tableName, columnName, columnType, columnLength))
                print("Table created successfully!")
                db.commit()
            except Exception as e:
                print("Table created failed!")
                break

    @classmethod
    def deleteTable(cls):
        cls.viewAllTables()
        print("Enter table name to delete: ")
        tableName = input()
        try:
            cursor.execute("DROP TABLE %s" % (tableName,))
            print("Table deleted successfully!")
            db.commit()
        except Exception as e:
            if e.errno == 1051:
                print("Table deleted failed! Table does not exist!")
            else:
                print("Table deleted failed!")

    @classmethod
    def updateTable(cls):
        cls.viewAllTables()
        print("Enter table name to update: ")
        tableName = input()
        print("What do you want to update?")
        print("1. Add column")
        print("2. Delete column")
        print("3. Rename column")
        print("4. Change column type")
        print("5. Cancel update")
        choice = input()
        if choice == '1':
            print("Enter column name: ")
            columnName = input()
            print("Enter column type: ")
            columnType = input()
            print("Enter column length: ")
            columnLength = input()
            try:
                cursor.execute("ALTER TABLE %s ADD %s %s(%s)" % (tableName, columnName, columnType, columnLength))
                print("Table updated successfully!")
                db.commit()
            except Exception as e:
                if e.errno == 1060:
                    print("Table updated failed! Column name is duplicated!")
                else:
                    print("Table updated failed!")
        elif choice == '2':
            print("Enter column name to delete: ")
            columnName = input()
            try:
                cursor.execute("ALTER TABLE %s DROP COLUMN %s" % (tableName, columnName))
                print("Table updated successfully!")
                db.commit()
            except Exception as e:
                if e.errno == 1091:
                    print("Table updated failed! Column does not exist!")
                else:
                    print("Table updated failed!")
        elif choice == '3':
            print("Enter column name to rename: ")
            columnName = input()
            print("Enter new column name: ")
            newColumnName = input()
            try:
                cursor.execute("ALTER TABLE %s RENAME COLUMN %s TO %s" % (tableName, columnName, newColumnName))
                print("Table updated successfully!")
                db.commit()
            except Exception as e:
                if e.errno == 1091:
                    print("Table updated failed! Column does not exist!")
                else:
                    print("Table updated failed!")
        elif choice == '4':
            print("Enter column name to change type: ")
            columnName = input()
            print("Enter new column type: ")
            newColumnType = input()
            print("Enter new column length: ")
            newColumnLength = input()
            try:
                cursor.execute("ALTER TABLE %s MODIFY %s %s(%s)" % (tableName, columnName, newColumnType, newColumnLength))
                print("Table updated successfully!")
                db.commit()
            except Exception as e:
                if e.errno == 1091:
                    print("Table updated failed! Column does not exist!")
                else:
                    print("Table updated failed!")
        elif choice == '5':
            print("Cancel update!")
        else:
            print("Invalid choice!")


    @classmethod
    def showColumnsOfTable(cls):
        cls.viewAllTables()
        print("Enter table name: ")
        tableName = input()
        try:
            cursor.execute("SHOW COLUMNS FROM %s" % (tableName,))
            result = cursor.fetchall()
            for x in result:
                print(x)
        except Exception as e:
            if e.errno == 1051:
                print("Table does not exist!")
            else:
                print("Show columns failed!")



    # Procedure

    @classmethod
    def viewAllProcedures(cls):
        cursor.execute("SHOW PROCEDURE STATUS")
        result = cursor.fetchall()
        for x in result:
            print(x)

    @classmethod
    def createNewProcedure(cls):
        print("Enter procedure name: ")
        procedureName = input()
        print("Enter number of parameters: ")
        numberOfParameters = input()
        for i in range(int(numberOfParameters)):
            print("Parameter %d" % (i + 1))
            print("Enter parameter name: ")
            parameterName = input()
            print("Enter parameter type: ")
            parameterType = input()
            try:
                cursor.execute("CREATE PROCEDURE %s (%s %s)" % (procedureName, parameterName, parameterType))
                print("Procedure created successfully!")
                db.commit()
            except Exception as e:
                if e.errno == 1304:
                    print("Procedure created failed! Procedure name is duplicated!")
                else:
                    print("Procedure created failed!")

    @classmethod
    def deleteProcedure(cls):
        cls.viewAllProcedures()
        print("Enter procedure name to delete: ")
        procedureName = input()
        try:
            cursor.execute("DROP PROCEDURE %s" % (procedureName,))
            print("Procedure deleted successfully!")
            db.commit()
        except Exception as e:
            if e.errno == 1305:
                print("Procedure deleted failed! Procedure does not exist!")
            else:
                print("Procedure deleted failed!")

# Function
    @classmethod
    def viewAllFunctions(cls):
        cursor.execute("SHOW FUNCTION STATUS")
        result = cursor.fetchall()
        for x in result:
            print(x)

    @classmethod
    def createNewFunction(cls):
        print("Enter function name: ")
        functionName = input()
        print("Enter number of parameters: ")
        numberOfParameters = input()
        for i in range(int(numberOfParameters)):
            print("Parameter %d" % (i + 1))
            print("Enter parameter name: ")
            parameterName = input()
            print("Enter parameter type: ")
            parameterType = input()
            try:
                cursor.execute("CREATE FUNCTION %s (%s %s)" % (functionName, parameterName, parameterType))
                print("Function created successfully!")
                db.commit()
            except Exception as e:
                if e.errno == 1304:
                    print("Function created failed! Function name is duplicated!")
                else:
                    print("Function created failed!")

    @classmethod
    def deleteFunction(cls):
        cls.viewAllFunctions()
        print("Enter function name to delete: ")
        functionName = input()
        try:
            cursor.execute("DROP FUNCTION %s" % (functionName,))
            print("Function deleted successfully!")
            db.commit()
        except Exception as e:
            if e.errno == 1305:
                print("Function deleted failed! Function does not exist!")
            else:
                print("Function deleted failed!")

    @classmethod
    def updateFunction(cls):
        cls.viewAllFunctions()
        print("Enter function name to update: ")
        functionName = input()
        print("What do you want to update?")
        print("1. Add parameter")
        print("2. Delete parameter")
        print("3. Rename parameter")
        print("4. Change parameter type")
        print("5. Cancel")
        print("Enter your choice: ")
        choice = input()

    #Trigger

    @classmethod
    def createNewTrigger(cls):
        print("1. Create a new simple trigger")
        print("2. Create a new compound trigger")
        print("3. Cancel")
        print("Enter your choice: ")
        choice = input()
        if choice == '1':
            print("Enter trigger name: ")
            triggerName = input()
            print("Enter table name: ")
            tableName = input()
            print("Enter trigger time: ")
            triggerTime = input()
            print("Enter trigger event: ")
            triggerEvent = input()
            print("Enter trigger body: ")
            triggerBody = input()
            try:
                cursor.execute("CREATE TRIGGER %s %s %s ON %s FOR EACH ROW %s" % (triggerName, triggerTime, triggerEvent, tableName, triggerBody))
                print("Trigger created successfully!")
                db.commit()
            except Exception as e:
                if e.errno == 1304:
                    print("Trigger created failed! Trigger name is duplicated!")
                else:
                    print("Trigger created failed!")
        elif choice == '2':
            print("Enter the command to create a compound trigger: ")
            command = input()
            try:
                cursor.execute(command)
                print("Trigger created successfully!")
                db.commit()
            except Exception as e:
                if e.errno == 1304:
                    print("Trigger created failed! Trigger name is duplicated!")
                else:
                    print("Trigger created failed!")
        elif choice == '3':
            print("Cancel creating trigger!")
        else:
            print("Invalid choice!")

    @classmethod
    def deleteTrigger(cls):
        cls.viewAllTriggers()
        print("Enter trigger name to delete: ")
        triggerName = input()
        try:
            cursor.execute("DROP TRIGGER %s" % (triggerName,))
            print("Trigger deleted successfully!")
            db.commit()
        except Exception as e:
            if e.errno == 1305:
                print("Trigger deleted failed! Trigger does not exist!")
            else:
                print("Trigger deleted failed!")

    @classmethod
    def viewAllTriggers(cls):
        cursor.execute("SHOW TRIGGERS")
        result = cursor.fetchall()
        for x in result:
            print(x)

    @classmethod
    def rollback(cls):
        try:
            cursor.execute("ROLLBACK")
            print("Rollback successfully!")
            db.commit()
        except Exception as e:
            print("Rollback failed!")





            




