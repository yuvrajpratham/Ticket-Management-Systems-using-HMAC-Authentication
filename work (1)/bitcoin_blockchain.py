import requests  # HTTP requests module
from dotenv import load_dotenv  # Reading key-value pairs in .env file
import os
# For filesystem operations
from pprint import pprint  # Pretty-printing
import json  # Loading and parsing JSON data
from tx import Tx  # Parsing transactions
from block import Block
import sys
load_dotenv()  # Loading env values
from io import BytesIO
from hashlib import sha256
import time

def get_url() -> str:
    """
    Retrieves the network address from environment variables.
    """
    return f"{os.getenv('NETWORK_ADDRESS')}"

def viewUser(user_wallet: str, testnet=False) -> dict:
    """
    Retrieves transactions associated with the given user wallet.
    Returns the 25 latest transactions.
    """
    try:
        new_url = f"{get_url()}{user_wallet}/txs"
        response = requests.get(new_url)
        pprint(response.json())
    except Exception as e:
        print(f"An error: {e} occurred in viewUser()", file=sys.stderr)

def verifyTransaction(tx: str) -> bool:
    """
    Takes a transaction hash and verifies the transaction.
    Returns True if the transaction is valid, else False.
    """
    try:
        s = BytesIO(tx)
        transaction = Tx.parse(s)
        return transaction.verify()
    except Exception as e:
        print(f"An error {e} occurred in verifyTransaction()", file=sys.stderr)

def createBlock(block_hash: str) -> Block:
    """
    Parses a block from the given block hash.
    """
    try:
        block_hash_stream = BytesIO(block_hash)
        block = Block.parse(block_hash_stream)
        return block
    except Exception as e:
        print(f"An error {e} occurred in createBlock()", file=sys.stderr)

def calculate_new_hash(block_header: str, nonce: int) -> str:
    """
    Calculates a new hash based on the block header and nonce.
    """
    try:
        data = block_header + hex(nonce)
        return sha256(data.encode()).hexdigest()
    except Exception as e:
        print(f"An error {e} occurred in calculate_new_hash()", file=sys.stderr)
        return None

def get_block_target(block: Block) -> int:
    """
    Gets the target for mining a block.
    """
    try:
        return block.target()
    except Exception as e:
        print(f"An error {e} occurred in get_block_target()", file=sys.stderr)
        return None

def mineBlock(block_header: str, target: str):
    """
    Mines a block by finding a nonce that results in a hash meeting the target difficulty.
    """
    try:
        nonce = 0
        while True:
            block_hash_result = calculate_new_hash(block_header, nonce)
            print(f"Calculating PoW block {block_header} Nonce: {nonce} hash: {block_hash_result}\t\n")
            time.sleep(5)
            if block_hash_result[:len(target)] == target:
                return nonce, block_hash_result
            else:
                nonce += 1
    except Exception as e:
        print(f"An error {e} occurred in mineBlock()", file=sys.stderr)
        return None

def miner(block: Block):
    """
    Mines a block using the provided block object.
    """
    try:
        target = get_block_target(block)
        mineBlock(block.serialize().hex(), str(target))
    except Exception as e:
        print(f"An error {e} occurred in miner()")
