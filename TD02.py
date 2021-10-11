#CREATION DU SEED

import random
import hashlib
rand = "".join( [str( random.randint (0, 1)) for v in range(128)] )
core = (hashlib.sha256(bytes([int(i) for i in rand]))).hexdigest()
concat = bin(int(core[0], 16))[2:].zfill(4)
seed = rand+str(concat)
print("Seed:\n", seed)
print("\n\n")

#DECOUPAGE DU SEED ET ASSOCIATION DES MOTS

string = seed
with open("wordlistEng.txt", "r") as f:
    lines = f.readlines()
lot = [ (int (string[i:i+11]), lines[int( string[i:i+11], 2)].strip()) for i in range(0, 128, 11)]
print("Association:\n", lot)
mnemonics = " ".join([lot[i][1] for i in range(12)])
print("Mnemonic:\n", mnemonics)
print("\n\n")


#EXTRACTION DU MPK & MCC

from backports.pbkdf2 import pbkdf2_hmac
import binascii 
key = pbkdf2_hmac("sha512", mnemonic.encode("utf8"), "mnemonic".encode("utf8"), 2048, 128)
print("key:\n", str(binascii.hexlify(key))[2:130])
MasterPrivatekey = str(binascii.hexlify(key))[2:66]
print("MasterPrivatekey:\n", MasterPrivatekey, len(MasterPrivatekey))
MasterChainCode = str(binascii.hexlify(key))[66:130]
print("MasterChainCode:\n", MasterChainCode, len(MasterChainCode))
print("\n\n")


#Master Public Key & child key
from mnemonic import Mnemonic
import bip32utils

mnemon = Mnemonic('english')
seed = mnemon.to_seed(mnemonics)
print(f'BIP39 Seed: {seed.hex()}\n')
root_key = bip32utils.BIP32Key.fromEntropy(seed)
root_public_hex = root_key.PublicKey().hex()
#Master Public Key
print(f'\tMaster Public Key: {root_public_hex}') 
#child key
child_key = root_key.ChildKey(0).ChildKey(0)
child_public_hex = child_key.PublicKey().hex()
print(f'\tChild Public : {child_public_hex}')

#Child key index 13
child_key = root_key.ChildKey(13).ChildKey(13)
child_public_hex = child_key.PublicKey().hex()
print(f'\tChild 13 Public : {child_public_hex}')

