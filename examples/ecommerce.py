"""E-commerce — associations, multiplicities, and composition.

Render to SVG with:
    curl -X POST https://editor.besser-pearl.org/besser_api/get-svg \
      -F "buml_file=@ecommerce.py;type=text/x-python" -o ecommerce.svg
"""
from besser.BUML.metamodel.structural import (
    DomainModel, Class, Property, Multiplicity, BinaryAssociation,
    StringType, IntegerType, FloatType, DateType,
)

customer = Class(name="Customer", attributes={Property(name="name", type=StringType), Property(name="email", type=StringType)})
order    = Class(name="Order",    attributes={Property(name="orderId", type=StringType), Property(name="placedOn", type=DateType)})
line     = Class(name="OrderLine", attributes={Property(name="quantity", type=IntegerType)})
product  = Class(name="Product",  attributes={Property(name="title", type=StringType), Property(name="price", type=FloatType)})

# A Customer places 0..* Orders.
c_end = Property(name="customer", type=customer, multiplicity=Multiplicity(1, 1))
o_end = Property(name="orders",   type=order,    multiplicity=Multiplicity(0, "*"))
places = BinaryAssociation(name="places", ends={c_end, o_end})

# An Order is composed of 1..* OrderLines (composition: the line cannot exist without the order).
o_end2   = Property(name="order", type=order, multiplicity=Multiplicity(1, 1), is_composite=True)
line_end = Property(name="lines", type=line,  multiplicity=Multiplicity(1, "*"))
contains = BinaryAssociation(name="contains", ends={o_end2, line_end})

# Each OrderLine refers to exactly one Product.
line_end2 = Property(name="line",    type=line,    multiplicity=Multiplicity(0, "*"))
p_end     = Property(name="product", type=product, multiplicity=Multiplicity(1, 1))
refers = BinaryAssociation(name="refers", ends={line_end2, p_end})

model = DomainModel(name="Shop", types={customer, order, line, product}, associations={places, contains, refers})
assert model.validate()["success"]
