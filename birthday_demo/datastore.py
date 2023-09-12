import json
import os


class DB:
    '''
    A class providing data storage and retrieval

    Methods
    -------
    __init__():
        Loads the data in `store_filename` and creates it if it doesn't exist
    create_or_update(username):
        Creates or updates a user record.
    get_dob(username):
        Returns the stored DOB for a user.
    '''

    def __init__(self):
        self.store_filename = '/tmp/data_file.json'
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
