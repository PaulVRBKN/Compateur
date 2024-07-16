from tkinter import filedialog
import tkinter as tk
import pandas as pd
import os

def detect_e(input_string):
  """
  Detects the presence of the letter "E" in a string using the 'in' operator.

  Args:
      input_string: The string to check for "E".

  Returns:
      True if "E" is found in the string, False otherwise.
  """

  return "E" in input_string.upper()  # Case-insensitive check

def get_float_from_scientific(text):
  """
  Extracts the float value from a string in scientific notation.

  Args:
      text: The string in scientific notation (e.g., "1.25000E-004").

  Returns:
      The extracted float value, or None if the conversion fails.
  """

  try:
    # Split the string at 'E' to separate the mantissa and exponent
    parts = text.split('E')

    # Convert the mantissa and exponent to floats
    mantissa = float(parts[0])
    exponent = float(parts[1])

    # Calculate the final value by multiplying the mantissa by 10 raised to the power of the exponent
    final_value = mantissa * (10**exponent)
    return final_value
  except (ValueError, IndexError):
    # Handle potential errors during conversion or incorrect format
    return None

def on_button_click():
   """
   This function is called when the button is clicked.
   It opens a file dialog, asks the user to select a directory,
   and then iterates over the files in that directory.
   """

   # Get the directory path from the user
   directory_path = tk.filedialog.askdirectory()
   
   Correlation_x = [[] for i in range(25)]
   Correlation_y = [[] for i in range(25)]
   CountRate_x = [[] for i in range(25)]
   CountRate_y = [[] for i in range(25)]
   Angle = [12,14,16,18,20,22,24,26,28,30,35,40,45,50,55,60,70,80,90,100,110,120,130,140,150]
   i = 0
   
   # Check if a directory was actually selected
   if directory_path:
       # Iterate over files in the selected directory
       for filename in os.listdir(directory_path):
           # Construct the full file path
           full_path = os.path.join(directory_path, filename)
           with open(full_path, "r") as f:
               temp = [line.strip() for line in f]
               angle = temp[19]
               parts = angle.split()
               angle = float(parts[3])
               
               is_correlation_section = True
               temp_cor_x = []
               temp_cor_y = []
               temp_count_x = []
               temp_count_y = []
               
               for j in range(26,len(temp)):
                  temp[j] = temp[j].strip()
                  
                  if not temp[j].startswith('"'):
                      if temp[j] !="":
                          if is_correlation_section:
                              # Correlation section
                              values = temp[j].split()
                              if detect_e(values[0]):
                                  temp_cor_x.append(get_float_from_scientific(values[0]))
                              else :
                                  temp_cor_x.append(float(values[0]))
                                  
                              if detect_e(values[1]):
                                  temp_cor_y.append(get_float_from_scientific(values[1]))
                              else :
                                   temp_cor_y.append(float(values[1]))
                          else:
                              # Count Rate section
                              values = temp[j].split()
                              if detect_e(values[0]):
                                  temp_count_x.append((values[0]))
                              else :
                                  temp_count_x.append(float(values[0]))
                                  
                              if detect_e(values[1]):
                                  temp_count_y.append(get_float_from_scientific(values[1]))
                              else :
                                 temp_count_y.append(float(values[1]))

                  # Switch to the other section when encountering the next section header
                  if temp[j] == '"Count Rate"':
                        is_correlation_section = not is_correlation_section
                    
               Correlation_x[i] = temp_cor_x
               Correlation_y[i] = temp_cor_y
               CountRate_x[i] = temp_count_x
               CountRate_y[i] = temp_count_y

           i +=1
       df_Correlation = pd.DataFrame({'X' : Correlation_x[0],
                                   'Angle_12' : Correlation_y[0],
                                   'Angle_14' : Correlation_y[1],
                                   'Angle_16' : Correlation_y[2],
                                   'Angle_18' : Correlation_y[3],
                                   'Angle_20' : Correlation_y[4],
                                   'Angle_22' : Correlation_y[5],
                                   'Angle_24' : Correlation_y[6],
                                   'Angle_26' : Correlation_y[7],
                                   'Angle_28' : Correlation_y[8],
                                   'Angle_30' : Correlation_y[9],
                                   'Angle_35' : Correlation_y[10],
                                   'Angle_40' : Correlation_y[11],
                                   'Angle_45' : Correlation_y[12],
                                   'Angle_50' : Correlation_y[13],
                                   'Angle_55' : Correlation_y[14],
                                   'Angle_60' : Correlation_y[15],
                                   'Angle_70' : Correlation_y[16],
                                   'Angle_80' : Correlation_y[17],
                                   'Angle_90' : Correlation_y[18],
                                   'Angle_100' : Correlation_y[19],
                                   'Angle_110' : Correlation_y[20],
                                   'Angle_120' : Correlation_y[21],
                                   'Angle_130' : Correlation_y[22],
                                   'Angle_140' : Correlation_y[23],
                                   'Angle_150' : Correlation_y[24]
        })
       df_CountsRate = pd.DataFrame({'X' : CountRate_x[0],
                                   'Angle_12' : CountRate_y[0],
                                   'Angle_14' : CountRate_y[1],
                                   'Angle_16' : CountRate_y[2],
                                   'Angle_18' : CountRate_y[3],
                                   'Angle_20' : CountRate_y[4],
                                   'Angle_22' : CountRate_y[5],
                                   'Angle_24' : CountRate_y[6],
                                   'Angle_26' : CountRate_y[7],
                                   'Angle_28' : CountRate_y[8],
                                   'Angle_30' : CountRate_y[9],
                                   'Angle_35' : CountRate_y[10],
                                   'Angle_40' : CountRate_y[11],
                                   'Angle_45' : CountRate_y[12],
                                   'Angle_50' : CountRate_y[13],
                                   'Angle_55' : CountRate_y[14],
                                   'Angle_60' : CountRate_y[15],
                                   'Angle_70' : CountRate_y[16],
                                   'Angle_80' : CountRate_y[17],
                                   'Angle_90' : CountRate_y[18],
                                   'Angle_100' : CountRate_y[19],
                                   'Angle_110' : CountRate_y[20],
                                   'Angle_120' : CountRate_y[21],
                                   'Angle_130' : CountRate_y[22],
                                   'Angle_140' : CountRate_y[23],
                                   'Angle_150' : CountRate_y[24]
        })
           
       df_Correlation.to_csv('Correlation.csv', sep='\t')
       df_CountsRate.to_csv('CountsRate.csv', sep='\t')
    

# # # Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Compacteur")
fenetre.geometry('600x600')

# # # Création d'un bouton
bouton = tk.Button(fenetre, text="Compacter", command=on_button_click)

# # # Affichage du bouton
bouton.pack()
fenetre.mainloop()
