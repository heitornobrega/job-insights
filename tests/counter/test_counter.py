from src.pre_built.counter import count_ocurrences


def test_counter():
    quantidade_palavras = count_ocurrences('data/jobs.csv', 'python')
    assert quantidade_palavras == 1639
