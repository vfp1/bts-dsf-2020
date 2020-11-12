![BTS](https://github.com/vfp1/bts-dsf-2020/blob/main/Logo-BTS.jpg?raw=1)

# bts-dsf-2020
Repository for BTS Data Science Foundations Course 2020

## Launch it with Binder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/vfp1/bts-dsf-2020/main)

# Sessions

Session | Description | Colab
--- | --- | ---
Session 1 | Introduction to Pandas. | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vfp1/bts-dsf-2020/blob/main/Session_1/01_Pandas_Introduction_Common_Data_Formats.ipynb)
Session 2 | More Pandas. | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vfp1/bts-dsf-2020/blob/main/Session_2/02_Pandas_continued.ipynb)
Session 3 | SQL, SQLite and Pandas. | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vfp1/bts-dsf-2020/blob/main/Session_2/02_Pandas_continued.ipynb)
Session 4 | Pandas and SQLite exercises in depth. | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vfp1/bts-dsf-2020/blob/main/Session_4/04_Pandas_&_SQLite_recap_through_exercises.ipynb)
Session 5 | Image array manipulation: Numpy and Scipy | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vfp1/bts-dsf-2020/blob/main/Session_5/05_Array_image_manipulation.ipynb)
Session 6 | Image array manipulation: Numpy and Scipy | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vfp1/bts-dsf-2020/blob/main/Session_6/06_Image_processing.ipynb)
Final assignment | Instructions for final assignment. Start as early as you can. | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vfp1/bts-dsf-2020/blob/main/Final_project/DSF_FINAL_PROJECT.ipynb)


## Additional Resources

### Pandas
* [Pandas Cheatsheet](https://www.w3resource.com/python-exercises/pandas/index.php)
* [Pandas Exercises](https://www.machinelearningplus.com/python/101-pandas-exercises-python/)

### NumPy
* Amazing visualizations explaining [NumPy](https://jalammar.github.io/visual-numpy/)

### Tidy Data (by [Markham's](https://github.com/justmarkham/DAT8))
* [Good Data Management Practices for Data Analysis](https://www.prometheusresearch.com/good-data-management-practices-for-data-analysis-tidy-data-part-2/) briefly summarizes the principles of "tidy data".
* [Hadley Wickham's paper](http://www.jstatsoft.org/article/view/v059i10) explains tidy data in detail and includes lots of good examples.
* Example of a tidy dataset: [Bob Ross](https://github.com/fivethirtyeight/data/blob/master/bob-ross/elements-by-episode.csv)
* Examples of untidy datasets: [NFL ticket prices](https://github.com/fivethirtyeight/data/blob/master/nfl-ticket-prices/2014-average-ticket-price.csv), [airline safety](https://github.com/fivethirtyeight/data/blob/master/airline-safety/airline-safety.csv), [Jets ticket prices](https://github.com/fivethirtyeight/data/blob/master/nfl-ticket-prices/jets-buyer.csv), [Chipotle orders](https://github.com/TheUpshot/chipotle/blob/master/orders.tsv)
* If your co-workers tend to create spreadsheets that are [unreadable by computers](https://bosker.wordpress.com/2014/12/05/the-government-statistical-services-terrible-spreadsheet-advice/), they may benefit from reading these [tips for releasing data in spreadsheets](http://www.clean-sheet.org/). (There are some additional suggestions in this [answer](http://stats.stackexchange.com/questions/83614/best-practices-for-creating-tidy-data/83711#83711) from Cross Validated.)

### Databases and SQL (by [Markham's](https://github.com/justmarkham/DAT8))
* This [GA slide deck](https://github.com/justmarkham/DAT5/blob/master/slides/20_sql.pdf) provides a brief introduction to databases and SQL. The [Python script](https://github.com/justmarkham/DAT5/blob/master/code/20_sql.py) from that lesson demonstrates basic SQL queries, as well as how to connect to a SQLite database from Python and how to query it using Pandas.
* The repository for this [SQL Bootcamp](https://github.com/brandonmburroughs/sql_bootcamp) contains an extremely well-commented SQL script that is suitable for walking through on your own.
* This [GA notebook](https://github.com/podopie/DAT18NYC/blob/master/classes/17-relational_databases.ipynb) provides a shorter introduction to databases and SQL that helpfully contrasts SQL queries with Pandas syntax.
* [SQLZOO](http://sqlzoo.net/wiki/SQL_Tutorial), [Mode Analytics](http://sqlschool.modeanalytics.com/), [Khan Academy](https://www.khanacademy.org/computing/computer-programming/sql), [Codecademy](https://www.codecademy.com/courses/learn-sql), [Datamonkey](http://datamonkey.pro/guess_sql/lessons/), and [Code School](http://campus.codeschool.com/courses/try-sql/contents) all have online beginner SQL tutorials that look promising. Code School also offers an [advanced tutorial](https://www.codeschool.com/courses/the-sequel-to-sql/), though it's not free.
* [w3schools](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all) has a sample database that allows you to practice SQL from your browser. Similarly, Kaggle allows you to query a large SQLite database of [Reddit Comments](https://www.kaggle.com/c/reddit-comments-may-2015/data) using their online "Scripts" application.
* [What Every Data Scientist Needs to Know about SQL](http://joshualande.com/data-science-sql/) is a brief series of posts about SQL basics, and [Introduction to SQL for Data Scientists](http://bensresearch.com/downloads/SQL.pdf) is a paper with similar goals.
* [10 Easy Steps to a Complete Understanding of SQL](https://web.archive.org/web/20150402234726/http://tech.pro/tutorial/1555/10-easy-steps-to-a-complete-understanding-of-sql) is a good article for those who have some SQL experience and want to understand it at a deeper level.
* SQLite's article on [Query Planning](http://www.sqlite.org/queryplanner.html) explains how SQL queries "work".
* [A Comparison Of Relational Database Management Systems](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems) gives the pros and cons of SQLite, MySQL, and PostgreSQL.
* If you want to go deeper into databases and SQL, Stanford has a well-respected series of [14 mini-courses](https://lagunita.stanford.edu/courses/DB/2014/SelfPaced/about).
* [Blaze](http://blaze.pydata.org) is a Python package enabling you to use Pandas-like syntax to query data living in a variety of data storage systems.

# This course is inspired and uses resources from:
* [Jake Vanderplas](https://github.com/jakevdp)
* [Markham's Course](https://github.com/justmarkham/DAT8/)
* [SciPy](https://scipy.org)
* [Scipy Lectures](https://scipy-lectures.org)
* [NumPy](https://numpy.org)

