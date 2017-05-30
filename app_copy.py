import os
import xml.etree.ElementTree as etree


# Get the path to the directory where the project is located
BASE_PATH = os.path.dirname(os.path.realpath(__file__))

# Get XML file and save its path to a variable
xml_file = os.path.join(BASE_PATH, "data\\product_listing_copy.xml")

# Access the XML file and parse it
tree = etree.parse(xml_file)

# Get the root element
root = tree.getroot()

# Loop through the elements
# Use the .tag and .attrib properties
for child in root:
    print(child.tag, child.attrib)

# Use the .text property to view the data inside of the elements
for child in root:
    for element in child:
        print(element.tag, ":", element.text)


# Write to XML file using .SubElement()
new_product = etree.SubElement(root, attrib)


# Create data in sub-elements using the .set() and .text() methods


# Save the XML using the .write() method


# Loop through the elements to see the changes