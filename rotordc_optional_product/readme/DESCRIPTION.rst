This module has two main behaviours:

- When selecting optional products in the 'add to cart' modal, the user is
  prevented from adding more than one optional product of the same internal
  category.
- When checking out, the user is redirected to an informative error page when
  they did not select all available optional products for their order. e.g. if a
  lamp has optional products with the internal categories 'light bulb' and
  'cable', then the user **must** select one optional product of both categories
  when ordering a lamp.
