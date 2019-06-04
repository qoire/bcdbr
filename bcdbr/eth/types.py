from dataclasses import dataclass
from typing import List

@dataclass
class BlockHeader:
    parenthash: bytes
    uncleshash: bytes
    author: bytes
    stateroot: bytes
    transactionsroot: bytes
    receiptsroot: bytes
    logsbloom: bytes
    difficulty: int
    gaslimit: int
    gasused: int
    timestamp: int
    extradata: bytes

@dataclass
class Transaction:
    accountnonce: int
    gasprice: int
    gaslimit: int
    recipient: bytes
    amount: int
    payload: bytes
    v: bytes
    r: bytes
    s: bytes

@dataclass
class BlockBody:
    transactions: List[Transaction]
    uncles: List[BlockHeader]

@dataclass
class Log:
    address: bytes
    topics: List[bytes]
    data: bytes

@dataclass
class Receipt:
    posttxstate: bytes
    cumulativegas: int
    bloom: bytes
    txhash: bytes
    contractaddress: bytes
    logs: List[Log]
    gasused: int

@dataclass
class Block:
    parenthash: bytes
    uncleshash: bytes
    author: bytes
    stateroot: bytes
    transactionsroot: bytes
    receiptsroot: bytes
    logsbloom: bytes
    difficulty: int
    gaslimit: int
    gasused: int
    timestamp: int
    extradata: bytes
    transactions: List[Transaction]
    uncles: List[BlockHeader]
    receipts: List[Receipt]

def make_block(header: BlockHeader, transactions: List[Transaction],
    uncles: List[BlockHeader], receipts: List[Receipt]):
    return Block(
        header.parenthash,
        header.uncleshash,
        header.author,
        header.stateroot,
        header.transactionsroot,
        header.receiptsroot,
        header.logsbloom,
        header.difficulty,
        header.gaslimit,
        header.gasused,
        header.timestamp,
        header.extradata,
        transactions,
        uncles,
        receipts)
