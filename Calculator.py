import tkinter as tk

def buttonClick(num):
    entry.insert(tk.END, num)
def setOperation(op):
    global firstNumber, operation
    firstNumber = entry.get()   # ekrandaki ilk sayıyı al
    operation = op               # işlem türünü kaydet (+)
    entry.delete(0, tk.END)      # ekranı temizle (ikinci sayıya hazırlan)
def calculate():
    global firstNumber, operation
    secondNumber = entry.get()   # ekrandaki ikinci sayıyı al
    if operation == "+":
        result = float(firstNumber) + float(secondNumber)
    elif operation == "-":
        result = float(firstNumber) - float(secondNumber)
    elif operation == "x":
        result = float(firstNumber) * float(secondNumber)
    elif operation == "÷":
        if float(secondNumber) != 0:
            result = float(firstNumber) / float(secondNumber)
        else:
            result = "Error"
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

    btnEquals = tk.Button(root, text="=", command=calculate)
    btnPlus = tk.Button(root, text="+", command=lambda: setOperation("+"))

# Pencere oluştur
root = tk.Tk()
root.title("Hesap Makinesi")  # Pencere başlığı
root.geometry("300x400")      # Pencere boyutu

# Ekran (Entry - kullanıcı işlemleri burada görecek)
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# "1" butonu
btn1 = tk.Button(root, text="1", width=5, height=2, font=("Arial", 14),command=lambda: buttonClick("1"))
btn1.grid(row=1, column=0, padx=2, pady=2)
#"2" butonu
btn2 = tk.Button(root, text="2", width=5, height=2, font=("Arial", 14),command=lambda: buttonClick("2"))
btn2.grid(row=1, column=1, padx=2, pady=2)
#"3" butonu
btn3 = tk.Button(root, text="3", width=5, height=2, font=("Arial", 14),command=lambda: buttonClick("3"))
btn3.grid(row=1, column=2, padx=2, pady=2)
#"4" butonu
btn4 = tk.Button(root, text="4", width=5, height=2, font=("Arial", 14),command=lambda: buttonClick("4"))
btn4.grid(row=2, column=0, padx=2, pady=2)
#"5" butonu
btn5 = tk.Button(root, text="5", width=5, height=2, font=("Arial", 14),command=lambda: buttonClick("5"))
btn5.grid(row=2, column=1, padx=2, pady=2)
#"6" butonu
btn6 = tk.Button(root, text="6", width=5, height=2, font=("Arial", 14),command=lambda: buttonClick("6"))
btn6.grid(row=2, column=2, padx=2, pady=2)
#"7" butonu
btn7 = tk.Button(root, text="7", width=5, height=2, font=("Arial", 14),command=lambda: buttonClick("7"))
btn7.grid(row=3, column=0, padx=2, pady=2)
#"8" butonu
btn8 = tk.Button(root, text="8", width=5, height=2, font=("Arial", 14),command=lambda: buttonClick("8"))
btn8.grid(row=3, column=1, padx=2, pady=2)
#"9" butonu
btn9 = tk.Button(root, text="9", width=5, height=2, font=("Arial", 14),command=lambda: buttonClick("9"))
btn9.grid(row=3, column=2, padx=2, pady=2)
#"0" butonu
btn0 = tk.Button(root, text="0", width=5, height=2, font=("Arial", 14),command=lambda: buttonClick("0"))
btn0.grid(row=4, column=1, padx=2, pady=2)
#"+" butonu
btnPlus = tk.Button(root, text="+",width=5,height=2, font=("Arial",14), command=lambda: setOperation("+"))
btnPlus.grid(row=2, column=3, padx=2, pady=2)
#"-" butonu
btnMinus = tk.Button(root, text="-",width=5,height=2, font=("Arial",14), command=lambda: setOperation("-"))
btnMinus.grid(row=3, column=3, padx=2, pady=2)
#"x" butonu
btnMulti = tk.Button(root, text="x", width=5, height=2, font=("Arial", 14), command=lambda: setOperation("x"))
btnMulti.grid(row=4, column=3, padx=2, pady=2)
#"÷" butonu
btnPart = tk.Button(root, text="÷", width=5, height=2, font=("Arial", 14), command=lambda: setOperation("÷"))
btnPart.grid(row=5, column=3, padx=2, pady=2)

#tamamını silme "C" butonu
def clear():
    entry.delete(0, tk.END)  # 0'dan END'e kadar her şeyi siler

btnClear = tk.Button(root, text="C", width=5, height=2, font=("Arial", 14), command=clear)
btnClear.grid(row=1, column=3, padx=2, pady=2)

#son karakteri silme
def backspace():
    current = entry.get()      # Entry içindeki mevcut yazı
    entry.delete(0, tk.END)    # Tamamını sil
    entry.insert(0, current[:-1])  # Son karakteri çıkarıp geri yaz

btnBack = tk.Button(root, text="⌫", width=5, height=2, font=("Arial", 14), command=backspace)
btnBack.grid(row=4, column=2, padx=2, pady=2)
# Pencereyi sürekli açık tut

#"," karakteri
btnComma = tk.Button(root, text=",",width=5,height=2, font=("Arial",14))
btnComma.grid(row=4, column=0, padx=2, pady=2)
#"=" butonu
btnEquals = tk.Button(root, text="=", width=19, height=2, font=("Arial", 14), command=calculate)
btnEquals.grid(row=5, column=0, columnspan=3, padx=2, pady=2)
root.mainloop()