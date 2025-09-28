def get_options_ratio(option, total):

	if total == 0:
		return 0
	return option / total

def get_faculty_rating(ratio):

	if 0 <= ratio < 0.6:
		return 'Unacceptable'
	if 0.6 < ratio <= 0.7:
		return 'Needs Improvement'
	if 0.7 < ratio <= 0.8:
		return 'Good'
	if 0.8 < ratio < 0.9:
		return 'Very Good'
	if 0.9 <= ratio < 1:
		return 'Excellent'

