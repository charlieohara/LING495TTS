with open("cmudict","r") as cmu:
    cmu_txt=cmu.readlines()
pronunciations={}
for line in cmu_txt:
    pronunciations[line.split()[0]]=line.split()[2:]

def text_to_phones(text):
    sentence=[]

    for word in text.split():
        word=word.upper()
        if word in pronunciations:
            sentence.append(pronunciations[word])
        else:
            print(word," is not in CMU.")
            sentence.append([])
    return sentence

def input_to_phones():
    return text_to_phones(input("What text do you want to be synthesized?"))

print(text_to_phones("let's give this a good old tryy!"))
input_to_phones()