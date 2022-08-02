import tkinter
from tkinter import messagebox


# 定义一个问题类
class Questionnaire(object):
    def __init__(self):
        self.d = {}

    # 传入的分别是问题、选择的选项和选择的内容
    def add_question(self, question, question_lst, answer):
        k = question_lst[answer][-1]
        # 判断是否存在该键 如果没有则创建该键值
        if not self.d.get(question):
            self.d[question] = {k: 1}
        else:
            # 如果问题已经存在提交结果 则判断选项是否存在，有则+1，无责新建1
            if not self.d[question].get(k):
                self.d[question][k] = 1
            else:
                self.d[question][k] += 1

    # 如果没有数据返回 真
    def is_empty(self):
        if not len(self.d):
            return True


# 执行提交问卷
def add_question():
    # 必须都选择了 才能判定
    if question1_answer.get() in range(len(question1_list)) and question2_answer.get() in range(len(question2_list)):
        # 添加选择的问题和选项传入类
        q.add_question(question1_title.get(), question1_list, question1_answer.get())
        q.add_question(question2_title.get(), question2_list, question2_answer.get())
        messagebox.showinfo(title='Submit feedback', message='Submitted successfully！')
    else:
        messagebox.showwarning(title='error warning', message='All must be done to submit！')


# 执行显示结果
def show_question():
    # 判定是否有数据
    if not q.is_empty():
        msg = ''
        for question, answers in q.d.items():
            msg += f'{question}\n'
            for k, v in answers.items():
                msg += f'{k}:{v}\n'
        messagebox.showinfo(title='show result', message=msg)
    else:
        messagebox.showwarning(title='error warning', message='Please submit the questionnaire first!')


# 主窗口基本信息
root = tkinter.Tk()
root.title('Survey')
width, height = 300, 400
width_max, height_max = root.maxsize()
s_center = '%dx%d+%d+%d' % (width, height, (width_max - width) / 2, (height_max - height) / 2)
root.geometry(s_center)
root.resizable(width=True, height=True)

leng = 0

# question 1
question1_title = tkinter.StringVar()
question1_title.set('1.Which action has the greatest impact on reducing threat of global warming ？')
tkinter.Label(root, textvariable=question1_title).grid(row=leng, column=1, sticky=tkinter.W)
leng += 1

question1_answer = tkinter.IntVar()
question1_list = [(0, 'recycling'), (1, 'reducing energy use '), (2, 'composting '), (3, 'planting trees'), (4, 'IDK')]
for index, name in question1_list:
    tkinter.Radiobutton(root, text=name, variable=question1_answer, value=index).grid(row=leng + index, column=1,
                                                                                      sticky=tkinter.W)
leng += 5

# 问卷二
question2_title = tkinter.StringVar()
question2_title.set('2.There are many different kinds of animals and plants, and they lives in many different types '
                    'of environment. what words is used to describe this idea ？')
tkinter.Label(root, textvariable=question2_title).grid(row=leng, column=1, sticky=tkinter.W)
leng += 1

question2_list = [(0, 'multiplicity '), (1, 'biodiversity'), (2, 'soc io-economics'), (3, 'evolution'), (4, 'IDK')]
question2_answer = tkinter.IntVar()
for index, adr in question2_list:
    tkinter.Radiobutton(root, text=adr, variable=question2_answer, value=index).grid(row=index + leng, column=1,
                                                                                     sticky=tkinter.W)
leng += 5

question3_title = tkinter.StringVar()
question3_title.set('3.The primary environmental benefit of wetland is？')
tkinter.Label(root, textvariable=question3_title).grid(row=leng, column=1, sticky=tkinter.W)
leng += 1

question3_list = [(0, 'a place to grow wild rice '), (1, 'a hide our for ducks'), (2, 'clean drinking water'), (3, 'filtering water')]
question3_answer = tkinter.IntVar()
for index, adr in question3_list:
    tkinter.Radiobutton(root, text=adr, variable=question3_answer, value=index).grid(row=index + leng, column=1,
                                                                                     sticky=tkinter.W)
leng += 5

question4_title = tkinter.StringVar()
question4_title.set('4.Have a ozone in the earths upper atmosphere protect us from？')
tkinter.Label(root, textvariable=question4_title).grid(row=leng, column=1, sticky=tkinter.W)
leng += 1

question4_list = [(0, 'alien invasion '), (1, 'harmful, cancer-causing light ray'), (2, 'extremely cold winter'), (3, 'extremely hot summer')]
question4_answer = tkinter.IntVar()
for index, adr in question4_list:
    tkinter.Radiobutton(root, text=adr, variable=question4_answer, value=index).grid(row=index + leng, column=1,
                                                                                     sticky=tkinter.W)
leng += 5

question5_title = tkinter.StringVar()
question5_title.set('5.What is the name of global agency that works to protect the physical earth')
tkinter.Label(root, textvariable=question5_title).grid(row=leng, column=1, sticky=tkinter.W)
leng += 1

question5_list = [(0, 'UNEP '), (1, 'UNESCO'), (2, 'WHO'), (3, 'UNICEF')]
question5_answer = tkinter.IntVar()
for index, adr in question5_list:
    tkinter.Radiobutton(root, text=adr, variable=question5_answer, value=index).grid(row=index + leng, column=1,
                                                                                     sticky=tkinter.W)
leng += 5


q = Questionnaire()

tkinter.Button(root, text='submit', command=add_question).grid(row=leng, column=1)
leng += 1

tkinter.Button(root, text='Check the result', command=show_question).grid(row=leng, column=1)
root.mainloop()
