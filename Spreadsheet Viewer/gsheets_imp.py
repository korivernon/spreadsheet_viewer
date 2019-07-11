import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
'''
Task 1:
Here I want to populate populate options to relevantly search a database
based on the options.

Make a way to search the available options using an input from the given option.

Task 2:
If a user chooses to search the database in regards to a certain option, they
can tailor their results based on that.

Task 3:
Front End Using Flask!
'''

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
basedir = os.path.abspath(os.path.dirname(__file__))
data_json = basedir+'/client_secret.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(data_json, scope)
client = gspread.authorize(credentials)
# Specify the file and sheet that you want to use.
sheet = client.open("Triangle Black Businesses (Responses)").sheet1
# Get the records on the sheet that is passed in.
list_of_hashes = sheet.get_all_records()
# Print the Keys in the dictionary to offer them as choices.
# Initialize the count to 0 so that we can output them as choices.
# Better interface for testing in Python IDLE.
options = [key for key in list_of_hashes[0].keys()]

# We don't want to have all of the options available to be chosen.
# You want to limit the amount of information available to the user to see.
# The user does not need to see everything.
lim_opt_set = ["("+str(option+1)+")"+" "+options[option] for option in range(len(options))]

def conv_input(val):
    # Convert String to list of selections
    temp_str = ''
    ret_lst=[]
    for i in range(len(val)):
        if (val[-1]) != '.':
            raise Exception("Please end your comma separated list with a period.")
        if (val[i]).isalpha():
            raise Exception("Numbers only please.")
        if val[i] != ',':
            temp_str+=selection
        elif val[i] == ',': #if it is equal to a comma, append the numbers
            if 1 <= int(temp_str) and int(temp_str) <= (len(options)-1): #if the value the user entered is not in the accepted range raise an exception
                ret_lst.append(int(temp_str))
                temp_str = ''
            else:
                raise IndexError
    return ret_lst


def choose_options(lim_opt_set, sel, val_set):
    #if passed a "sel, lim_opt_set string" == del 1,3,5, select those options but delete the others
    #1,3,5,9 --> [1,3,5,9]
    # delete in logarithmic time ..
    for i in len(val_set):
        if v
limit_option = options[2:6:]


# Print the Outputs
print("The options are: \n==========================")
option_storage = ["("+str(option+1)+")"+" "+limit_option[option] for option in range(len(limit_option))]
# print(option_storage)

# Loop Over Limit Option and print the results.
for option in option_storage:
    # We only want the Business Name, Products, and Service Offered.
    print("   -",option)
print("==========================")
    # Output for the options.

search = input("Database Query (Select Number): ")
result = limit_option[int(search)-1]
# search = 'Products or Services Offered'

print(limit_option[1])
print(search,"Results")
db_elements_num = len(list_of_hashes)

for _ in range(db_elements_num):
    #fix if statements
    if (result in options):
        # Printing the Businesses
        print((_+1),list_of_hashes[_][result])
    if (result in options):
        # Searching the Product or Service Offered.
        print(list_of_hashes[_]['Business Name']+":\n  -",list_of_hashes[_][result])
    if (int(search)-1 == limit_option[1]):
        # Printing the Business Contact Information
        print(list_of_hashes[_]['Business Name']+":\n  -",list_of_hashes[_]['Products or Services Offered'],list_of_hashes[_]['Business Contact (Owner)'],list_of_hashes[_]['Business Number'])
    #if list_of_hashes[result][search]
