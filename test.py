from data.testdata import *
import pytest


@pytest.mark.parametrize("start, end, points", [(0, 100, POINTS_0_P),
                                                (0, 100, POINTS_1_P),
                                                (0, 100, POINTS_2_P),
                                                (0, 100, POINTS_3_P),
                                                (0, 100, POINTS_4_P),
                                                (0, 100, POINTS_5_P)])
def test_discount_card_1(start, end, points):
    assert start <= points < end
    print(' min discount 1%')


@pytest.mark.parametrize("start, end, points", [(100, 200, POINTS_3_P),
                                                (100, 200, POINTS_4_P),
                                                (100, 200, POINTS_5_P),
                                                (100, 200, POINTS_6_P),
                                                (100, 200, POINTS_7_P),
                                                (100, 200, POINTS_8_P)])
def test_discount_card_2(start, end, points):
    assert start <= points < end
    print(' discount 3%')


@pytest.mark.parametrize("start, end, points", [(200, 500, POINTS_6_P),
                                                (200, 500, POINTS_7_P),
                                                (200, 500, POINTS_8_P),
                                                (200, 500, POINTS_9_P),
                                                (200, 500, POINTS_10_P),
                                                (200, 500, POINTS_11_P)])
def test_discount_card_3(start, end, points):
    assert start <= points < end
    print(' discount 5%')


@pytest.mark.parametrize("start, points", [(500, POINTS_9_P),
                                           (500, POINTS_10_P),
                                           (500, POINTS_11_P)])
def test_discount_card_4(start, points):
    assert points >= start
    print(' max discount 10%')
