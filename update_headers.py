"""Change the headers used by the csv"""
import csv


standard_headers = [
    "title",
    "id",
    "stage",
    "creation",
    "creator",
    "activity",
    "actor",
    "nosy",
    "type",
    "components",
    "versions",
    "dependencies",
    "assignee",
    "keywords",
    "priority",
    "status",
    "resolution",
    "nosy_count",
    "message_count",
]


def scrub():
    """Perform cleaning of data file"""
    pass


def polish_row(row):
    """Convert the data in each row to desired format"""

    pass


def tidy_header():
    """Make header human readable"""
    pass
