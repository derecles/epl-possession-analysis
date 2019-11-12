library("ggplot2", "dplyr")

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
  team_avg_pp <- (home_avg_pp + away_avg_pp) / 2
  team_avg_pe <- (home_avg_pe + away_avg_pe) / 2
  all_pp <- c(all_pp, team_avg_pp)
  all_pe <- c(all_pe, team_avg_pe)
}

# Display scatterplot with SLS line
model <- lm(all_pe ~ all_pp)
par(lwd = 2)
plot(all_pp, all_pe, main = "Possession vs. Match Outcomes", xlab = "Average Possession per Match (%)", ylab = "Average Points Earned per Match", xlim = c(40, 60), ylim = c(0, 2.5), col = "blue")
abline(model, col = "red")

# Display equation of SLS line on scatterplot
coeff_grad <- round(coef(model)[2], 4)
coeff_int <- round(coef(model)[1], 2)
eq <- paste0("y = ", abs(coeff_grad), "x ", ifelse(sign(coeff_int) == 1, " + ", " - "), abs(coeff_int))
mtext(eq, side = 3, line = -2)

# Display regression statistics
summary(model)