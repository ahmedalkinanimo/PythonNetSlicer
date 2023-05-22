

#----------------------------------------------------------------------
class IPAddress:

    @classmethod
    def validateIp(cls, inputIP: str)->bool:
        """ the validateIp method checks various conditions to ensure that an IP address is valid based on the specified criteria. """
        try:
            inputIP=inputIP.strip()             # Remove any leading/trailing white spaces
            ipPrefix=inputIP.split("/")         # Split the IP address into IP and prefix
            if len(ipPrefix)!=2:                # Check if IP address has exactly one prefix
                 raise ValueError("Invalid IP address format. Please provide the IP address in the correct format.")

            prefix=int(ipPrefix[1])             # Convert prefix to an integer
            if prefix <0 or prefix >32:           # Check if prefix is within valid range
                raise ValueError("Invalid IP address format. Please provide the IP address in the correct format.")
	    
            octets = [int(substring) for substring in str(ipPrefix[0]).split(".")]    # Split the IP address into octets
            if len(octets)!=4:                   # Check if IP address has exactly four octets
                raise ValueError("Invalid IP address format. Please provide the IP address in the correct format.")

            for octet in octets:                # Check if each octet is within valid range
                if octet < 0 or octet > 255:
                    raise ValueError("Invalid IP address format. Please provide the IP address in the correct format.")
            print("valid IP address")
            return True                         # IP address is valid
        
        except Exception as e:
            print("An error occurred:", str(e)) # Print the error message if an exception occurs
            return False                        # IP address is invalid due to an error

    def __str__(self)->str:
        return self._ipAddress+"\n"+self._subnet_mask_str
    
    def __init__(self, inputIp: str):
        # Initialize instance variables
        self._ipAddress = ""
        self._subnet_mask_str = ""
        self._subnet_mask = [0,0,0,0]

        # Set the IP address based on the input
        self.set_Ip(inputIp)
        
        # Set the IP address octets and prefix length
        self.set_IpOctetsAndPrefix()
        
        # Set the subnet mask octets
        self.set_subnetMaskOctets()


    def set_Ip(self, inputIp: str):
        self._ipAddress=inputIp.strip()

  
    def set_IpOctetsAndPrefix(self):
        # Split the IP address and prefix into separate components
        OctPrefixList=self._ipAddress.split("/")
        # Extract the prefix and convert it to an integer
        self._prefix=int(OctPrefixList[1])
        # Split the IP address into octets and convert them to integers
        self._octets = [int(substring) for substring in str(OctPrefixList[0]).split(".")]


    def set_subnetMaskOctets(self):
        # Determining the subnet mask in the form of a string and numerical value for the octets
        
        # Generating a sequence of 32 ones and shifting them to the left by (32 - prefix)
        # Example: if the prefix is 24, the 32 ones will be shifted to the left by 8, resulting in 24 ones assigned to the mask
        mask = 0xFFFFFFFF << (32 - self._prefix)

        # Breaking down the mask into 4 octets of the subnet mask and generating the string form of the subnet mask
        step_size = 24
        
        for i in range(4):
            # For each iteration, the mask will be shifted to the right by a step size (adapted) and a
            # bitwise AND operation will be performed with 0xFF (11111111) to find the octets
            self._subnet_mask[i] = (mask >> step_size) & 0xFF
            step_size -= 8
            self._subnet_mask_str += str(self._subnet_mask[i]) + ("." if i != 3 else "")

    def get_Ip(self)->str:
        return self._ipAddress
  
    def get_Prefix(self)->int:
        return self._prefix

    def get_IpOctets(self)->list[int]:
        return self._octets

    def get_subnetMaskOctets(self)->list[int]:
        return self._subnet_mask

    def get_subnetMaskStr(self)->str:
        return self._subnet_mask_str
    
#------------------------------------------------------------------

class NetworkIpAddress:

    def __init__(self, ip: IPAddress):
        # Initialize instance variables
        self._enteredIp = ""
        self._netIp = ""
        self._netPrefix = 0
        self._netIpOctet = [0, 0, 0, 0]
        self._firstIpAddress = ""
        self._lastIpAddress = ""
        self._broadCastIpAddress = ""
        self._numberOfHosts = 0
        self._netSubnetMask=[0,0,0,0]

        # Set the entered IP
        self.set_entered_Ip(ip)

        # Set the the subnet mask Octets
        self.set_SubnetMask()
        
        # Set the network IP, the network Ip Octets & network prefix
        self.set_netIp()

        # Set the first IP address
        self.set_first_IpAddress()

        # Set the last IP address
        self.set_last_IpAddress()

        # Set the broadcast IP address
        self.set_broadCast_IpAddress()

        # Set the number of hosts
        self.set_number_of_hosts()

        
    def __str__(self)->str: 
        return "Net IP: "+self._netIp+"/"+str(self._netPrefix)+"\n1st IP address: "+self._firstIpAddress+"\nlast IP address: "+self._lastIpAddress+"\nBroad Cast IP address: "+self._broadCastIpAddress+"\n# usable IP addresses: "+str(self._numberOfHosts)

    # getter methods
    def get_entered_Ip(self)-> str:
        return self._netSubnetMask

    def get_SubnetMask(self)-> str:
        return self._enteredIp

    def get_netIp(self)-> str:
        return self._netIp

    def get_first_IpAddress(self)-> str:
        return self._firstIpAddress

    def get_last_IpAddress(self)-> str:
        return self._lastIpAddress

    def get_broadCast_IpAddress(self)->str:
        return self._broadCastIpAddress

    def get_number_of_hosts(self)-> int:
        return self._numberOfHosts

    def get_netPrefix(self)-> int:
        return self._netPrefix

    # setter methods
    def set_entered_Ip(self, ip: IPAddress):
        self._enteredIp = ip
        
    def set_netIp(self):
        self._netPrefix = self._enteredIp.get_Prefix()
        tempStr= ""
        for i in range(4):
            self._netIpOctet[i]=self._enteredIp.get_IpOctets()[i] & self._enteredIp.get_subnetMaskOctets()[i]
            self._netIp+=str(self._netIpOctet[i])+"." if i!=3 else str(self._netIpOctet[i])

    def set_first_IpAddress(self):
        for i in range(4):
            self._firstIpAddress+=str(self._netIpOctet[i])+"." if i!=3 else str(self._netIpOctet[i]+1)

    def set_last_IpAddress(self):
        for i in range(4):
            octet=self._netIpOctet[i]
            wildCard=255-self._netSubnetMask[i]
            self._lastIpAddress +=str(octet|wildCard)+"." if i != 3 else str((octet|wildCard)-1)

    def set_broadCast_IpAddress(self):
        for i in range(4):         
            octet=self._netIpOctet[i]
            wildCard=255-self._netSubnetMask[i]
            self._broadCastIpAddress +=str(octet|wildCard)+"." if i != 3 else str(octet|wildCard)
            
    def set_number_of_hosts(self):
        self._numberOfHosts=int(2**(32-self._netPrefix)-2)

    def set_SubnetMask(self):
        self._netSubnetMask=self._enteredIp.get_subnetMaskOctets()
     
#---------------------------------------------------------------------------------------
