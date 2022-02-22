def try_me(A, B):
    """calculates P(B/A) when given independent probs of A and B"""
    A_and_B = A * B
    result = A_and_B / A
    return result
