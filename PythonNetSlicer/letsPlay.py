def set_broadCast_IpAddress(octets,subnetmask):
    BC=""
    for i in range(4):         
        octet = octets[i]
        mask=subnetmask[i]
        wildCard=255-mask
        BC+=str(octet | wildCard)+"." if i!=3 else str(octet | wildCard)
        #broadcast_octet = (octet | (255 - octet))
        #broadcast_ip.append(str(broadcast_octet))
        #self._broadCastIpAddress=".".join(str(i) for i in broadcast_ip)
    print(BC)


octects=[192,168,128,0]
subnetmask=[255,255,252,0]

set_broadCast_IpAddress(octects,subnetmask)
