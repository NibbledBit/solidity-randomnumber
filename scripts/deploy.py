from brownie import network, config, VRFv2Consumer
from scripts.helpful_scripts import get_publish_account


def deploy_contract():
    publish_account = get_publish_account()
    print(f"Account {publish_account}")

    # configure dependencies
    print(f"The active network is {network.show_active()}")

    print("Deploying VRFv2Consumer")
    deployed_contract = VRFv2Consumer.deploy(
        980,
        {"from": publish_account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Deployed: {deployed_contract}")
    return deployed_contract


def main():
    deploy_contract()
