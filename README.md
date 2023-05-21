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
   
