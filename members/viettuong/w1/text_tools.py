def wordcount(text:str)->dict[str,int]:
          text=text.lower()
          for p in ".,!?:":
                  text=text.replace(p,"")
          words=text.split()
          count={}
          for word in words:
                  count[word]=count.get(word,0)+1

          return count

def topk(text:str,k:int)->list[tuple[str,int]]:
        count=wordcount(text)
        sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    
        return sorted_items[:k]