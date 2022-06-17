# Module 1 - Creating a Blockchain YO!

# Installed
# Flask==0.12.2:  pip install Flask==0.12.2
# Already have Postman yo!

# import libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Building the Blockchain

class Blockchain:
    # first initialize the class
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1, 
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash }
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        # the -1 gets the last index of the chain 
        # I think positive starting with 0 goes left to right and negative right to left
        return self.chain[-1]
    
   def proof_of_work(self, previous_proof):
       new_proof = 1
       check_proof = False
       while check_proof is False:
           # operation must be non-symmetrical.  can't be new + prev because prev + new will be the same sum
           # if it was symmetrical you would get the same hash every 2 blocks
           # hash_operation = hashlib.sha256(new_proof - previous_proof) this would be too simple but would work
           # this one is still pretty easy.  more challenging is better
           hash_operation = haslib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
           if hash_operation[:4] == '0000':
               check_proof = True
           else:
               new_proof += 1
       return new_proof
   
   def hash(self, block):
       # turning the block key value pairs in to a json string using the json 
       # library dumps then encoding it so that the hash function will recognize it
       encoded_block = json.dumps(block, sort_keys = True).encode()
       # hashing the function using the haslib library then hexdigest turns to a hexadecimal string
       return haslib.sha256(encoded_block).hexdigest()
   
    
        #test
    def is_chain_valid(self, chain):
        block_index = 1
        previous_block = chain[0]
        while block_index < len(chain):
            # getting the current block for testing in the chain
            block = chain[block_index]
            # check that block at current index's previous_hash matches our hash of that block
            if block['previous_hash'] != self.hash(previous_block):
                return False
            # taking proof of the previous block then take the current proof by getting the proof key of 
            # our current block then compute the hash operation between the proof of the previous block 
            # and the proof of our current block then check if the hash function starts with the 4 leading zeros
            # 1 proof of previous block
            previous_proof = previous_block['proof']
            # 2 proof of current block
            proof = block['proof']
            # 3 check that the operation of our 2 proofs starts with 4 leading zeros this has to 
            # be the same operation as the hashing operation used in the proof_of_work
            hash_operation = haslib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            # if the hash_operation's 4 leading zeros are not equal to 4 zeros return false
            if hash_operation[:4] != '0000'
                return False
            # set previous block to current block
            previous_block = block
            # increment block_index
            block_index += 1
        # finally if it does not ever return false then the chain is valid
        return True
            



















         
        
        
        
        
        
        
        
        
# Part 2 - Mining the Blockchain