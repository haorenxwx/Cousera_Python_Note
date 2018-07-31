#week5_Datainweb.py

======
web services

wire protocol
python
fixtionary ---->	<person>	---->			Java
		Serialize		<name>	De-serialize	HashMap(json, xml)

======
eXtensible Markup Language(XML)

- share structure data
<person> #Start Tag
	<name>Chuck</name> #Chuck: Text Cotent
	<phone type="intl"> #type="intl": Attribute
	+1 734 303 4456
	</phone>
	<email hide="yes"/> # />: Self Closing Tag
</person> #End Tag
- White Spaca in XML not mater
- Tags: indicate the beginning and ending of element
- Attribute: Keyword/value pairs on the opening tag of XML
- Serialize/De-serialize: Convert data in one program into a common format that can be stored and transmit between systems in a programming language-independent manner

the XML structure is like a tree or a path


======
XML Schema

Used for validation
Include all the data type we can used in the XML file
Like: DTD, XSD

用XSD structure 举例：
XSD Structure:

<xs:complexType name='person'>#xs:complexType
	<xs:sequence>#xs: sequence
		<xs:element name="lastname" type="xs:string"
			minOccurs="1" maxOccurs="1"/>#xs:element
		<xs:element name="age" type="xs:string"/>
		<xs:element name="databorn" type="xs:data"/>
		<xs:element name="startdate" type="xs:dataTime"/>
		<xs:element name="prize" type="xs:decimal"/>
		<xs:element name="weeks" type="xs:integer"/>
	</xs:sequence>
</xs:complexType>
A simple element is an XML element that contains only text. It cannot contain any other elements or attributes.


======
Parsing XML

import xml.etree.ElementTree as ET
data = '''<person>
	<name>Chuck</name>
	<phone type="intl">
		+1 734 303 4456
	</phone>
	<email hide="yes"/>
</person>
'''
tree = ET.fromstring(data)
# extract data and give us back a tree
print('Name:',tree.find('name').text)
# from the html file, find the name <tree>
print('Attr:',tree.find('email').get('hide'))
# get the attribute value hide in the tag <email>

#if there are multiple tags using findall:
import xml.etree.ElementTree as ET
input = '''<stuff>
	<users>
		<user x ='2'>
			<id>001</id>
			<name>Chuck</name>
		</user>
		<user x="7">
			<id>009</id>
			<name>Brent</name>
		</user>
	</users>
</stuff>'''

stuff = ET.fromstring(data)
lst = stuff.findall('users/user')
#extract many little tree's information ['tree1','tree2']
print('User count:',len(lst))
for item in lst:
	print('Name',item.find('name').text)
	print('Id',item.find('id').text)
	print('Attribute',item.get('x'))
















