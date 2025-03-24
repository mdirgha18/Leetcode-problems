class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        today = 0 # Keeps the track of the last day covered by a meeting 

        for i, j in sorted(meetings, key=lambda x:x[0]): 
            if j <= today:
                # If the meeting ends before or on 'today', it's already covered
                continue
            elif i > today:
                # If the meeting starts after 'today', we count all free days before it
                days -= j - i + 1
            else:
                # If the meeting overlaps with 'today', only count the uncovered part
                days -= j - today
            # Update 'today' to the end of the current meeting
            today = j 

        return days # remaining free days after accounting for all the meetings 

class Solution:
  def countDays(self, days: int, meetings: List[List[int]] -> int:
    today = o
  for i, j in sorted(meetings, key=lambda, x:x[0]):
    if j <= today:
      continue
    elif i > today:
      days -= j - i + 1
    else:
      days -= j - today
    today = j
  return days
        
