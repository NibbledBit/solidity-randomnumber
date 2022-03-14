from brownie import VRFv2Consumer
from scripts.helpful_scripts import get_publish_account


def vrf_random():
    publish_account = get_publish_account()

    deployed_contract = VRFv2Consumer[-1]
    print(deployed_contract)
    deployed_contract.requestRandomNumber({"from": publish_account})


def main():
    vrf_random()
