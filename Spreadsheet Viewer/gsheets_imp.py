import gspread
import copy
from oauth2client.service_account import ServiceAccountCredentials
import os
from test_sheets import search
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
lim_opt_set = ["("+str(option)+")"+" "+options[option] for option in range(len(options))]
lim_opt_set = copy.deepcopy(lim_opt_set[1::])
lim_opt_set_ref = copy.deepcopy(lim_opt_set[1::])
lim_opt_set_len = len(lim_opt_set)

def conv_input(val):
    # Convert string to list of selections using a comma separated list
    # corresponding to the numbers.
    val = str(val)
    val+=','
    temp_str,ret_lst = '',[]
    for i in range(len(val)):
        if (val[i]).isalpha():
            raise Exception("Numbers only please.")
        if val[i] != ',':
            temp_str+=val[i]
        elif val[i] == ',': #if it is equal to a comma, append the numbers
            if 1 <= int(temp_str) and int(temp_str) <= (len(options)-1): #if the value the user entered is not in the accepted range raise an exception
                ret_lst.append(int(temp_str))
                temp_str = ''
            else:
                raise IndexError
    return ret_lst

def choose_options(lim_opt_set,val_set):
    # Select only the options that were indicated in the comma separated
    # list.
    placement,val_set = 0, conv_input(val_set)
    val_set_len = len(val_set)
    for i in range(len(val_set)):
        sel_index = (int(val_set[i])-1)
        if sel_index == i:
            placement+=1
        else: # If sel index != to the value
            lim_opt_set[placement],lim_opt_set[sel_index] = lim_opt_set[sel_index],lim_opt_set[placement]
    for i in range((len(lim_opt_set))-val_set_len):
        lim_opt_set.pop()
    return lim_opt_set

db_elements_num = len(list_of_hashes)

def listify(column):
    word_lst = [word.lower().strip(',').strip('.') for word in word_lst]
    storage = {}
    for word in word_lst:
        if word not in storage:
            storage[word] = 1
        else:
            storage[word] += 1
    return storage
# Search relevancy searches for the results with similar wording to the
# search parameter snd gives it a score.
def search_relevancy(resultants,search_column,parameter):
    # resultant is the output list, search_column is a dictionary object
    # loaded with occurances, parameter is what wer are searching for.

    for _ in range(db_elements_num):
        if search_column[parameter] <= 1:
            score = search_column[parameter]
            # Loop over resultants list to get all of the desired outputs
            for resultant in resultants:
                ret_res = string(resultant)+string(list_of_hashes[_][resultant])
            ret_infromation = (score,ret_res)
            nodes += [ret_information]
        else:
            pass
    return nodes

def rank_search():
    # Use sorting algorithm to rank the search as efficiently as possible
    pass

def print_result(RESULT,list_of_hashes):
    for _ in range(db_elements_num):
        #fix if statements
        if (RESULT in options):
            # Printing the Businesses
            print((_+1),list_of_hashes[_][RESULT])
        if (RESULT in options):
            # Searching the Product or Service Offered.
            print(list_of_hashes[_]['Business Name']+":\n  -",list_of_hashes[_][RESULT])
        if (int(search)-1 == limit_option[1]):
            # Printing the Business Contact Information
            print(list_of_hashes[_]['Business Name']+":\n  -",list_of_hashes[_]['Products or Services Offered'],list_of_hashes[_]['Business Contact (Owner)'],list_of_hashes[_]['Business Number'])
        #if list_of_hashes[RESULT][search]
