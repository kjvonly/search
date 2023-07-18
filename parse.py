import json

bn = None
with open('booknames.json') as booknames: 
  bn = json.loads(str(booknames.read()))

def get_short_name(bookname):
   id = bn['booknamesByName'][bookname]
   return bn['shortNames'][str(id)]
with open('all.json') as all:
    chapters = json.loads(str(all.read()))
    for c in chapters:
      c = chapters[c]
      chapterNumber = c['number']
      book = get_short_name(c['bookName']).lower()
      
      verses = c['verses']
      for k in verses:
        v = verses[k]
        verseNumber = v['number']  
        print(json.dumps({"index": {"_id": "{}_{}_{}".format(book, chapterNumber, verseNumber) } }))
        doc = {}
        doc['book'] = book
        doc['chapter'] = chapterNumber
        doc['text'] = v['text']
        words = []
        for w in v['words']:
            word = {}
            word['text'] = w['text']
            if w['class']:
              word['class'] = []
              for c in w['class']:
                  word['class'].append(c)
            if w['href']:
              word['href'] = []
              for h in w['href']:
                word['href'].append(h)
            words.append(word)
        doc['words'] = words
        print(json.dumps(doc))