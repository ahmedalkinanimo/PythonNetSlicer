from abc import ABC, abstractmethod
from IPAddress import NetworkIpAddress

class SubnettingStrategy(ABC):
    # An abstract base class representing a subnetting strategy.
    @abstractmethod
    def subnet(self, net_ip: NetworkIpAddress)->list[str]:
        """
        Abstract method for subnetting.
        Parameters:
        - net_ip (NetworkIpAddress): The network IP address.
        Returns:
        - list[str]: A list of subnets generated based on the strategy.
        """
        pass
