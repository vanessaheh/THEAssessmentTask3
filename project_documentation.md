# **Assessment Task 3**
## Phase 1: Identifying and defining
### **Mind map:**
### **Define your purpose:**
"Gosford High students are at risk of future gambling habits due to lootbox games"
### **Requirements outline**
**Functional requirements:**  

**Data loading:**  
The system should be able to import CSV files and .png images. It must notify the user when errors such as incorrect formatting or missing files.  

**Data cleaning:**  
The system needs to remove rows with NA and double values such as "yes, no". It should also allow users to filter through groups of data based on the questions asked in the local survey (eg. "How do you feel about spending money on lootbox games?", where the user can view the number of people who chose each option). 

**Data analysis:**  
The interface should be clean, consistent, and visually appealing (chart colours) and 

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
1. User opens the program and is presented with the text based menu
2. The user selects one of the following options:  
a. View dataset  
b. View visualisation  
c. Search or filter data  
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
| Potential_spenders| float64| N | How students feel about spending money on lootbox systems in games|3| Can only be 1-5, 1 as in not good at all, 5 as in great


## Phase 3: Producing and Implementing


## Phase 4: Testing and evaluating
**Test your analysis**

**Analyse and conclude**

**Peer verification**

**Evaluate your project**
