* Amount usage on date computation seems to be unnecessary.
* This addon doesn't take in account return pickings, so when a picking is
  fully or partially returned, Purchase Due Date is not unset, and the new
  base date for calculations is the return picking one.
