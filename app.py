import os
import xml.etree.ElementTree as etree


# Get the path to the directory where the project is located
BASE_PATH = os.path.dirname(os.path.realpath(__file__))

# Get XML file and save its path to a variable
xml_file = os.path.join(BASE_PATH, "test_file.xml")

# Access the XML file and parse it
tree = etree.parse(xml_file)

# Get the root element
root = tree.getroot()

# Now, we can run some commands on the tree object

"""
TODOS:

1. Parse the XML list and show the root
    The parse() function returns an object which represents the entire document. 
2. Iterate through the elements
    Elements are lists
    Define what a list is
    Define a for loop
    Show the data in powershell
    Nest the for loop
3. Show how to access attributes
    Attributes are dictionaries
    Definie what a dictionary is
    Show example of the attrib property
4. Search for a node
    Find a specific element within the tree
    tree.findall() will only return what it can find until the root
    Query the XML and pull data from it
5. Write to the XML file
    new_product = etree.SubElement(root, 'product')
    etree.SubElement(new_product, "name").text = "some value 1"
"""

# https://docs.python.org/3.4/library/xml.etree.elementtree.html