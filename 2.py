# key
alphabet = {
        'a' : 'c', 
        'b' : 'd', 
        'c' : 'e', 
        'd' : 'f', 
        'e' : 'g', 
        'f' : 'h', 
        'g' : 'i', 
        'h' : 'j', 
        'i' : 'k', 
        'j' : 'l', 
        'k' : 'm', 
        'l' : 'n', 
        'm' : 'o', 
        'n' : 'p', 
        'o' : 'q', 
        'p' : 'r', 
        'q' : 's', 
        'r' : 't', 
        's' : 'u', 
        't' : 'v', 
        'u' : 'w', 
        'v' : 'x', 
        'w' : 'y', 
        'x' : 'z', 
        'y' : 'a', 
        'z' : 'b'
    }
# data
input_data = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# soulotion 1
# input_changed = list(input_data)
# for item in range(len(input_changed)):
#     input_changed[item] = alphabet.get(input_changed[item], input_changed[item])
# print("".join(input_changed))

# soulotion 2
# output = input_data.maketrans(alphabet)
# print(input_data.translate(output))

# soulotion 3 (class base)
class Translator:
    def __init__(self,data_input):
        self.data_input = data_input
    
    def translator(self):
        output = self.data_input.maketrans(alphabet)
        self.data_input.translate(output)
        return self.data_input.translate(output)


sample = Translator(input_data)
print(sample.translator())

sample = Translator('map')
print(sample.translator())
