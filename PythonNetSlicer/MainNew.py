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

def final_results_print(subnets : list[str]):
    print("Subnet IP address \t 1st IP \t\t  last IP \t\t   Broadcast IP \tusable IPs")
    print("-------------------------------------------------------------------------------------------------------------")
    for i in subnets:
        net = NetworkIpAddress(IPAddress(i))
        print('{:<25}{:<25}{:<25}{:<21}{:<5}'.format(i,net.get_first_IpAddress(),net.get_last_IpAddress(),net.get_broadCast_IpAddress(),net.get_number_of_hosts()))
    print("-------------------------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    print("Welcome to NetSlicer")
    print("This application performs subnetting on a given IPv4 address using three different subnetting methods. It ensures the input IPv4 address is valid and calculates the corresponding network IPv4 address. For each network, the application determines the first, last, and broadcast IPv4 addresses. Additionally, it computes the number of available usable IP addresses.")
    print("NOTE: use a full screen window for a better view of the printed data\n")
    ip = IPSubnetCalculator.ip_address_input()
    choice1 = 0
    choice2 = 0
    flag = True
    while flag:
        print("\nWhat would you like me to do? (current network IP address: "+ip.get_netIp()+"/"+str(ip.get_netPrefix())+")")
        print("1- Print Network Details.")
        print("2- Subnet the Given IP Address Based on the Required Number of Hosts per Subnet.")
        print("3- Subnet the Given IP Address Based on the Required Number of Subnets.")
        print("4- Subnet The Given IP Address Using VLSM.")
        print("5- Exit.")
        try:
            choice1 = int(input("Enter your choice. [1,2,3, 4 or 5]: "))
            # ------------------------------------------------------
            if choice1 == 1: # Option 1: Print Network Details
                IPSubnetCalculator.network_info(ip)
                screen_holder("continue")
                choice2 = int(input("whould you like to: 1-Enter a new IP address. 2- Use the same IP address. 3-Exit: "))
                if choice2 == 1:
                    ip = IPSubnetCalculator.ip_address_input()
                elif choice2 == 2:
                    pass
                elif choice2 == 3:
                    flag = False
                    print("Thanks for using netSlicer.")
                    screen_holder("exit")
                else:
                    print("Invalid option, please make another selection.")
                    screen_holder("continue")
            # ------------------------------------------------------
            elif choice1 == 2: # Option 2: Subnet IP Address by Hosts
                subnets = IPSubnetCalculator.subnet_by_hosts(ip)
                if len(subnets) == 0:
                    print("It's impossible to complete the task with the given information")
                else:
                    print("Subnet IP addresses:")
                    final_results_print(subnets)
                    
                screen_holder("continue")

                choice2 = int(input("whould you like to: 1-Enter a new IP address. 2- Use the same IP address. 3-Exit: "))
                if choice2 == 1:
                    ip = IPSubnetCalculator.ip_address_input()
                elif choice2 == 2:
                    pass
                elif choice2 == 3:
                    flag = False
                    print("Thanks for using netSlicer.")
                    screen_holder("exit")
                else:
                    print("Invalid option, please make another selection.")
                    screen_holder("continue")
            # -------------------------------------------------------
            elif choice1 == 3: # Option 3: Subnet IP Address by Subnets
                subnets = IPSubnetCalculator.subnet_by_networks(ip)
                if len(subnets) == 0:
                    print("It's impossible to complete the task with the given information")
                else:
                    print("Subnet IP addresses:")
                    final_results_print(subnets)
                        
                screen_holder("continue")        
                choice2 = int(input("whould you like to: 1-Enter a new IP address. 2- Use the same IP address. 3-Exit: "))
                if choice2 == 1:
                    ip = IPSubnetCalculator.ip_address_input()
                elif choice2 == 2:
                    pass
                elif choice2 == 3:
                    flag = False
                    print("Thanks for using netSlicer.")
                    screen_holder("exit")
                else:
                    print("Invalid option, please make another selection.")
                    screen_holder("continue")
            # ---------------------------------------------------------
            elif choice1 == 4: # Option 4: Subnet IP Address Using VLSM
                subnets = IPSubnetCalculator.subnet_by_VLSM(ip)
                if len(subnets) == 0:
                    print("It's impossible to complete the task with the given information")
                else:
                    print(len(subnets),"subnets can be created:")
                    final_results_print(subnets)
                        
                screen_holder("continue")
                choice2 = int(input("whould you like to: 1-Enter a new IP address. 2- Use the same IP address. 3-Exit: "))
                if choice2 == 1:
                    ip = IPSubnetCalculator.ip_address_input()
                elif choice2 == 2:
                    pass
                elif choice2 == 3:
                    flag = False
                    print("Thanks for using netSlicer.")
                    screen_holder("exit")
                else:
                    print("Invalid option, please make another selection.")
                    screen_holder("continue")
            # ---------------------------------------------------------

            elif choice1 == 5: # Option 4: Exit
                flag = False
                print("Thanks for using netSlicer.")
                screen_holder("exit")
            else:
                print("Invalid option, please make another selection.")
                screen_holder("continue")

        except ValueError:
            print("Invalid option, please enter a valid integer choice.")
            screen_holder("continue")

            
