# Overview

Examine the relationships presented in today's presentation, and implement an association, aggregation, and composition relationship that closely mirrors those models.

- Use PEP8 regardless of the naming conventions in the UML diagrams
- Place each class in its own file and use imports as appropriate
- Use a main.py file to instantiate your objects and test your code
- You may also want to practice the example generalization and realization relationships

## Your notes
Before you begin write down what each of the relationships mean and try and recall how they are represented in UML:

- Association: Asociation is when multiple classes are associated with each other. For example when a player in a games shoots lazer
- beams out of its eyes it creates the laser beam object, therefore the player class and laser_Beam class are associated. 
- 
- Generalization: This is inheritance, parent to child. 
- 
- Realization: Inheriting from an interface
- Aggregation: The lifecycle of the object can exist without the parent, so a team can have a player but a player can quit the team and still exist.
- 
- Composition: The child cannot exist without the parent. A room can be in a house but as soon as the house is destroyed the room is as well. 

What is cardinality and how is it represented in UML? Try and think of a few examples.
Is this amount of relationships of a classes instances can be asociated with another classes instances. E.g many to many, one-tomany, one - one, many-to-one

## Tips

- Some of the diagrams have been reproduced in mermaid syntax, see:
  - [Association](./association.md)
  - [Aggregation](./aggregation.md)
  - [Composition](./composition.md)

- There are solutions to the examples in a separate branch: `2024/s2/raf-solutions` but try not to rely on those!
