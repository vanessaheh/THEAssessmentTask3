# **Assessment Task 3**
## Phase 1: Identifying and defining
### **Mind map:**
![alt text](mindmap.png)
### **Define your purpose:**
"Gosford High students are at risk of future gambling habits due to lootbox games"
### **Requirements outline**
**Functional requirements:**  

**Data loading:**  
The system should be able to import CSV files and .png images. It must notify the user when errors such as incorrect formatting or missing files. 

**Data cleaning:**  
The system needs to remove rows with NA and double values such as "yes, no". Unnecessary colums must be removed when the data is printed.
Additionally, it should also allow users to filter through groups of data based on the questions asked in the local survey. 

**Data analysis:**  
The interface should be clean, consistent, and visually appealing (chart colours). Through the data filtering menu, the number of people who chose each option will be counted and displayed.

eg. 
"Whether students play lootbox games"
yes -> 75
no -> 80

**Data visualisation:**  
The system should include data visualisation tools such as tables and bar graphs using Pandas and Matplotlib to help users compare data and identify patterns easily. All visualisations must include clear titles, axis labels and visually appealing colours.

**Data reporting:**
The system should display the cleaned and filtered datasets directly in the terminal, while visual representations are automatically opened in a new window.

### **Non-functional requirements**

**Usability:**  
The user interface will allow users to view data and apply data filters by selecting presented options and subtitles. The README file will define the purpose of the interface, include a usage guide, and list all features.  

**Reliability:**
To maintain data reliabilty and integrity, the rows with missing values (NA) or contradictory answers (e. "yes", "no") are removed, ensuring that only valid data ia analysed and used in the dataset. The displayed results should match the cleaned dataset without bias or error.

### **Use case:**  

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
c. Filter/search data  
d. Exit

3. The system performs the requested action and outputs to the user

**Postconditions:**
- user has viewed/interacted with the data
- data remains available

## Phase 2: Researching and Planning
**Hypothesis: Gosford High students are at risk of future gambling habits due to lootbox games**

### **Research your chosen issue- SEEI**  

Lootboxes in video games have become increasingly controversial due to their structural and psychological similarities to traditional gambling mechanics, particularly in how they normalise gambling behaviour among adolescents.
By using in game currency or even real money for a chance at a desirable item, lootboxes blur the line between gaming and gambling. Players are exposed to concepts like risk, chance and *variable ratio enforcement* without realising they may be developing unhealthy, addictive behaviours. These mechanics are often paired with bright visuals and exciting sounds, making the system seem fun and harmless instead of potentially harmful.


For example, a teenager who regularly engages with lootbox games may become desensitised to spending money on chance-based systems, reducing the perceived danger of actual gambling and increasing his likelihood of engaging in it later in life.

As lootboxes become more common in video games, it is crucial to recognise the damaging impact of these systems and protect vulnerable communities from being exploited under the guise of play.

- In a recent study, a survery of 1000 individuals,  20% self reported that their first exposure to gambling-like behaviours came through lootbox components in video games, often during adolescence.

- Median monthly expenditure on lootbox mechanics was $50/month for adolescents, increasing to $72 for young adults.

- According to the NSW Responsible gambling fund:

    *"Both adolescents and young adults who had either opened, bought or sold
loot boxes within the last 12 months were also more likely to have: 1- gambled
in the last 12 months (young adults), 2- gambled more frequently (young
adults), 3- spent more money gambling (young adults), 4- suffered more
gambling problems (adolescents and young adults), 5- suffered more
gambling-related harm (young adults), and 6- endorsed more positive
attitudes towards gambling (adolescents and young adults)."* 

****
*variable ratio enforcement:*   
When a win is given after an unpredictable amount of attempts.   
For example, a player keeps opening lootboxes in hopes to get a rare item. Because the reward could come at any time, they are compelled to keep spending.


***LINKS***  
https://forms.gle/n8GHvjxE7aqjcFCb6 <-- link of lootbox games form sent to students 

https://acquire.cqu.edu.au/articles/report/Loot_Boxes_Are_they_grooming_youth_for_gambling_/13405073

https://www.lifeworksnw.org/2025/02/27/loot-box-games-and-problem-gambling/

https://pubmed.ncbi.nlm.nih.gov/35397261/



### **Data dictionary**
| FIELD | DATATYPE | FORMAT FOR DISPLAY | DESCRIPTION | EXAMPLE | VALIDATION
|---|---|---|---|---|---|
| Play lootbox games| object | XX...XX| Whether students play lootbox games (yes/no)| yes | Can only be yes or no|
| Spent money on lootbox systems | object | XX...XX | Whether students have spent money on lootbox systems in games (yes/no)| no| Can only be yes or no|
| Spending feelings (1-bad, 5-great)| float64| N | How students feel about spending money on lootbox systems in games|3| Can only be 1-5, 1 as in not good at all, 5 as in great
| Timestamp | Datetime64 | DD-MM-YYY HH:MM:SS | Time students filled the form |7/31/2025 11:03:36| Must be in the non-reversible format DD-MM-YYY HH:MM:SS



