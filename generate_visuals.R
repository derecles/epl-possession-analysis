require("ggplot2", "dplyr")

# Initialize a dataframe
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
epl_data <- read.csv(file = "epl_data.csv", header = TRUE, sep = ",")

# Get a vector of unique team names
team_names = unique(epl_data$name_home)

# Initialize two empty vectors
all_pp = vector()
all_pe = vector()

# For each team, calculate average possession and average points earned and append to vectors
for (team in team_names) {
  home_avg_pp <- mean(epl_data[epl_data$name_home == team, "pp_home"])
  away_avg_pp <- mean(epl_data[epl_data$name_away == team, "pp_away"])
  home_avg_pe <- mean(epl_data[epl_data$name_home == team, "pe_home"])
  away_avg_pe <- mean(epl_data[epl_data$name_away == team, "pe_away"])
  team_avg_pp <- mean(home_avg_pp, away_avg_pp)
  team_avg_pe <- mean(home_avg_pe, away_avg_pe)
  all_pp <- c(all_pp, team_avg_pp)
  all_pe <- c(all_pe, team_avg_pe)
}

# Display a graph
model <- lm(all_pe ~ all_pp)
plot(all_pp, all_pe, xlab = "Average Possession (%)", ylab = "Average Points")
abline(model, col = "blue")
summary(model)