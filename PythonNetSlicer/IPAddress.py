
'''
public class IPAddress {
	
	
	public void setSubnetMask() {
		// determining the subnet mask in a form of string and numerical value for the octets		
		this.subnetMaskStr="";
		// generating a sequence of 32 ones and shifting them to the left by (32-prefix)
		// example: if prefix is 24, the 32 of the ones will be shifted to the left by 8 and we will end up with 24 ones
		// whic will be assigned to mask
		int mask = 0xFFFFFFFF << (32 - prefix);
		// the following procedure is to break down the mask into 4 octets of the subnet mask and to generat the string form of the subnet mask
		int stepSize=24;
		for(int i=0;i<4;i++) {
			// for each iteration, the mask will be shifted to the right by a step size (adapted) and a
			// bitwise AND operation will be performed with 0xFF (11111111) to find the octets 
			this.subnetMask[i]=mask>>>stepSize & 0xFF;
			stepSize-=8;
			this.subnetMaskStr+=(i!=3?Integer.toString(subnetMask[i])+".":Integer.toString(subnetMask[i]));
		}
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
        return self.ipAddress+"\n"+self.subnet_mask_str
    
    def __init__(self, inputIp: str):
        self.ipAddress = ""
        self.subnet_mask_str = ""
        self.subnet_mask = [0,0,0,0]
        self.set_Ip(inputIp)
        self.set_IpOctetsAndPrefix()
        self.set_subnetMaskOctets()

    def set_Ip(self, inputIp: str):
        self.ipAddress=inputIp.strip()
  
    def set_IpOctetsAndPrefix(self):
        OctPrefixList=self.ipAddress.split("/")
        self.prefix=int(OctPrefixList[1])
        self.octets = [int(substring) for substring in str(OctPrefixList[0]).split(".")]

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
            self.subnet_mask[i] = (mask >> step_size) & 0xFF
            step_size -= 8
            self.subnet_mask_str += str(self.subnet_mask[i]) + ("." if i != 3 else "")

    def get_Ip(self)->str:
        return self.ipAddress
  
    def get_Prefix(self)->int:
        return self.prefix

    def get_IpOctets(self)->list[int]:
        return self.octets

    def get_subnetMaskOctets(self)->list[int]:
        return self.subnet_mask

    def get_subnetMaskStr(self)->str:
        return self.subnet_mask_str
    
#------------------------------------------------------------------

class NetworkIpAddress:
    pass
