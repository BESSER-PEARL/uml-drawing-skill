"""Task tracker — an enumeration used as an attribute type, plus composition.

Render to SVG with:
    curl -X POST https://editor.besser-pearl.org/besser_api/get-svg \
      -F "buml_file=@tasks.py;type=text/x-python" -o tasks.svg
"""
from besser.BUML.metamodel.structural import (
    DomainModel, Class, Property, Multiplicity, BinaryAssociation,
    Enumeration, EnumerationLiteral, StringType, DateType,
)

priority = Enumeration(name="Priority", literals={
    EnumerationLiteral(name="LOW"), EnumerationLiteral(name="MEDIUM"), EnumerationLiteral(name="HIGH"),
})
project = Class(name="Project", attributes={Property(name="name", type=StringType)})
task    = Class(name="Task",    attributes={
    Property(name="title", type=StringType),
    Property(name="due", type=DateType),
    Property(name="level", type=priority),  # attribute typed by an enumeration
})

# A Project is composed of 0..* Tasks.
p_end = Property(name="project", type=project, multiplicity=Multiplicity(1, 1), is_composite=True)
t_end = Property(name="tasks",   type=task,    multiplicity=Multiplicity(0, "*"))
has = BinaryAssociation(name="has", ends={p_end, t_end})

model = DomainModel(name="Tracker", types={project, task, priority}, associations={has})
assert model.validate()["success"]
