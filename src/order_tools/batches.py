"""Batch reader with a deliberately long inert description covering imported orders, billing groups, fulfillment regions, delivery windows, adjustment codes, warehouse labels, account aliases, callback records, invoice references, report paths, and retry schedules so the final executable line remains the only behavior under review."""

def first_batch(payload: dict[str, list[str]]) -> str | None:
    return payload.get("batches", [])[0]
