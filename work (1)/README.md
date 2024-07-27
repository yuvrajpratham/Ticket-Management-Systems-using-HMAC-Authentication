# Blockchain Tools

This Python program provides several tools for working with blockchain data, including retrieving transactions associated with a wallet ID, verifying transactions, creating blocks, and mining blocks.

## Prerequisites

Before running the program, make sure you have the following installed:

- Python 3.x
- `requests` library: You can install it using pip:
- `dotenv` library: You can install it using pip:


## Installation

1. Clone the repository:


2. Navigate to the project directory:


3. Install dependencies:


## Usage

### Setting Environment Variables

Create a `.env` file in the root directory of the project and add the following variables:


Replace `https://blockstream.info/api/address/` with the appropriate API URL for the blockchain you're working with.

### Running the Program

You can run the program using the following command:


Make sure to replace `main.py` with the name of your main Python script.

### Functions

- `viewUser(user_wallet: str, testnet=False) -> dict`: Retrieves transactions associated with a wallet ID. By default, it returns the 25 latest transactions. Eg: 
- `verifyTransaction(tx: str) -> bool`: Verifies a transaction using its hash.
- `createBlock(block_hash: str) -> Block`: Parses a block from a block hash string.
- `mineBlock(block_header: str, target: str)`: Mines a block by finding a nonce that results in a hash meeting the target difficulty.
- `miner(block: Block)`: Mines a block using the provided block object.


## Sample Operations

### viewUser Function

```python
# Example user wallet address
user_wallet = "12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX"

# View transactions associated with the user wallet
viewUser(user_wallet)

# Example transaction hash
tx = bytes.fromhex('0100000001813f79011acb80925dfe69b3def355fe914bd1d96a3f5f71bf8303c6a989c7d1000000006b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278afeffffff02a135ef01000000001976a914bc3b654dca7e56b04dca18f2566cdaf02e8d9ada88ac99c39800000000001976a9141c4bc762dd5423e332166702cb75f40df79fea1288ac19430600')

# Verify the transaction
is_valid = verifyTransaction(tx_hash)
print(f"Transaction verification result: {is_valid}")

# Example block hash
f = bytes.fromhex('020000208ec39428b17323fa0ddec8e887b4a7c53b8c0a0a220cfd0000000000000000005b0750fce0a889502d40508d39576821155e9c9e3f5c3157f961db38fd8b25be1e77a759e93c0118a4ffd71d')
from bitcoin_blockchain import createBlock


# Create a block
new_block = createBlock(f)
print(f"New block created: {new_block}")


# Example block object
f = bytes.fromhex('020000208ec39428b17323fa0ddec8e887b4a7c53b8c0a0a220cfd0000000000000000005b0750fce0a889502d40508d39576821155e9c9e3f5c3157f961db38fd8b25be1e77a759e93c0118a4ffd71d')
new_block = createBlock(f)

# Mine a block using the block object
miner(new_block)

```
