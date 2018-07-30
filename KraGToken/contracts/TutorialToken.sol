pragma solidity ^0.4.24;

import "openzeppelin-solidity/contracts/token/ERC20/MintableToken.sol";
import "openzeppelin-solidity/contracts/token/ERC20/StandardBurnableToken.sol";

contract TutorialToken is MintableToken, StandardBurnableToken {
    string public name = "KraG Token: 1 token = 1kWh";
    string public symbol = "KraG";
    uint8 public decimals = 6;
    uint public INITIAL_SUPPLY = 1000;


    constructor() public {
        totalSupply_ = INITIAL_SUPPLY;
        balances[msg.sender] = INITIAL_SUPPLY;
    }
}