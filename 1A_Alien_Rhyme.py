from collections import deque


def get_pair_and_remain(recursive_dict, root=False):
    if not recursive_dict:
        return (0, 1)

    pair, remain = (0, 0)
    for k, v in recursive_dict.items():
        v_pair, v_remain = get_pair_and_remain(v)
        pair, remain = pair + v_pair , remain + v_remain

    if not root:
        if remain > 1:
            pair, remain = pair + 1, remain - 2

    return (pair, remain)

def trie_recursion(trie_ds, word):
    try:
        letter = word.popleft()
        out = trie_recursion(trie_ds.get(letter, {}), word)
    except IndexError:
        return {}

    if not trie_ds.get(letter):
        trie_ds[letter] = out

    return trie_ds

def solve():
    trie = {}
    words = list()

    for _ in range(int(input())):
        words.append(reversed('_'+input()))
        
    for word in words:
        trie = trie_recursion(trie, deque(word))

    return get_pair_and_remain(trie, root=True)[0] * 2

for idx in range(int(input())):
    result = solve()
    print('Case #{}: {}'.format(idx+1, result))
