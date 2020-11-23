"""
    My quadtree structure isn't optimal. It stores 4 subtrees per node, but actual objects should only be
    stored inside the leaves, not inner nodes. Therefore the collection holding the actual objects needs to be
    moved to the leaves.
    Pseudocode:
        Insert an object into the quadtree:
        Check if the object intersects the current node. If so, recurse. If you've reached the leaf level, insert the object into the collection.
        Delete an object from the quadtree:
        Execute the exact same steps as if inserting the object, but when you've reached the leaf level delete it from the collection.
        Test if an object intersects any object inside the quadtree:
        Execute the exact same steps as if inserting the object, but when you've reached the leaf level check for collision with all the objects in the collection.
        Test for all collisions between all objects inside the quadtree:
        For every object in the quadtree execute the single object collision test.
        Update the quadtree:
        Delete all objects from the quadtree whose position has been modified and insert them again.
"""

