import pytest
from brownie import network, config
from scripts.deploy_vrf import deploy_vrf

from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_publish_account,
)


def test_deploy_contract():
    if network.show_active() != "rinkeby":
        pytest.skip("only for Rinkeby testing.")
    deployed_contract = deploy_vrf()


def test_random_number():
    if network.show_active() != "rinkeby":
        pytest.skip("only for Rinkeby testing.")

    publish_account = get_publish_account()

    deployed_contract = deploy_vrf()

    deployed_contract.requestRandomWords({"from": publish_account})
