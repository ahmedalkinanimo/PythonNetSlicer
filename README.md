# PythonNetSlicer
PythonNetSlicer


    def set_entered_Ip(ip: IPAddress):
        self._enteredIp = ip
        
    def set_netIp():
        self._netPrefix = self._enteredIp.get_Prefix()
        tempStr= ""
        for i in range(4):
            self._netIpOctet[i]=self._enteredIp.get_IpOctets()[i] & self._enteredIp.get_subnetMaskOctets()[i]
            self._netIp+=str(this.netIpOctet[i])+"." if i!=3 else str(this.netIpOctet[i])
   
   def __str__(self)->str:
        return "Net IP: "+self._netIp+"/"+self._netPrefix+"\n1st IP address: "+self._firstIpAddress+"\nlast IP address: "+self._lastIpAddress+"\n Broad Cast IP                   address: "+self._broadCastIpAddress+"\n # usable IP addresses: "+self._numberOfHosts 


    def set_number_of_hosts():
        self._numberOfHosts=int(2^(32-self._netPrefix)-2)
        
       def set_first_IpAddress():
        for i in range(4):
            self._firstIpAddress+=str(this.netIpOctet[i])+"." if i!=3 else str(this.netIpOctet[i]+1)
        
