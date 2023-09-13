"""Simple data store."""

import json
import os
import typing


class DB:
    """A class providing data storage and retrieval.

    Methods
    -------
    __init__():
        Loads the data in `store_filename` and creates it if it doesn't exist
    create_or_update(username, dob):
        Creates or updates a user record.
    get_dob(username):
        Returns the stored DOB for a user.
    """

    def __init__(self):
        """Load data or create empty store."""
        self.store_filename = '/tmp/data_file.json'
        if not os.path.isfile(self.store_filename):
            with open(self.store_filename, "w") as store_file:
                store_file.write('{}')
        with open(self.store_filename, "r") as store_file:
            self.data = json.load(store_file)

    def create_or_update(self, username: str, dob: str) -> None:
        """Create or update a user record."""
        self.data[username] = dob
        with open(self.store_filename, "w") as store_file:
            store_file.write(json.dumps(self.data))

    def get_dob(self, username: str) -> typing.Optional[str]:
        """Return the DOB of a user or None."""
        return self.data.get(username, None)
