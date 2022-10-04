from bluepy.btle import Scanner, DefaultDelegate, Peripheral

def check_distance(dev):
    is_in_class = dev.rssi < -70
    if is_in_class:
        print("Le scanner est sorti de la classe")
    else:
        print("Le scanner est dans la classe")


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)



while True:
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(2.0)
    for dev in devices:
        if (dev.addr == "c0:4f:59:d9:7c:db"):
            print ("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        for (adtype, desc, value) in dev.getScanData():
            if desc == "Manufacturer" and value[8:40] == "00112233445566778899ffffffffffff":
                check_distance(dev)
    scanner.clear()
