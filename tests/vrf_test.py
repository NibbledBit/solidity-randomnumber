import pytest
from brownie import network, config, VRF_RandomNumber
from scripts.deploy import deploy_contract

from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_publish_account,
)


def test_deploy_contract():
    if network.show_active() != "rinkeby":
        pytest.skip("only for Rinkeby testing.")
    deployed_contract = deploy_contract()


def test_random_number():
    if network.show_active() != "rinkeby":
        pytest.skip("only for Rinkeby testing.")

    publish_account = get_publish_account()

    deployed_contract = deploy_contract()

    deployed_contract.requestRandomWords({"from": publish_account})
