import math
from IPAddress import NetworkIpAddress
from SubnettingStrategy import SubnettingStrategy

class subnetBasedStrategy(SubnettingStrategy):

    def __init__(self, numberOfSubs: int):
        self._num_of_subs=numberOfSubs

    def subnet(self, net_ip: NetworkIpAddress)->list[str]:
        """
        Subnet the given network IP address based on the number of subnets required.
        Args:
            net_ip (NetworkIpAddress): The network IP address.
        Returns:
            list[str]: List of subnets generated based on the number of subnets required.
        """
        subnets = []
        borrowed_bits = int(math.ceil(math.log(self._num_of_subs) / math.log(2)))
        if borrowed_bits >= (32-net_ip.get_netPrefix()-1):
            # If the number of required subnets is greater than or equal to the available subnet portion, return empty subnets
            return subnets
        new_prefix = net_ip.get_netPrefix()+borrowed_bits
        usable_IP = int(math.pow(2,32-new_prefix))

        #  generates a list of subnets based on the given network IP address and the number of subnets required.
        for i in range(self._num_of_subs):
            subnet = ""
            accumulative_number_of_hosts = i*usable_IP
            mask_mod = bytearray([0,0,0,0])
            for j in range(4):
                mask_mod[j] = int((accumulative_number_of_hosts >> j*8) & 0xFF)
            for x in range(4):
                if x != 3:
                    subnet+= str(net_ip.get_netIpOctet()[x]+mask_mod[3-x])+"."
                else:
                    subnet+= str(net_ip.get_netIpOctet()[x]+mask_mod[3-x])+"/"+str(new_prefix)
            subnets.append(subnet)
        return subnets
