import math
from IPAddress import NetworkIpAddress
from SubnettingStrategy import SubnettingStrategy

class VLSMBasedStrategy(SubnettingStrategy):

    def __init__(self, hosts_lists_count):
        self._hosts_lists_count=hosts_lists_count

    def possibleNumOfNetworks(self, net_ip: NetworkIpAddress)->int:
        """
        Calculate the possible number of networks based on the given network IP address.
        Args:
            net_ip (NetworkIpAddress): The network IP address.
        Returns:
            int: The possible number of networks.
        """
        count=0
        sum=0
        for i in self._hosts_lists_count:
            sum+= int(math.pow(2, math.ceil(math.log2(i))))
            if sum <= (net_ip.get_number_of_hosts()+2):
                count+=1
            else:
                break
        return count

    def subnet(self, net_ip: NetworkIpAddress)->list[str]:
        """
        Subnet the given network IP address based on the VLSM strategy.
        Args:
            net_ip (NetworkIpAddress): The network IP address.
        Returns:
            list[str]: List of subnets generated based on the VLSM strategy.
        """
        subnets = []
        number_of_subnets = self.possibleNumOfNetworks(net_ip)    
        if number_of_subnets == 0:
            # If no valid subnets can be generated, return empty subnets
            return subnets
        accumulative_number_of_hosts = 0

        # generates a list of subnets based on the given network IP address and the number of subnets required. 
        for i in range(number_of_subnets):
            subnet = ""
            usable_IP = int(math.pow(2, math.ceil(math.log2(self._hosts_lists_count[i]+2))))
            new_prefix=32-int(math.ceil(math.log2(usable_IP)))
            mask_mod = bytearray([0,0,0,0])
            for j in range(4):
                mask_mod[j] = int((accumulative_number_of_hosts >> j*8) & 0xFF)
            for x in range(4):
                if x != 3:
                    subnet+= str(net_ip.get_netIpOctet()[x]+mask_mod[3-x])+"."
                else:
                    subnet+= str(net_ip.get_netIpOctet()[x]+mask_mod[3-x])+"/"+str(new_prefix)
            subnets.append(subnet)
            accumulative_number_of_hosts+= usable_IP

        return subnets;

