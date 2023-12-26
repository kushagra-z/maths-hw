from fractions import Fraction
import tkinter as tk
from tkinter import ttk

fb = {'cons': 71, 'mark': 65, "name":"FaceBook"}
yt = {'cons': 51, 'mark': 35, 'name': "YouTube"}
ig = {'cons': 49, 'mark': 59, 'name': "Instagram"}
tt = {'cons': 38, 'mark': 39, 'name': "TikTok"}
sc = {'cons': 19, 'mark': 9, 'name': "Snapchat"}



indPop = 1420000000
usaPop = 331900000


def consInd(percentage):
  return percentage / 100 * indPop


def consUSA(percentage):
  return percentage / 100 * usaPop


def markInd(percentage):
  return percentage / 100 * indPop


def markUSA(percentage):
  return percentage / 100 * usaPop


def print_method_cosumers(sm):
    print(f"Consumer for {sm.get('name')} in India are",     
    consInd(sm.get("cons")), "and in USA are",     
    consUSA(sm.get("cons")))

def simplest_ratio(sm):
    a = consInd(sm.get("cons"))
    b = consUSA(sm.get("cons"))
    value = a/b
    z = Fraction(value).limit_denominator()
    return(z)


def simplest_ratio_m(sm):
    a = consInd(sm.get("mark"))
    b = consUSA(sm.get("mark"))
    value = a/b
    z = Fraction(value).limit_denominator()
    return(z)


def final_data(sm):
   
   a = consInd(sm.get("cons")); b = consUSA(sm.get("cons")); c = float(a) , ":" , float(b)
   value = sm.get("name"), sm.get("cons"), consInd(sm.get("cons")), consUSA(sm.get("cons")), c ,simplest_ratio(sm) 
   
   return value

def final_data_m(sm):
   
   a = consInd(sm.get("mark")); b = consUSA(sm.get("mark")); c = float(a) , ":" , float(b)
   value = sm.get("name"), sm.get("mark"), consInd(sm.get("mark")), consUSA(sm.get("mark")), c ,simplest_ratio_m(sm) 
   
   return value

print(simplest_ratio(ig))






class Table:
   # window
  window = tk.Tk()
  window.geometry('1200x800')
  window.title('Maths Holiday HomeWork')

  # data 
  sm_names = ["FaceBook", "Consumer in %", "Consumers in India", "Consumer in USA", "Ratio", "Ratio(Simplest)"]

  # treeview 
  table = ttk.Treeview(window, columns = ('scmd', 'cons', 'cons_ind', "cons_usa", "ratio", "ratio_simple"), show = 'headings')
  table.heading('scmd', text = 'Social Media')
  table.heading('cons', text = 'Consumer in %')
  table.heading('cons_ind', text = 'Consumer in India')
  table.heading('cons_usa', text="Consumer in USA")
  table.heading('ratio', text='Ratio(in to usa)')
  table.heading("ratio_simple", text="Ratio in Simplest form")
  table.pack(fill = 'both', expand = True)

  # insert values into a table
  # table.insert(parent = '', index = 0, values = ('John', 'Doe', 'JohnDoe@email.com'))

  table.insert(index=0, values=(final_data(sc)), parent='' )
  table.insert(index=0, values=(final_data(tt)), parent='' )
  table.insert(index=0, values=(final_data(ig)), parent='' )
  table.insert(index=0, values=(final_data(yt)), parent='' )
  table.insert(index=0, values=(final_data(fb)), parent='' )


  table.insert(parent = '', index = tk.END, values = ('**********' * 6,'**********' * 6,'**********' * 6,'**********' * 6,'**********' * 6,'**********' * 6, ))

  table = ttk.Treeview(window, columns = ('scmd', 'cons', 'cons_ind', "cons_usa", "ratio", "ratio_simple"), show = 'headings')
  table.heading('scmd', text = 'Social Media')
  table.heading('cons', text = 'Marketers in %')
  table.heading('cons_ind', text = 'Marketers in India')
  table.heading('cons_usa', text="Marketers in USA")
  table.heading('ratio', text='Ratio(in to usa)')
  table.heading("ratio_simple", text="Ratio in Simplest form")
  table.pack(fill = 'both', expand = True)

  table.insert(index=0, values=(final_data_m(sc)), parent='' )
  table.insert(index=0, values=(final_data_m(tt)), parent='' )
  table.insert(index=0, values=(final_data_m(ig)), parent='' )
  table.insert(index=0, values=(final_data_m(yt)), parent='' )
  table.insert(index=0, values=(final_data_m(fb)), parent='' )



  # events
  def item_select(_):
    print(table.selection())
    for i in table.selection():
      print(table.item(i)['values'])
    # table.item(table.selection())

  def delete_items(_):
    print('delete')
    for i in table.selection():
      table.delete(i)

  table.bind('<<TreeviewSelect>>', item_select)
  table.bind('<Delete>', delete_items)

  # run 
  window.mainloop()
   
   