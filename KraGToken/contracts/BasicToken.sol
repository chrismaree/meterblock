pragma solidity ^0.4.24;


import "./ERC20Basic.sol";
import "./SafeMath.sol";


/**
 * @title Basic token
 * @dev Basic version of StandardToken, with no allowances.
 */
contract BasicToken is ERC20Basic {
    using SafeMath for uint256; // import safemath library to deal with floating point arithmetic

    mapping(address => uint256) internal balances;

    uint256 internal totalSupply_;

  /**
  * @dev Total number of tokens in existence
  */
    function totalSupply() public view returns (uint256) {
        return totalSupply_;
    }

  /**
  * @dev Transfer token for a specified address
  * @param _to The address to transfer to.
  * @param _value The amount to be transferred.
  */

  // Allows for transfer of tokens between wallets
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_value <= balances[msg.sender]); // Require that the transfer value is less/equal to than the curent wallet balance
        require(_to != address(0)); // Require that transfer address is not the 0x address

        balances[msg.sender] = balances[msg.sender].sub(_value); // Subtract transfer amount from sending address
        balances[_to] = balances[_to].add(_value); // Add transfer amount to transferred address
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

  /**
  * @dev Gets the balance of the specified address.
  * @param _owner The address to query the the balance of.
  * @return An uint256 representing the amount owned by the passed address.
  */
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

}
