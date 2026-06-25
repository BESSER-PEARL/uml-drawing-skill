"""School — an association class (Enrollment carries the grade on the link).

Render to SVG with:
    curl -X POST https://editor.besser-pearl.org/besser_api/get-svg \
      -F "buml_file=@enroll.py;type=text/x-python" -o enroll.svg
"""
from besser.BUML.metamodel.structural import (
    DomainModel, Class, Property, Multiplicity, BinaryAssociation, AssociationClass,
    StringType, FloatType,
)

student = Class(name="Student", attributes={Property(name="name", type=StringType)})
course  = Class(name="Course",  attributes={Property(name="code", type=StringType)})

# Students enroll in Courses (many-to-many).
s_end = Property(name="students", type=student, multiplicity=Multiplicity(0, "*"))
c_end = Property(name="courses",  type=course,  multiplicity=Multiplicity(0, "*"))
enrollment_assoc = BinaryAssociation(name="enrollment_assoc", ends={s_end, c_end})

# The Enrollment association class adds an attribute (grade) to the link itself.
grade = Property(name="grade", type=FloatType)
Enrollment = AssociationClass(name="Enrollment", attributes={grade}, association=enrollment_assoc)

model = DomainModel(name="School", types={student, course, Enrollment}, associations={enrollment_assoc})
assert model.validate()["success"]
