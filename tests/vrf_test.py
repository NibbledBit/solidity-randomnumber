import pytest
from brownie import network, config, VRF_RandomNumber

from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_publish_account,
)


def test_deploy_contract():
    if network.show_active() != "rinkeby":
        pytest.skip("only for Rinkeby testing.")
    # Get Account
    publish_account = get_publish_account()
    print(f"Account {publish_account}")

    # configure dependencies
    print(f"The active network is {network.show_active()}")

    print("Deploying BasicNFT")
    deployed_contract = VRF_RandomNumber.deploy(
        config["networks"][network.show_active()]["vrf_subscription"],
        {"from": publish_account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Deployed: {deployed_contract}")
    return deployed_contract
