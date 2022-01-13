# Author: Michael Morriss
# Date: 1/17/2020
# Description: A Library simulator demonstrating various features including a list of
# available library items and patrons, and the ability to check out items, request items for hold, and
# searching through the list of items and identifying items and patrons by giving id codes, and
# responsible for keeping track of patron fines and updating fines each day increment.

class LibraryItem:
    """
    Creates a library item object with a item ID and name, also provides various methods regarding
    the item's current status
    """
    def __init__(self, library_item_id, title):
        """Initializes the Library item's data members."""
        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._location = "ON_SHELF"
        self._date_checked_out = None

    def get_location(self):
        """Returns the location of the library item"""
        return self._location

    def get_library_item_id(self):
        """Returns the item ID of the library item"""
        return self._library_item_id

    def get_title(self):
        """Returns the title of the library item"""
        return self._title

    def get_checked_out_by(self):
        """Returns the patron who checked out the library item"""
        return self._checked_out_by

    def get_requested_by(self):
        """Returns the patron who requested the library item"""
        return self._requested_by

    def get_date_checked_out(self):
        """Returns the date the library item was checked out by a patron"""
        return self._date_checked_out

    def set_checked_out_by(self, co_name):
        """Sets the name of the person who checked out the item."""
        self._checked_out_by = co_name

    def set_date_checked_out(self, co_date):
        """Sets the date to the day the library item was checked out."""
        self._date_checked_out = co_date

    def set_location(self, new_location):
        """Sets the new location of the library item location."""
        self._location = new_location

    def set_requested_by(self, req_patron):
        """Sets the patron that is requesting the library item."""
        self._requested_by = req_patron

class Book(LibraryItem):
    """
    Creates a Book object that inherits methods from the LibraryItem class.
    """

    def __init__(self, library_item_id, title, author):
        """Initializes the Book object data members"""
        super().__init__(library_item_id, title)
        self._author = author
        self._check_out_length = 21
        self._artist = None
        self._director = None

    def get_library_item_id(self):
        """Returns the item ID of the book"""
        return self._library_item_id

    def get_title(self):
        """Returns the title of the book"""
        return self._title

    def get_author(self):
        """Returns the author of the book"""
        return self._author

    def get_artist(self):
        """Returns the artist of the album"""
        return self._artist

    def get_director(self):
        """Returns the director of the movie"""
        return self._director

    def get_check_out_length(self):
        """Returns the check out length of the book"""
        return self._check_out_length


class Album(LibraryItem):
    """
    Creates an Album object that inherits methods from the LibraryItem class.
    """

    def __init__(self, library_item_id, title, artist):
        """Initializes the Album object data members"""
        super().__init__(library_item_id, title)
        self._artist = artist
        self._check_out_length = 14
        self._author = None
        self._director = None

    def get_library_item_id(self):
        """Returns the item ID of the album"""
        return self._library_item_id

    def get_title(self):
        """Returns the title of the album"""
        return self._title

    def get_artist(self):
        """Returns the artist of the album"""
        return self._artist

    def get_director(self):
        """Returns the director of the movie"""
        return self._director

    def get_author(self):
        """Returns the author of the book"""
        return self._author

    def get_check_out_length(self):
        """Returns the check out length of the album"""
        return self._check_out_length


class Movie(LibraryItem):
    """
    Creates a Movie object that inherits methods from the LibraryItem class.
    """

    def __init__(self, library_item_id, title, director):
        """Initializes the Album object data members"""
        super().__init__(library_item_id, title)
        self._director = director
        self._check_out_length = 7
        self._author = None
        self._artist = None

    def get_library_item_id(self):
        """Returns the item ID of the movie"""
        return self._library_item_id

    def get_title(self):
        """Returns the title of the movie"""
        return self._title

    def get_director(self):
        """Returns the director of the movie"""
        return self._director

    def get_artist(self):
        """Returns the artist of the album"""
        return self._artist

    def get_author(self):
        """Returns the author of the book"""
        return self._author

    def get_check_out_length(self):
        """Returns the check out length of the movie"""
        return self._check_out_length


class Patron:
    """
    Creates a Patron object.
    """

    def __init__(self, patron_id, name):
        """Initializes the private data members patron id and name of the Patron object"""
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_patron_id(self):
        """Returns the ID of the patron."""
        return self._patron_id

    def get_name(self):
        """Returns the name of the patron."""
        return self._name

    def get_checked_out_items(self):
        """Returns the list of items checked out by the patron."""
        return self._checked_out_items

    def get_fine_amount(self):
        """Returns the fine amount of the patron in dollars."""
        return self._fine_amount

    def add_library_item(self, LibraryItem):
        """Adds an existing library item to the patron's checked out items."""
        self._checked_out_items.append(LibraryItem)

    def remove_library_item(self, LibraryItem):
        """Removes an item checked out by a patron from their checked out items list."""
        item_index = -1

        for item in self._checked_out_items:
            item_index += 1
            if item == LibraryItem:
                del self._checked_out_items[item_index]

    def amend_fine(self, amount):
        """Increases or decreases the patron's fine amount."""
        if amount > 0:
            self._fine_amount = self._fine_amount + amount
        elif amount < 0:
            self._fine_amount = self._fine_amount + amount


