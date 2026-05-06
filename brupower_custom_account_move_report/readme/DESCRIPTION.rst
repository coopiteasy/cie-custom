Brupower custom module for invoices report.

* Add a binary field to ``account.move`` (``consumption_graph_image``) to store an SVG image
* Include this SVG image at the end of the ``account.move`` report
* Add a writable text computed field (``consumption_graph_svg``) to allow to get and set the SVG image as text
