# Poll_Simulator

For Poll_Simulator application i have used python django framework which is using MVC pattern itself.
There are 2 apps:

1. Poll Simulator
2. Main

1.Poll Simulator:
It contaimns models views and urls as there is no need to use use database we dont need any model.
View Contains 4 functions:
-add_candidate function adding candidate and also check duplicate values.
-vote_candidate fnxtion use for voting by students, where also duplication values of students are handled.
-vote_result and vote_summary function is just use to display the result.
-Home page having all the page links is also there.

2. Main
Every django app have this main app which is handling all the pages.


For storing candidates and voters tuples are used as they are immutable.
For storing votes dictionary having key-value pair used.