class Library:
    """
    Creates a Library object.
    """

    def __init__(self):
        """Initializes the private data members of the Library class"""
        self._holdings = []
        self._members = []
        self._current_date = 0

    def get_holdings(self):
        """Returns the list of library items in the library holdings"""
        return self._holdings

    def get_members(self):
        """Returns the list of members at the library."""
        return self._members

    def get_current_date(self):
        """Returns the amount of days since object created."""

    def add_library_item(self, new_item):
        """Adds a new library item object to the holdings list."""
        self._holdings.append(new_item)

    def add_patron(self, new_patron):
        """Adds a new patron object to the list of Library members."""
        self._members.append(new_patron)

    def get_library_item_from_id(self, add_id):
        """Returns the library item corresponding to the given item id."""
        for item in self._holdings:
            if add_id == item.get_library_item_id():
                return item
        return None

    def get_patron_from_id(self, search_id):
        """Returns the patron object corresponding to the given patron id"""
        for person in self._members:
            if search_id == person.get_patron_id():
                return person
        return None

    def check_out_library_item(self, patron_id, library_item_id):
        """Checks an item out corresponding to library item id and patron id."""
        co_patron = self.get_patron_from_id(patron_id)              # Patron object from patron id
        co_item = self.get_library_item_from_id(library_item_id)    # Library item object from item id
        item_checked = co_item.get_checked_out_by()
        patron_hold = co_item.get_requested_by()

        if co_patron is None:
            return "patron not found"
        elif co_item is None:
            return "item not found"
        elif item_checked is not None:
            return "item already checked out"
        elif patron_hold is not None:
            return "item on hold by other person"
        else:
            co_item.set_checked_out_by(co_patron)               # Updates the Library item's checked_out_by
            co_item.set_date_checked_out(self._current_date)    # Updates the Library item's date_checked_out
            co_item.set_location("CHECKED_OUT")                 # Updates the Library item's location
            if patron_hold is co_patron:
                co_item.set_requested_by(None)                  # Updates requested_by if patron matches requester
            co_patron.add_library_item(co_item)                 # Adds library item to patron's checked out items
            return "check out successful"

    def return_library_item(self, library_item_id):
        """Returns a Patron's checked out library item back to the Library."""
        return_item = self.get_library_item_from_id(library_item_id)
        return_status = return_item.get_location()
        return_patron = return_item.get_checked_out_by()
        return_request = return_item.get_requested_by()

        if return_item is None:
            return "item not found"
        elif return_status != "CHECKED_OUT":
            return "item already in library"
        else:
            return_patron.remove_library_item(return_item)      # Removes the returned item from patron's checked items
            if return_request is None:                          # Updates item location based on hold status
                return_item.set_location("ON_SHELF")
            else:
                return_item.set_location("ON_HOLD_SHELF")
            return_item.set_checked_out_by(None)                # Clears the item's checked_out_by
            return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        """Requests for an available library item to be placed on hold for a valid patron."""
        req_item = self.get_library_item_from_id(library_item_id)
        req_patron = self.get_patron_from_id(patron_id)

        if req_patron is None:
            return "patron not found"
        elif req_item is None:
            return "item not found"
        elif (req_item.get_requested_by() is not None) or (req_item.get_location() == "ON_HOLD_SHELF"):
            return "item already on hold"
        else:
            req_item.set_requested_by(req_patron)               # Updates the requested_by of the library item
            if req_item.get_location() == "ON_SHELF":
                req_item.set_location("ON_HOLD_SHELF")
            return "request successful"

    def pay_fine(self, patron_id, amount_paid):
        """Processes a payment that is applied to a patron's fine amount."""
        person = self.get_patron_from_id(patron_id)
        if person is None:
            return "patron not found"
        elif amount_paid > 0:
            person.amend_fine((amount_paid * -1))
        return "payment successful"

    def increment_current_date(self):
        """Increments the current date and increases fine amounts for overdue items."""
        self._current_date += 1
        member_list = self._members
        date = self._current_date

        for person in member_list:
            for co_item in person.get_checked_out_items():
                check_out = co_item.get_date_checked_out()
                days_checked = date - check_out
                if (co_item.get_author() is not None) and (days_checked > 21):      # Amends book based on late days.
                    total_fine = 0.1
                    person.amend_fine(total_fine)
                elif (co_item.get_artist() is not None) and (days_checked > 14):    # Amends album based on late days.
                    total_fine = 0.1
                    person.amend_fine(total_fine)
                elif (co_item.get_director() is not None) and (days_checked > 7):   # Amends movie based on late days.
                    total_fine = 0.1
                    person.amend_fine(total_fine)

