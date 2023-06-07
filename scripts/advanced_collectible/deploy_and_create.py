from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
    fund_with_link,
)
from brownie import AdvancedCollectible, network, config

sample_token_uri = (
    "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
)


def deploy_advanced_collectible():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )

    fund_with_link(advanced_collectible.address)
    tx_created = advanced_collectible.createCollectible({"from": account})
    tx_created.wait(1)
    print("a new token has been created 🙌🙌")
    return advanced_collectible, tx_created


def main():
    deploy_advanced_collectible()
