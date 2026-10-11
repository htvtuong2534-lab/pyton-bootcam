def summary(scores:list[float])->dict:
          if not scores:
                  raise ValueError("This is an empty list")
          sorted_scores=sorted(scores)
          n=len(sorted_scores)
          minval=sorted_scores[0]
          maxval=sorted_scores[n-1]
          meanval=round(sum(scores)/2,2)
          if n%2 != 0:
                  medianval=sorted_scores[n//2]
          else:
                  (sorted_scores[n//2-1] + sorted_scores[n//2])/2.0
          median_val = round(median_val, 2)
    
          return {
          "min": minval,
          "max": maxval,     
          "mean": meanval,
          "median": median_val
          }
