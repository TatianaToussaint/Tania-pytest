from common.testdata import *

def test_sample_string(sample_string):
    assert isinstance(sample_string, str)
    assert "sample" in sample_string


def test_sample_list(sample_list):
    assert isinstance(sample_list, list)
    assert len(sample_list)== 5

