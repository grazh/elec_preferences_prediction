## The Impact of Students' Academic Performance on the Choice of the Econometrics-2 Course
### Authors

* [grazh](https://github.com/grazh)
* [supervo1d](https://github.com/superVo1d)

### Goal
- to investigate the influence of a student's academic results on his choice of the course "Econometrics-2".

### Desription
We collected data on students' success in mathematical disciplines that are compulsory for all students, and that can influence the choice of the course "Econometrics-2" by the student. In addition, number of group and the number of retest variables were selected as parameters reflecting the general attitude towards the student's studies throughout the entire period of study.

### Files content
* /eda/student_data.xlsx - contains data about 253 third year students of the Faculty of Economics.
  * birth - factor variable for birth date,
  * contract - binary for paid-for education,
  * group - factor var. for student's group,
  * linal1 - factor var. for Linear algebra-I score,
  * terver - factor var. for Probability theory score,
  * matstat - factor var. for Mathematical statistics score,
  * ecm1 - factor var. for Econometrics-I score,
  * ecm2 - binary for Econometrics-II enrollment.

All data was collected with the help of Administration of the Faculty of Economics on the condition of preserving the confidential information of students.

### Exploratory Data Analysis

Let's study the descriptive statistics. (Table 1)

<p align="center">
  <img width="700" height="600" src="https://user-images.githubusercontent.com/55653514/111038709-7e30db00-843b-11eb-968b-76288c0af599.png">
</p>

We can see that it's about 40% of students who've chosen Econometrics-II. 30% of students pay for the education and mean number of retests is 3.6 with the maximum of 28 retakes.

Now we can analyse correlation matrix (Plot 1).

<p align="center">
  <img width="700" height="700" src="https://user-images.githubusercontent.com/55653514/111039765-c8688b00-8440-11eb-9e5b-d8412600c8d8.png">
</p>

It's shown that Econometrics-I score is highly correlated with the Econometrics-II enrollment. Also we can see group number negative correlation with academic performance just like with the choice of "Econometrics-2".

<p align="right">
  Plot 2
</p>


<p align="center">
  Enrollment distribution
</p>

![image](https://github.com/grazh/elec_preferences_prediction/blob/master/plots/ecm1_mark.png)

Now let's study ***Plot 2***. We can see the distribution of Econometrics-I score of students who signed up for Econometrics-II. After studying both graphs we note that a noticeably larger number of enrolled students have excellent grades, meanwhile other group of students has worse grades. So, we can claim that Econometrics-I grade is correlated with econometrics-II enrollment.

The next step is to study the relationship between paid and budgetary forms of education, a student's group and his enrollment in the course "Econometrics-2". ***Plot 3*** shows two graphs: on the left for students on a paid basis of education and budgetary on the right. The y-axis represents the average grade for Mathematical statistics, Linear algebra-I, Probability theory and Econometrics-I. The x-axis represents the group number of a student. Markers are red for students who enrolled for Econometrics-II and blue for others. Markers alpha is 50%, so more intense crosses report about bigger number of students. After studying the figure we can note that the majority of contract students did not sign up for Econometrics-II. Also let's note that red crosses saturation is higher in the top left for budget students. At the same time blue crosses are more intense in lower right. That means that students with higher average grade from groups 301-305 are more likely to enroll for Econometrics-II than students from other groups.

<p align="right">
  Plot 3
</p>

<p align="center">
  Scatter plot for groups and average score
</p>

![image](https://github.com/grazh/elec_preferences_prediction/blob/master/plots/contract_means.png)


Finally, we can study the grades that students who enrolled for Econometrics-II get earlier in the university, they are marked in red in the ***Plot 4***, and student's who didn't enroll for Ecm-II are blue. There are parallel axes in this figure from left to right: the binary for Econometrics-II enrollment which is 6 for enrolled and 2 for others (for clarity), the Econometrics-I grade, the Linear algebra grade, the Mathematical statistics grade, the Probability theory grade and binary for form of education which is 6 for budget form and 2 for paid. It can be seen on the figure, that top part that matches high grades in subjects is predominantly red, that means that almost all excelent students enroll for Econometrics-2. At the same time, the bottom part of the picture is predominantly blue, meaning that students with bad marks are more unlikely to enroll for Econometrics-II. It's hard to point out a good separation criterion, nevertheless we have seen that a small percentage of contract students has enrolled for Econometrics-II. Also we can assume that 4-5 score for Linear algebra is a good criterion for distinguishing students who has enrolled for the course we are interested in.

<p align="right">
  Plot 4
</p>

<p align="center">
  Parallel coordinates
</p>

![image](https://github.com/grazh/elec_preferences_prediction/blob/master/plots/parallel.jpg)
