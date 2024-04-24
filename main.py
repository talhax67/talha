meme_dict = {
          "CRİNGE": "garip ya da utandırıcı birşey",
          "LOL": "komik bir şeye verilen cevap",
          "CREEPY": "ürkütücü"
          }
          
          
word = input("anlamadığın bir kelimeyi benimle paylaş!")

if word in meme_dict:
    print(word, " kelimesinin anlamı =", meme_dict[world])
else:
    print("Maalesef verdiğiniz kelime listemde yok!!!")
