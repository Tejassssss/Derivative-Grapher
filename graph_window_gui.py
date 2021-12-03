from tkinter import ttk
from tkinter import *
global graph_dict
global current_point
graph_dict = []
current_point = 1
window = Tk()
window.geometry('700x700')

def draw_graph(event):
    global graph_dict
    global current_point
    if not graph_dict:
        graph_dict.append([0,0,event.y])
        print(graph_dict[0])
    elif graph_dict[current_point-1][1] <= event.x - 1:
        graph_dict.append([current_point,event.x,event.y])
        current_point+=1
        print(graph_dict[current_point-1])
        canvas1.create_oval(graph_dict[current_point-2][1],graph_dict[current_point-2][2],graph_dict[current_point-1][1],graph_dict[current_point-1][2],fill='black',width=10)

def graph_derivities():
    global graph_dict
    global current_point
    global first_derivite_points, second_derivite_points
    first_derivite_points = find_derivitives(graph_dict)
    canvas2.create_line(0,87.5,500,87.5,fill='black',width=3)
    canvas3.create_line(0,87.5,500,87.5,fill='black',width=3)
    for i in first_derivite_points:
        canvas2.create_oval(i[1],i[2],i[1],i[2],fill='black',width=5)
    second_derivite_points = find_derivitives(first_derivite_points)
    for i in second_derivite_points:
        canvas3.create_oval(i[1],i[2],i[1],i[2],fill='black',width=5)
    # for i in range(len(first_derivite_points)-1):
    #     canvas2.create_oval(first_derivite_points[i-1][1],first_derivite_points[i-1][2],first_derivite_points[i][1],first_derivite_points[i][2],fill='black',width=5)

def find_derivitives(graph_points):
    derivitives_dict = []
    for i in graph_points:
        if i[0] != 0 and i[0] != len(graph_points)-1:
            derivitives_dict.append([i[0],i[1],((graph_points[i[0]+1][2] - graph_points[i[0]-1][2])/(graph_points[i[0]+1][1] - graph_points[i[0]-1][1])*30 + 87.5)])
            #derivitives_dict.append([i[0],i[1],((graph_points[i[0]+1][2] - graph_points[i[0]-1][2])/(graph_points[i[0]+1][1] - graph_points[i[0]-1][1])*30 + 87.5)])

    return derivitives_dict

canvas1 = Canvas(window, width=500, height=175, background='white')
canvas1.place(relx=0.5,rely=0.05,anchor='n')
og_label = Label(window, text='Original Graph')
og_label.place(relx=0.14,rely=0.05,anchor='sw')

canvas2 = Canvas(window, width=500, height=175, background='white')
canvas2.place(relx=0.5,rely=0.5,anchor='center')
first_label = Label(window, text='First Derivitive')
first_label.place(relx=0.14,y=262.5, anchor='sw')

canvas3 = Canvas(window, width=500, height=175, background='white')
canvas3.place(relx=0.5,rely=0.95,anchor='s')
first_label = Label(window, text='Second Derivitive')
first_label.place(relx=0.14,y=437.5, anchor='nw')

canvas1.bind('<Motion>',draw_graph)

derivities_button = Button(window, text='Find Derivites', command=graph_derivities)
derivities_button.place(relx=0.5,rely=0,anchor='n')

window.mainloop()