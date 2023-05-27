from IPAddress import *
from NetSegmentation import *
from hostBasedStrategy import *
from subnetBasedStrategy import *
from VLSMBasedStrategy import *

def screen_holder(word: str):
    # Display a message and wait for user input
    print("Press Enter to "+word+"...", end='')
    input()

class IPSubnetCalculator():

    @staticmethod
    def subnet_by_hosts(ip: NetworkIpAddress)->list[str]:
        try:
            number_of_hosts=int(input("How Many hosts do You Need per network? "))
            if number_of_hosts <= 0:
                print("Number of Hosts Must Be Greater Than Zero.")
            else:
                # Apply host-based subnetting strategy and return the subnets
                subnets=NetSegmentation(hostBasedStrategy(number_of_hosts)).apply_subnet(ip)
                return subnets
                
        except ValueError:
            print("Invalid Entry, please enter a valid input.")
            screen_holder("continue")

    @staticmethod
    def subnet_by_networks(ip: NetworkIpAddress)->list[str]:
        try:
            number_of_subnets=int(input("How Many subnets do You Need? "))
            if number_of_subnets <= 0:
                print("Number of Subnets Must Be Greater Than Zero.")
            else:
                # Apply subnet-based subnetting strategy and return the subnets
                subnets=NetSegmentation(subnetBasedStrategy(number_of_subnets)).apply_subnet(ip)
                return subnets
                
        except ValueError:
            print("Invalid Entry, please enter a valid input.")
            screen_holder("continue")

    @staticmethod
    def subnet_by_VLSM(ip: NetworkIpAddress)->list[str]:
        try:
            list_hosts = input("Enter the # of hosts of each subnet,(space-separated): ").split()
            # Convert the input values to integers
            list_hosts = [int(num) for num in list_hosts]         
            for host in list_hosts:
                if host <= 0:
                    raise ValueError("")
            # Sort the list in ascending order 
            list_hosts = sorted(list_hosts, reverse=True)
            # Apply VLSM-based subnetting strategy and return the subnets
            subnets=NetSegmentation(VLSMBasedStrategy(list_hosts)).apply_subnet(ip)
            return subnets
            
        except ValueError:
            print("Invalid Entry, please enter a valid input.")
            screen_holder("continue")

    @staticmethod
    def network_info(ip: NetworkIpAddress):
        # Display network details
        print("\nNetwork Details:")
        print(ip)
        print()

    @staticmethod
    def ip_address_input()->NetworkIpAddress:
        valid=False
        while not valid:
            inputIp=input("Enter an IP address: ")
            if IPAddress.validateIp(inputIp):
                valid=True
        return NetworkIpAddress(IPAddress(inputIp))
