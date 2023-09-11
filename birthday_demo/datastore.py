import json


class DB:

    def __init__(self):
        self.store_filename = 'data_file.json'
        with open("data_file.json", "r") as store_file:
            self.data = json.load(store_file)

    def create_or_update(self, username, dob):
        self.data[username] = dob
        with open("data_file.json", "w") as store_file:
            store_file.write(json.dumps(self.data))

    def get_dob(self, username):
        return self.data[username]
