from scripts.helpful_scripts import get_account, fund_with_link
from brownie import network, AdvancedCollectible, config


def create_collectible():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address)
    tx_created = advanced_collectible.createCollectible({"from": account})
    tx_created.wait(1)
    print("a new token has been created 🙌🙌")
    return advanced_collectible, tx_created


def main():
    create_collectible()
