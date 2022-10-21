import xmlrpc.client
c = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(c)
print(c.system.listMethods())
print(c.system.methodHelp("phone"))
print(c.system.methodSignature("phone"))
print(c.phone("Bert")) # BERT is designed to help computers understand the meaning of ambiguous language in text by using surrounding text to establish context. 

# answer is ITALY