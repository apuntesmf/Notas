import sqlite3
import datetime
import tkinter as tk
import os
from fpdf import FPDF
fecha = datetime.datetime.now()
fecha=str(fecha.strftime("%x"))

def cargar_med(componente,mg,mg2,ml,m1,m2,m3,ds,ds2):
    lista = [componente]
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    sal=componente
    cursor.execute("""SELECT * FROM medicamentos WHERE sal=?""",(sal,))
    prueba = cursor.fetchall()[0]
    for x in prueba:
        lista.append(x)
    conexion.close()
    mgl = lista[3]
    mg2l= lista[4]
    mll = lista[5]
    dosis = lista[6]
    m1.delete("0", 'end')
    m2.delete("0", 'end')
    m3.delete("0", 'end')
    ds.delete("0", 'end')
    mg.insert("0",mgl)
    mg2.insert("0",mg2l)
    ml.insert("0",mll)
    ds2.insert("0",dosis)
    print(mgl)
    print(mg2l)
    print(mll)

def receta(m,var_h, var_dosis, var_peso, var_mg, var_ml, var_check, var_medicamento,var_dias):
    horas = var_h 
    dosis=var_dosis
    peso=var_peso
    mg=var_mg
    ml=var_ml
    check = var_check
    medicamento = var_medicamento
    dias=var_dias
    print(dosis)
    print(peso)
    print(mg)
    print(ml)
    if check == 0:
        resultado = round((peso * dosis * ml) / mg, 2)
        m.insert('1.0', medicamento + ' '+str(mg)+' mg/' + str(ml)+ ' ml '+ 'tomar  '+ str(resultado)+ ' ml cada '+horas+ ' por ' + str(dias)+' días. ')
    else:
        if horas == "6":
            a = round(((dosis*peso*ml)/mg)/4, 1)
            
            m.insert('end', medicamento + ' '+str(mg)+' mg/' + str(ml)+ ' ml '+' tomar  '+str(a)+ ' ml cada '+horas+ ' por ' + str(dias)+' días. ' )
            print(a)
        elif horas == "8":
            a = round(((dosis*peso*ml)/mg)/3,1)
            
            m.insert('end', medicamento + ' '+str(mg)+' mg/' + str(ml)+ ' ml '+' tomar  '+str(a)+ ' ml cada '+horas+ ' por ' + str(dias)+' días. ')
            print(a)
        elif horas == "12":
            a = round(((dosis*peso*ml)/mg)/2,1)
            m.insert('end', medicamento + ' '+str(mg)+' mg/' + str(ml)+ ' ml '+' tomar  '+str(a)+ ' ml cada '+horas+ ' por ' + str(dias)+' días. ')
            print(a)
        else:
            a = round(((dosis*peso*ml)/mg),1)
            m.insert('end', medicamento + ' '+str(mg)+' mg /' + str(ml)+ ' ml '+' tomar  '+str(a)+ ' ml cada '+horas+ ' por ' + str(dias)+' días. ')
            print(a)

def gen_receta(medico,paterno,materno,nombre,dnacimiento,mnacimiento,anacimiento,edad,manejo):
    try:
        var_medico = medico
        conexion = sqlite3.connect('notas.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM medico WHERE nombre=? ",(var_medico,))
        var_receta=cursor.fetchone()
        print(var_receta)
        pdf = FPDF()
        paciente_nombre=paterno +" "+ materno +" "+ nombre
        var_nacimiento= dnacimiento+"/"+mnacimiento+"/"+anacimiento
        cedula = var_receta[2]
        cedula_esp = var_receta[3]
        fecha = datetime.datetime.now()
        medico = var_receta[1]
        #folio = 0
        pdf.add_page()

        pdf.set_font("Arial", size=10)
        pdf.set_xy(10,20)
        pdf.multi_cell(200,5,txt = "Dr."+medico+ "\nMedico Familiar\nXochicalco/UABC\n" +str(cedula)+"/"+str(cedula_esp),align = 'L')
        pdf.image('recursos/Picture1.png', x=135,y=0, w=31, h=20)
        pdf.set_xy(50,20)
        pdf.multi_cell(200,5,txt = "Av. Reforma #1000 y calle B, Telefono(686)552-2300\ncolonia Primera seccion, Mexicali, Baja California, C.p. 2110", align = 'C')

        pdf.set_xy(10,50)
        pdf.cell(100,10,txt="Nombre: "+paciente_nombre,align="L")

        pdf.set_xy(90,50)
        pdf.cell(100,10,txt="Edad: " +edad,align="L",)
        pdf.set_xy(110,50)
        pdf.cell(110,10,txt="f.Nacimiento: " + var_nacimiento,align="L")
        pdf.set_xy(165,50)
        pdf.cell(110,10,txt="Fecha: "+fecha.strftime("%x"),align="L")

        pdf.image('recursos/Picture2.png', x=135,y=50)
        pdf.set_xy(10,80)
        pdf.multi_cell(0,5,txt = manejo, align = 'J', border=1)

        pdf.set_xy(10,250)
        pdf.multi_cell(200,5,txt = "FARMACIA\nHISPANO AMERICANO\nReforma #1007-A Colonia Primera Seccion\nTelefono 552-9487", align = 'L')

        pdf.set_xy(60,250)
        pdf.multi_cell(200,5,txt = "Dr."+medico+"\nMedico Familiar\nCed.Prof."+str(cedula)+"/"+str(cedula_esp), align = 'C')

        pdf.output("prueba.pdf")
    except:
        tk.messagebox.showinfo('Error','No se selecciono medico.')

