"""Exact finite consistency checks; Python 3.10+, standard library only.

These computations support inspection of the accompanying proof. They do not
prove its infinite statement, establish novelty, or solve general plethysm.
All partitions, tableaux, and polynomial coefficients are generated locally.
"""

from collections import Counter
import hashlib
from math import comb, lcm


def partitions(n, maximum=None):
    """All partitions in decreasing lexicographic order; rows decrease weakly."""
    if n == 0:
        yield ()
        return
    for first in range(min(n, n if maximum is None else maximum), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def hooks(mu):
    """English Ferrers diagram, zero-based cells; include the cell itself."""
    return [row - j + sum(other > j for other in mu[i + 1 :])
            for i, row in enumerate(mu) for j in range(row)]


def hook_divisibility():
    failures = []
    partition_count = divisor_count = 0
    for w in range(3, 16):
        for mu in partitions(w):
            partition_count += 1
            lengths = hooks(mu)
            for d in range(2, max(lengths) + 2):
                divisor_count += 1
                if sum(h % d != 0 for h in lengths) < 2:
                    failures.append({"mu": mu, "d": d, "hooks": lengths})
    return {
        "w_range_inclusive": [3, 15],
        "d_range": "2..max(hooks)+1 inclusive, for each partition",
        "partitions_checked": partition_count,
        "partition_divisor_pairs_checked": divisor_count,
        "failures": failures,
        "passed": not failures,
    }


def half_difference():
    """Evaluate the cancellation identity using exact, unbounded integers."""
    failures = []
    count = 0
    for w in range(3, 101):
        value = sum((-1) ** s * comb(w, s) * (w - 2 * s) ** (w - 2)
                    for s in range((w - 1) // 2 + 1))
        count += 1
        if value:
            failures.append({"w": w, "sum": value})
    return {
        "w_range_inclusive": [3, 100],
        "identities_checked": count,
        "formula": "sum_{0<=s<w/2} (-1)^s binom(w,s) (w-2s)^(w-2) = 0",
        "arithmetic": "exact integers",
        "failures": failures,
        "passed": not failures,
    }


def direct_tableau_weights(mu, h):
    """Enumerate SSYT: entries 0..h, weak rows and strict columns.

    A tableau has SL2 weight sum(2*T(c)-h). This direct enumeration uses no
    hook-content formula. Empty sets of tableaux produce the zero character.
    """
    cells = [(i, j) for i, row in enumerate(mu) for j in range(row)]
    tableau = {}
    counts = Counter()

    def visit(index, exponent):
        if index == len(cells):
            counts[exponent] += 1
            return
        i, j = cells[index]
        lower = max(tableau.get((i, j - 1), 0),
                    tableau.get((i - 1, j), -1) + 1)
        for value in range(lower, h + 1):
            tableau[i, j] = value
            visit(index + 1, exponent + 2 * value - h)
        tableau.pop((i, j), None)

    visit(0, 0)
    return counts


def ssyt_coefficients():
    """Compare adjacent SSYT weight differences with the subset formula.

    The formula is obtained by expanding the hook-content numerator, then
    taking positive coefficients of (q-q^-1) times the Schur character.
    The denominator coefficient DP and the direct tableaux are independent
    algorithms for these finite specializations.
    """
    failures = []
    partition_count = specializations = comparisons = tableau_instances = 0
    for w in range(3, 8):
        for mu in partitions(w):
            partition_count += 1
            cells = [(i, j) for i, row in enumerate(mu) for j in range(row)]
            b = sum(i * row for i, row in enumerate(mu))
            terms = []
            for mask in range(1 << w):
                size = mask.bit_count()
                shift = 2 * b + 2 * sum(
                    1 + j - i for index, (i, j) in enumerate(cells)
                    if (mask >> index) & 1)
                terms.append(((-1) ** size, w - 2 * size, shift))
            largest_index = max(k + slope * h - shift
                                for h in range(6)
                                for k in range(1, w * h + 2)
                                for sign, slope, shift in terms) + 1
            coefficients = [0] * (largest_index + 1)
            coefficients[0] = 1
            for hook in hooks(mu):
                for n in range(2 * hook, largest_index + 1):
                    coefficients[n] += coefficients[n - 2 * hook]

            def g(n):
                positive = coefficients[n - 1] if 0 <= n - 1 <= largest_index else 0
                negative = coefficients[n + 1] if 0 <= n + 1 <= largest_index else 0
                return positive - negative

            for h in range(6):
                counts = direct_tableau_weights(mu, h)
                tableau_instances += sum(counts.values())
                specializations += 1
                for k in range(1, w * h + 2):
                    direct = counts[k - 1] - counts[k + 1]
                    formula = sum(sign * g(k + slope * h - shift)
                                  for sign, slope, shift in terms)
                    comparisons += 1
                    if direct != formula:
                        failures.append({"mu": mu, "h": h, "k": k,
                                         "direct_ssyt": direct,
                                         "subset_formula": formula})
    return {
        "w_range_inclusive": [3, 7],
        "h_range_inclusive": [0, 5],
        "k_range": "1..w*h+1 inclusive, for each specialization",
        "partitions_checked": partition_count,
        "tableau_instances": tableau_instances,
        "specializations": specializations,
        "coefficient_comparisons": comparisons,
        "arithmetic": "exact integers",
        "failures": failures,
        "passed": not failures,
    }


def multiply_binomial(coefficients, exponent, coefficient=1, modulus=None):
    """Multiply a dense ascending polynomial by 1-coefficient*z^exponent."""
    result = coefficients + [0] * exponent
    for degree, value in enumerate(coefficients):
        result[degree + exponent] -= coefficient * value
        if modulus is not None:
            result[degree + exponent] %= modulus
    return result


def binomial_product(exponents):
    polynomial = [1]
    for exponent in exponents:
        polynomial = multiply_binomial(polynomial, exponent)
    return polynomial


def exact_divide(numerator, denominator):
    """Integer polynomial long division; fail if any remainder is nonzero."""
    if not denominator or denominator[-1] == 0:
        raise ValueError("denominator must have a nonzero leading coefficient")
    remainder = numerator[:]
    while remainder and remainder[-1] == 0:
        remainder.pop()
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    while len(remainder) >= len(denominator):
        value, residue = divmod(remainder[-1], denominator[-1])
        if residue:
            raise ArithmeticError("nonintegral polynomial quotient")
        shift = len(remainder) - len(denominator)
        quotient[shift] = value
        for i, coefficient in enumerate(denominator):
            remainder[i + shift] -= value * coefficient
        while remainder and remainder[-1] == 0:
            remainder.pop()
    if remainder:
        raise ArithmeticError("nonzero polynomial remainder")
    return quotient


def denominator_comparison():
    """Compare stated bounds; no claim of minimality or measured speed."""
    rows = []
    expected = {
        (3, 2, 1): (25, 15, 60, 15),
        (4, 2, 1): (60, 38, 840, 24),
        (4, 4, 4, 4): (145, 70, 720720, 420),
        (6,): (25, 22, 60, 60),
    }
    for mu, expected_values in expected.items():
        w = sum(mu)
        lengths = hooks(mu)
        delta = 1 if w % 2 == 0 else 2
        old_exponents = [delta * i for i in range(1, w + 1)]
        if w % 2 == 0:
            old_exponents.append(1)
        old = binomial_product(old_exponents)
        new = exact_divide(binomial_product([delta * h for h in lengths]),
                           [1, -2, 1])
        quotient = exact_divide(old, new)
        slopes = (w + 1) // 2
        actual = (len(old) - 1 + slopes, len(new) - 1 + slopes,
                  lcm(*old_exponents), lcm(*(delta * h for h in lengths)))
        rows.append({
            "mu": mu, "w": w, "hook_lengths": lengths,
            "old_bivariate_z_degree_bound": actual[0],
            "new_bivariate_z_degree_bound": actual[1],
            "old_pure_z_degree": len(old) - 1,
            "new_pure_z_degree": len(new) - 1,
            "old_fixed_weight_period_bound": actual[2],
            "new_fixed_weight_period_bound": actual[3],
            "old_divisible_by_new_exactly": True,
            "quotient_degree": len(quotient) - 1,
            "expected_values_verified": actual == expected_values,
        })
    return {
        "comparisons": rows,
        "comparisons_checked": len(rows),
        "limits": [
            "Denominators, recurrence orders, and periods are upper bounds, not minima.",
            "Period bounds concern eventual quasipolynomials at fixed output weight.",
            "Degree reductions are not measured running time or algorithmic complexity.",
            "The new general bounds depend on the accompanying proof being correct.",
        ],
        "passed": all(row["expected_values_verified"] for row in rows),
    }


def sparse_multiply(left, right):
    """Exact bivariate polynomials: keys are (q exponent, z exponent)."""
    result = Counter()
    for (a, b), x in left.items():
        for (c, d), y in right.items():
            result[a + c, b + d] += x * y
    return {key: value for key, value in result.items() if value}


def sparse_product(*factors):
    result = {(0, 0): 1}
    for factor in factors:
        result = sparse_multiply(result, factor)
    return result


def odd_mu3_example():
    """Cross-multiply the exact symbolic identity, with no CAS dependency.

    A_(3)=(q+q^4*z^3)/((1-z^4)*(1-q^2*z^2)*(1-q^3*z)).
    Verify D*Q*A/(1-z^2)^2 = q*(1+z^2+z^4)*(1-q*z+q^2*z^2)
    by comparing the two integer bivariate polynomial cross-products.
    """
    def factor(q_degree, z_degree):
        return {(0, 0): 1, (q_degree, z_degree): -1}

    denominator = sparse_product(factor(0, 4), factor(2, 2), factor(3, 1))
    numerator = {(1, 0): 1, (4, 3): 1}
    d = sparse_product(factor(0, 2), factor(0, 4), factor(0, 6))
    q_factor = sparse_product(factor(1, 1), factor(3, 1))
    expected = sparse_product({(1, 0): 1},
                              {(0, 0): 1, (0, 2): 1, (0, 4): 1},
                              {(0, 0): 1, (1, 1): -1, (2, 2): 1})
    left = sparse_product(d, q_factor, numerator)
    right = sparse_product(factor(0, 2), factor(0, 2), expected, denominator)
    keys = left.keys() | right.keys()
    residual = {str(key): left.get(key, 0) - right.get(key, 0)
                for key in sorted(keys) if left.get(key, 0) != right.get(key, 0)}
    return {
        "mu": [3],
        "method": "exact sparse bivariate polynomial cross-multiplication",
        "identity": "D_mu*Q_w*A_mu/(1-z^2)^2 = q*(1+z^2+z^4)*(1-q*z+q^2*z^2)",
        "nonzero_residual_coefficients": residual,
        "passed": not residual,
    }


def sl2_series(mu, maximum_h, q=2, modulus=None):
    """Compute A_mu(z,q) through z^maximum_h by hook-content specialization.

    Only weights up to the middle are needed, by the symmetry of the SL2
    character. Adjacent weight differences give irreducible multiplicities.
    Exact q values and modular residues do not establish a symbolic identity.
    """
    w = sum(mu)
    b = sum(i * row for i, row in enumerate(mu))
    length = max(0, w * maximum_h // 2 - b) + 1
    inverse = [0] * length
    inverse[0] = 1
    for hook in hooks(mu):
        for degree in range(hook, length):
            inverse[degree] += inverse[degree - hook]
            if modulus is not None:
                inverse[degree] %= modulus
    powers = [1] * (w * maximum_h + 2)
    for degree in range(1, len(powers)):
        powers[degree] = powers[degree - 1] * q
        if modulus is not None:
            powers[degree] %= modulus
    answer = []
    for h in range(maximum_h + 1):
        middle = w * h // 2 - b
        if h < len(mu) - 1 or middle < 0:
            answer.append(0)
            continue
        polynomial = inverse[: middle + 1]
        for i, row in enumerate(mu):
            for j in range(row):
                exponent = h + j - i + 1
                for degree in range(middle, exponent - 1, -1):
                    polynomial[degree] -= polynomial[degree - exponent]
                    if modulus is not None:
                        polynomial[degree] %= modulus
        value = sum((coefficient - (polynomial[t - 1] if t else 0))
                    * powers[w * h - 2 * (t + b) + 1]
                    for t, coefficient in enumerate(polynomial))
        answer.append(value % modulus if modulus is not None else value)
    return answer


def conjectured_denominator(mu, q=2, modulus=None):
    w = sum(mu)
    polynomial = [1]
    for hook in hooks(mu):
        polynomial = multiply_binomial(polynomial, hook * (1 if w % 2 == 0 else 2),
                                       modulus=modulus)
    for slope in range(w, 0, -2):
        coefficient = pow(q, slope, modulus) if modulus is not None else q ** slope
        polynomial = multiply_binomial(polynomial, 1, coefficient, modulus)
    # Exact division by (1-z)^2, using cumulative sums rather than a CAS.
    for _ in range(2):
        for degree in range(1, len(polynomial)):
            polynomial[degree] += polynomial[degree - 1]
            if modulus is not None:
                polynomial[degree] %= modulus
        if polynomial[-1]:
            raise ArithmeticError("candidate denominator division was not exact")
        polynomial.pop()
    return polynomial


def check_partition_specialization(mu, q=2, modulus=None):
    """Check the prescribed finite zero window after the numerator bound.

    The window uses the published coarse rationality bound. As a computation
    this remains a finite consistency check; it cannot establish the theorem
    for arbitrary mu, nor a polynomial identity for unspecified symbolic q.
    """
    w = sum(mu)
    denominator = conjectured_denominator(mu, q, modulus)
    bound = len(denominator) - mu[0] - 2
    coarse_degree = (1 + w * (w + 1) // 2 + w // 2 if w % 2 == 0
                     else w * (w + 1) + (w + 1) // 2)
    maximum_h = bound + coarse_degree
    series = sl2_series(mu, maximum_h, q, modulus)
    digest = hashlib.sha256()
    failure = None
    for degree in range(maximum_h + 1):
        coefficient = sum(denominator[j] * series[degree - j]
                          for j in range(min(degree, len(denominator) - 1) + 1))
        if modulus is not None:
            coefficient %= modulus
        digest.update((str(coefficient) + "\n").encode("ascii"))
        if degree > bound and coefficient and failure is None:
            failure = {"degree": degree, "coefficient": str(coefficient)}
    return {
        "mu": mu, "q": q, "modulus": modulus,
        "numerator_degree_bound": bound, "maximum_h": maximum_h,
        "coefficients_sha256": digest.hexdigest(),
        "failure": failure, "passed": failure is None,
    }


def ssyt_series_cross_checks():
    """Independently evaluate the series via direct outer SSYT characters."""
    comparisons = 0
    failures = []
    for w in range(1, 7):
        for mu in partitions(w):
            for q in (2, 3):
                series = sl2_series(mu, 12 // w, q)
                for h in range(1, 12 // w + 1):
                    counts = direct_tableau_weights(mu, h)
                    expected = sum((counts[k - 1] - counts[k + 1]) * q ** k
                                   for k in range(1, w * h + 2))
                    comparisons += 1
                    if series[h] != expected:
                        failures.append({"mu": mu, "h": h, "q": q,
                                         "hook_content": str(series[h]),
                                         "ssyt": str(expected)})
    return {"w_range_inclusive": [1, 6], "q_values": [2, 3],
            "h_range": "1..floor(12/w) inclusive",
            "comparisons": comparisons, "failures": failures,
            "passed": not failures}


def denominator_specializations(progress=print):
    checks = []
    counts = Counter()
    for mode, maximum, qs, modulus in (
        ("exact_integer_specialization", 11, (2, 3), None),
        ("modular_screening", 14, (2,), 1000000007),
    ):
        for w in range(3, maximum + 1):
            for mu in partitions(w):
                for q in qs:
                    check = check_partition_specialization(mu, q, modulus)
                    check["mode"] = mode
                    checks.append(check)
                    counts[mode] += 1
            progress(f"{mode}: w={w} checked", flush=True)
    return {
        "counts": dict(counts),
        "exact_w_range_inclusive": [3, 11],
        "modular_w_range_inclusive": [3, 14],
        "exact_q_values": [2, 3],
        "modular_q_value": 2,
        "prime_modulus": 1000000007,
        "limits": [
            "Exact refers to integer arithmetic at q=2 and q=3, not symbolic q.",
            "A modular zero may hide a nonzero integer or polynomial value.",
            "No finite range proves the infinite theorem or establishes priority.",
        ],
        "checks": checks,
        "passed": all(check["passed"] for check in checks),
    }
