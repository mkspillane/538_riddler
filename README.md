The riddler on 538 presented the following problem on August 30, 2019 (https://fivethirtyeight.com/features/a-peaceful-but-not-peaceful-transition-of-power-in-riddler-nation/):
"In a distant, war-torn land, there are 10 castles. There are two warlords: you and your archenemy. Each castle has its own strategic value for a would-be conqueror. Specifically, the castles are worth 1, 2, 3, ..., 9, and 10 victory points. You and your enemy each have 100 soldiers to distribute, any way you like, to fight at any of the 10 castles. Whoever sends more soldiers to a given castle conquers that castle and wins its victory points. If you each send the same number of troops, you split the points. You don?t know what distribution of forces your enemy has chosen until the battles begin. Whoever wins the most points wins the war."

In order to find an appropriate strategy I used an iterative strategy to generate progressively better plan.  I started with 1600 troop plans randomly generated where each soldier is sent with equal probability to each castle.  I then followed the following iterative process:
1) All 1600 plans compete in a round robin and their records are recorded

2 a) Half of the next generation of models are taken at random from the current generation with probability equal to their fraction of the total wins with one troop from each castle re-assigned randomly to another castle with probability equal to fraction of troops sent to each castle.

2 b) The other half are hold overs of the top 80 from each of the previous 10 generations.
3) Repeat 15 times.

I found in testing that if too many rounds were completed the plans overfit to self competition.  This was the reason for adding step 2b, but I found that even with this the overfitting still occurred.  The final model submitted was an average of the top 100 plans of the final generation.  The submitted plan would beat the winners from previous rounds of this completion in Feb and May 2017 as well as May 2019.  However, whether it will do better than those strategies against all submitted strategies is yet to be determined.
