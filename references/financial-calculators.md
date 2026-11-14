# Financial calculator integrity

## Principles
- Document business assumptions: principal, APR vs APY, accrual, amortization, draw/repayment period, payment timing, compounding, fees, discounts, fixed/variable rate treatment.
- Preserve validated formulas unless owner approves a change.
- Define rounding at each stage; compare against independent reference calculations.
- Reject NaN, Infinity, negative or out-of-range values where invalid; handle scientific notation intentionally.
- Avoid arbitrary business caps. Obtain approved modeling range or document proposed technical limit.
- Protect against floating-point precision loss and unsafe conversions; avoid claiming exact decimal arithmetic without suitable implementation.

## Boundary matrix
- Zero, negative, minimum, maximum, just above maximum, very large, decimal fractions, exponent notation, malformed text.
- Zero and extreme interest rates; draw/repayment periods; mortgage exceeding home value; discounts exceeding base rate; fees and mixed-rate transitions.
- Comparison page, future draws, optional panels, URL defaults, embed configuration, downloads.

## Reporting
Separate security vulnerabilities from mathematical correctness defects. Record input, expected reference result, actual result, tolerance, assumptions and user-visible message.
