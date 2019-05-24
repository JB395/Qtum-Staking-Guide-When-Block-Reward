version = "05-12-2019"

import hashlib                          # for SHA-256 hash algorithm
import secrets				# for cryptographically strong random numbers
import random                           # for pseudo-random numbers

'''

Block Reward Simulator SHA256

Copyright (c) 2019 Jackson Belove
Unpublished software, MIT License

A program to simulate the spacing between block rewards.

'''

print("Block Reward Simulator SHA256, version", version)   

blockRewards = 2000           # the number of block rewards to get
walletWeight = 20000          # weight of wallet
networkWeight = 20000000      # the network weight
totalBlocks = 0               # total blocks in the simulation

print("Block rewards =", blockRewards)
print("Wallet weight =", walletWeight)
print("Network weight =", networkWeight)

for i in range(blockRewards):

    blockSpacing = 1                        # spacing to a block reward

    while True:

        temp = str(secrets.randbits(256)).encode('utf-8') # get a really big random number
                
        hash_object = hashlib.sha256(temp)                # get SHA256 hash
        hex_dig = hash_object.hexdigest()
                                     
        # print(hex_dig)  # 0df34ba99348c61d540586b516925d2836103625268c6387e33f3b3a89174f9f

        hashProofOfStake = int(hex_dig, 16) # convert hex string to a really big decimal int             

        # print("hpos =",  hashProofOfStake /1E+74)   # hpos = 904.6357352016154, 442.1381383150125                                                                          
        
        if hashProofOfStake < 2**256 * walletWeight / networkWeight:  # e.g., under the target
            print(blockSpacing)                      # got a block reward!!!
            break        

        blockSpacing += 1                           # better luck next time
        totalBlocks += 1

print("total blocks =", totalBlocks)

  
        



    
