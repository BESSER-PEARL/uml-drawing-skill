"""Organization — a self-referential association (Employee manages Employee).

Render to SVG with:
    curl -X POST https://editor.besser-pearl.org/besser_api/get-svg \
      -F "buml_file=@org.py;type=text/x-python" -o org.svg
"""
from besser.BUML.metamodel.structural import (
    DomainModel, Class, Property, Multiplicity, BinaryAssociation, StringType,
)

employee   = Class(name="Employee",   attributes={Property(name="name", type=StringType), Property(name="title", type=StringType)})
department = Class(name="Department", attributes={Property(name="name", type=StringType)})

# An Employee manages 0..* other Employees (self-reference — distinct end names).
manages    = Property(name="manages",   type=employee, multiplicity=Multiplicity(0, "*"))
managed_by = Property(name="managedBy", type=employee, multiplicity=Multiplicity(0, 1))
supervision = BinaryAssociation(name="supervision", ends={manages, managed_by})

# Every Department has 1..* staff.
dept_end = Property(name="department", type=department, multiplicity=Multiplicity(1, 1))
emp_end  = Property(name="staff",      type=employee,   multiplicity=Multiplicity(1, "*"))
belongs = BinaryAssociation(name="belongs", ends={dept_end, emp_end})

model = DomainModel(name="Org", types={employee, department}, associations={supervision, belongs})
assert model.validate()["success"]
