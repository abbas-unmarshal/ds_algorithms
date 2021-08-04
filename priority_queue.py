class prior_queue:
    def __init__(self):
        self.data=[]
        self.size=0
    def push (self,element):
        prev_size=self.size
        if self.size==0:
            self.data.append(element)
            self.size+=1
        else:
            for i in range(self.size):
                if self.data[i]<element:
                    self.data.insert(i,element)
                    self.size+=1
                    break
        if prev_size==self.size:
            self.data.append(element)
            self.size+=1
    def print(self):
        for i in self.data:
            print(i)
pq=prior_queue()
pq.push(2)
pq.push(4)
pq.push(1)
pq.push(10)
pq.print()