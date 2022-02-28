from BF_Api import BF_Api

def main():
    # Call constructor BF_Api which gets the connection to blockfrost api via api key in the bfKeyFile
    bfKeyFile = "bf_api_key.txt" # File should contain a single line of the api key for bf
    blockfrostApi = BF_Api(bfKeyFile)

if __name__ == '__main__':
    main()