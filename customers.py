"""Customers at Hackbright."""

customers = {}


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        customers[self.email] = self

for line in open("customers.txt"):
    line = line.strip().split("|")
    customer = Customer(line[0], line[1], line[2], line[3])


def get_by_email(email):
    if email in customers:
        return customers[email]
    else:
        return False
