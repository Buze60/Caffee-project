

 
print("           <>>>>>     <<>>     #**<>   <<**><>   <<**><>  ")
print("           <>        <<<>>>    #**<>   <<**>>    <<**>>     MANU") 
print("           <>>>>>  <>>    <>>  #       <<**><>   <<**><> ")
print("           *****************************************************")
print("           *****************************************************")

                  
def main():
  #initialize the  caffe manu

    manu_list=[]
    choice = 0
    while choice != 5:
      print("...<<<Caffe Manager>>>..")
      print("        1)Add a order ")
      print("        2) Lookup order")
      print("        4) To delete order")
      print("        3) Dispaly order")
      print("        5)Quit")
      choice = int(input("..........plaesa enter the number from 1~5 \n"))
      if choice == 1:
        print("<<<.....Adding a order number...>>>")
        Name_order = (input("write  the order number>>> "))
        name_customer = input("write the name of the customer>>>")
        No_order = int(input("write the amout that>>>"))
        manu_list.append([Name_order, name_customer, No_order])
      elif choice == 2:
        print("***....Lookup order...***")
        keyword = input("<<<...enter saerch term:  ")
        for order in manu_list:
          if keyword in order:
            print(order)
            
      elif choice==3:
        print("***Displaying all custemr order...>>>")
        print("**************************************")
        for i in range(len(manu_list)):
          if manu_list=="":
            print("there is no list....")
          else:
            print(manu_list[i])
          
      elif choice == 4:
        print("...to delete order...>>!")
        del(manu_list)
        
      elif choice == 5:
        print("Quiting...>>>")

    print("programm terminated...>>>")


main()
