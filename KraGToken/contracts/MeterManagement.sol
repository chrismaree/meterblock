pragma solidity ^0.4.24;

import "./BasicToken.sol";
import "./StandardToken.sol";
import "./Ownable.sol";

contract MeterManagement is BasicToken, Ownable, StandardToken {
    
    mapping(address=>address) public metersToOwner;
    mapping(address=>address) public ownerToMeter;

    event Burn(address indexed burner, uint256 value);
    event Mint(address indexed to, uint256 amount);

    modifier hasMintPermission() {
        require(metersToOwner[msg.sender] != 0);
        _;
    }
    
    modifier onlyMeterOwner(address _meterAddress){
        require(metersToOwner[_meterAddress] == msg.sender);
        _;
    }
  
  function enroleMeter(address _meterAddress, address _ownerAddress)
        onlyOwner
        public
    {
        metersToOwner[_meterAddress] = _ownerAddress;
        ownerToMeter[_ownerAddress] = _meterAddress;
    }
    
    
    function transferMeterOwnership(address _meterAddress, address _newOwnerAddress)
        onlyMeterOwner(_meterAddress)
        public
    {
        metersToOwner[_meterAddress] = _newOwnerAddress;
        ownerToMeter[_newOwnerAddress] = _meterAddress;
    }
  
  /**
   * @dev Burns a specific amount of tokens.
   * @param _value The amount of token to be burned.
   */
  function burn(uint256 _value) public {
    _burn(msg.sender, _value);
  }

  function _burn(address _who, uint256 _value) internal {
    require(_value <= balances[_who]);
    // no need to require value <= totalSupply, since that would imply the
    // sender's balance is greater than the totalSupply, which *should* be an assertion failure

    balances[_who] = balances[_who].sub(_value);
    totalSupply_ = totalSupply_.sub(_value);
    emit Burn(_who, _value);
    emit Transfer(_who, address(0), _value);
  }

  /**
   * @dev Function to mint tokens 
   * @param _amount The amount of tokens to mint.
   * @return A boolean that indicates if the operation was successful.
   */    
    function mint(uint256 _amount)
        public
        hasMintPermission
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