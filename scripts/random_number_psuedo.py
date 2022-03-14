from brownie import PsuedoRandomNumber
from scripts.helpful_scripts import get_publish_account


def vrf_random():
    publish_account = get_publish_account()

    deployed_contract = PsuedoRandomNumber[-1]
    print(deployed_contract)
    random = deployed_contract.requestRandomNumber({"from": publish_account})
    print(random)


def main():
    vrf_random()
