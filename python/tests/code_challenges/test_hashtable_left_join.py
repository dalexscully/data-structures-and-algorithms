import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "NONE"],
        ["wrath", "anger", "delight"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected


def test_both_empty():
    hash1 = {}
    hash2 = {}

    actual = left_join(hash1, hash2)
    expected = []

    assert actual == expected


def test_left_empty():
    hash1 = {}
    hash2 = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }

    actual = left_join(hash1, hash2)
    expected = []

    assert actual == expected


def test_right_empty():
    hash1 = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }

    hash2 = {}

    actual = left_join(hash1, hash2)

    expected = [
        ["diligent", "employed", "NONE"],
        ["fond", "enamored", "NONE"],
        ["guide", "usher", "NONE"],
        ["outfit", "garb", "NONE"],
        ["wrath", "anger", "NONE"],
    ]
