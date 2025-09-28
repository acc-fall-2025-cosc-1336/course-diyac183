import sys
sys.path.append("./")
from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

def test_get_options_ratio_basic():
	assert get_options_ratio(5, 10) == 0.5
	assert get_options_ratio(0, 10) == 0
	assert get_options_ratio(10, 10) == 1
	assert get_options_ratio(3, 0) == 0

def test_get_faculty_rating_table():
	assert get_faculty_rating(0.59) == 'Unacceptable'
	assert get_faculty_rating(0.6) == 'Unacceptable'
	assert get_faculty_rating(0.61) == 'Needs Improvement'
	assert get_faculty_rating(0.7) == 'Needs Improvement'
	assert get_faculty_rating(0.71) == 'Good'
	assert get_faculty_rating(0.8) == 'Good'
	assert get_faculty_rating(0.81) == 'Very Good'
	assert get_faculty_rating(0.89) == 'Very Good'
	assert get_faculty_rating(0.9) == 'Excellent'
	assert get_faculty_rating(0.99) == 'Excellent'
	assert get_faculty_rating(1) == 'Invalid Ratio'
