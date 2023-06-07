from brownie import network, AdvancedCollectible
import pytest
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_contract,
    get_account,
)
from scripts.advanced_collectible.deploy_and_create import deploy_advanced_collectible


def test_can_create_advanced_collectible():
    # deploy the contract
    # create an NFT
    # get a random breed back
    account = get_account()

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for lcoal testing")
        # act
    advance_collectible, creation_transaction = deploy_advanced_collectible()
    requestId = creation_transaction.events["requestedCollectible"]["requestId"]
    random_number = 3423
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, advance_collectible.address, {"from": account}
    )

    # assert

    assert advance_collectible.tokenCounter() == 1
    assert advance_collectible.tokenIdToBreed(0) == random_number % 3
