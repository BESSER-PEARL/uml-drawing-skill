"""Vehicles — an inheritance hierarchy with an abstract superclass.

Render to SVG with:
    curl -X POST https://editor.besser-pearl.org/besser_api/get-svg \
      -F "buml_file=@vehicles.py;type=text/x-python" -o vehicles.svg
"""
from besser.BUML.metamodel.structural import (
    DomainModel, Class, Property, Generalization, StringType, IntegerType, FloatType,
)

vehicle  = Class(name="Vehicle", attributes={Property(name="vin", type=StringType)}, is_abstract=True)
car      = Class(name="Car",     attributes={Property(name="doors", type=IntegerType)})
truck    = Class(name="Truck",   attributes={Property(name="payloadTons", type=FloatType)})
electric = Class(name="ElectricCar", attributes={Property(name="rangeKm", type=IntegerType)})

# general = parent, specific = child.
g1 = Generalization(general=vehicle, specific=car)
g2 = Generalization(general=vehicle, specific=truck)
g3 = Generalization(general=car, specific=electric)

model = DomainModel(name="Fleet", types={vehicle, car, truck, electric}, generalizations={g1, g2, g3})
assert model.validate()["success"]
