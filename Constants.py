#WIN32_DLL   = 'uFCoder.dll'
#LINUX_SO    = 'libuFCoder1x-x86-64bit.so'

#========== Dlogic Card =============================
DL_OK                       = 0
DL_MIFARE_ULTRALIGHT        = 0x01
DL_MIFARE_ULTRALIGHT_EV1_11 = 0x02
DL_MIFARE_ULTRALIGHT_EV1_21 = 0x03
DL_MIFARE_ULTRALIGHT_C      = 0x04
DL_NTAG_203                 = 0x05
DL_NTAG_210                 = 0x06
DL_NTAG_212                 = 0x07
DL_NTAG_213                 = 0x08
DL_NTAG_215                 = 0x09
DL_NTAG_216                 = 0x0A
DL_MIFARE_MINI              = 0x20
DL_MIFARE_CLASSIC_1K        = 0x21
DL_MIFARE_CLASSIC_4K        = 0x22
DL_MIFARE_PLUS_S_2K         = 0x23
DL_MIFARE_PLUS_S_4K         = 0x24
DL_MIFARE_PLUS_X_2K         = 0x25
DL_MIFARE_PLUS_X_4K         = 0x26
DL_MIFARE_DESFIRE           = 0x27
DL_MIFARE_DESFIRE_EV1_2K    = 0x28
DL_MIFARE_DESFIRE_EV1_4K    = 0x29
DL_MIFARE_DESFIRE_EV1_8K    = 0x2A

#========= Sound and Light ===========================
FUNCT_LIGHT_OK              = 4
FUNCT_SOUND_OK              = 0 #4 Tripple sound
FUNCT_LIGHT_ERROR           = 2
FUNCT_SOUND_ERROR           = 0 #2 Long sound  

#==========Authentication ============================
MIFARE_AUTHENT1A            = 0x60
MIFARE_AUTHENT1B            = 0x61
KEY_INDEX                   = 0
MAX_BLOCK                   = 0x0F #0x0A dec:16

#==========Sectors and max bytes =====================    
MAX_SECTORS_1k             = 0x10 #16
MAX_SECTORS_4k             = 0x28 #40                                   
MAX_BYTES_ULTRALIGHT       = 0x30 #48                       
MAX_BYTES_ULTRALIGHT_C     = 0x90 #144
MAX_BYTES_NTAG_203         = 0x90 #144
MAX_BYTES_CLASSIC_1K       = 0x2f0 #752
MAX_BYTES_CLASSIC_4k       = 0xd70 #3440
MAX_BYTES_TOTAL_NTAG_203   = 0xa8 #168
MAX_BYTES_TOTAL_ULTRAL_C   = 0xa8 #168   Mifare Ultralight C
MAX_BYTES_TOTAL_ULTRALIGHT = 0x40 #64  # 72?

#===============Format Sing============================
FORMAT_SIGN                = 0x00 
TIME_SLEEP                 = 0.6

 
def MaxBytes(cardType):
    if cardType == DL_NTAG_203:
        return MAX_BYTES_NTAG_203
    elif cardType == DL_MIFARE_ULTRALIGHT:
        return MAX_BYTES_ULTRALIGHT
    elif cardType == DL_MIFARE_ULTRALIGHT_C:
        return MAX_BYTES_ULTRALIGHT_C 
    elif cardType == DL_MIFARE_CLASSIC_1K:            
        return  MAX_BYTES_CLASSIC_1K
    elif cardType == DL_MIFARE_CLASSIC_4K:
        return MAX_BYTES_CLASSIC_4k 
    elif cardType == DL_MIFARE_PLUS_S_4K:
        return MAX_BYTES_CLASSIC_4k              
    
def MaxBlock(cardType):
    if cardType == DL_MIFARE_ULTRALIGHT: return MAX_BYTES_TOTAL_ULTRALIGHT/4
    elif cardType == DL_MIFARE_ULTRALIGHT_C:return MAX_BYTES_TOTAL_ULTRAL_C/4             
    elif cardType == DL_NTAG_203:return MAX_BYTES_TOTAL_NTAG_203/4               
    elif cardType == DL_MIFARE_CLASSIC_1K:return MAX_SECTORS_1k * 4
    elif cardType == DL_MIFARE_CLASSIC_4K:return (( MAX_SECTORS_1k * 2) * 4) + (( MAX_SECTORS_1k - 8) * 16)            
    elif cardType == DL_MIFARE_PLUS_S_4K:return (( MAX_SECTORS_1k * 2) * 4) + (( MAX_SECTORS_1k - 8) * 16)              
                                

