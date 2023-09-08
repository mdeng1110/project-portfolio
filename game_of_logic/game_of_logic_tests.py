from game_of_logic import *

def test_valid_url():
    test_id = 100
    assert(url_validate(test_id)) == True


def test_invalid_url():
    test_id = 100000
    assert(url_validate(test_id)) == False


def test_preprocess_ebook():
    ebook = '***-|="\';.&?!_,\\:@~`%$#*()+[]{}<>***'
    assert(preprocess_ebook(ebook)) == []


def test_get_interesting_words():
    test_words = ['list', 'words', 'sequence']
    assert(get_interesting_words(test_words)) == ['sequence']


def test_word_map():
    word_list = ['word', 'word', 'list']
    assert(generate_word_map(word_list)) == {
        'word': 2, 
        'list': 1
    }


def test_amount_of_results():
    word_map = {'produced': 1, 'gregory': 1, 'counters': 9, 'darting': 1, 'heaven': 1, 'similar': 2}
    assert(amount_of_results(word_map, len(word_map) - 1)) == [('counters', 9), ('similar', 2), ('produced', 1), ('gregory', 1), ('darting', 1)]