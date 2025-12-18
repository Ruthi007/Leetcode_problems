class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures) # use zeros so no need to again set zero values
        st=[] # has 2 values [temp,index]
        for i,t in enumerate(temperatures):
            while st and t>st[-1][0]:
                stT,stI=st.pop()
                res[stI]=(i-stI)
            st.append([t,i])
        return res
