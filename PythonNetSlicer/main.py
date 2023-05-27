from IPSubnetCalculator import *

'''
The primary aim of this project is to develop an application that can subnet a 
given IPv4 address using three different subnetting methods. Additionally, the 
application validates the input IPv4 address and computes the corresponding network 
IPv4 address. For each network, the application determines the first, last, and 
broadcast IPv4 addresses and also computes the number of available usable IP 
addresses. The goal of this project is to accomplish these tasks without relying on 
any pre-existing network libraries.
Strategic Pattern Design will be utilized in this project.

'''

def screen_holder(word: str):
    # Display a message
    print("Press Enter to " + word + "...", end='')
    # Wait for user input
    input()


if __name__ == "__main__":
    # Initialize variables
    choice = 0
    ip = IPSubnetCalculator.ip_address_input()

    # Main menu loop
    while choice != 6:
        print("\nWhat would you like me to do?")
        print("1- Print Network Details.")
        print("2- Subnet the Given IP Address Based on the Required Number of Hosts per Subnet.")
        print("3- Subnet the Given IP Address Based on the Required Number of Subnets.")
        print("4- Subnet The Given IP Address Using VLSM.")
        print("5- Enter a New IP Address.")
        print("6- Exit.\n")

        try:
            choice = int(input("Enter your choice. [1,2,3,4,5 or 6]: "))# Prompt user for choice
            # ------------------------------------------------------
            if choice == 1: # Option 1: Print Network Details
                IPSubnetCalculator.network_info(ip)
                screen_holder("continue")
            # ------------------------------------------------------
            elif choice == 2: # Option 2: Subnet IP Address by Hosts
                subnets = IPSubnetCalculator.subnet_by_hosts(ip)
                if len(subnets) == 0:
                    print("It's impossible to complete the task with the given information")
                else:
                    print("Subnet IP addresses:")
                    for i in subnets:
                        print(i)

                screen_holder("continue")
            # -------------------------------------------------------
            elif choice == 3: # Option 3: Subnet IP Address by Subnets
                subnets = IPSubnetCalculator.subnet_by_networks(ip)
                if len(subnets) == 0:
                    print("It's impossible to complete the task with the given information")
                else:
                    print("Subnet IP addresses:")
                    for i in subnets:
                        print(i)
                        
                screen_holder("continue")
            # ---------------------------------------------------------
            elif choice == 4: # Option 4: Subnet IP Address Using VLSM
                subnets = IPSubnetCalculator.subnet_by_VLSM(ip)
                if len(subnets) == 0:
                    print("It's impossible to complete the task with the given information")
                else:
                    print(len(subnets),"subnets can be created:")
                    for i in subnets:
                        print(i)
                screen_holder("continue")
            # ---------------------------------------------------------
            elif choice == 5: # Option 5: Enter a New IP Address
                ip = IPSubnetCalculator.ip_address_input()

            elif choice == 6: # Option 6: Exit
                print("Thanks for using netSlicer.")
                screen_holder("exit")

            else:
                print("Invalid option, please make another selection.")
                screen_holder("continue")

        except ValueError:
            print("Invalid option, please enter a valid integer choice.")
            screen_holder("continue")




        