## Phase 3: Producing and Implementing
(In main.py, data.csv, data_module.py)

## Phase 4: Testing and evaluating

### **Analyse and conclude**

Lootboxes have become a common feature in modern video games, offering the player a chance at a desired or "rare" item for in-game currency or real money. Despite being marketed as harmless, their structure closely mirrors the fundamental mechanics of traditional gambling, especially in how they encourage repeated spending through unpredictable outcomes. This raises serious concerns about how lootboxes may influence the behaviour of more vulnerable and impressionable members of society- adolescents.
In my survey, 75 (48%) of 155 students reported playing games that include lootbox mechanics, 53 (71%) of those who had confessed to spending real money on them. These results not only highlight the widespread engagement with lootbox games is, but how frequently these interactions escalate into financial expenditures, especially given how they may not understand the potential risks associate with repeated spending in a randomized system.
However, when asked how they felt about spending on lootbox mechanics, the majority of responses expressed negativity, with 70 students selected "1" (on a scale from 1- bad to 5-great), while only 25 chose "5". Although different from expected, this serves to underscore a common pattern in gambling. Players are left feeling dissapointed and regretful, yet continue to spend, driven by the hope that further participation will result in a worthwhile reward.

In conclusion, these survey results support the link between lootbox gaming and gambling behaviours. The widespread use, financial expenditures and psychological impacts all point towards what may become future gambling habits, emphasising the need for awareness and regulations among video games like these to prevent long term harm.

### **Peer verification**  
**ARISA**:  

| PLUS | MINUS |
|---|---|
|- The use of time.sleep makes the program feel more structured and controlled|  |
|- Visually appealing | - Time.sleep is not consistent |
|- Easy to navigate and there is an exit/back in each set of options|
|- When I type a number that is not a valid, it reprints the options and an error message | - When I type a word instead of a number, the program crashes (error) 
|- Dataset is clean and accurate | - Can't search for data (but can filter)|
|- README is easy to follow with visuals | 
 
 
**IMPLICATION**

While Vanessa's project is overall structured, clear and accessible with several positive aspects, it may need to undergo slight changes to create a more cohesive program. To enhance reliabilty and user experience, input handling should be fixed to prevent crashes from unexpected entries (letters specifically) and the timing between text could use more consistency (the seconds). Introducing search functions alongside filtering would also significantly improve how users are able to draw valuable insight from the data analysed and visualised.

### **Evaluate your project**

**Evaluate your system and results in relation to your Requirements Outline:**  
Overall, the system met most of the goals I set out in the requirements outline, although it is slightly different to what I had imagined. While I had a clear plan at the beginning, some parts had to be adjusted along the way based on what worked best with the data.
- I was originally going to fit all my data into **one** visualisation, but I later realised my "spending feelings" column would need to be converted into an average. <--- would affect data analysis
- I was originally going to add a "search feature", but I didn't know how to make it work and was short on time

Regardless of these changes, I am proud of how my program turned out.

**Evaluate your system in relation to peer feedback:**  
In response to Arisa's feedback, I have made several adjustments in my code. 
I fixed the issue with the error messages (removed int from int(input)) and made sure all my time.sleeps were the same. However, I have decided not to implement searching of data, mainly due to the lack of time. While this feature would have improved user experience, I believe the current version still meets its main purpose.

**Evaluate your project in relation to project management:**  
While building my project, my time management could have been better. I found that I spent longer than neccessary on smaller parts, such as the mindmap, which left less time for both the code and project documentation (I ended up doing most of it in the last week). In future assessments, I aim to make a schedule and break parts into smaller tasks while prioritising more important components.

**Is the data valid, accurate and timely?**  
The data used in this project was collected from a recent survey of students at Gosford high school, making my program timely and relevant. Furthermore, I have removed the incomplete and inconsistent responses in the original dataset to ensure it is valid.  
However, it **may not be completely accurate**, as it relies on student honesty, which could have led to skewed results and bias. Despite this potential setback, the overall result should not have been affected.

**Is it unbiased?**  
The data could be biased if the students taking the survey were influenced by social desirability or misunderstood the questions/wording. 
Since the survey was only distributed to a small number of students, it may not represent the whole school population. 

**Do we need to improve its security – if so, how?**  
To improve the security of my program, authentication including as usernames and passwords could be implemented. This would help manage and view who is able to access the data, protecting the privacy of students' responses. Additionally, certain features such as viewing response counts, could be further restricted to selected users.

**Could the UX be more accessible – if so, how?**  
The user experience could be made more accessible by utilising different colours for visibility, including graphics, allowing alternative input, and adding data searching features to further enhance navigation and usability. I could have also enforced multi-language options or captions would ensure the program is accessible to a broader audience. 

______