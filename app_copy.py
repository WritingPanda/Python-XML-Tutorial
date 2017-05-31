# impor the correct python modules for use
import os
import xml.etree.ElementTree as etree


# Get the path to the directory where the project is located
BASE_PATH = os.path.dirname(os.path.realpath(__file__))

# Get XML file and save its path to a variable
# xml_file = os.path.join(BASE_PATH, "data\\product_listing_copy.xml")
xml_file = os.path.join(BASE_PATH, "data\\product_listing.xml")

# Access the XML file, save it to memory, and parse it
tree = etree.parse(xml_file)

# Get root element with .getroot()
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
new_product = etree.SubElement(root, "product", attrib={"id": "4"})
new_product_name = etree.SubElement(new_product, "name")
new_product_description = etree.SubElement(new_product, "description")
new_product_cost = etree.SubElement(new_product, "cost")
new_product_shipping = etree.SubElement(new_product, "shipping")

# Create data in sub-elements using the .set() and .text() methods
# Creates a new attribute in the new_product element
new_product.set("new", "true")
# Check to see the new attribute
print(new_product.attrib)

# Creates the text data in each of the subelements of the new_product element
new_product_name.text = "Python Pants"
new_product_description.text = "These pants will surely help you code like crazy!"
# numbers and floats must be strings
new_product_cost.text = "39.95"
new_product_shipping.text = "4.00"

# Save the XML using the .write() method
tree.write(xml_file)

# Loop through the elements to see the changes
for child in root:
    print(child.tag, child.attrib)

for child in root:
    for element in child:
        print(element.tag, ":", element.text)
