#!/usr/bin/env python3

from anagram import Anagram


def test_anagram():
    listen = Anagram("listen")
    assert listen.match(['enlists', 'google', 'inlets', 'banana']) == ['inlets']
    assert listen.match(['enlist', 'google', 'silent', 'tinsel']) == ['silent', 'tinsel']
    assert listen.match(['enlists', 'google', 'banana']) == []
    assert listen.match(['enlist', 'google', 'silent']) == ['silent']

def test_anagram_with_empty_list():
    listen = Anagram("listen")
    assert listen.match([]) == []

def test_anagram_with_no_matches():
    listen = Anagram("listen")
    assert listen.match(['cat', 'dog', 'bird']) == []

def test_anagram_with_multiple_matches():
    listen = Anagram("listen")
    assert listen.match(['enlist', 'tinsel', 'silent', 'inlets']) == ['enlist', 'tinsel', 'silent', 'inlets']