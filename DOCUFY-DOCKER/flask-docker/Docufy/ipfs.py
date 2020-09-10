import requests

class IPFS:

    pinata_api_key = "4ce3a7d51ec746ec3580"
    pinata_secret_api_key = "fdeadcdb93970485af97f6ef62ee177ea632a24f4c6bb81a77c218cfc0dba87d"
    
    #testAuthentication
    def __init__(self):

        x = requests.get(url='https://api.pinata.cloud/data/testAuthentication', headers={
            "pinata_api_key": IPFS.pinata_api_key,
            "pinata_secret_api_key": IPFS.pinata_secret_api_key
        })
        print(x.status_code)
        print(x.headers)
        print(x.json())

    #pinList
    @staticmethod
    def getPinList():
        x = requests.get(url="https://api.pinata.cloud/data/pinList?status=pinned", headers={
            "pinata_api_key": IPFS.pinata_api_key,
            "pinata_secret_api_key": IPFS.pinata_secret_api_key
        })
        return x.text

    #userPinnedDataTotal
    @staticmethod
    def getPinnedDataTotal():
        x = requests.get(url="https://api.pinata.cloud/data/userPinnedDataTotal", headers={
            "pinata_api_key": IPFS.pinata_api_key,
            "pinata_secret_api_key": IPFS.pinata_secret_api_key
        })
        return x.text

    #pinJSONtoIPFS
    @staticmethod
    def addBlock(block):
        mydata = {
            "pinataContent": block
        }
        x = requests.post(url="https://api.pinata.cloud/pinning/pinJSONToIPFS", json=mydata, headers={
            "Content-Type": "application/json",
            "pinata_api_key": IPFS.pinata_api_key,
            "pinata_secret_api_key": IPFS.pinata_secret_api_key
        })
        return x.text

    #getDataFromHash
    @staticmethod
    def getBlock(hash):
        ipfs_hash = hash

        x = requests.get("https://gateway.pinata.cloud/ipfs/{}".format(ipfs_hash))
        return x.text

    #removePinFromIPFS
    @staticmethod
    def removeBlock(hash):
        ipfs_pin_hash = hash

        x = requests.post(url="https://api.pinata.cloud/pinning/removePinFromIPFS", data={"ipfs_pin_hash": ipfs_pin_hash}, headers={
            "pinata_api_key": IPFS.pinata_api_key,
            "pinata_secret_api_key": IPFS.pinata_secret_api_key
            })
        return x.text