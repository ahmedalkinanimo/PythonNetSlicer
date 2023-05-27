import math
from IPAddress import NetworkIpAddress
from SubnettingStrategy import SubnettingStrategy

class hostBasedStrategy(SubnettingStrategy):

    def __init__(self, numberOfHosts: int):
        self._num_of_hosts=numberOfHosts

    def subnet(self, net_ip: NetworkIpAddress)->list[str]:
        """
        Subnet the given network IP address based on the number of hosts required.
        Args:
            net_ip (NetworkIpAddress): The network IP address.
        Returns:
            list[str]: List of subnets generated based on the number of hosts required.
        """
        subnets = []
        host_portion=32-net_ip.get_netPrefix()
        kept_bits = int(math.ceil(math.log(self._num_of_hosts + 2) / math.log(2)))
        if kept_bits >= host_portion:
            # If the number of required hosts is greater than or equal to the available host portion, return empty subnets
            return subnets

        # finding the number of subents
        borrowed_bits = host_portion-kept_bits
        new_prefix = net_ip.get_netPrefix()+borrowed_bits
        usable_IP = int(math.pow(2,32-new_prefix))
        num_of_subNets = int(math.pow(2, borrowed_bits))

        #  generates a list of subnets based on the given network IP address and the number of subnets required.
        for i in range(num_of_subNets):
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
        return subnets;
