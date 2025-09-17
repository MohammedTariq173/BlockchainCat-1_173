from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()

@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(sender="System", receiver="You", amount=1)  # reward
    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'Block mined successfully!',
        'block': block
    }
    return jsonify(response), 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

@app.route('/is_valid', methods=['GET'])
def is_valid():
    valid = blockchain.is_chain_valid(blockchain.chain)
    if valid:
        response = {'message': 'Blockchain is valid!'}
    else:
        response = {'message': 'Blockchain is NOT valid!'}
    return jsonify(response), 200

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    json_data = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']
    if not all(key in json_data for key in transaction_keys):
        return 'Missing transaction data', 400
    index = blockchain.add_transaction(json_data['sender'], json_data['receiver'], json_data['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
