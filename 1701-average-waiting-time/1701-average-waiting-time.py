class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        first_task_time = customers[0][1] + customers[0][0]
        task_ending_time = [first_task_time]

        if len(customers) > 1:
            for i in range(1, len(customers)):
                if customers[i][0] < task_ending_time[i-1]:
                    x = customers[i][1] + task_ending_time[i-1]
                else:
                    x = customers[i][1] + customers[i][0]
                task_ending_time.append(x)
        
        total_wait = 0
        count = 0
        for i in range(len(customers)):
            if task_ending_time[i] < customers[i][0]:
                total_wait += customers[i][0]     
            else:
                total_wait += (task_ending_time[i] - customers[i][0])
            count += 1
        
        return total_wait/count
