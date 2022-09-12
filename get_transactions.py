from web3 import Web3
from constants import GETH_IPC_ENDPOINT, INITIAL_BLOCK, NUMBER_BLOCKS, TRANSACTIONS_FILE

def get_transactions():
    web3 = Web3(Web3.IPCProvider(GETH_IPC_ENDPOINT))

    f = open(TRANSACTIONS_FILE, "w")

    for i in range(0, NUMBER_BLOCKS):
        print("Block: " + str(i))
        txs = web3.eth.getBlock(INITIAL_BLOCK + i)['transactions']

        for tx in txs:
            f.write("- \"" + tx.hex() + "\"\n")

    f.close()
