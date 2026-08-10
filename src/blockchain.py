import json
from web3 import Web3
from eth_account import Account
import hashlib
import numpy as np

class OnChainAnchor:
    def __init__(self, rpc_url, private_key, contract_address):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.account = Account.from_key(private_key)
        self.contract_address = contract_address
        
        # Load ABI (Compiled from Hardhat)
        with open("artifacts/contracts/VoiceRegistry.sol/VoiceRegistry.json") as f:
            self.abi = json.load(f)["abi"]
            
        self.contract = self.w3.eth.contract(address=contract_address, abi=self.abi)

    def hash_embedding(self, embedding: np.ndarray) -> bytes:
        """Converts the float array to a deterministic bytes32 hash."""
        vector_bytes = embedding.tobytes()
        return hashlib.sha3_256(vector_bytes).digest()

    def anchor_voice(self, embedding: np.ndarray, user_wallet: str):
        voice_hash = self.hash_embedding(embedding)
        
        tx = self.contract.functions.registerVoice(voice_hash, user_wallet).build_transaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gas': 2000000,
            'gasPrice': self.w3.eth.gas_price
        })
        
        signed_tx = self.account.sign_transaction(tx)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return self.w3.eth.wait_for_transaction_receipt(tx_hash)
