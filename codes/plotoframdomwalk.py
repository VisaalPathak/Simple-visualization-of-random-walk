from randomwalk import RandomWalk
import matplotlib.pyplot as plt

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    point_numbers = range(rw.num_points)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap=plt.cm.Blues, edgecolors='none',  s = 15)
    ax.set_title("A graph of Random walk")
    ax.scatter(0,0, c = 'g',edgecolors='none', s = 100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1], c = 'r', edgecolors='none', s = 100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    ask = input("Want to create another walk?(y/n): ")
    if ask == 'n':
        break
