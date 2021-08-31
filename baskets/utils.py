def totals(baskets):
    total_s = 0
    total_q = 0
    for basket in baskets:
        total_s += basket.sum()
        total_q += basket.quantity
    return total_s, total_q
