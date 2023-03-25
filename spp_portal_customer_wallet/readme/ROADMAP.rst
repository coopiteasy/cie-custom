- When a pos.order is partially paid using the customer wallet, do not let
  ``foodprint_payments_per_month`` for that order exceed the amount paid using
  the customer wallet. This prevents "Of which FoodPrint expenses" from
  exceeding the customer wallet amount.
