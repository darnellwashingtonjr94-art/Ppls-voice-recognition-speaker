// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract VoiceRegistry {
    address public admin;
    
    // Maps a keccak256 hash of the voice embedding to an on-chain identity
    mapping(bytes32 => address) public voiceAnchors;
    
    event VoiceRegistered(bytes32 indexed voiceHash, address indexed owner);

    constructor() {
        admin = msg.sender;
    }

    function registerVoice(bytes32 _voiceHash, address _wallet) external {
        require(msg.sender == admin, "Only system backend can anchor voices");
        require(voiceAnchors[_voiceHash] == address(0), "Voiceprint already registered");
        
        voiceAnchors[_voiceHash] = _wallet;
        emit VoiceRegistered(_voiceHash, _wallet);
    }
    
    function verifyVoice(bytes32 _voiceHash) external view returns (address) {
        return voiceAnchors[_voiceHash];
    }
}
