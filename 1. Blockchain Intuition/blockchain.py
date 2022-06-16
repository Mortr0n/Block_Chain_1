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

# Part 2 - Mining the Blockchain