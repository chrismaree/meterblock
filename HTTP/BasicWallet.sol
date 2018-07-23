contract BasicWallet {
    uint256 public walletBalance = 0;
    
    function BasicWallet(){
    }
    
    function decrementTokens(uint256 value){
        assert(walletBalance>value);
        walletBalance = walletBalance - value;
    }
    
    function setWalletBalance(uint value){
        walletBalance = value;
    }

}