from web3 import Web3
import yaml
from constants import GETH_IPC_ENDPOINT, TRANSACTIONS_FILE

def get_addresses_from_transactions():
    web3 = Web3(Web3.IPCProvider(GETH_IPC_ENDPOINT))

    f = open(TRANSACTIONS_FILE, "r")
    fo = open(LICIT_YAML_FILE, "a")

    print("Loading transactions...")
    tx_list = yaml.safe_load(f)
    f.close()
    print("Done.")

    unique_addresses = set()

    for idx, tx in enumrate(tx_list):
        if idx % 500 == 0:
            print("Processing TX #" + str(idx))

        try:
            tx_data = web3.eth.getTransaction(tx)
        except Exception as e:
            print("EXCEPTION on tx " + str(idx) + ": " + str(tx)  + " =>" + str(e))
            continue

        if tx_data['from'] is not None and tx_data['from'] not in unique_addresses:
            unique_addresses.add(tx_data['from'])
            fo.write("- \"" + str(tx_data['from']) + "\"\n")

        if tx_data['to'] is not None and tx_data['to'] not in unique_addresses:
            unique_addresses.add(tx_data['to'])
            fo.write("- \"" + str(tx_data['to']) + "\"\n")

        if len(unique_addresses) % 250 == 0:
            print(str(len(unique_addresses))  + " addresses discovered...")

        if len(unique_addresses) >= 10000:
            print("DONE!")
            fo.close()
            exit
