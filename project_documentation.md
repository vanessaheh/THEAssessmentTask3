# **Assessment Task 3**
## Phase 1: Identifying and defining
### **Mind map:**
### **Define your purpose:**
"Gosford High students are at risk of future gambling habits due to lootbox games"
### **Requirements outline**
**Functional requirements:**  

**Data loading:**  
The system should be able to import CSV files. It must notify the user if the requested data does not exist or is not within the available options.

eg. "Invalid selection..."

**Data cleaning:**  
The system needs to handle missing values by removing them from the output. It should also allow users to view each column seperately and display the amount of people who chose each option. 

(eg. "Whether studenst play lootbox games",  
 yes -> 80  
 no -> 120)

**Data analysis:**  
The interface should be able to count and calculate the percentages of people who chose each option. 

(eg. "Whether studenst play lootbox games"  
yes -> 80 -> 40% )

**Data visualisation:**  
The system should include data visualisation tools such as ______ using Pandas and Matplotlib to help users compare data and identify patterns easily.

**Data reporting:**  
The data will 

### **Non-functional requirements**

**Usability:**  
The interface will allow users to view and filter data by selecting presented options. The README file will define the purpose of the interface, where the data is from, and include a usage guide.  

**Reliability:**

**Use case:**  
**Actor:** User  

**Goal:**  To access and interact with existing data through the program's user interface.  

**Preconditions:**  
- The data has been preloaded into the system by an administrator/ programmer
- The user has access to the system interface  

**Main flow:**
1. The user opens the program and is presented with the text-based menu
2. The user selects one of the following options:  
a. View dataset  
b. View visualisation  
c. Filter data  
d. Exit

3. The system performs the requested action and outputs to the user

**Postconditions:**
- user has viewed/interacted with the data
- data remains available

## Phase 2: Researching and Planning
**Chosen issue: Gosford High students are at risk of future gambling habits due to lootbox games**

**Research your chosen issue- SEEI**  

Lootboxes in video games have become increasingly controversial due to their structural and psychological similarities to gambling mechanics. The randomised reward system, whether requiring in-game currency or real money, mirrors the thrill of traditional gambling, particularly through variable ratio schedules (where the player is guaranteed a reward after participating in a certain amount of times) and the "near miss effect". 

In a recent study, one in five problem gamblers reported that their first first exposure to gambling-like behaviours came through lootbox components in video games, often during adolescence.

**Data dictionary**
| FIELD | DATATYPE | FORMAT FOR DISPLAY | DESCRIPTION | EXAMPLE | VALIDATION
|---|---|---|---|---|---|
| Lootbox_players| object | XX...XX| Whether students play lootbox games (yes/no)| yes | Can only be yes or no|
| Lootbox_spenders| object | XX...XX | Whether students have spent money on lootbox systems in games (yes/no)| no| Can only be yes or no|
| Opinion_on_spending| float64| N | How students feel about spending money on lootbox systems in games|3| Can only be 1-5, 1 as in not good at all, 5 as in great


## Phase 4: Testing and evaluating
**Test your analysis**

**Analyse and conclude**

**Peer verification**

**Evaluate your project**
