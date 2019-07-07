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
sheet = client.open("Triangle Black Businesses (Responses)").sheet1

list_of_hashes = sheet.get_all_records()
# These are the available options to search for.
options = [key for key in list_of_hashes[0].keys()]
# print(options)
print("The options are: ")
for option in options[2:6:]:
    # We only want the Business Name, Products, and Service Offered.
    print("   -"+option)
    # Output for the options.

# search = input("Database Query: ")
search = 'Products or Services Offered'

print(search,"Results")
db_elements_num = len(list_of_hashes)
for _ in range(db_elements_num):
    if (search == 'Business Name'):
        print((_+1),list_of_hashes[_][search])
    if (search == 'Products or Services Offered'):
        print(list_of_hashes[_]['Business Name']+":\n  -",list_of_hashes[_]['Products or Services Offered'])
    if (search == 'Business Contact (Owner)'):
        print(list_of_hashes[_]['Business Name']+":\n  -",list_of_hashes[_]['Products or Services Offered'],list_of_hashes[_]['Business Contact (Owner)'],list_of_hashes[_]['Business Number'])
    #if list_of_hashes[result][search]
print(list_of_hashes[0]['Products or Services Offered'])
