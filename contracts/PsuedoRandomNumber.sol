// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

contract PsuedoRandomNumber {
    uint256 controlSeed = 0;

    function requestRandomNumber() public returns (uint256) {
        controlSeed++;
        return
            uint256(
                keccak256(
                    abi.encodePacked(
                        block.difficulty,
                        block.timestamp,
                        controlSeed
                    )
                )
            );
    }
}
