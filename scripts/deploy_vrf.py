from brownie import network, config, VRFv2Consumer
from scripts.helpful_scripts import get_publish_account


def deploy_vrf():
    publish_account = get_publish_account()
    print(f"Account {publish_account}")

    # configure dependencies
    print(f"The active network is {network.show_active()}")

    TEST = config["networks"][network.show_active()]["vrf_subscription"]
    print(f"Subscription: {TEST}")
    print("Deploying VRFv2Consumer")
    deployed_contract = VRFv2Consumer.deploy(
        TEST,
        {"from": publish_account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Deployed: {deployed_contract}")
    return deployed_contract
    # NOTE after deploying contract, go to https://vrf.chain.link/rinkeby and add address as consumer


def main():
    deploy_vrf()
