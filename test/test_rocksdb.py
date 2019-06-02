import rocksdb
from pprint import pprint

    # column_families = {}
    # column_families[b"COL_STATE"] = rocksdb.ColumnFamilyOptions()
    # column_families[b"COL_HEADERS"] = rocksdb.ColumnFamilyOptions()
    # column_families[b"COL_BODIES"] = rocksdb.ColumnFamilyOptions()
    # column_families[b"COL_EXTRA"] = rocksdb.ColumnFamilyOptions()
    # column_families[b"COL_TRACE"] = rocksdb.ColumnFamilyOptions()
    # column_families[b"COL_ACCOUNT_BLOOM"] = rocksdb.ColumnFamilyOptions()
    # column_families[b"COL_NODE_INFO"] = rocksdb.ColumnFamilyOptions()

def test_rocksdbinitial():
    column_families = {}
    column_families[b"col0"] = rocksdb.ColumnFamilyOptions()
    column_families[b"col1"] = rocksdb.ColumnFamilyOptions()
    column_families[b"col2"] = rocksdb.ColumnFamilyOptions()
    column_families[b"col3"] = rocksdb.ColumnFamilyOptions()
    column_families[b"col4"] = rocksdb.ColumnFamilyOptions()
    column_families[b"col5"] = rocksdb.ColumnFamilyOptions()
    column_families[b"col6"] = rocksdb.ColumnFamilyOptions()
    column_families[b"col7"] = rocksdb.ColumnFamilyOptions()
    db = rocksdb.DB("/Users/yao/Source/Work/Ethereum/parity-ethereum/target/release/storage/chains/ethereum/db/906a34e69aec8c0d/overlayrecent/db",rocksdb.Options(), column_families = column_families)

    col0 = db.get_column_family(b'col7')
    print(list(db.iterkeys(col0)))