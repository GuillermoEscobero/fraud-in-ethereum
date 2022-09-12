from get_features import get_features
from get_transactions import get_transactions
from get_addresses_from_transactions import get_addresses_from_transactions

# Data is saved in intermediate files
def main():
    get_transactions()
    get_addresses_from_transactions()
    get_features()

if __name__ == "__main__":
    main()
