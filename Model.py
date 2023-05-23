class customer:
    id = 0
    name = ""
    phone_number = ""
    email = ""
    address = ""
    type = ""
    totalpoint = 0

    def __init__(self, id, name, phone_number, email, address, type, totalpoint):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.type = type
        self.totalpoint = totalpoint

    def __str__(self):
        print("- ID: " + str(self.id) + ", Name: " + self.name + ", Phone number: " + self.phone_number + ", Email: " + self.email + ", Address: " + self.address + ", Type: " + self.type + ", Total point: " + str(self.totalpoint))

class event:
    id = 0
    name = ""
    stage_id = 0
    artist_id = 0
    date = ""
    open_time = ""
    end_time = ""
    quantity = 0
    des = ""

    def __init__(self, id, name, stage_id, artist_id, date, open_time, end_time, quantity, des):
        self.id = id
        self.name = name
        self.stage_id = stage_id
        self.artist_id = artist_id
        self.date = date
        self.open_time = open_time
        self.end_time = end_time
        self.quantity = quantity
        self.des = des

    def __str__(self):
        print("- ID: " + str(self.id) + ", Name: " + self.name + ", Stage ID: " + str(self.stage_id) + ", Artist ID: " + str(self.artist_id) + ", Date: " + self.date + ", Open time: " + self.open_time + ", End time: " + self.end_time + ", Quantity: " + str(self.quantity) + ", Description: " + self.des)

