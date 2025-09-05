* This addon doesn't take in account return pickings, so when a picking is
  fully or partially returned, Purchase Due Date is not unset, and the new
  base date for calculations is the return picking one.
* `account_payment_term_extension` dependency may be removed, as unneeded
  starting from v17 (not verified).
