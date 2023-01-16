from utils_CeV import data, coins

num = data.read_money("Enter the price: ")
coins.summary(num, 13, 22, True)