
FICA_RATE = 0.0765
FEDERAL_RATE = 0.08
OVERTIME_THRESHOLD = 40
OVERTIME_MULTIPLIER = 1.5

def get_gross_pay(hours, rate):
    """Return gross pay."""
    if hours > OVERTIME_THRESHOLD:
        regular_pay = OVERTIME_THRESHOLD * rate
        overtime_pay = (hours - OVERTIME_THRESHOLD) * rate * OVERTIME_MULTIPLIER
        return regular_pay + overtime_pay
    return hours * rate

def get_fica_tax(gross_pay):
    """Return FICA tax (uses global FICA_RATE)."""
    return gross_pay * FICA_RATE

def get_federal_tax(gross_pay):
    """Return federal tax (uses global FEDERAL_RATE)."""
    return gross_pay * FEDERAL_RATE