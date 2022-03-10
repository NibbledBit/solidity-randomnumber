from brownie import network, config
from scripts.helpful_scripts import get_account


# def deploy_contract(contract):
#     # Get Account
#     publish_account = get_account()
#     print(f"Account {publish_account}")

#     # configure dependencies
#     print(f"The active network is {network.show_active()}")

#     print("Deploying BasicNFT")
#     deployed_contract = contract.deploy(
#         {"from": publish_account},
#         publish_source=config["networks"][network.show_active()].get("verify"),
#     )
#     print(f"Deployed: {deployed_contract}")
#     return deployed_contract
