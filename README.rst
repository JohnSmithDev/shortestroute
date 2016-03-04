Shortest Route
==============

Framework and algorithms for finding optimal/good as-the-crow-flies routes
between a set of points.

Background
----------

This code isn't intended for any realistic production use; rather, it was an
intellectual exercise for me to spend some time looking at a problem space I'd
been aware of for a while, plus it gave me a change-of-pace after spending
several days wrestling with a Linux display driver problem.

Several years ago, my brother had a job where he had to go out to customers in
various locations each day, and he complained that the job list he was given
was very suboptimal in terms of allocating locations that were geographically
close together and thus having a poor meaningful work-time vs travel-time ratio.
At the time, this struck me as something that really should have been a solved
problem.

(Now, his complaints were more about there being a team of workers who had to
go out, and that the jobs weren't sensibly allocated over the team, which is a
more complicated problem than examined here, but let that pass for now :-)

For this code, I've distilled the problem down as follows:

1. There are a number of locations that must be visited once, with the
   exception of an origin point which must be returned to at the end.
2. The locations can be visited in any order, other than the origin being both
   the start and end of the journey.
3. We want to minimize the distance travelled between points, although a
   reasonably optimal (say within 5-10%?) journey is acceptable rather than
   mandating that the most absolutely efficient journey must be calculated,
   especially if the former can be computed much more quickly/efficiently than
   the latter.
4. Travel between all points is as-the-crow-flies - which is unrealistic from a
   real-world point-of-view, but makes this problem much more compact

I'm sure there's already a fair body of academic research, existing algorithms
for this sort of problem in existence, which I haven't looked at, and so all
this is just re-inventing the wheel.  That's fine though, it's an exercise to
satisfy my own curiousity and exercise my brain, rather than an attempt to
pioneer new ground.


Implementation
--------------

I'm less interested in writing perfect implementations of any particular
algorithm than I am in seeing how various approaches to solving the problem
balance the quality of the result versus resource taken.

A basic framework providing useful classes and helper functions are in
point.py, pointset.py and basesolver.py, so just implementing a solve method
for a class inheriting from BaseSolver should be sufficient.

That said, one of the top things on my TODO list is to build an instrumented
variant of the brute force solver, which will make it easier to determine the
efficiency and effectiveness of more normal algorithms.


