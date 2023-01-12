import numpy as np
import random

#  Flow matrix
Flow = [[0,0,5,0,5,2,10,3,1,5,5,5,0,0,5,4,4,0,0,1],
        [0,0,3,10,5,1,5,1,2,4,2,5,0,10,10,3,0,5,10,5],
        [5,3,0,2,0,5,2,4,4,5,0,0,0,5,1,0,0,5,0,0],
        [0,10,2,0,1,0,5,2,1,0,10,2,2,0,2,1,5,2,5,5],
        [5,5,0,1,0,5,6,5,2,5,2,0,5,1,1,1,5,2,5,1],
        [2,1,5,0,5,0,5,2,1,6,0,0,10,0,2,0,1,0,1,5],
        [10,5,2,5,6,5,0,0,0,0,5,10,2,2,5,1,2,1,0,10],
        [3,1,4,2,5,2,0,0,1,1,10,10,2,0,10,2,5,2,2,10],
        [1,2,4,1,2,1,0,1,0,2,0,3,5,5,0,5,0,0,0,2],
        [5,4,5,0,5,6,0,1,2,0,5,5,0,5,1,0,0,5,5,2],
        [5,2,0,10,2,0,5,10,0,5,0,5,2,5,1,10,0,2,2,5],
        [5,5,0,2,0,0,10,10,3,5,5,0,2,10,5,0,1,1,2,5],
        [0,0,0,2,5,10,2,2,5,0,2,2,0,2,2,1,0,0,0,5],
        [0,10,5,0,1,0,2,0,5,5,5,10,2,0,5,5,1,5,5,0],
        [5,10,1,2,1,2,5,10,0,1,1,5,2,5,0,3,0,5,10,10],
        [4,3,0,1,1,0,1,2,5,0,10,0,1,5,3,0,0,0,2,0],
        [4,0,0,5,5,1,2,5,0,0,0,1,0,1,0,0,0,5,2,0],
        [0,5,5,2,2,0,1,2,0,5,2,1,0,5,5,0,5,0,1,1],
        [0,10,0,5,5,1,0,2,0,5,2,2,0,5,10,2,2,1,0,6],
        [1,5,0,5,1,5,10,10,2,2,5,5,5,0,10,0,0,1,6,0]]

#  Distance matrix
Distance = [[0,1,2,3,4,1,2,3,4,5,2,3,4,5,6,3,4,5,6,7],
            [1,0,1,2,3,2,1,2,3,4,3,2,3,4,5,4,3,4,5,6],
            [2,1,0,1,2,3,2,1,2,3,4,3,2,3,4,5,4,3,4,5],
            [3,2,1,0,1,4,3,2,1,2,5,4,3,2,3,6,5,4,3,4],
            [4,3,2,1,0,5,4,3,2,1,6,5,4,3,2,7,6,5,4,3],
            [1,2,3,4,5,0,1,2,3,4,1,2,3,4,5,2,3,4,5,6],
            [2,1,2,3,4,1,0,1,2,3,2,1,2,3,4,3,2,3,4,5],
            [3,2,1,2,3,2,1,0,1,2,3,2,1,2,3,4,3,2,3,4],
            [4,3,2,1,2,3,2,1,0,1,4,3,2,1,2,5,4,3,2,3],
            [5,4,3,2,1,4,3,2,1,0,5,4,3,2,1,6,5,4,3,2],
            [2,3,4,5,6,1,2,3,4,5,0,1,2,3,4,1,2,3,4,5],
            [3,2,3,4,5,2,1,2,3,4,1,0,1,2,3,2,1,2,3,4],
            [4,3,2,3,4,3,2,1,2,3,2,1,0,1,2,3,2,1,2,3],
            [5,4,3,2,3,4,3,2,1,2,3,2,1,0,1,4,3,2,1,2],
            [6,5,4,3,2,5,4,3,2,1,4,3,2,1,0,5,4,3,2,1],
            [3,4,5,6,7,2,3,4,5,6,1,2,3,4,5,0,1,2,3,4],
            [4,3,4,5,6,3,2,3,4,5,2,1,2,3,4,1,0,1,2,3],
            [5,4,3,4,5,4,3,2,3,4,3,2,1,2,3,2,1,0,1,2],
            [6,5,4,3,4,5,4,3,2,3,4,3,2,1,2,3,2,1,0,1],
            [7,6,5,4,3,6,5,4,3,2,5,4,3,2,1,4,3,2,1,0]]

#  Cost function
def Cost(Solution):
    Array_length = len(Solution)
    Costt = 0
    count = 0
    for i in range(Array_length-1):
        for j in range(i+1,Array_length):
            count += 1 
            Costt = Costt+Distance[i][j]*Flow[Solution[i] - 1][Solution[j]-1]
    # print(Costt)
    return Costt


#  Generating neighbourhood
def Neighbourhood_generation(Solution):
    Start = Solution[:]
    Neighbourhood_complete = []
    Array_length = len(Solution)

    for i in range(Array_length -1 ):
        for j in range(i+1,Array_length):
            # if(i!=j):
            Swap = [Start[i]-1,Start[j]-1]
            temp = Start[j]
            Start[j] = Start[i]
            Start[i] = temp
            #  Recording the swapped values
            Neighbourhood_complete.append([Start[:],Swap])
            Start = Solution[:]

    return Neighbourhood_complete


