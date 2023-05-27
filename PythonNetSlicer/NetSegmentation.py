from IPAddress import NetworkIpAddress
from SubnettingStrategy import SubnettingStrategy

class NetSegmentation:
    """
    A class that performs network segmentation based on a given subnetting strategy.
    """

    def __init__(self, sns: SubnettingStrategy):
        """
        Initializes the NetSegmentation object with a subnetting strategy.
        Parameters:
        - sns (SubnettingStrategy): The subnetting strategy to be used for segmentation.
        """
        self._sns = sns

    def apply_subnet(self, net_ip: NetworkIpAddress) -> list[str]:
        """
        Applies the subnetting strategy to the given network IP address.
        Parameters:
        - net_ip (NetworkIpAddress): The network IP address.
        Returns:
        - list[str]: A list of subnets generated based on the subnetting strategy.
        """
        return self._sns.subnet(net_ip)
