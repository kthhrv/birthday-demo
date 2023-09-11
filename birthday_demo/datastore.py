import json
import os


class DB:

    def __init__(self):
        self.store_filename = 'data_file.json'
        if not os.path.isfile(self.store_filename):
            print('creating DB')
            with open(self.store_filename, "w") as store_file:
                store_file.write('{}')
        with open(self.store_filename, "r") as store_file:
            self.data = json.load(store_file)

    def create_or_update(self, username, dob):
        self.data[username] = dob
        with open(self.store_filename, "w") as store_file:
            store_file.write(json.dumps(self.data))

    def get_dob(self, username):
        if not username in self.data:
            return None
        return self.data[username]