#  We update tabu structure after every iteration and subtracts 1 from all the positions
def Tabu_Structure_Check_Update(Solution,Tabu_Structure):
    Tabu_Length = len(Tabu_Structure)

    Value_Swap_i = Solution[1][0]
    Value_Swap_j = Solution[1][1]

    if Value_Swap_j < Value_Swap_i:
        temp = Value_Swap_j
        Value_Swap_j = Value_Swap_i
        Value_Swap_i = temp
        

    for i in range(Tabu_Length-1):
        for j in range(i+1,Tabu_Length):
            #  Subtract 1 from all positions having value greater than zerp
            if Tabu_Structure[i][j] > 0:
                Tabu_Structure[i][j] = Tabu_Structure[i][j] - 1
            if i == Value_Swap_i and j == Value_Swap_j:
                
                #  Tabu tenure of 10
                Tabu_Structure[i][j] = 10

                #  IF using long term mememory uncomment the below line
                # Tabu_Structure[j][i] +=1
  
    return Tabu_Structure

  
#  Move function
def Move(Neighbourhood_complete, Latest_cost,Tabu_Structure):
    # Intializing best cost and best solution in a neighbourhood
    Best_Solution_neighbourhood  = Neighbourhood_complete[0]
    best_cost = 5000

    # Uncooment below code for aspiration criteria
    # best_Aspiration_cost = Latest_cost
    # Best_Solution_Aspiration = Neighbourhood_complete[0]

    for neighbour in Neighbourhood_complete:

        Value_Swap_i = neighbour[1][0]
        Value_Swap_j = neighbour[1][1]

        if Value_Swap_j < Value_Swap_i:
            # checking which value is smaller for tabu structure
            temp = Value_Swap_j
            Value_Swap_j = Value_Swap_i
            Value_Swap_i = temp
        
        if Tabu_Structure[Value_Swap_i][Value_Swap_j] == 0:

            # Uncomment below code for Frequency criteria (long term memmory)
            # cost = Cost(neighbour[0]) + Tabu_Structure[Value_Swap_j][Value_Swap_i]

            cost = Cost(neighbour[0])
             
            #  Checking best cost for a solution in a neighbourhood
            if cost < best_cost:
                Best_Solution_neighbourhood = neighbour
                best_cost = cost


    #  uncomment below code for aspiratio criteria 
    #     else:
    #         cost_2 = Cost(neighbour[0])
    #         if cost_2 < best_Aspiration_cost:
    #             Best_Solution_Aspiration = neighbour
    #             best_Aspiration_cost = cost_2

    # if best_cost > best_Aspiration_cost:
    #     best_cost = best_Aspiration_cost
    #     Best_Solution_neighbourhood = Best_Solution_Aspiration

    return Best_Solution_neighbourhood, best_cost

def main():

    #  Intializing tabu structure
    Tabu_Structure = np.zeros((20,20),dtype=int)
    Best_Solution = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],[0,0]]

    # Two different intial solutions
    # Best_Solution =   [[4,5,6,7,8,9,11,10,12,13,14,16,15,17,18,19,20,1,2,3],[0,0]]
    # Best_Solution =   [[4,5,6,8,7,9,10,11,13,12,14,16,15,17,19,18,1,2,3,20],[0,0]]
    i =0
    global_optimal_solution = [Best_Solution, Cost(Best_Solution[0])]
    while i < 5000:
        # Intializing final cost
        Cost_final = Cost(Best_Solution[0])

        # Generation og neighbourhood
        Complete_Neighbourhood = Neighbourhood_generation(Best_Solution[0])
        
        #  Uncomment below code for Randomization
        # Best_Solution,Cost_final =  Move(random.sample(Complete_Neighbourhood,3), global_optimal_solution[1],Tabu_Structure)

        #  Getting best solution from a neighbourhood
        Best_Solution,Cost_final =  Move(Complete_Neighbourhood, global_optimal_solution[1],Tabu_Structure)

        # Updating tabu structure
        Tabu_Structure = Tabu_Structure_Check_Update(Best_Solution,Tabu_Structure)

        # Comparing the current best cost with overall best cost optained
        if Cost(Best_Solution[0]) < global_optimal_solution[1]:
            global_optimal_solution[0] = Best_Solution
            global_optimal_solution[1] = Cost(Best_Solution[0])

        #  Stopping criteria
        if global_optimal_solution[1] == 1285:
            print(i)
            break
        i =i+1
    
    print(global_optimal_solution[0][0])
    print(global_optimal_solution[1])


if __name__ == "__main__":
    main()
    
















# B= [19,7,4,6,17,20,18,14,5,3,9,8,15,2,12,10,16,1,11,13]

# A = [18,14,10,3,9,4,2,12,11,16,19,15,20,8,13,17,5,7,1,6]
# Cost(A)
