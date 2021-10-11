# TD2_BITCOIN
* Used libraries : 
  - random : for getting a random number, 
  - hashlib (sha256)
  - backports.pbkdf2.pbkdf2_hmac for extending a key "mnemonic words" in a way that we can extract MasterPrivateKey & MasterChainCode.
  - binascii for converting to hex
  - mnemonic to convert from mnemonic words
  - bip32utils to get Master Public Key from Master Private Key & for deriving child  keys.
  
* the .txt file is the file containing mnemonic english words.
