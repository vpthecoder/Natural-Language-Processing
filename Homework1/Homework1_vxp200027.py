# import libraries
import pathlib
import sys
import re
import pickle


# Person class; it has 5 attributes: first name, last name, middle initial, id, and phone
class Person():
    # initalize attributes
    def __init__(self, last, first, mi, id2, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id2 = id2
        self.phone = phone

    # check id, if id is not in correct form ask for input and run function again, two letters four digits
    def checkid(self, id):
        if re.search('^[a-z]{2}[0-9]{4}$', id.lower()):
            self.id2 = id
            return True

        else:
            id2 = input("ID invalid: " + id + " is two letters followed by 4 digits\nPlease enter a valid id:");
            self.checkid(id2)

    #check phone, if phone is not in correct form ask for input and run function again
    def checkphone(self, phone):
        if re.search("^\d{3}-\d{3}-\d{4}$", phone):
            self.phone = phone
            return True

        else:
            phone = input("Phone " + phone + " is invalid\nEnter phone number in form 123-456-7890\nEnter phone "
                                             "number: ")
            self.checkphone(phone)

    # format first name with capital letter, format last name with capital letter, format middle initial
    # with capital letter, check id and check phone
    def format(self):
        self.last = self.last.lower()
        self.first = self.first.lower()
        self.last = self.last.capitalize()
        self.first = self.first.capitalize()
        self.mi = self.mi.capitalize()
        if self.mi == "":
            self.mi = "X"
        self.checkid(self.id2)
        self.checkphone(self.phone)

    # display person attributes for each person object
    def display(self):
        print("Employee id: " + self.id2 + "\n" + self.first + "\n" + self.mi + "\n" + self.last + "\n" + self.phone)


# main function
def main(filepath):
    with open(pathlib.Path.cwd().joinpath(filepath), 'r') as f:

        # read file
        text_in = f.read()

    #split each line
    tokens = text_in.splitlines()

    # remove first line from list
    token = (tokens[1:])

    #create dictionary
    person_dict = {}

    # for each line split line by the comma to get individual attributes
    for line in token:
        last, first, mi, id2, phone = line.split(',')

        # store attributes into person object
        person = Person(last, first, mi, id2, phone)

        # format person data
        person.format()

        # if id is not in dict add person to dict with key as id
        if person.id2 not in person_dict:
            person_dict[person.id2] = person

            # else print cannot add
        else:
            print("You cannot have duplicate keys")

    # save the pickle file
    pickle.dump(person_dict, open('dict.p', 'wb'))  # write binary
    # read the pickle file

    dict_in = pickle.load(open('dict.p', 'rb'))  # read binary
    print("Employee list: " + "\n")
    # display all persons in the dictionary
    for i in dict_in:
        dict_in[i].display()

# if there is no filename as parameter ask for parameter
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
        exit()
    else:
        fp = sys.argv[1]

        main(fp)
