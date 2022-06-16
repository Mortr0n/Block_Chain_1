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
   
        #test
# Part 2 - Mining the Blockchain