
import ctypes
import Constants, ErrCodes

uFR = ctypes.cdll.LoadLibrary("libuFCoder-aarch64.so")

class uFRCoder(object):
    connection = False
    readerSerial = ""
    
    def open(self):
        if self.connection != True:
            fnResult = uFR.ReaderOpen()
            if fnResult == Constants.DL_OK:
                self.connection = True
                #print('CONNECTED', ErrCodes.UFCODER_ERROR_CODES[fnResult])
            else:
                self.connection = False
                #print('NOT CONNECTED', ErrCodes.UFCODER_ERROR_CODES[fnResult])
        return self.connection

    def close(self):
        uFR.ReaderClose()
        self.connection = False
        
    def read(self):
        fnResult = ctypes.c_ulong()
        readerType = ctypes.c_uint32()
        readerSerial = ctypes.c_uint32()
        cardType = ctypes.c_uint8()
        cardUIDSize = ctypes.c_uint8()
        cardUID = (ctypes.c_ubyte * 9)()
        dlogicCardType = ctypes.c_uint8()
        cardUIDHEX = str()
        result = None
        
        if self.connection:
            
            fnResult = uFR.GetReaderType(ctypes.byref(readerType))           
            if fnResult == Constants.DL_OK:
            
                fnResult = uFR.GetReaderSerialNumber(ctypes.byref(readerSerial))
                if fnResult == Constants.DL_OK:
                    
                    self.readerSerial = hex(readerSerial.value).upper()
                    
                    fnResult = uFR.GetCardIdEx(ctypes.byref(cardType),cardUID,ctypes.byref(cardUIDSize))
                    if fnResult == Constants.DL_OK:
                    
                        fnResult = uFR.GetDlogicCardType(ctypes.byref(dlogicCardType))
                        if fnResult == Constants.DL_OK:
                            for n in range(cardUIDSize.value):
                                cardUIDHEX +=  '%0.2x' % cardUID[n]
                            result = cardUIDHEX.upper()
                            #print("Card:", cardUIDHEX.upper())
                    else:
                        result = ""
                        #print("No Card Present")
                else:
                    self.close()
                    result = None
            else:
                self.close()
                result = None
        else:
            result = None
                
        return result
        
    def signal(self, lightValue, soundValue):
        uiSignal = uFR.ReaderUISignal
        uiSignal.argtypes = (ctypes.c_uint8, ctypes.c_uint8)
        uiSignal.restype = ctypes.c_int
        uiSignal(lightValue,soundValue)


if __name__ == "__main__":
    import time
    ufr = uFRCoder()
    ufr.open()
    print(ufr.read())
    
    # signal test
    # 1# 1 - zöld, 2 - piros, 3 - zöld piros váltakozva, 4 - piros villog, 5 - 
    # 2# 1 - rövid síp, 2 - hosszú síp, 3 - dupla síp, 4 - tripla síp, 5 - tiltás dallam
    ufr.signal(0, 5)
    
    ufr.close()
    
