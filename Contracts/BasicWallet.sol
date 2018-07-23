contract BasicWallet {
    uint256 public walletBallance;
    
    function BasicWallet(uint256 startingBallance){
        walletBallance = startingBallance;
        
    }
    
    function decrementTokens(uint256 value){
        walletBallance = walletBallance - value;
    }
    
}