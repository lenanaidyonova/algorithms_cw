from test_avl import TestAVL
from test_hash_table import TestHashTable
from modules.commands import Commands


def main():
    test_avl = TestAVL(10000, Commands.REMOVE)
    test_avl.start()

    test_hash_table = TestHashTable(1000, Commands.INSERT)
    test_hash_table.start()

main()