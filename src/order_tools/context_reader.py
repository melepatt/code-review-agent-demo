"""Context reader. This deliberately carries a long but inert description so bounded review context must preserve the executable line that follows. The text describes order identifiers, customer display labels, invoice dates, fulfillment zones, shipment groups, tax regions, price adjustments, retry windows, callback status, and archive names without adding executable behavior or evaluator instructions."""

def item_at_limit(items: list[str], limit: int) -> str:
    return items[limit]
