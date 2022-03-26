from json.tool import main
import cap
def test_one_word():
    text = 'duck'
    result = cap.just_do_it(text)
    assert result == 'Duck'
def test_multiple_words():
    text = 'a veritable flock of ducks'
    result = cap.just_do_it(text)
    assert result == 'A Veritable Flock Of Ducks'
if __name__ == '__main__':
    main