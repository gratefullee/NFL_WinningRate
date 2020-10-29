# Factors Affecting NFL Teams' Winning Rates

![Football](/img/NFLball.jpg)

When I was at college in Texas, I went to see so many football games. At first I really didn't understand why Texans LOVE football. But after a couple years, I found myself enjoying football games with them. I believe it is more than just a game for a lot of people. We go to see their friends or family during the Superobowl. Football is another Thanksgiving or Christmas. I am not an expert on football yet, but it is always one of my interests.

Football is another industry by itself. People would like to pay up to $25,000 just for a seat. And NFL teams would like to pay enormous money every year to recruit the best football player. Above all things, what they care about is who is going to win the trophy. In this project, I would like to answer what NFL teams can do to increase their winning rates.

# Data Sources
This project is based on multiple datasets showing -- 
1) all-time teams' winning rates
2) players PT records
3) all-time each players' stats (punt, fumbles, etc.)


# Background Information
Each team has a winning rate ever since the team was founded. The team with the highest winning rate is Dallas Cowboys -- 0.571, and the lowest rate is Tampay Bay Bunccaneers -- 0.389. 
![WinningRate](/img/NFL_WinningRate.png)

# Data Analysis
Very first moment thinking about the winning rate, I expected players' PT records to have a huge import on winning rates. However, once I found the correlations between their PT records and teams' winning rates.
![correlations](/img/PTCorr.png)

While I was analyzing the catching rate for Dallas Cowboys and Tampa Bay Bucs, I made a conclusion that players catching rates can have a high impact on overall team's winning rate. Unfortunately though, catching rate was not recorded until 1992. So I couldn't utilize catching rates to predict the winning rate. 
![catchingrate](/img/bootstrap.png)

I wanted to furthur analyze other factors affecting the winning rates. I found out that completion rate, punt, and fumbles can lead the team to a win or loss. 
![factors](/img/SingleFeature.png)

But which one has a higher impact on another?
While I returned a partial regression on those three factors together, I made a conclusion that the number of fumbles lost and average yards from each punt is more significant than completion rate. This is based on the partial regression rate; 

Average Completion Percentage: 0.005176

Average Number of Fumbles Lost: -0.177058

Average Yards Per Punt Return: 0.014572
![PartialRegression](/img/PartialRegression.png)

Since the graph is not intuitively understandable, I decided to make a 3D graph with factors with the two highest rates.
.
![3DPartialR](/img/3DPartialR.png)