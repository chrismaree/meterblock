pragma solidity ^0.4.24;

import "./MintableToken.sol";
import "./StandardBurnableToken.sol";


contract KraGToken is MintableToken, StandardBurnableToken {
    string public name = "KraG Token: 1 token = 1kWh";
    string public symbol = "KraG";
    uint8 public decimals = 6;
    uint public INITIAL_SUPPLY = 1000;

    mapping(address=>address) public metersToOwner;

    constructor() public {
        totalSupply_ = INITIAL_SUPPLY;
        balances[msg.sender] = INITIAL_SUPPLY;
    }

    modifier hasMintPermission() {
        require(metersToOwner[msg.sender] != 0);
        _;
    }

    function enroleMeter(address _meter, address _owner)
        onlyOwner
        public
    {
        metersToOwner[_meter] = _owner;
    }


    function mint(uint256 _amount)
        public
        hasMintPermission
        canMint
        returns (bool)
    {
        totalSupply_ = totalSupply_.add(_amount);
        balances[msg.sender] = balances[msg.sender].add(_amount);

        increaseApproval(metersToOwner[msg.sender], _amount);

        emit Mint(msg.sender, _amount);
        emit Transfer(address(0), msg.sender, _amount);
        return true;
    }
}