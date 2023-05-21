
'''
public class networkIPAddress{
		
	public void setNetIp() { 
		// this method will find the network IP address: in a String form and numerical form of 4 octets
		//  Network IP address = Entered IP address & (bitwise AND) subnet mask
		this.netIp="";
		String temp;
		for(int i=0;i<4;i++) {
			this.netIpOctet[i]=this.enteredIp.getIpOctet()[i]&this.enteredIp.getSubnetMask()[i];
			temp=String.valueOf(this.netIpOctet[i]);
			this.netIp+=(i!=3?temp+".":temp);
		}
	}
	
	

	public void setFirstIpAddress() {
		// this method will find the 1st available IP address: 
		//  1st available IP address = netIP+1
		this.firstIpAddress="";
		for(int i=0;i<4;i++) {
			firstIpAddress+=(i!=3?String.valueOf(this.netIpOctet[i])+".":String.valueOf(this.netIpOctet[i]+1));
		}
	}

	public void setLastIpAddress() {
		// this method will find the last IP address:
		// last IP address= [netIP ~ (bitwise negation) of subnet mask] -1
		// integers are represented using two's complement notation in Java. 
		// To convert the bitwise negation of 255 back to its unsigned binary representation, 
		// we added 256 to the result
		this.lastIpAddress="";
		for(int i=0;i<4;i++) {
			lastIpAddress+=(i!=3?String.valueOf(netIpOctet[i]|(~enteredIp.getSubnetMask()[i]+256))+".":String.valueOf(netIpOctet[i]|(~enteredIp.getSubnetMask()[i]+256)-1));
		}
	}

	public void setbroadCastIpAddress() {
		// this method will find the broad cast IP address:
		// broad cast IP address= netIP ~ (bitwise negation) of subnet mask
		// integers are represented using two's complement notation in Java. 
		// To convert the bitwise negation of 255 back to its unsigned binary representation, 
		// we added 256 to the result
		this.broadCastIpAddress="";
		for(int i=0;i<4;i++) {
			broadCastIpAddress+=(i!=3?String.valueOf(netIpOctet[i]|(~enteredIp.getSubnetMask()[i]+256))+".":String.valueOf(netIpOctet[i]|(~enteredIp.getSubnetMask()[i]+256)));
		}
	}

	public void setNumberOfHosts() {
		// the size of host portion of the ip address = 32- prefix
		// # of usable hosts = 2 to the power of (32- prefix) -2
		this.numberOfHosts=(int)Math.pow(2,(32-this.enteredIp.getPrefix()))-2;
	}
	
	public String toString() {
		// returns a string representation of an object (Network IP address) 
		String str="Entered IP address: "+this.getEnteredIp();
		str+="\nNetwork Ip address :"+this.netIp+"/"+this.getPrefix();
		str+="\nSubnet mask: "+this.enteredIp.getSubnetMaskStr();
		str+="\nNumber of Hosts :"+this.numberOfHosts;
		str+="\nBroad Cast Ip Address :"+this.broadCastIpAddress;
		str+="\nFirst Ip Address :"+this.firstIpAddress;
		str+="\nLast Ip Address :"+this.lastIpAddress;
		return str;
	}
	
	public void setNetIpOctet(int netIpOctet, int ind) {
		this.netIpOctet[ind] = netIpOctet;
	}
    
	
}
'''
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
        mask = 0xFFFFFFFF << (32 - self.prefix)

        # Breaking down the mask into 4 octets of the subnet mask and generating the string form of the subnet mask
        step_size = 24
        
        for i in range(4):
            # For each iteration, the mask will be shifted to the right by a step size (adapted) and a
            # bitwise AND operation will be performed with 0xFF (11111111) to find the octets
            self._subnet_mask[i] = (mask >> step_size) & 0xFF
            step_size -= 8
            self._subnet_mask_str += str(self.subnet_mask[i]) + ("." if i != 3 else "")

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

        # Set the entered IP
        self.set_entered_Ip(enteredIp)

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
        pass

    # getter methods
    def get_entered_Ip()-> str:
        return self._enteredIp

    def get_netIp()-> str:
        return self._netIp

    def get_first_IpAddress()-> str:
        return self._firstIpAddress

    def get_last_IpAddress()-> str:
        return self._lastIpAddress

    def get_broadCast_IpAddress()->str:
        return self._broadCastIpAddress

    def get_number_of_hosts()-> int:
        return self._numberOfHosts

    def get_netPrefix()-> int:
        return self._netPrefix

    # setter methods
    def set_entered_Ip(ip: IPAddress):
        self._enteredIp = ip
        
    def set_netIp():
        self._netPrefix = self._enteredIp.get_Prefix()
        tempStr= ""
        for i in range(4):
            self._netIpOctet[i]=self._enteredIp.get_IpOctets()[i] & self._enteredIp.get_subnetMaskOctets()[i]
            self._netIp+=str(this.netIpOctet[i])+"." if i!=3 else str(this.netIpOctet[i])
    

    def set_first_IpAddress():
        pass

    def set_last_IpAddress():
        pass

    def set_broadCast_IpAddress():
        pass

    def set_number_of_hosts():
        pass
     
#---------------------------------------------------------------------------------------
