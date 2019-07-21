from gsheets_imp import choose_options,conv_input,lim_opt_set,list_of_hashes
"""
Choose Options and Testing
"""
def test_options():
    print("Choose Options Test")
    print(lim_opt_set)
    val_set = input("Please select options in a comma separated list: ")
    print(choose_options(lim_opt_set,val_set))
test_options()

# Testing for test_base
from gsheets_imp import options,print_result
def test_base():
    limit_option = options[2:6:]
    # Drop down menu functionality

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
    RESULT = limit_option[int(search)-1]
    # search = 'Products or Services Offered'

    print(limit_option[1])
    print(search,"Results")
    print_result(RESULT,list_of_hashes)
test_base()
