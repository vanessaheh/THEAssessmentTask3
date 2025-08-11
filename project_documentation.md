# **Assessment Task 3**
## Phase 1: Identifying and defining
### **Mind map:**
### **Define your purpose:**
"Gosford High students are at risk of future gambling habits due to lootbox games"
### **Requirements outline**
**Functional requirements:**  

**Data loading:**  
The system should be able to import CSV files. It must notify the user when errors such as incorrect formatting or missing files.  

**Data cleaning:**  
The system needs to handle missing values by filling gaps with the average or the commonly chosen option when appropriate. It should also allow users to filter through groups of data based on the questions asked in the local survey (eg, "How do you feel about spending money on lootbox games?", where the user can view the number/percentage of people who chose each option). 

**Data analysis:**  
The interface should be able to calculate and display percentages, ratios, and the mean, median and mode of data groups.  

**Data visualisation:**  
The system should include data visualisation tools such as tables, pie charts and bar graphs using Pandas and Matplotlib to help users compare data and identify patterns easily.

**Data reporting:**


### **Non-functional requirements**

**Usability:**  
The user interface will allow users to view data, apply data filters, and update an entry by selecting presented options and subtitles. The README file will define the purpose of the interface, include a usage guide, and list all controls.  

**Reliability:**

**Use case:**  
**Actor:** User  

**Goal:**  To access and interact with existing data through the program's user interface.  

**Preconditions:**  
- The data has been preloaded into the system by an administrator/ programmer
- The user has access to the system interface  

**Main flow:**
1. The user enters username
2. The user opens the program and is presented with the hypothesis
3. Then, the text-based menu appears
4. The user selects one of the following options:  
a. View visualisation  
b. Sort/filter data
5. The system performs the requested action and outputs to the user

**Postconditions:**
- user has viewed/interacted with the data
- updates are SAVED TO THE USERNAME
- data remains available

## Phase 2: Researching and Planning
**Chosen issue: Gosford High students are at risk of future gambling habits due to lootbox games**

**Research your chosen issue**  
Lootboxes in video games have become increasingly controversial due to their structural and psychological similarities to gambling mechanics. The randomised reward system, whether requiring in-game currency or real money, mirrors the thrill of traditional gambling, particularly through variable ratio schedules (where the player is guaranteed a reward after participating in a certain amount of times) and the "near miss effect". 

In a recent study, one in five problem gamblers reported that their first first exposure to gambling-like behaviours came through lootbox components in video games, often during adolescence.

**Data dictionary**
| FIELD | DATATYPE | FORMAT FOR DISPLAY | DESCRIPTION | EXAMPLE | VALIDATION
|---|---|---|---|---|---|
| Population | object | XX...XX| 
| Row 2, Cell 1 | object | XX...XX |
| Row 2, Cell 1 | float64| N |


## Phase 3: Producing and Implementing


## Phase 4: Testing and evaluating
**Test your analysis**

**Analyse and conclude**

**Peer verification**

**Evaluate your project**
