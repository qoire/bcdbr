import plyvel
from pprint import pprint

from bcdbr.eth import gethdb, decoding

GETH_DB_PATH = "/home/yao/Ethereum/geth-linux-amd64-1.8.27-4bcc0a37/geth-storage/geth/chaindata"
db = gethdb.create_db(GETH_DB_PATH)

def test_empty_block_body_decoding():
    block_body_bytes = gethdb.get_block_body(db, 1)

    assert block_body_bytes != None
    body = decoding.block_body(block_body_bytes)

    assert body.transactions == []
    assert body.uncles == []

def test_full_block_body_decoding():
    # https://etherscan.io/block/5000006 depicts block rewards & uncles
    block_body_bytes = gethdb.get_block_body(db, 5000006)

    assert block_body_bytes != None

    body = decoding.block_body(block_body_bytes)
    assert body.transactions != []
    # withold testing uncles until after implementation

def test_block_receipts_decoding():
    receipts_bytes = gethdb.get_receipts(db, 5000006)
    assert receipts_bytes != None
    receipts = decoding.receipts(receipts_bytes)
    assert len(receipts) == 202

def test_retrieve_full_block():
    block = gethdb.get_fullblock_from_num(db, 5000006)
    assert block.parenthash.hex() == "5c04a0fc96cd81f28cfcdb6e25a20266e78067f4712aa2fbb85f21435f7b068a"
    assert block.uncleshash.hex() == "99004d7c7986d2d0fbf1b678f96d7d4504d28f4b662b27a924f965683359a28c"
