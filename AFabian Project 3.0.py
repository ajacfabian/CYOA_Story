import tkinter as tk
from tkinter import *

LARGE_FONT= ("Arial", 16)

class CYOA(tk.Tk):
    def __init__(self):
        
        tk.Tk.__init__(self)
        container = tk.Frame(self)

        container.pack(side='top', fill='both', expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (IntroPage, Left, Friend, Market, Right, Caves, Valley, Flowers, Home2, Store, Keep, DayJob, Paid, Bank, Rabbits, Guild2,
                  Bar, House1, House2, House3, Move_In1, Move_In2, Move_In3, Bank2, Round, Alone, Fight, Jail, Peace, Guild, Right2, Valley2,
                  Cave_Split, Cave_Right, Cave_Left):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_frame(IntroPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
class IntroPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text = 'You are at your house', font = LARGE_FONT)
        text = tk.Label(self, text = 'It is the early 1900s, and you live in a small rural village. The nearest town is a good hour\'s walk away. \n'
                        'You finally have two days off from your job at the local cobbler, so you decide to go for a walk as a way to pass the time. \n\n'
                        'You leave your house and head to the main road. You can go right or left, which way do you go?')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button = tk.Button(self, text = 'Go Left', command = lambda: controller.show_frame(Left))
        button.pack()

        button2 = tk.Button(self, text = 'Go Right', command = lambda: controller.show_frame(Right))
        button2.pack()

class Left(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You went to the left on the main road', font = LARGE_FONT)
        text = tk.Label(self, text = 'You follow the road and eventually find yourself in the next town over. \n'
                        'It is slightly larger than yours, so the general store has an improved selection compared to the one in your village. \n'
                        'You also recall that one of your former classmates lives in this town, so you could always visit them for a while to catch up. \n\n'
                        'You can head to your friend\'s house, the general store, or home.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Go to your friend\'s house', command = lambda: controller.show_frame(Friend))
        button1.pack()

        button2 = tk.Button(self, text = 'Go to the general store', command = lambda: controller.show_frame(Market))
        button2.pack()

        button3 = tk.Button(self, text = 'Head back home', command = lambda: controller.show_frame(Home2))
        button3.pack()

class Friend(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You went to your friend\'s house', font = LARGE_FONT)
        text = tk.Label(self, text = 'Your friend greets you happily, it has been a while since you visited them. \n'
                        'You spend the day catching up and meet their family, and at night they cook a delicious meal where you eat too much. \n\n'
                        'You stay at their house for the night and head back to your house to clean up and get ready for the day')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Go home', command = lambda: controller.show_frame(Home2))
        button1.pack()

class Market(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You went to the general store', font = LARGE_FONT)
        text = tk.Label(self, text = 'You see many things in this general store that you can\'t find in the one in your village. \n'
                        'You load up with supplies, happy to have found some goods that you haven\'t found in your town in a long while. \n\n'
                        'Do you go visit your friend in this town or head home?')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Visit your friend', command = lambda: controller.show_frame(Friend))
        button1.pack()

        button2 = tk.Button(self, text = 'Head home', command = lambda: controller.show_frame(Home2))
        button2.pack()

class Right(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You went to the right on the main road', font = LARGE_FONT)
        text = tk.Label(self, text = 'You follow the road, which leads you to some mountainous terrrain. \n'
                        'You recall warnings about dangerous animals in the area, but you consider yourself a skilled outdoorsman so you feel safe. \n\n'
                        'You can head home (better safe than sorry), to the nearby caves, or a valley with lots of greenery. Which way will you go?')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Head back home', command = lambda: controller.show_frame(IntroPage))
        button1.pack()

        button2 = tk.Button(self, text = 'Go to the caves', command = lambda: controller.show_frame(Caves))
        button2.pack()

        button3 = tk.Button(self, text = 'Go to the valley', command = lambda: controller.show_frame(Valley))
        button3.pack()

class Caves(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You went to the caves', font = LARGE_FONT)
        text = tk.Label(self, text = 'These remind you of the caves you used to play in as a child with your friends, how nostalgic. \n'
                        'Mothers have been warning their children for years about the possibility of bears, but you played in caves \n'
                        'just like these before with no repercussions in the past. \n\n'
                        'Do you heed the warning now that you\'re older and wiser, or do you enter the caves for a bit of spelunking?')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Heed the warning', command = lambda: controller.show_frame(Right))
        button1.pack()

        button2 = tk.Button(self, text = 'Enter the caves', command = lambda: controller.show_frame(Cave_Split))
        button2.pack()

class Cave_Split(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You went into the caves', font = LARGE_FONT)
        text = tk.Label(self, text = 'You enter the caves, ignoring the warnings of your mother and your friends\' mothers. \n'
                        'These look like typical caves you find in this region, so you think nothing of exploring them for a bit. \n\n'
                        'You come across a branching path in the cave, do you go right or left?')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Right', command = lambda: controller.show_frame(Cave_Right))
        button1.pack()

        button2 = tk.Button(self, text = 'Left', command = lambda: controller.show_frame(Cave_Left))
        button2.pack()

class Cave_Right(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You chose the right split', font = LARGE_FONT)
        text = tk.Label(self, text = 'You continue exploring the cave for a while, forgetting about the left path you could have chosen. \n\n'
                        'You decide to leave the caves and head back home, as you\'ve gotten dirty from spelunking all day.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Head home', command = lambda: controller.show_frame(Home2))
        button1.pack()

class Cave_Left(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You chose the left split', font = LARGE_FONT)
        text = tk.Label(self, text = 'You explore the cave and see an exit you didn\' know about. You follow the path and come across a \n'
                        'large furry mass. Startled, you trip and fall onto your face. Unfortunately for you, this knocks some rocks loose \n'
                        'which wakes the bear. The bear is upset that you woke it up and attacks you. As you get attacked, you realise that \n'
                        'you should have listened to the warnings. Unfortunately, you do not survive the attack.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Play again?', command = lambda: controller.show_frame(IntroPage))
        button1.pack()

        button2 = tk.Button(self, text = 'Quit', command = lambda: controller.destroy())
        button2.pack()

class Valley(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You went to the valley', font = LARGE_FONT)
        text = tk.Label(self, text = 'You enter a beautiful valley with many plants and a small stream flowing in the centre. \n'
                        'You recognise some of the plants as you explore the valley, and decide to spend some time exploring it. \n\n'
                        'You can leave the valley, admire the flowers, or collect some herbs you found prior to going home.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Leave the valley', command = lambda: controller.show_frame(Right))
        button1.pack()

        button2 = tk.Button(self, text = 'Admire the flowers', command = lambda: controller.show_frame(Flowers))
        button2.pack()

        button3 = tk.Button(self, text = 'Collect herbs', command = lambda: controller.show_frame(Store))
        button3.pack()

class Store(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You went to the general store to sell your herbs', font = LARGE_FONT)
        text = tk.Label(self, text = 'Seeing as you have some herbs that you don\'t need, you go to the general store in your \n'
                        'town to sell them to make medicine and other herbal remedies. They pay you a decent amount, which is much appreciated. \n\n'
                        'You then head home and get some sleep, as you\'ve been out and about all day.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'The next day', command = lambda: controller.show_frame(Home2))
        button1.pack()

class Flowers(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You admired the flowers', font = LARGE_FONT)
        text = tk.Label(self, text = 'You admired the flowers around the stream, and decided to bring your friends here when you all have time off. \n'
                        'After some time exploring the valley, you gather some loose wood to act as fuel for your stove and head home.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'The next day', command = lambda: controller.show_frame(Home2))
        button1.pack()

class Home2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You went back home', font = LARGE_FONT)
        text = tk.Label(self, text = 'You start your second day off refreshed after a good night\'s sleep and eat a hearty breakfast. As the day \n'
                        'is just beginning, you decide to occupy yourself. \n\n'
                        'You can either find someone who needs help around the village, or go to the general store to see if they have jobs to do.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Help around the village', command = lambda: controller.show_frame(DayJob))
        button1.pack()

        button2 = tk.Button(self, text = 'Go to the general store', command = lambda: controller.show_frame(Guild))
        button2.pack()

class DayJob(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You went to find a day job', font = LARGE_FONT)
        text = tk.Label(self, text = 'As you thought would happen, you don\'t need to look around long to find someone who could use a spare hand. \n'
                        'Your neighbour a few doors down could use some help building the walls of their new barn. You decide to assist them, and \n'
                        'when the work is finished almost half the day has passed. Kindly, they decide to pay you for your work.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Get Paid', command = lambda: controller.show_frame(Paid))
        button1.pack()

class Paid(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You got paid, huzzah!', font = LARGE_FONT)
        text = tk.Label(self, text = 'You have a fair bit of money from your activities, so you decide to do something with it. \n\n'
                        'Do you go to the bank to deposit the money in your account or to the village bar to relax a bit.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'To the bank', command = lambda: controller.show_frame(Bank))
        button1.pack()

        button2 = tk.Button(self, text = 'To the bar', command = lambda: controller.show_frame(Bar))
        button2.pack()

class Bank(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You went to the Bank', font = LARGE_FONT)
        text = tk.Label(self, text = 'You deposit your money and become aware that you have saved up a decent amount of money from your work. \n'
                        'You think about what you really need, and the first thing that pops into your head is a new house. The one you currently \n'
                        'live in is a bit on the small side and on the outskirts of your village, and the bank is willing to give you a loan. \n\n'
                        'The bank has 3 houses for sale that are close to what you are looking for.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Look at the first house', command = lambda: controller.show_frame(House1))
        button1.pack()

        button2 = tk.Button(self, text = 'Look at the second house', command = lambda: controller.show_frame(House2))
        button2.pack()

        button3 = tk.Button(self, text = 'Look at the third house', command = lambda: controller.show_frame(House3))
        button3.pack()

class Bank2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You went to the Bank', font = LARGE_FONT)
        text = tk.Label(self, text = 'You deposit your money and become aware that you have saved up a decent amount of money from your work. \n'
                        'You think about what you really need, and the first thing that pops into your head is a new house. The one you currently \n'
                        'live in is a bit on the small side and on the outskirts of your village, and the bank is willing to give you a loan. \n\n'
                        'The bank has 3 houses for sale that are close to what you are looking for.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Look at the first house', command = lambda: controller.show_frame(House1))
        button1.pack()

        button2 = tk.Button(self, text = 'Look at the second house', command = lambda: controller.show_frame(House2))
        button2.pack()

        button3 = tk.Button(self, text = 'Look at the third house', command = lambda: controller.show_frame(House3))
        button3.pack()

        button4 = tk.Button(self, text = 'Keep what you have', command = lambda: controller.show_frame(Keep))
        button4.pack()

class Keep(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You decide to not buy a new house', font = LARGE_FONT)
        text = tk.Label(self, text = 'The houses that you\'ve seen look good, but you don\'t think it worth it to sell your current house \n'
                        'and buy a new one. You don\'t regret not buying one of the other houses, as your account in the bank is ready for \n'
                        'any unforseen expenses you may have. You go back to your house and go to bed early as you have work tomorrow.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Restart', command = lambda: controller.show_frame(IntroPage))
        button1.pack()

        button2 = tk.Button(self, text = 'Quit', command = lambda: controller.destroy())
        button2.pack()

class House1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You visit the first house', font = LARGE_FONT)
        text = tk.Label(self, text = 'The first house is similarly sized to the one you currently live in, however it is much closer \n'
                        'to the centre of the village, meaning your trips to the general store and work will be shorter. While a bit \n'
                        'on the small side, the proximity to centre of the village is worth not buying a bigger house and the price \n'
                        'is reasonable too. \n\n'
                        'You could buy this house, or you could go back to the bank to look at the other houses they have.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Buy the house', command = lambda: controller.show_frame(Move_In1))
        button1.pack()

        button2 = tk.Button(self, text = 'Back to the Bank', command = lambda: controller.show_frame(Bank2))
        button2.pack()

class House2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You visit the second house', font = LARGE_FONT)
        text = tk.Label(self, text = 'The second house is much larger than the one you currently own, however it is painted in a \n'
                        'rather unappealing shade of tan. It is also on the outskirts of the village, similarly to your current \n'
                        'home. The price on this one is decently high, and you expect that if you buy it you\'ll have to work quite \n'
                        'a bit more than you currently do to pay it off in any reasonable amount of time. \n\n'
                        'You could buy this house, or you could go back to the bank to look at the other houses they have.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Buy the house', command = lambda: controller.show_frame(Move_In2))
        button1.pack()

        button2 = tk.Button(self, text = 'Back to the Bank', command = lambda: controller.show_frame(Bank2))
        button2.pack()

class House3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You visit the third house', font = LARGE_FONT)
        text = tk.Label(self, text = 'The third house is the type of house you think you would like. It is larger than your current home \n'
                        'and closer to the centre of the village, however it has been on the market for a while now and is looking a bit \n'
                        'run down, with much work to be done to fix it up to a place where you could see yourself living. Other than that, \n'
                        'it looks good. \n\n'
                        'You could buy this house, or you could go back to the bank to look at the other houses they have.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Buy the house', command = lambda: controller.show_frame(Move_In3))
        button1.pack()

        button2 = tk.Button(self, text = 'Back to the Bank', command = lambda: controller.show_frame(Bank2))
        button2.pack()

class Move_In1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You bought the first house', font = LARGE_FONT)
        text = tk.Label(self, text = 'Although the new house is the same size as your old house, you are happy about your purchase \n'
                        'as you are closer to the centre of the village. You\'ll be able to get to work and the general store much \n'
                        'quicker, and you\'ll see more people. Overall, a solid purchase.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Restart', command = lambda: controller.show_frame(IntroPage))
        button1.pack()

        button2 = tk.Button(self, text = 'Quit', command = lambda: controller.destroy())
        button2.pack()

class Move_In2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You bought the second house', font = LARGE_FONT)
        text = tk.Label(self, text = 'This large house will require a new coat of paint, but you can see yourself living here in \n'
                        'the future with your family, as the large amount of land around the house will be ample to build smaller \n'
                        'houses for your children and their families when they get to that age. The future looks bright.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Restart', command = lambda: controller.show_frame(IntroPage))
        button1.pack()

        button2 = tk.Button(self, text = 'Quit', command = lambda: controller.destroy())
        button2.pack()

class Move_In3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You bought the third house', font = LARGE_FONT)
        text = tk.Label(self, text = 'Although the house is in rough condition, you can get some of the major fixes done in a \n'
                        'few days after work. Within a few weeks, the house looks as though it had always had someone living \n'
                        'in it. Once fixed, the house looks good and you start to have guests over. You becoe friends with your \n'
                        'neighbours and are glad you purchsed this house.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Restart', command = lambda: controller.show_frame(IntroPage))
        button1.pack()

        button2 = tk.Button(self, text = 'Quit', command = lambda: controller.destroy())
        button2.pack()

class Bar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You go to the bar', font = LARGE_FONT)
        text = tk.Label(self, text = 'After your hard day of work, you feel like relaxing a bit at the bar. While this may \n'
                        'not be the most reasonable thing to do, you feel as though you have earned it from you day\'s hard \n'
                        'work. You see some of the regulars, and they greet you. \n\n'
                        'Do you feel generous and buy the bar a round, or do you drink alone at the bar?')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Buy a round', command = lambda: controller.show_frame(Round))
        button1.pack()

        button2 = tk.Button(self, text = 'Drink alone', command = lambda: controller.show_frame(Alone))
        button2.pack()

class Round(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You bought a round for the bar', font = LARGE_FONT)
        text = tk.Label(self, text = 'Everyone thanks you for buying them a round, and you find that one of your friends \n'
                        'is in the bar. You sit with them and talk for a while. Some rowdy drinkers in the corner get animated \n'
                        'and start waving their arms about knocking a beer mug at you and your friend. It splashes on your friend \n'
                        'dousing them in beer. You stand up ready to go knock some sense into them, but your friend tries to \n'
                        'pursuade you to let it go. \n\n'
                        'Do you let your friend pursuade you, or ignore them and punch the one who knocked the beer mug off?')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Be convinced', command = lambda: controller.show_frame(Peace))
        button1.pack()

        button2 = tk.Button(self, text = 'Punch the drunk', command = lambda: controller.show_frame(Fight))
        button2.pack()

class Alone(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You drank alone', font = LARGE_FONT)
        text = tk.Label(self, text = 'Tired after your day\'s labours, you find a seat at the bar and order some drinks. \n'
                        'As the night wears on, your neighbours get drunk and spill their beer on you. \n\n'
                        'Do you punch the drunk or let it go?')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Punch them', command = lambda: controller.show_frame(Fight))
        button1.pack()

        button2 = tk.Button(self, text = 'Let it go', command = lambda: controller.show_frame(Peace))
        button2.pack()

class Fight(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You punch the drunk', font = LARGE_FONT)
        text = tk.Label(self, text = 'Upset that they spilled their beer on you, you punch the drunk. Seeing as you don\'t fight that often, \n'
                        'you don\'t throw a very good punch and get punched back. The drunk\'s friends start to punch you as well, and you get \n'
                        'beaten up. Thankfully someone gets the village policeman to stop the brawl. Unfortunately for you, as you were part of \n'
                        'the brawl you go to the village jail for the night to cool off.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Night in Jail', command = lambda: controller.show_frame(Jail))
        button1.pack()

class Jail(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You spent the night in jail', font = LARGE_FONT)
        text = tk.Label(self, text = 'You wake up with an aching head as you realise you have to get ready for work. You apologise to the policeman \n'
                        'and those you fought last night and make your way home to change into your work clothes.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Restart', command = lambda: controller.show_frame(IntroPage))
        button1.pack()

        button2 = tk.Button(self, text = 'Quit', command = lambda: controller.destroy())
        button2.pack()

class Peace(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You let it go', font = LARGE_FONT)
        text = tk.Label(self, text = 'The drunk apologises for spilling beer on your friend and buys you both a beer to make up for it. Your friend \n'
                        'thanks you for not making a scene, and you both drink more than you perhaps should. You go home late at night and worry about \n'
                        'what state you\'ll be in tomorrow morning. At least your boss isn\'t as strict as your old school teacher, or you\'d be in \n'
                        'trouble coming into work feeling as bad as you do.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Restart', command = lambda: controller.show_frame(IntroPage))
        button1.pack()

        button2 = tk.Button(self, text = 'Quit', command = lambda: controller.destroy())
        button2.pack()

class Guild(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You go to the general store', font = LARGE_FONT)
        text = tk.Label(self, text = 'You ask the clerk if there are any jobs that need doing, and they tell you that the apothecary \n'
                        'could use some herbs from the valley down the road, the bowyer is looking for straight shafts of wood, \n'
                        'and that the village butcher is looking for some rabbits to sell. \n\n'
                        'You can pick one of the three jobs to do.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Hunt rabbits', command = lambda: controller.show_frame(Right2))
        button1.pack()

        button2 = tk.Button(self, text = 'Gather plants', command = lambda: controller.show_frame(Right2))
        button2.pack()

class Right2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You go to a potentially familiar place', font = LARGE_FONT)
        text = tk.Label(self, text = 'You leave the town and go to a place with mountainous terrain that leads to areas with different terrains. \n'
                        'Caves are visible, so you may be able to find some sleeping rabbits there. A valley is located a bit further down the path, which \n'
                        'may have some herbs or shafts of wood that you need. Otherwise you may be able to find trap some rabbits where you currently are. \n\n'
                        'What do you do?')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Look for rabbits', command = lambda: controller.show_frame(Rabbits))
        button1.pack()

        button2 = tk.Button(self, text = 'Go to the caves', command = lambda: controller.show_frame(Caves))
        button2.pack()

        button3 = tk.Button(self, text = 'Go to the valley', command = lambda: controller.show_frame(Valley2))
        button3.pack()

class Valley2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You go to the valley', font = LARGE_FONT)
        text = tk.Label(self, text = 'This is a nice valley, full of plant life and with a stream in the centre. You look around and find some straight pieces \n'
                        'of wood, as well as many herbs. You don\'t find any traces of rabbits however. You can only pick up a certain amount of plant \n'
                        'matter as it is too hard to carry both herbs and straight pieces wood. \n\n'
                        'You can pick some herbs, gather straight pieces of wood, or leave to find rabbits elsewhere.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Herbs', command = lambda: controller.show_frame(Guild2))
        button1.pack()

        button2 = tk.Button(self, text = 'Wood', command = lambda: controller.show_frame(Guild2))
        button2.pack()

        button3 = tk.Button(self, text = 'Back to previous location', command = lambda: controller.show_frame(Right2))
        button3.pack()

class Rabbits(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You hunted rabbits', font = LARGE_FONT)
        text = tk.Label(self, text = 'Considering yourself a decent outdoorsman, you create some simple traps with some of the vegetation found around you. \n'
                        'While you wait for the traps to spring and capture rabbits, you actively try to herd some of them into the traps. \n'
                        'It isn\'t always successful, however you manage to trap a few rabbits. ')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Get rewards', command = lambda: controller.show_frame(Guild2))
        button1.pack()

class Guild2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'You returned to the general store', font = LARGE_FONT)
        text = tk.Label(self, text = 'The general store is happy with what you brought back and thanks you for your help. \n'
                        'They pay you, so you stop working for the day.')
        
        label.pack(pady = 10, padx = 10)
        text.pack(pady = 20, padx = 20)

        button1 = tk.Button(self, text = 'Get Paid', command = lambda: controller.show_frame(Paid))
        button1.pack()

def main():
    Story = CYOA()

main()
