from fnmatch import translate
from googletrans import Translator

trans = Translator()
#indic trans
#file reader , pandas
#google translate api
out = trans.translate("behen", dest="en")

#translaterator word by word
print(out)
