import sqlite3
import datetime
import random
import csv
import os
import tkinter as tk
import sqlite3
import calculo
from fpdf import FPDF
from tkinter import  ttk, Menu
from tkinter import messagebox as msg
from tkinter.scrolledtext import ScrolledText
from tkinter import Menu
from decimal import Decimal



ven = tk.Tk()
ven.title("pacientes")
ven.geometry('870x870')    
ven.minsize(870,700)
'''
VARIABLES GLOBALES
'''
nombre_archivo = 'listado.csv'
fecha = datetime.datetime.now()
fecha=str(fecha.strftime("%x"))

px=[]
var_pat = tk.StringVar() #crea la variable que asignara el valor de la nota
var_mat = tk.StringVar() #crea la variable que asignara el valor de la nota
var_name = tk.StringVar() #crea la variable que asignara el valor de la nota
var_sal=tk.StringVar()
var_mg=tk.StringVar()
var_mg2=tk.StringVar()
var_ml = tk.StringVar() #crea la variable que asignara el valor de la nota
#conecta a la base de datos y crea el cursor


#Genera la lista de enfermedades para elcombobox
conexion = sqlite3.connect('notas.db')
cursor = conexion.cursor()
cursor.execute("SELECT enfermedad FROM enfermedades ")
dc=[]
for i in cursor:
    dc.append(i)

md=[]
cursor.execute("SELECT nombre FROM Medico ")
for h in cursor:
    md.append(h[0])


cursor.execute("SELECT enfermedad FROM urgencias ")
ux=[]
for y in cursor:
    ux.append(y)

lista_completa=dc+ux

cursor.execute("SELECT sal FROM medicamentos ")
sal=[]
for m in cursor:
    sal.append(m)

cursor.execute("SELECT nombre FROM seguros ")
seguro=[]
for x in cursor:
    seguro.append(x)

conexion.close()

#Funciones de base de datos
def a_enfermedad(txt_neuro2, piel2, cabeza2, cuello2, torax2,abdomen2,genitales2,extremidades2,analisis2,manejo2,seleccion,consulta):
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    if consulta==1:
        vardx=seleccion
        var1=txt_neuro2
        var2=piel2
        var3=cabeza2
        var4=cuello2
        var5=torax2
        var6=abdomen2
        var7=genitales2
        var8=extremidades2
        var9=analisis2
        var10=manejo2
        cursor.execute("""UPDATE enfermedades SET neurologico=?,piel=?,cabeza=?,cuello=?,torax=?,abdomen=?,genitales=?,extremidades=?,analisis=?,manejo=? WHERE enfermedad = ?""", (var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,vardx))
        conexion.commit()
        tk.messagebox.showinfo('Enfermedad','Enfermedad actualizada')
        conexion.close()
    else:
        vardx=seleccion
        var1=txt_neuro2
        var2=piel2
        var3=cabeza2
        var4=cuello2
        var5=torax2
        var6=abdomen2
        var7=genitales2
        var8=extremidades2
        var9=analisis2
        var10=manejo2
        cursor.execute("""UPDATE urgencias SET neurologico=?,piel=?,cabeza=?,cuello=?,torax=?,abdomen=?,genitales=?,extremidades=?,analisis=?,manejo=? WHERE enfermedad = ?""", (vardx,var1,var2,var3,var4,var5,var6,var7,var8,var9,var10))
        conexion.commit()
        tk.messagebox.showinfo('Enfermedad','Enfermedad actualizada')
        conexion.close()
def f_enfermedad(txt_neuro2, piel2, cabeza2, cuello2, torax2,abdomen2,genitales2,extremidades2,analisis2,manejo2,var_diagnostico2,consulta):
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    if consulta==1:
        vardx=var_diagnostico2
        var1=txt_neuro2
        var2=piel2
        var3=cabeza2
        var4=cuello2
        var5=torax2
        var6=abdomen2
        var7=genitales2
        var8=extremidades2
        var9=analisis2
        var10=manejo2
        cursor.execute("""INSERT INTO enfermedades (enfermedad,neurologico,piel,cabeza,cuello,torax,abdomen,genitales,extremidades,analisis,manejo) VALUES(?,?,?,?,?,?,?,?,?,?,?)""",(vardx,var1,var2,var3,var4,var5,var6,var7,var8,var9,var10))
        conexion.commit()
        conexion.close()
    else:
        vardx=var_diagnostico2
        var1=txt_neuro2
        var2=piel2
        var3=cabeza2
        var4=cuello2
        var5=torax2
        var6=abdomen2
        var7=genitales2
        var8=extremidades2
        var9=analisis2
        var10=manejo2
        cursor.execute("""INSERT INTO urgencias (enfermedad,neurologico,piel,cabeza,cuello,torax,abdomen,genitales,extremidades,analisis,manejo) VALUES(?,?,?,?,?,?,?,?,?,?,?)""",(vardx,var1,var2,var3,var4,var5,var6,var7,var8,var9,var10))
        conexion.commit()
        conexion.close()
'''
def c_enfermedad(txt_neuro2, piel2, cabeza2, cuello2, torax2,abdomen2,genitales2,extremidades2,analisis2,manejo2,var_diagnostico2,consulta):
    var1 =var_diagnostico2
    if consulta == 'consulta':
        conexion = sqlite3.connect('notas.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT neurologico FROM enfermedades  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        txt_neuro2.insert("end",val[0])
        cursor.execute("SELECT piel FROM enfermedades  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        piel2.insert("end",val[0])
        cursor.execute("SELECT cabeza FROM enfermedades  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        cabeza2.insert("end",val[0])
        cursor.execute("SELECT cuello FROM enfermedades  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        cuello2.insert("end",val[0])
        cursor.execute("SELECT torax FROM enfermedades  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        torax2.insert("end",val[0])
        cursor.execute("SELECT abdomen FROM enfermedades  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        abdomen2.insert("end",val[0])
        cursor.execute("SELECT genitales FROM enfermedades  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        genitales2.insert("end",val[0])
        cursor.execute("SELECT extremidades FROM enfermedades  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        extremidades2.insert("end",val[0])
        cursor.execute("SELECT manejo FROM enfermedades  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        manejo2.insert("end", val[0])
        cursor.execute("SELECT analisis FROM enfermedades  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        analisis2.insert("end", val[0])
        conexion.close()
    else:
        conexion = sqlite3.connect('notas.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT neurologico FROM urgencias  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        txt_neuro2.insert("end",val[0])
        cursor.execute("SELECT piel FROM urgencias  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        piel2.insert("end",val[0])
        cursor.execute("SELECT cabeza FROM urgencias  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        cabeza2.insert("end",val[0])
        cursor.execute("SELECT cuello FROM urgencias  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        cuello2.insert("end",val[0])
        cursor.execute("SELECT torax FROM urgencias  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        torax2.insert("end",val[0])
        cursor.execute("SELECT abdomen FROM urgencias  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        abdomen2.insert("end",val[0])
        cursor.execute("SELECT genitales FROM urgencias  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        genitales2.insert("end",val[0])
        cursor.execute("SELECT extremidades FROM urgencias  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        extremidades2.insert("end",val[0])
        cursor.execute("SELECT manejo FROM urgencias  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        manejo2.insert("end", val[0])
        cursor.execute("SELECT analisis FROM urgencias  WHERE enfermedad = ?",(var1,))
        conexion.commit()
        val=cursor.fetchone()
        analisis2.insert("end", val[0])
        conexion.close()
        '''
def n_enfermedad():
    topenfermedad = tk.Toplevel(ven)
    topenfermedad.title("Agregar enfermedad")

    topenfermedad = ttk.LabelFrame(topenfermedad, text="Exploracion Fisica")
    topenfermedad.grid(column=0, row=0, padx=2, pady=4)

    ttk.Label(topenfermedad, text="Neurologico").grid(column=0,row=0, padx=2, pady=4)
    txt_neuro2 = ScrolledText(topenfermedad, height=4, width="60")
    txt_neuro2.grid(column=1, row=0, padx=2, pady=4)

    ttk.Label(topenfermedad, text="Piel y tegumentos").grid(column=0,row=1, padx=2, pady=4)
    piel2 = ScrolledText(topenfermedad, height=4, width="60")
    piel2.grid(column=1,row=1, padx=2, pady=4)

    ttk.Label(topenfermedad, text="Cabeza").grid(column=0,row=2, padx=2, pady=4)
    cabeza2 = ScrolledText(topenfermedad, height=4, width="60")
    cabeza2.grid(column=1,row=2, padx=2, pady=4)

    ttk.Label(topenfermedad, text="Cuello").grid(column=0,row=3, padx=2, pady=4)
    cuello2 = ScrolledText(topenfermedad, height=4, width="60")
    cuello2.grid(column=1,row=3, padx=2, pady=4)

    ttk.Label(topenfermedad, text="Torax").grid(column=0,row=4, padx=2, pady=4)
    torax2 = ScrolledText(topenfermedad, height=4, width="60")
    torax2.grid(column=1,row=4, padx=2, pady=4)

    ttk.Label(topenfermedad, text="Abdomen").grid(column=0,row=5, padx=2, pady=4)
    abdomen2 = ScrolledText(topenfermedad, height=4, width="60")
    abdomen2.grid(column=1,row=5, padx=2, pady=4)

    ttk.Label(topenfermedad, text="Genitales").grid(column=0,row=6, padx=2, pady=4)
    genitales2 = ScrolledText(topenfermedad, height=4, width="60")
    genitales2.grid(column=1,row=6, padx=2, pady=4)

    ttk.Label(topenfermedad, text="Extremidades").grid(column=0,row=7, padx=2, pady=4)
    extremidades2 = ScrolledText(topenfermedad, height=4, width="60")
    extremidades2.grid(column=1,row=7, padx=2, pady=4)

    ttk.Label(topenfermedad, text="Analisis").grid(column=0,row=8, padx=2, pady=4)
    analisis2 = ScrolledText(topenfermedad, height=4, width="60")
    analisis2.grid(column=1,row=8, padx=2, pady=4)

    ttk.Label(topenfermedad, text="Manejo").grid(column=0,row=9, padx=2, pady=4)
    manejo2 = ScrolledText(topenfermedad, height=4, width="60")
    manejo2.grid(column=1,row=9, padx=2, pady=4)

    ttk.Label(topenfermedad, text="Diagnostico").grid(column=0,row=10, padx=2, pady=4)
    var_diagnostico2= tk.StringVar()
    diagnostico2 = ttk.Entry(topenfermedad, width="60", textvariable=var_diagnostico2)
    diagnostico2.grid(column=1, row=10, padx=2, pady=4)

    consulta=tk.IntVar()
    r1 = ttk.Radiobutton(
            topenfermedad,
            text = 'consulta',
            value=1,
            variable=consulta
        )
    r1.grid(column=2,row=10, padx=5,pady=5)
    r2 = ttk.Radiobutton(
            topenfermedad,
            text = 'urgencias',
            value=2,
            variable=consulta
        )
    r2.grid(column=2,row=11, padx=5,pady=5)
    combo2 = ttk.Combobox(
        topenfermedad,
        state="readonly",
        values= lista_completa
    )
    seleccion=combo2.get()
    combo2.grid(column=2,row=12)
    add_med = ttk.Button(topenfermedad, text="Agregar enfermedad", command=lambda:f_enfermedad(txt_neuro2.get("1.0","end-1c"), piel2.get("1.0","end-1c"), cabeza2.get("1.0","end-1c"), cuello2.get("1.0","end-1c"), torax2.get("1.0","end-1c"),abdomen2.get("1.0","end-1c"),genitales2.get("1.0","end-1c"),extremidades2.get("1.0","end-1c"),analisis2.get("1.0","end-1c"),manejo2.get("1.0","end-1c"),var_diagnostico2.get(),consulta.get()))
    add_med.grid(column=1, row=11, padx=2)
    actualizar_med = ttk.Button(topenfermedad, text="actualizar enfermedad", command=lambda:a_enfermedad(txt_neuro2.get("1.0","end-1c"), piel2.get("1.0","end-1c"), cabeza2.get("1.0","end-1c"), cuello2.get("1.0","end-1c"), torax2.get("1.0","end-1c"),abdomen2.get("1.0","end-1c"),genitales2.get("1.0","end-1c"),extremidades2.get("1.0","end-1c"),analisis2.get("1.0","end-1c"),manejo2.get("1.0","end-1c"),combo2.get(),consulta.get()))
    actualizar_med.grid(column=1, row=12, padx=2)
    #cargar_enf=ttk.Button(topenfermedad, text="cargar", command=lambda:c_enfermedad(txt_neuro2.get("1.0","end-1c"), piel2.get("1.0","end-1c"), cabeza2.get("1.0","end-1c"), cuello2.get("1.0","end-1c"), torax2.get("1.0","end-1c"),abdomen2.get("1.0","end-1c"),genitales2.get("1.0","end-1c"),extremidades2.get("1.0","end-1c"),analisis2.get("1.0","end-1c"),manejo2.get("1.0","end-1c"),var_diagnostico2.get(),consulta))
    #cargar_enf.grid(column=2, row=13, padx=2)

    
    

def n_medicamento():
    topmed = tk.Toplevel(ven)
    topmed.title("Agregar medicamento")
    ttk.Label(topmed, text="Nombre").grid(column=0, row=0)
    pat = ttk.Entry(topmed, width="20", textvariable=var_sal)
    pat.grid(column=1, row=0,padx=2, pady=4) 
    
    ttk.Label(topmed, text="Mg").grid(column=2, row=0)
    var_mg= tk.StringVar()
    mg = ttk.Entry(topmed, width="20", textvariable=var_mg)
    mg.grid(column=3, row=0,padx=2, pady=4) # crea la caja de texto para escribir la nota
    
    ttk.Label(topmed, text="Mg2").grid(column=4, row=0)
    var_mg2= tk.StringVar()
    mg2 = ttk.Entry(topmed, width="20", textvariable=var_mg2)
    mg2.grid(column=5, row=0,padx=2, pady=4)
    
    tk.Label(topmed, text="ml").grid(column=6, row=0)
    var_ml= tk.StringVar()
    ml = ttk.Entry(topmed, width="20", textvariable=var_ml)
    ml.grid(column=7, row=0,padx=2, pady=4) # crea la caja de texto para escribir la nota
   
    button_busqueda=ttk.Button(topmed, text="Agregar", command=cargar)
    button_busqueda.grid(column=0, row=1, padx=2)
def lab():
    top = tk.Toplevel(ven)
    top.title("Laboratorios")
    frame_laboratorio = ttk.LabelFrame(top, text="Laboratorios")
    frame_laboratorio.grid(column=0, row=0, pady=2)

    check_roja = tk.IntVar()
    check2 = tk.Checkbutton(frame_laboratorio, text="Serie roja", variable=check_roja)
    check2.grid(column=0, row=0)
    check_blanca = tk.IntVar()
    check3 = tk.Checkbutton(frame_laboratorio, text="Serie blanca", variable=check_blanca)
    check3.grid(column=1, row=0)
    check_quimica = tk.IntVar()
    check4 = tk.Checkbutton(frame_laboratorio, text="Quimica", variable=check_quimica)
    check4.grid(column=2, row=0)
    check_otro = tk.IntVar()
    check5 = tk.Checkbutton(frame_laboratorio, text="Otros", variable=check_otro)
    check5.grid(column=3, row=0)

    ttk.Label(frame_laboratorio, text="Hemoglobina").grid(column=0, row=1)
    var_hemo=tk.StringVar()
    hemo = ttk.Entry(frame_laboratorio, width="20", textvariable=var_hemo)
    hemo.grid(column=1, row=1)

    ttk.Label(frame_laboratorio, text="Eritrocitos").grid(column=2, row=1)
    var_eritros=tk.StringVar()
    eritros = ttk.Entry(frame_laboratorio, width="20", textvariable=var_eritros)
    eritros.grid(column=3, row=1)

    ttk.Label(frame_laboratorio, text="Hematocrito").grid(column=4, row=1)
    var_hemato=tk.StringVar()
    hemato = ttk.Entry(frame_laboratorio, width="20", textvariable=var_hemato)
    hemato.grid(column=5, row=1)

    ttk.Label(frame_laboratorio, text="V.C.M").grid(column=0, row=2)
    var_vcm=tk.StringVar()
    vcm = ttk.Entry(frame_laboratorio, width="20", textvariable=var_vcm)
    vcm.grid(column=1, row=2)

    ttk.Label(frame_laboratorio, text="H.C.M").grid(column=2, row=2)
    var_hcm=tk.StringVar()
    hcm = ttk.Entry(frame_laboratorio, width="20", textvariable=var_hcm)
    hcm.grid(column=3, row=2)

    ttk.Label(frame_laboratorio, text="C.M.H.G").grid(column=4, row=2)
    var_cmhg=tk.StringVar()
    cmhg = ttk.Entry(frame_laboratorio, width="20", textvariable=var_cmhg)
    cmhg.grid(column=5, row=2)

    ttk.Label(frame_laboratorio, text="Plaquetas").grid(column=0, row=3)
    var_plaqueta=tk.StringVar()
    plaqueta = ttk.Entry(frame_laboratorio, width="20", textvariable=var_plaqueta)
    plaqueta.grid(column=1, row=3)

    ttk.Label(frame_laboratorio, text="Leucocitos").grid(column=2, row=3)
    var_leuco=tk.StringVar()
    leuco = ttk.Entry(frame_laboratorio, width="20", textvariable=var_leuco)
    leuco.grid(column=3, row=3)

    ttk.Label(frame_laboratorio, text="Neutrofilos%").grid(column=4, row=3)
    var_neutro=tk.StringVar()
    neutro = ttk.Entry(frame_laboratorio, width="20", textvariable=var_neutro)
    neutro.grid(column=5, row=3)

    ttk.Label(frame_laboratorio, text="Linfocitos%").grid(column=0, row=4)
    var_linfo=tk.StringVar()
    linfo = ttk.Entry(frame_laboratorio, width="20", textvariable=var_linfo)
    linfo.grid(column=1, row=4)

    ttk.Label(frame_laboratorio, text="Monocitos%").grid(column=2, row=4)
    var_mono=tk.StringVar()
    mono = ttk.Entry(frame_laboratorio, width="20", textvariable=var_mono)
    mono.grid(column=3, row=4)

    ttk.Label(frame_laboratorio, text="Eosinofilos%").grid(column=4, row=4)
    var_eos=tk.StringVar()
    eos = ttk.Entry(frame_laboratorio, width="20", textvariable=var_eos)
    eos.grid(column=5, row=4)

    ttk.Label(frame_laboratorio, text="Basofilos%").grid(column=0, row=5)
    var_baso=tk.StringVar()
    baso = ttk.Entry(frame_laboratorio, width="20", textvariable=var_baso)
    baso.grid(column=1, row=5)

    ttk.Label(frame_laboratorio, text="Neutrfilos#").grid(column=2, row=5)
    var_neutro2=tk.StringVar()
    neutro2 = ttk.Entry(frame_laboratorio, width="20", textvariable=var_neutro2)
    neutro2.grid(column=3, row=5)

    ttk.Label(frame_laboratorio, text="Linfocitos#").grid(column=4, row=5)
    var_linfo2=tk.StringVar()
    linfo2 = ttk.Entry(frame_laboratorio, width="20", textvariable=var_linfo2)
    linfo2.grid(column=5, row=5)

    ttk.Label(frame_laboratorio, text="Monocitos#").grid(column=0, row=6)
    var_mono2=tk.StringVar()
    mono2 = ttk.Entry(frame_laboratorio, width="20", textvariable=var_mono2)
    mono2.grid(column=1, row=6)

    ttk.Label(frame_laboratorio, text="Eosinofilos#").grid(column=2, row=6)
    var_eos2=tk.StringVar()
    eos2 = ttk.Entry(frame_laboratorio, width="20", textvariable=var_eos2)
    eos2.grid(column=3, row=6)

    ttk.Label(frame_laboratorio, text="Basofilos#").grid(column=4, row=6)
    var_baso2=tk.StringVar()
    baso2 = ttk.Entry(frame_laboratorio, width="20", textvariable=var_baso2)
    baso2.grid(column=5, row=6)

    ttk.Label(frame_laboratorio, text="").grid(column=0, row=7)#separacion para distincion entre quimica y formula roja y blanca

    ttk.Label(frame_laboratorio, text="Glucosa").grid(column=0, row=8)
    var_gluc=tk.StringVar()
    gluc = ttk.Entry(frame_laboratorio, width="20", textvariable=var_gluc)
    gluc.grid(column=1, row=8)

    ttk.Label(frame_laboratorio, text="urea").grid(column=2, row=8)
    var_urea=tk.StringVar()
    urea = ttk.Entry(frame_laboratorio, width="20", textvariable=var_urea)
    urea.grid(column=3, row=8)

    ttk.Label(frame_laboratorio, text="Creatinina").grid(column=4, row=8)
    var_creatinina=tk.StringVar()
    creatinina = ttk.Entry(frame_laboratorio, width="20", textvariable=var_creatinina)
    creatinina.grid(column=5, row=8)

    ttk.Label(frame_laboratorio, text="Nitrogeno ureico").grid(column=0, row=9)
    var_nitro=tk.StringVar()
    nitro = ttk.Entry(frame_laboratorio, width="20", textvariable=var_nitro)
    nitro.grid(column=1, row=9)

    ttk.Label(frame_laboratorio, text="Colesterol").grid(column=2, row=9)
    var_colesterol=tk.StringVar()
    colesterol = ttk.Entry(frame_laboratorio, width="20", textvariable=var_colesterol)
    colesterol.grid(column=3, row=9)



    ttk.Label(frame_laboratorio, text="LDL").grid(column=0, row=10)
    var_ldl=tk.StringVar()
    ldl = ttk.Entry(frame_laboratorio, width="20", textvariable=var_ldl)
    ldl.grid(column=1, row=10)

    ttk.Label(frame_laboratorio, text="HDL").grid(column=2, row=10)
    var_hdl=tk.StringVar()
    hdl = ttk.Entry(frame_laboratorio, width="20", textvariable=var_hdl)
    hdl.grid(column=3, row=10)

    ttk.Label(frame_laboratorio, text="vldl").grid(column=4, row=10)
    var_vldl=tk.StringVar()
    vldl = ttk.Entry(frame_laboratorio, width="20", textvariable=var_vldl)
    vldl.grid(column=5, row=10)

    ttk.Label(frame_laboratorio, text="ALT").grid(column=0, row=11)
    var_alt=tk.StringVar()
    alt = ttk.Entry(frame_laboratorio, width="20", textvariable=var_alt)
    alt.grid(column=1, row=11)

    ttk.Label(frame_laboratorio, text="AST").grid(column=2, row=11)
    var_ast=tk.StringVar()
    ast = ttk.Entry(frame_laboratorio, width="20", textvariable=var_ast)
    ast.grid(column=3, row=11)

    ttk.Label(frame_laboratorio, text="Bilirrubina Total").grid(column=4, row=11)
    var_bt=tk.StringVar()
    bt = ttk.Entry(frame_laboratorio, width="20", textvariable=var_bt)
    bt.grid(column=5, row=11)

    ttk.Label(frame_laboratorio, text="Bilirrubine Directa").grid(column=0, row=12)
    var_bd=tk.StringVar()
    bd = ttk.Entry(frame_laboratorio, width="20", textvariable=var_bd)
    bd.grid(column=1, row=12)

    ttk.Label(frame_laboratorio, text="Bilirrubina Indirecta").grid(column=2, row=12)
    var_bi=tk.StringVar()
    bi = ttk.Entry(frame_laboratorio, width="20", textvariable=var_bi)
    bi.grid(column=3, row=12)

    ttk.Label(frame_laboratorio, text="Hemoglobina Glucosilada").grid(column=4, row=12)
    var_hglu=tk.StringVar()
    hglu = ttk.Entry(frame_laboratorio, width="20", textvariable=var_hglu)
    hglu.grid(column=5, row=12)

    ttk.Label(frame_laboratorio, text="Fosfatasa alcalina").grid(column=0, row=13)
    var_fa=tk.StringVar()
    fa = ttk.Entry(frame_laboratorio, width="20", textvariable=var_fa)
    fa.grid(column=1, row=13)

    ttk.Label(frame_laboratorio, text="GGT").grid(column=2, row=13)
    var_ggt=tk.StringVar()
    ggt = ttk.Entry(frame_laboratorio, width="20", textvariable=var_ggt)
    ggt.grid(column=3, row=13)

    ttk.Label(frame_laboratorio, text="Sodio").grid(column=4, row=13)
    var_na=tk.StringVar()
    na = ttk.Entry(frame_laboratorio, width="20", textvariable=var_na)
    na.grid(column=5, row=13)

    ttk.Label(frame_laboratorio, text="Potasio").grid(column=0, row=14)
    var_k=tk.StringVar()
    potasio = ttk.Entry(frame_laboratorio, width="20", textvariable=var_k)
    potasio.grid(column=1, row=14)

    ttk.Label(frame_laboratorio, text="Calcio").grid(column=2, row=14)
    var_ca=tk.StringVar()
    calcio = ttk.Entry(frame_laboratorio, width="20", textvariable=var_ca)
    calcio.grid(column=3, row=14)

    ttk.Label(frame_laboratorio, text="Cloro").grid(column=4, row=14)
    var_cl=tk.StringVar()
    cl = ttk.Entry(frame_laboratorio, width="20", textvariable=var_cl)
    cl.grid(column=5, row=14)

    ttk.Label(frame_laboratorio, text="Otros: ").grid(column=0, row=15)
    var_labotro=tk.StringVar()
    otroslab= ttk.Entry(frame_laboratorio, width="20", textvariable=var_labotro)
    otroslab.grid(column=1, row=15)
def excel():
    date=datetime.datetime
    filename = f"date.strftime(%X)lista.csv"
    
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor() 
    cursor.execute("SELECT p.apellido_p, p.apellido_m, p.nombre, p.seguros, p.fecha FROM paciente p")
    resultado = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    csvfile = csv.writer(open(filename, 'w', newline=''), delimiter=',', lineterminator='\r\n',quoting=csv.QUOTE_ALL, escapechar='\\')
    csvfile.writerow(headers)
    csvfile.writerows(resultado)

def cargar():
    var1=var_sal.get()
    var2=var_mg.get()
    var3=var_mg2.get()
    var4=var_ml.get()
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    cursor.execute("""INSERT INTO Medicamentos (sal,mg,mg2,ml) VALUES(?,?,?,?)""",(var1,var2,var3,var4))
    conexion.commit()
    conexion.close()
def paciente():
    fecha = datetime.datetime.now()
    fecha=str(fecha.strftime("%x"))
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    var0=sexo_eleccion.get()
    var1=var_paterno.get()
    var2=var_materno.get()
    var3=var_nombre.get()
    var4=f_dia.get()
    var5=f_mes.get()
    var6=f_ano.get()
    var7=var_edad.get()
    var8=var_calle.get()
    var9=var_colonia.get()
    var10=var_numero.get()
    var11=var_postal.get()
    var12=var_telefono.get()
    var13=var_alergias.get()
    var14=var_enfermedades.get()
    var15=var_hospitalizacion.get()
    var16=var_cirugias.get()
    var17=var_traumatismos.get()
    var18=var_transfusiones.get()
    var19=var_etilismo.get()
    var20=var_tabaco.get()
    var21=var_toxicomania.get()
    var22=var_otros.get()
    var23=var_menarca.get()
    var24=var_ivsa.get()
    var25=var_npsa.get()
    var26=var_gesta.get()
    var27=var_parto.get()
    var28=var_cesarea.get()
    var29=var_aborto.get()
    var30=var_citologia.get()
    var31=dia_cb.get()
    var32=mes_cb.get()
    var33=ano_cb.get()
    var34=var_sdg.get()
    var35=var_usg.get()
    var36=combo_seguro.get()
    
    cursor.execute("SELECT apellido_p AND apellido_m AND nombre FROM paciente WHERE apellido_p = ? AND apellido_m = ? AND nombre = ?", (var1, var2, var3))
    busqueda = cursor.fetchone()
    conexion.commit()
    if busqueda is not None:
        conexion.close()
        tk.messagebox.showinfo('Paciente','Paciente ya existe en la base de datos')
        conexion.close()
    else:
        cursor.execute("""INSERT INTO paciente  (sexo, apellido_p, apellido_m, nombre, f_dia, f_mes, f_ano, edad, calle,colonia, numero, cp, telefono,alergias,enfermedades,hospitalizaciones,cirugias,traumatismos,transfusiones,etilismo,tabaquismo,toxicomanias,otros,menarca,ivsa,npsa,gestas,partos,cesareas,abortos,citologias,m_dia,m_mes,m_ano,sdg,sdu,seguros,fecha) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(var0,var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,fecha))
        conexion.commit()
        conexion.close()
        tk.messagebox.showinfo('Paciente','Paciente almacenado')

def buscar_paciente():
    px=[]
    lista=[]
    var1= var_paterno.get()
    var2= var_materno.get()
    var3 = var_nombre.get()
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    try:
        cursor.execute ("SELECT * FROM paciente WHERE apellido_p = ? AND apellido_m = ? AND nombre = ?", (var1, var2, var3))
        prueba = cursor.fetchall()[0]
        conexion.commit()
    except:
        tk.messagebox.showinfo('Paciente','No se encontro paciente')
    else:
        for x in prueba:
            lista.append(x)
        for x in prueba:
            px.append(x)
        conexion.close()
        sexo_eleccion.delete("0",'end')
        sexo_eleccion.insert("0",lista[1])
        alergia.delete("0",'end') 
        enfermedades.delete("0",'end') 
        hospitalizacion.delete("0",'end')    
        cirugia.delete("0",'end')    
        traumatismo.delete("0",'end')   
        transfusion.delete("0",'end')   
        etilico.delete("0",'end')    
        tabaco.delete("0",'end') 
        toxicomania.delete("0",'end')   
        otros.delete("0",'end')  
        f_dia.insert("0",lista[5])
        f_mes.insert("0",lista[6])
        f_ano.insert("0",lista[7])
        edad.insert("0",lista[8])
        calle.insert("0",lista[9])
        colonia.insert("0",lista[10])
        numero.insert("0",lista[11])
        postal.insert("0",lista[12])
        telefono.insert("0",lista[13])
        alergia.insert("0",lista[14])
        enfermedades.insert("0",lista[15])
        hospitalizacion.insert("0",lista[16])
        cirugia.insert("0",lista[17])
        traumatismo.insert("0",lista[18])
        transfusion.insert("0",lista[19])
        etilico.insert("0",lista[20])
        tabaco.insert("0",lista[21])
        toxicomania.insert("0",lista[22])
        otros.insert("0",lista[23])
        menarca.insert("0",lista[24])
        ivsa.insert("0",lista[25])
        npsa.insert("0",lista[26])
        gesta.insert("0",lista[27])
        parto.insert("0",lista[28])
        cesarea.insert("0",lista[29])
        aborto.insert("0",lista[30])
        citologia.insert("0",lista[31])
        dia_cb.insert("0",lista[32])
        mes_cb.insert("0",lista[33])
        ano_cb.insert("0",lista[34])
        sdg.insert("0",lista[35])
        usg.insert("0",lista[36])
        conexion = sqlite3.connect('notas.db')
        cursor = conexion.cursor()
        cursor.execute ("SELECT id FROM paciente WHERE apellido_p = ? AND apellido_m = ? AND nombre = ?", (var1, var2, var3))
        id = cursor.fetchall()[0]
        conexion.commit()
        cursor.execute("SELECT fecha FROM consulta WHERE  foreign_p=?", (id))
        resultado = cursor.fetchall()
        conexion.commit()
        for each in resultado:
            lista_fecha.insert(0,each)
        conexion.close()
        

def cargar_nota(event):
    lnota=[]
    var1= var_paterno.get()
    var2= var_materno.get()
    var3 = var_nombre.get()
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    cursor.execute ("SELECT id  FROM paciente WHERE apellido_p = ? AND apellido_m = ? AND nombre = ?", (var1, var2, var3))
    id = cursor.fetchone()
    conexion.commit()

    for each in lista_fecha.get(lista_fecha.curselection()):
        pass
    
    id = id[0]
    cursor.execute("SELECT * FROM consulta WHERE fecha=? and foreign_p=?", (each, id))
    resultado=cursor.fetchall()
    conexion.commit()
    for n in resultado:
        lnota.append(n)
    for x in range(len(lnota)):
        g_nota.insert("end", lnota[x])
        g_nota.insert("end", "\n\n\n\n")
    conexion.close()
         
def actualizar_paciente():
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    var0=sexo_eleccion.get()
    var1=var_paterno.get()
    var2=var_materno.get()
    var3=var_nombre.get()
    var4=f_dia.get()
    var5=f_mes.get()
    var6=f_ano.get()
    var7=var_edad.get()
    var8=var_calle.get()
    var9=var_colonia.get()
    var10=var_numero.get()
    var11=var_postal.get()
    var12=var_telefono.get()
    var13=var_alergias.get()
    var14=var_enfermedades.get()
    var15=var_hospitalizacion.get()
    var16=var_cirugias.get()
    var17=var_traumatismos.get()
    var18=var_transfusiones.get()
    var19=var_etilismo.get()
    var20=var_tabaco.get()
    var21=var_toxicomania.get()
    var22=var_otros.get()
    var23=var_menarca.get()
    var24=var_ivsa.get()
    var25=var_npsa.get()
    var26=var_gesta.get()
    var27=var_parto.get()
    var28=var_cesarea.get()
    var29=var_aborto.get()
    var30=var_citologia.get()
    var31=dia_cb.get()
    var32=mes_cb.get()
    var33=ano_cb.get()
    var34=var_sdg.get()
    var35=var_usg.get()
    var36=combo_seguro.get()
    cursor.execute("""UPDATE paciente SET sexo=?, apellido_p=?, apellido_m=?, nombre=?, f_dia=?, f_mes=?, f_ano=?, edad=?, calle=?,colonia=?, numero=?, cp=?, telefono=?,alergias=?,enfermedades=?,hospitalizaciones=?,cirugias=?,traumatismos=?,transfusiones=?,etilismo=?,tabaquismo=?,toxicomanias=?,otros=?,menarca=?,ivsa=?,npsa=?,gestas=?,partos=?,cesareas=?,abortos=?,citologias=?,m_dia=?,m_mes=?,m_ano=?,sdg=?,sdu=?,seguros=?,fecha=? WHERE apellido_p=? AND apellido_m=? AND nombre=?""",(var0,var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,fecha,var1,var2,var3))
    conexion.commit()
    tk.messagebox.showinfo('Paciente','Paciente actualizado')
    conexion.close()

# Funciones de nota medica
def evo():
    g_check=check_embarazo.get()
    g_signos = "Tension arterial: " + var_tension.get() + ", Frecuencia cardiaca: " + var_fr.get() + ", Frecuencia respiratoria: " + var_fr.get() + ", Temperatura: " + var_temp.get() + ", Saturacion: " + var_sat.get()
    g_nombre = var_paterno.get() + " " + var_materno.get() +" "+ var_nombre.get()
    g_pp = var_alergias.get() + var_enfermedades.get() + var_hospitalizacion.get() + var_cirugias.get() + var_transfusiones.get() + var_traumatismos.get()
    g_np = var_etilismo.get() + var_tabaco.get() + var_toxicomania.get()
    g_gyo = "Menarca: "+ var_menarca.get() + ", Inicio de vida sexual activa: " + var_ivsa.get() + ", numero de parejas sexualmente activas: "+ var_npsa.get() + ", gestas: "+ var_gesta.get() + ", partos: "+ var_parto.get() + ", cesarea: "+ var_cesarea.get() + ", aborto: "+ var_aborto.get() + ", citologias: "+ var_citologia.get() + ", fecha de ultima menstruacion: "+ dia_cb.get() + "/" + mes_cb.get() + "/" +var_menstruacion.get()
    g_ef = txt_neuro.get("1.0","end-1c") + piel.get("1.0","end-1c") + cabeza.get("1.0","end-1c") + cuello.get("1.0","end-1c") + torax.get("1.0","end-1c") + abdomen.get("1.0","end-1c") + genitales.get("1.0","end-1c") + extremidades.get("1.0","end-1c")
    g_actual = actual.get("1.0","end-1c")
    g_diagnostico = var_diagnostico.get()
    

    if sexo_eleccion.get() == "Femenino":
        if g_check == 1:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " +  "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSemanas de gestacion por fum: " +var_sdg.get()+ ", semanas de gestacion por ultrasonido: "+ var_usg.get() + "\n\nAPNP: "+g_np+"\n\nSignos vitales: " + g_signos + ".\n\nExploracion fisica:"+g_ef+".\n\nAnalisis:"+txt_analisis.get("1.0","end-1c")+".\n\nManejo:\n\n" +manejo.get("1.0","end-1c")+ "\n\nDiagnostico: "+g_diagnostico )
        else:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " +  "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+ "\n\nAPNP: "+g_np+"\n\nSignos vitales: " + g_signos + ".\n\nExploracion fisica:"+g_ef+".\n\nAnalisis:"+txt_analisis.get("1.0","end-1c")+".\n\nManejo:" +manejo.get("1.0","end-1c")+ "\n\nDiagnostico: "+g_diagnostico) 

    else:
        g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+ "\n\nAPNP: "+g_np+"\n\nSignos vitales: " + g_signos + ".\n\nExploracion fisica:"+g_ef+".\n\nAnalisis:"+txt_analisis.get("1.0","end-1c")+".\n\nManejo:\n\n" +manejo.get("1.0","end-1c")+ "\n\nDiagnostico: "+g_diagnostico)
        
def gen_historia():
    #Funcion para generar las notas del paciente, almacena los valores en variables y finalmente lo agrega al scrolledtext para su revision modificacion y copiado.
    g_check=check_embarazo.get()
    g_signos = "Tension arterial: " + var_tension.get() + "Frecuencia cardiaca: " + var_fr.get() + ",Frecuencia respiratoria: " + var_fr.get() + ",Temperatura: " + var_temp.get() + ",Saturacion: " + var_sat.get()
    g_nombre = var_paterno.get() + " " + var_materno.get() +" "+ var_nombre.get()
    g_direccion = var_calle.get() + ", colonia: "+var_colonia.get() +", numero: " + var_numero.get() +", codigo postal: " + var_postal.get()
    g_pp = var_alergias.get() + var_enfermedades.get() + var_hospitalizacion.get() + var_cirugias.get() + var_transfusiones.get() + var_traumatismos.get()
    g_np = var_etilismo.get() + var_tabaco.get() + var_toxicomania.get()
    g_gyo = "Menarca: "+ var_menarca.get() + ", Inicio de vida sexual activa: " + var_ivsa.get() + ", numero de parejas sexualmente activas: "+ var_npsa.get() + ", gestas: "+ var_gesta.get() + ", partos: "+ var_parto.get() + ", cesarea: "+ var_cesarea.get() + ", aborto: "+ var_aborto.get() + ", citologias: "+ var_citologia.get() + ", fecha de ultima menstruacion: "+ dia_cb.get() + "/" + mes_cb.get() + "/" +var_menstruacion.get()
    g_ef = txt_neuro.get("1.0","end-1c") + piel.get("1.0","end-1c") + cabeza.get("1.0","end-1c") + cuello.get("1.0","end-1c") + torax.get("1.0","end-1c") + abdomen.get("1.0","end-1c") + genitales.get("1.0","end-1c") + extremidades.get("1.0","end-1c")
    g_actual = actual.get("1.0","end-1c")
    g_diagnostico = var_diagnostico.get()

    if sexo_eleccion.get() == "Femenino":
        if g_check == 1:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSemanas de gestacion por fum: " +var_sdg.get()+ ", semanas de gestacion por ultrasonido: "+ var_usg.get() + "\n\nAPNP: "+g_np+"\n\nSignos vitales: " + g_signos + ".\n\nExploracion fisica:"+g_ef+".\n\nAnalisis:"+txt_analisis.get("1.0","end-1c")+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +manejo.get("1.0","end-1c") )
            
        else:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+ "\n\nAPNP: "+g_np+"\n\nSignos vitales: " + g_signos + ".\n\nExploracion fisica:"+g_ef+".\n\nAnalisis:"+txt_analisis.get("1.0","end-1c")+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +manejo.get("1.0","end-1c") )
    
    else:
        g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+ "\n\nAPNP: "+g_np+"\n\nSignos vitales: " + g_signos + ".\n\nExploracion fisica:"+g_ef+".\n\nAnalisis:"+txt_analisis.get("1.0","end-1c")+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +manejo.get("1.0","end-1c") )
        
          
def nota_texto():
    rand=random.randint(0,100)
    g_nombre = var_paterno.get() + " " + var_materno.get() +" "+ var_nombre.get()
    g_ef = txt_neuro.get("1.0","end-1c") + piel.get("1.0","end-1c") + cabeza.get("1.0","end-1c") + cuello.get("1.0","end-1c") + torax.get("1.0","end-1c") + abdomen.get("1.0","end-1c") + genitales.get("1.0","end-1c") + extremidades.get("1.0","end-1c")
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    cursor.execute ("SELECT id FROM paciente WHERE apellido_p = ? AND apellido_m = ? AND nombre = ?", (var_paterno.get(), var_materno.get(), var_nombre.get()))
    prueba=cursor.fetchall()[0]
    conexion.commit()
    lista_id = []
    for m in prueba:
        lista_id.append(m)
    peso=var_kg.get()
    tension=var_tension.get()
    frecuencaf=var_fc.get()
    frecuenciar=var_fr.get()
    temp=var_temp.get()
    saturacion=var_sat.get()
    pad=actual.get("1.0","end-1c")
    ident=var_diagnostico.get()
    exploracion = g_ef
    try:
        f = open("notas/"+g_nombre+str(rand)+".txt","x")
        g_check = check_embarazo.get()
        g_pp = var_alergias.get() + var_enfermedades.get() + var_hospitalizacion.get() + var_cirugias.get() + var_transfusiones.get() + var_traumatismos.get()
        g_np = var_etilismo.get() + var_tabaco.get() + var_toxicomania.get()
        g_gyo = "Menarca: "+ var_menarca.get() + ", Inicio de vida sexual activa: " + var_ivsa.get() + ", numero de parejas sexualmente activas: "+ var_npsa.get() + ", Gestas: "+ var_gesta.get() + ", partos: "+ var_parto.get() + ", cesarea: "+ var_cesarea.get() + ", aborto: "+ var_aborto.get() + ", citologias: "+ var_citologia.get() + ", fecha de ultima menstruacion: "+dia_cb.get() + "/" + mes_cb.get() + "/" +var_menstruacion.get()
        g_ef = var_neuro.get() + var_piel.get() + var_cabeza.get() + var_cuello.get() + var_torax.get() + var_abdomen.get() + var_genitales.get() + var_extremidades.get()
        g_actual = actual.get("1.0","end-1c")
        g_signos = "Tensión arterial: " + var_tension.get() + "Frecuencia cardiaca: " + var_fr.get() + ",Frecuencia respiratoria: " + var_fr.get() + ",Temperatura: " + var_temp.get() + ",Saturacion: " + var_sat.get()
        g_ef = var_neuro.get() + var_piel.get() + var_cabeza.get() + var_cuello.get() + var_torax.get() + var_abdomen.get() + var_genitales.get() + var_extremidades.get()
        g_nombre = var_paterno.get() + " " + var_materno.get() +" "+ var_nombre.get()
        g_signos = "Tension arterial: " + var_tension.get() + ", Frecuencia cardiaca: " + var_fr.get() + ", Frecuencia respiratoria: " + var_fr.get() + ", Temperatura: " + var_temp.get() + ", Saturacion: " + var_sat.get()
        g_ef = txt_neuro.get("1.0","end-1c") + piel.get("1.0","end-1c") + cabeza.get("1.0","end-1c") + cuello.get("1.0","end-1c") + torax.get("1.0","end-1c") + abdomen.get("1.0","end-1c") + genitales.get("1.0","end-1c") + extremidades.get("1.0","end-1c")
        g_nota = g_nombre + '\n\n' + g_actual + '\n\n' + g_pp + '\n\n' + g_np + '\n\n' + g_signos + '\n\n' + g_ef + '\n\n'
        g_notafem = g_nombre + '\n\n' + g_actual + '\n\n' + g_pp + '\n\n' + g_np + '\n\n' + '\n\n' + g_gyo + '\n\n' + g_signos + '\n\n' + g_ef + '\n\n'
        g_diagnostico = var_diagnostico.get()
        
        if sexo_eleccion.get() == "Femenino":
            if g_check == 1:
                word_nota = g_notafem +'\n' + txt_analisis.get("1.0","end-1c") + '\n\n' + g_diagnostico + '\n\n' + manejo.get("1.0","end-1c")
                f.write(word_nota)
                f.close()
                conexion = sqlite3.connect('notas.db')
                cursor = conexion.cursor()
                cursor.execute ("SELECT id FROM paciente WHERE apellido_p = ? AND apellido_m = ? AND nombre = ?", (var_paterno.get(), var_materno.get(), var_nombre.get()))
                prueba=cursor.fetchall()[0]
                conexion.commit()
                lista_id = []
                for m in prueba:
                    lista_id.append(m)
                    print(lista_id)
                peso=var_kg.get()
                tension=var_tension.get()
                frecuencaf=var_fc.get()
                frecuenciar=var_fr.get()
                temp=var_temp.get()
                saturacion=var_sat.get()
                pad=actual.get("1.0","end-1c")
                exploracion=g_ef
                ident=var_diagnostico.get()
                print(lista_id[0])
                cursor.execute("""INSERT INTO consulta (fecha,peso,ta,fc,fr,temp,s02,pa,ef,analisis,manejo,diagnostico,foreign_p) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",(fecha,peso,tension,frecuencaf,frecuenciar,temp,saturacion,pad,exploracion,txt_analisis.get("1.0","end-1c"),manejo.get("1.0","end-1c"),ident,lista_id[0]))
                conexion.commit()
                conexion.close()
            else:
                word_nota = g_notafem +'\n\n'+ txt_analisis.get("1.0","end-1c") + '\n\n' + g_diagnostico + '\n\n' + manejo.get("1.0","end-1c")
                f.write(word_nota)
                f.close()
                conexion = sqlite3.connect('notas.db')
                cursor = conexion.cursor()
                cursor.execute ("SELECT id FROM paciente WHERE apellido_p = ? AND apellido_m = ? AND nombre = ?", (var_paterno.get(), var_materno.get(), var_nombre.get()))
                prueba=cursor.fetchall()[0]
                conexion.commit()
                lista_id = []
                for m in prueba:
                    lista_id.append(m)
                    print(lista_id)
                peso=var_kg.get()
                tension=var_tension.get()
                frecuencaf=var_fc.get()
                frecuenciar=var_fr.get()
                temp=var_temp.get()
                saturacion=var_sat.get()
                pad=actual.get("1.0","end-1c")
                exploracion=g_ef
                ident=var_diagnostico.get()
                print(lista_id[0])
                cursor.execute("""INSERT INTO consulta (fecha,peso,ta,fc,fr,temp,s02,pa,ef,analisis,manejo,diagnostico,foreign_p) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",(fecha,peso,tension,frecuencaf,frecuenciar,temp,saturacion,pad,exploracion,txt_analisis.get("1.0","end-1c"),manejo.get("1.0","end-1c"),ident,lista_id[0]))
                conexion.commit()
                conexion.close()
        else:
            word_nota = g_nota +'\n\n'+ txt_analisis.get("1.0","end-1c") + '\n\n' + g_diagnostico + '\n\n' + manejo.get("1.0","end-1c")
            f.write(word_nota)
            f.close()
            conexion = sqlite3.connect('notas.db')
            cursor = conexion.cursor()
            cursor.execute ("SELECT id FROM paciente WHERE apellido_p = ? AND apellido_m = ? AND nombre = ?", (var_paterno.get(), var_materno.get(), var_nombre.get()))
            prueba=cursor.fetchall()[0]
            conexion.commit()
            lista_id = []
            for m in prueba:
                lista_id.append(m)
                print(lista_id)
            peso=var_kg.get()
            tension=var_tension.get()
            frecuencaf=var_fc.get()
            frecuenciar=var_fr.get()
            temp=var_temp.get()
            saturacion=var_sat.get()
            pad=actual.get("1.0","end-1c")
            exploracion=g_ef
            ident=var_diagnostico.get()
            print(lista_id[0])
            cursor.execute("""INSERT INTO consulta (fecha,peso,ta,fc,fr,temp,s02,pa,ef,analisis,manejo,diagnostico,foreign_p) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",(fecha,peso,tension,frecuencaf,frecuenciar,temp,saturacion,pad,exploracion,txt_analisis.get("1.0","end-1c"),manejo.get("1.0","end-1c"),ident,lista_id[0]))
            conexion.commit()
            conexion.close()
        status.config(foreground='green')
    except FileNotFoundError:
        f = open("notas/"+g_nombre+".txt","x")
        #GENERA LA NOTA EN UN ARCHIVO DE TEXTO
        g_check = check_embarazo.get()
        g_pp = var_alergias.get() + var_enfermedades.get() + var_hospitalizacion.get() + var_cirugias.get() + var_transfusiones.get() + var_traumatismos.get()
        g_np = var_etilismo.get() + var_tabaco.get() + var_toxicomania.get()
        g_gyo = "Menarca: "+ var_menarca.get() + ", Inicio de vida sexual activa: " + var_ivsa.get() + ", numero de parejas sexualmente activas: "+ var_npsa.get() + ", Gestas: "+ var_gesta.get() + ", partos: "+ var_parto.get() + ", cesarea: "+ var_cesarea.get() + ", aborto: "+ var_aborto.get() + ", citologias: "+ var_citologia.get() + ", fecha de ultima menstruacion: "+ dia_cb.get() + "/" + mes_cb.get() + "/" +var_menstruacion.get()
        g_ef = var_neuro.get() + var_piel.get() + var_cabeza.get() + var_cuello.get() + var_torax.get() + var_abdomen.get() + var_genitales.get() + var_extremidades.get()
        g_actual = actual.get("1.0","end-1c")
        g_signos = "Tensión arterial: " + var_tension.get() + "Frecuencia cardiaca: " + var_fr.get() + ",Frecuencia respiratoria: " + var_fr.get() + ",Temperatura: " + var_temp.get() + ",Saturacion: " + var_sat.get()
        g_ef = var_neuro.get() + var_piel.get() + var_cabeza.get() + var_cuello.get() + var_torax.get() + var_abdomen.get() + var_genitales.get() + var_extremidades.get()
        g_nombre = var_paterno.get() + " " + var_materno.get() +" "+ var_nombre.get()
        g_signos = "Tension arterial: " + var_tension.get() + ", Frecuencia cardiaca: " + var_fr.get() + ", Frecuencia respiratoria: " + var_fr.get() + ", Temperatura: " + var_temp.get() + ", Saturacion: " + var_sat.get()
        g_ef = txt_neuro.get("1.0","end-1c") + piel.get("1.0","end-1c") + cabeza.get("1.0","end-1c") + cuello.get("1.0","end-1c") + torax.get("1.0","end-1c") + abdomen.get("1.0","end-1c") + genitales.get("1.0","end-1c") + extremidades.get("1.0","end-1c")
        g_nota = g_nombre + '\n\n' + g_actual + '\n\n' + g_pp + '\n\n' + g_np + '\n\n' + g_signos + '\n\n' + g_ef + '\n\n'
        g_notafem = g_nombre + '\n\n' + g_actual + '\n\n' + g_pp + '\n\n' + g_np + '\n\n' + '\n\n' + g_gyo + '\n\n' + g_signos + '\n\n' + g_ef + '\n\n'
        g_diagnostico = var_diagnostico.get()
        
        if sexo_eleccion.get() == "Femenino":
            if g_check == 1:
                word_nota = g_notafem +'\n' + txt_analisis.get("1.0","end-1c") + '\n\n' + g_diagnostico + '\n\n' + manejo.get("1.0","end-1c")
                f.write(word_nota)
                f.close()
                conexion = sqlite3.connect('notas.db')
                cursor = conexion.cursor()
                cursor.execute ("SELECT id FROM paciente WHERE apellido_p = ? AND apellido_m = ? AND nombre = ?", (var_paterno.get(), var_materno.get(), var_nombre.get()))
                prueba=cursor.fetchall()[0]
                conexion.commit()
                lista_id = []
                for m in prueba:
                    lista_id.append(m)
                    print(lista_id)
                peso=var_kg.get()
                tension=var_tension.get()
                frecuencaf=var_fc.get()
                frecuenciar=var_fr.get()
                temp=var_temp.get()
                saturacion=var_sat.get()
                pad=actual.get("1.0","end-1c")
                exploracion=g_ef
                ident=var_diagnostico.get()
                print(lista_id[0])
                cursor.execute("""INSERT INTO consulta (fecha,peso,ta,fc,fr,temp,s02,pa,ef,analisis,manejo,diagnostico,foreign_p) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",(fecha,peso,tension,frecuencaf,frecuenciar,temp,saturacion,pad,exploracion,txt_analisis.get("1.0","end-1c"),manejo.get("1.0","end-1c"),ident,lista_id[0]))
                conexion.commit()
                conexion.close()
            else:
                word_nota = g_notafem +'\n\n'+ txt_analisis.get("1.0","end-1c") + '\n\n' + g_diagnostico + '\n\n' + manejo.get("1.0","end-1c")
                f.write(word_nota)
                f.close()
                conexion = sqlite3.connect('notas.db')
                cursor = conexion.cursor()
                cursor.execute ("SELECT id FROM paciente WHERE apellido_p = ? AND apellido_m = ? AND nombre = ?", (var_paterno.get(), var_materno.get(), var_nombre.get()))
                prueba=cursor.fetchall()[0]
                conexion.commit()
                lista_id = []
                for m in prueba:
                    lista_id.append(m)
                    print(lista_id)
                peso=var_kg.get()
                tension=var_tension.get()
                frecuencaf=var_fc.get()
                frecuenciar=var_fr.get()
                temp=var_temp.get()
                saturacion=var_sat.get()
                pad=actual.get("1.0","end-1c")
                exploracion=g_ef
                ident=var_diagnostico.get()
                print(lista_id[0])
                cursor.execute("""INSERT INTO consulta (fecha,peso,ta,fc,fr,temp,s02,pa,ef,analisis,manejo,diagnostico,foreign_p) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",(fecha,peso,tension,frecuencaf,frecuenciar,temp,saturacion,pad,exploracion,txt_analisis.get("1.0","end-1c"),manejo.get("1.0","end-1c"),ident,lista_id[0]))
                conexion.commit()
                conexion.close()
        else:
            word_nota = g_nota +'\n\n'+ txt_analisis.get("1.0","end-1c") + '\n\n' + g_diagnostico + '\n\n' + manejo.get("1.0","end-1c")
            f.write(word_nota)
            f.close()
            conexion = sqlite3.connect('notas.db')
            cursor = conexion.cursor()
            cursor.execute ("SELECT id FROM paciente WHERE apellido_p = ? AND apellido_m = ? AND nombre = ?", (var_paterno.get(), var_materno.get(), var_nombre.get()))
            prueba=cursor.fetchall()[0]
            conexion.commit()
            lista_id = []
            for m in prueba:
                lista_id.append(m)
                print(lista_id)
            peso=var_kg.get()
            tension=var_tension.get()
            frecuencaf=var_fc.get()
            frecuenciar=var_fr.get()
            temp=var_temp.get()
            saturacion=var_sat.get()
            pad=actual.get("1.0","end-1c")
            exploracion=g_ef
            ident=var_diagnostico.get()
            print(lista_id[0])
            cursor.execute("""INSERT INTO consulta (fecha,peso,ta,fc,fr,temp,s02,pa,ef,analisis,manejo,diagnostico,foreign_p) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",(fecha,peso,tension,frecuencaf,frecuenciar,temp,saturacion,pad,exploracion,txt_analisis.get("1.0","end-1c"),manejo.get("1.0","end-1c"),ident,lista_id[0]))
            conexion.commit()
            conexion.close()
        status.config(foreground='green')
        
        
        

        
    # se abre la base de datos para crear la nota de exploracion fisica del paciente
      
    

def seleccionar():
    var1 =combo.get()
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT neurologico FROM enfermedades  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    txt_neuro.insert("end",val[0])
    cursor.execute("SELECT piel FROM enfermedades  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    piel.insert("end",val[0])
    cursor.execute("SELECT cabeza FROM enfermedades  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    cabeza.insert("end",val[0])
    cursor.execute("SELECT cuello FROM enfermedades  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    cuello.insert("end",val[0])
    cursor.execute("SELECT torax FROM enfermedades  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    torax.insert("end",val[0])
    cursor.execute("SELECT abdomen FROM enfermedades  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    abdomen.insert("end",val[0])
    cursor.execute("SELECT genitales FROM enfermedades  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    genitales.insert("end",val[0])
    cursor.execute("SELECT extremidades FROM enfermedades  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    extremidades.insert("end",val[0])
    cursor.execute("SELECT manejo FROM enfermedades  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    manejo.insert("end", val[0])
    cursor.execute("SELECT analisis FROM enfermedades  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    txt_analisis.insert("end", val[0])
    diagnostico.insert("end",var1)
    conexion.close()

def seleccionar_u():
    var1 =combo2.get()
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT neurologico FROM urgencias  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    txt_neuro.insert("end",val[0])
    cursor.execute("SELECT piel FROM urgencias  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    piel.insert("end",val[0])
    cursor.execute("SELECT cabeza FROM urgencias  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    cabeza.insert("end",val[0])
    cursor.execute("SELECT cuello FROM urgencias  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    cuello.insert("end",val[0])
    cursor.execute("SELECT torax FROM urgencias  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    torax.insert("end",val[0])
    cursor.execute("SELECT abdomen FROM urgencias  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    abdomen.insert("end",val[0])
    cursor.execute("SELECT genitales FROM urgencias  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    genitales.insert("end",val[0])
    cursor.execute("SELECT extremidades FROM urgencias  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    extremidades.insert("end",val[0])
    cursor.execute("SELECT manejo FROM urgencias  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    manejo.insert("end", val[0])
    cursor.execute("SELECT analisis FROM urgencias  WHERE enfermedad = ?",(var1,))
    conexion.commit()
    val=cursor.fetchone()
    txt_analisis.insert("end", val[0])
    conexion.close()
def n_limpiar():
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT enfermedad FROM enfermedades ")
    dc=[]
    for i in cursor:
        dc.append(i)
    conexion.commit()
    conexion.close()
    #Realiza limpieza de los campos de texto para realizar nueva nota
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    g_nota.delete("1.0", "end")
    lista_fecha.delete(0,'end')    
    alergia.delete("0",'end')
    alergia.insert('end',t_alergia)
    f_dia.delete("0",'end') 
    f_mes.delete("0",'end')
    f_ano.delete("0",'end')
    paterno.delete("0",'end')
    materno.delete("0",'end')
    nombre.delete("0",'end')
    edad.delete("0",'end')
    calle.delete("0",'end')
    colonia.delete("0",'end')
    telefono.delete("0",'end')
    postal.delete("0",'end')
    numero.delete("0",'end')
    enfermedades.delete("0",'end') 
    enfermedades.insert('end',t_enf)
    hospitalizacion.delete("0",'end')    
    hospitalizacion.insert('end',t_hosp)
    cirugia.delete("0",'end')    
    cirugia.insert('end',t_cir)
    traumatismo.delete("0",'end')

    traumatismo.insert('end',t_trauma)
    transfusion.delete("0",'end')   
    transfusion.insert('end',t_trans)
    etilico.delete("0",'end')    
    etilico.insert('end',t_etilismo)
    tabaco.delete("0",'end') 
    tabaco.insert('end',t_tabaquismo)
    toxicomania.delete("0",'end')   
    toxicomania.insert('end',t_drogas)
    otros.delete("0",'end')  
    menarca.delete("0",'end')    
    ivsa.delete("0",'end')
    npsa.delete("0",'end')
    gesta.delete("0",'end')
    parto.delete("0",'end')
    cesarea.delete("0",'end')
    aborto.delete("0",'end')
    citologia.delete("0",'end')
    #menstruacion.delete("0",'end')
    sdg.delete("0",'end')
    usg.delete("0",'end')
    actual.delete("1.0", "end-1c")
    analisis.delete("0",'end')
    manejo.delete("1.0", "end-1c")
    txt_analisis.delete("1.0", "end-1c")
    svt.delete('0','end')
    kg.delete('0','end')
    kg.insert('end',0)
    fc.delete('0','end')
    fr.delete('0','end')
    tc.delete('0','end')
    sat.delete('0','end')
    txt_neuro.delete("1.0", "end-1c")   
    piel.delete("1.0", "end-1c")    
    cabeza.delete("1.0", "end-1c")   
    cuello.delete("1.0", "end-1c")   
    torax.delete("1.0", "end-1c")   
    abdomen.delete("1.0", "end-1c")   
    genitales.delete("1.0", "end-1c")
    extremidades.delete("1.0", "end-1c")
    diagnostico.delete('0','end')
    '''
    hemo.delete("0","end")
    hemato.delete("0","end")
    eritros.delete("0","end")
    plaqueta.delete("0","end")
    vcm.delete("0","end")
    hcm.delete("0","end")
    cmhg.delete("0","end")
    leuco.delete("0","end")
    neutro.delete("0","end")
    neutro2.delete("0","end")
    linfo.delete("0","end")
    linfo2.delete("0","end")
    eos.delete("0","end")
    eos2.delete("0","end")
    mono.delete("0","end")
    mono2.delete("0","end")
    baso.delete("0","end")
    baso2.delete("0","end")
    gluc.delete("0","end")
    urea.delete("0","end")
    creatinina.delete("0","end")
    nitro.delete("0","end")
    fa.delete("0","end")
    colesterol.delete("0","end")
    hdl.delete("0","end")
    ldl.delete("0","end")
    vldl.delete("0","end")
    alt.delete("0","end")
    ast.delete("0","end")
    bd.delete("0","end")
    bi.delete("0","end")
    bt.delete("0","end")
    ggt.delete("0","end")
    na.delete("0","end")
    potasio.delete("0","end")
    calcio.delete("0","end")
    cl.delete("0","end")
    hglu.delete("0","end")
    otros.delete("0","end")
    '''
    sexo_eleccion.set('')
    combo_seguro.set('')
    status.config(foreground='red')
def pres_a(event):
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    var0=sexo_eleccion.get()
    var1=var_paterno.get()
    var2=var_materno.get()
    var3=var_nombre.get()
    var4=f_dia.get()
    var5=f_mes.get()
    var6=f_ano.get()
    var7=var_edad.get()
    var8=var_calle.get()
    var9=var_colonia.get()
    var10=var_numero.get()
    var11=var_postal.get()
    var12=var_telefono.get()
    var13=var_alergias.get()
    var14=var_enfermedades.get()
    var15=var_hospitalizacion.get()
    var16=var_cirugias.get()
    var17=var_traumatismos.get()
    var18=var_transfusiones.get()
    var19=var_etilismo.get()
    var20=var_tabaco.get()
    var21=var_toxicomania.get()
    var22=var_otros.get()
    var23=var_menarca.get()
    var24=var_ivsa.get()
    var25=var_npsa.get()
    var26=var_gesta.get()
    var27=var_parto.get()
    var28=var_cesarea.get()
    var29=var_aborto.get()
    var30=var_citologia.get()
    var31=var_media.get()
    var32=dia_cb.get()
    var33=mes_cb.get()
    var34=var_menstruacion.get()
    var35=var_sdg.get()
    var36=var_usg.get()
    var37=combo_seguro.get()
    cursor.execute("""INSERT INTO paciente (sexo, apellido_p, apellido_m, nombre, f_dia, f_mes, f_ano, edad, calle,colonia, numero, cp, telefono,alergias,enfermedades,hospitalizaciones,cirugias,traumatismos,transfusiones,etilismo,tabaquismo,toxicomanias,otros,menarca,ivsa,npsa,gestas,partos,cesareas,abortos,citologias,m_dia,m_mes,m_ano,sdg,sdu,seguros,fecha) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(var0,var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var32,var33,var34,var35,var37,fecha))
    '''ssss'''
    conexion.commit()
    conexion.close()   

def cargar_med():
    lista = []
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    sal=combomed.get()
    cursor.execute("""SELECT * FROM medicamentos WHERE sal=?""",(sal,))
    prueba = cursor.fetchall()[0]
    for x in prueba:
        lista.append(x)
    conexion.close()
    mg = lista[2]
    mg2= lista[3]
    ml = lista[4]
    medmg.delete("0", 'end')
    medmg2.delete("0", 'end')
    medml.delete("0", 'end')
    medmg.insert("0",mg)
    medmg2.insert("0",mg2)
    medml.insert("0",ml)
    
def receta():
    horas = dia_med.get() 
    dosis=Decimal(var_dosis.get())
    peso=Decimal(var_kg.get())
    mg=Decimal(var_medmg.get())
    ml=Decimal(var_medml.get())
    check = check_med.get()
    medicamento = combomed.get()
    dias=var_media.get()
    if check == 1:
        resultado = Decimal((peso * dosis * ml) / mg)
        print('corrio')
        print(resultado)
        manejo.insert('end', medicamento + ' '+str(var_medmg.get())+' mg/' + str(var_medml.get())+ ' ml '+ 'tomar  '+ str(resultado)+ ' ml cada '+horas+ ' por ' + str(dias)+' días. ')
    else:
        if horas == "6":
            a = round(((dosis*peso*ml)/mg)/4, 1)
            
            manejo.insert('end', medicamento + ' '+str(var_medmg.get())+' mg/' + str(var_medml.get())+ ' ml '+' tomar  '+str(a)+ ' ml cada '+horas+ ' por ' + str(dias)+' días. ' )
            print(a)
        elif horas == "8":
            a = round(((dosis*peso*ml)/mg)/3,1)
            
            manejo.insert('end', medicamento + ' '+str(var_medmg.get())+' mg/' + str(var_medml.get())+ ' ml '+' tomar  '+str(a)+ ' ml cada '+horas+ ' por ' + str(dias)+' días. ')
            print(a)
        elif horas == "12":
            a = round(((dosis*peso*ml)/mg)/2,1)
            manejo.insert('end', medicamento + ' '+str(var_medmg.get())+' mg/' + str(var_medml.get())+ ' ml '+' tomar  '+str(a)+ ' ml cada '+horas+ ' por ' + str(dias)+' días. ')
            print(a)
        else:
            a = round(((dosis*peso*ml)/mg),1)
            manejo.insert('end', medicamento + ' '+str(var_medmg.get())+' mg /' + str(var_medml.get())+ ' ml '+' tomar  '+str(a)+ ' ml cada '+horas+ ' por ' + str(dias)+' días. ')
            print(a)

def gen_receta():
    var_medico = combo_medico.get()
    print(var_medico)
    conexion = sqlite3.connect('notas.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM medico WHERE nombre=? ",(var_medico,))
    var_receta=cursor.fetchone()
    print(var_receta)
    pdf = FPDF()
    paciente_nombre=var_paterno.get() +" "+ var_materno.get() +" "+ var_nombre.get()
    var_nacimiento= var_dianacimiento.get()+"/"+var_mes.get()+"/"+var_ano.get()
    cedula = var_receta[2]
    cedula_esp = var_receta[3]
    fecha = datetime.datetime.now()
    medico = var_receta[1]
    #folio = 0
    pdf.add_page()

    pdf.set_font("Arial", size=10)
    pdf.set_xy(10,20)
    pdf.multi_cell(200,5,txt = "Dr."+medico+ "\nMedico Familiar\nXochicalco/UABC\n" +str(cedula)+"/"+str(cedula_esp),align = 'L')
    pdf.image('Picture1.png', x=135,y=0, w=31, h=20)
    pdf.set_xy(50,20)
    pdf.multi_cell(200,5,txt = "Av. Reforma #1000 y calle B, Telefono(686)552-2300\ncolonia Primera seccion, Mexicali, Baja California, C.p. 2110", align = 'C')

    pdf.set_xy(10,50)
    pdf.cell(100,10,txt="Nombre: "+paciente_nombre,align="L")

    pdf.set_xy(90,50)
    pdf.cell(100,10,txt="Edad: " +edad.get(),align="L",)
    pdf.set_xy(110,50)
    pdf.cell(110,10,txt="f.Nacimiento: " + var_nacimiento,align="L")
    pdf.set_xy(165,50)
    pdf.cell(110,10,txt="Fecha: "+fecha.strftime("%x"),align="L")

    pdf.image('Picture2.png', x=135,y=50)
    pdf.set_xy(10,80)
    pdf.multi_cell(0,5,txt = manejo.get("1.0","end-1c"), align = 'J', border=1)

    pdf.set_xy(10,250)
    pdf.multi_cell(200,5,txt = "FARMACIA\nHISPANO AMERICANO\nReforma #1007-A Colonia Primera Seccion\nTelefono 552-9487", align = 'L')

    pdf.set_xy(60,250)
    pdf.multi_cell(200,5,txt = "Dr."+medico+"\nMedico Familiar\nCed.Prof."+str(cedula)+"/"+str(cedula_esp), align = 'C')



    pdf.output("prueba.pdf")

def info():
    tk.messagebox.showinfo('Acerca de','Version: 20.02.24A\n Autor: Med.Luna Medico Familiar.\n apuntesmf.com \n Contacto: drlunamf@hotmail.com')
    

# ++++++++++++++++++++++++++++++++++++++
#   GENERA LOS TABS DE NAVEGACION
# ++++++++++++++++++++++++++++++++++++++


#barra de menu

menu_bar = Menu(ven)
ven.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
base_menu = Menu(menu_bar, tearoff=0)
gab_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label='Guardar lista de pacientes', command=excel)
file_menu.add_command(label='Acerca de', command=info)

menu_bar.add_cascade(label="Base de datos", menu=base_menu)
base_menu.add_command(label='Guardar paciente', command=paciente)
base_menu.add_command(label='Actualizar paciente', command=actualizar_paciente)

base_menu.add_command(label='Agregar y actualizar enfermedad ', command=n_enfermedad)
base_menu.add_command(label='Agregar medicamento', command=n_medicamento)

menu_bar.add_cascade(label="Gabinete", menu=gab_menu)
gab_menu.add_command(label='Laboratorios', command=lab)


#tabs
tabs = ttk.Notebook(ven)
tab1 = ttk.Frame(tabs)
tabs.add(tab1, text='Datos personales')
tabs.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabs)
tabs.add(tab2, text='Exploración física')
tabs.pack(expand=1, fill='both')


tab4 = ttk.Frame(tabs)
tabs.add(tab4, text='Analisis y manejo')
tabs.pack(expand=1, fill='both')

tab5 = ttk.Frame(tabs)
tabs.add(tab5, text='Nota final')
tabs.pack(expand=1, fill='both')


#texto que se insertara en las cajas de texo para explroacion fisica
t_alergia= 'Alergias a medicamentos negadas, '
t_enf= 'enfermedades crónico-degenerativas negadas, '
t_hosp= 'hospitalizaciones negadas, '
t_cir= 'cirugías negadas, '
t_trans= 'transfusiones negadas, '
t_trauma= 'traumatismos negados.'
# texto para no patologicos
t_etilismo = 'etilismo negado, '
t_tabaquismo = 'tabaquismo negado,'
t_drogas = ' uso de drogas negadas.'


# ++++++++++++++++++++++++++++++++++++++
#   Frame de nombre edad fecha de nacimiento
#   Domicilio, nnumero telefonico de contacto
# ++++++++++++++++++++++++++++++++++++++
#Nombre y apellido
frame_datospers = ttk.LabelFrame(tab1, text="Datos personales")# crea el frame para los datos del paciente.
frame_datospers.grid(column=0, row=0, pady=2)# asigna el espacio en el que aparecera el frame.

ttk.Label(frame_datospers, text="Sexo:").grid(column=0, row=0)
sexo=tk.StringVar()# No tengo idea de en donde este este
sexo_eleccion = ttk.Combobox(frame_datospers, width=12, textvariable=sexo)
sexo_eleccion["values"] = ("Masculino", "Femenino")
sexo_eleccion.grid(column=1, row=0)
sexo_eleccion.current(0)
button_s=ttk.Button(frame_datospers, text="buscar",command=buscar_paciente )
button_s.grid(column=2, row=0, padx=2)
ttk.Label(frame_datospers, text="Medico:").grid(column=3, row=0)
combo_medico = ttk.Combobox(
        frame_datospers,
        state="readonly",
        values= md,
    )
combo_medico.grid(column=4,row=0)


#etiquetas
ttk.Label(frame_datospers, text="Apellido Paterno").grid(column=0, row=1)
var_paterno = tk.StringVar() #crea la variable que asignara el valor de la nota
paterno = ttk.Entry(frame_datospers, width="20", textvariable=var_paterno)
paterno.grid(column=1, row=1) # crea la caja de texto para escribir la nota

ttk.Label(frame_datospers, text="Apellido Materno").grid(column=2, row=1)
var_materno = tk.StringVar() #crea la variable que asignara el valor de la nota
materno = ttk.Entry(frame_datospers, width="20", textvariable=var_materno)
materno.grid(column=3, row=1) # crea la caja de texto para escribir la nota

ttk.Label(frame_datospers, text="Nombres").grid(column=4, row=1)
var_nombre = tk.StringVar() #crea la variable que asignara el valor de la nota
nombre = ttk.Entry(frame_datospers, width="20", textvariable=var_nombre)
nombre.grid(column=5, row=1,padx=2, pady=4) # crea la caja de texto para escribir la nota

#Edad del paciente 
ttk.Label(frame_datospers, text="Edad").grid(column=0, row=2)
var_edad = tk.StringVar() #crea la variable que asignara el valor de la nota
edad = ttk.Entry(frame_datospers, width="10", textvariable=var_edad)
edad.grid(column=1, row=2,padx=2, pady=4) # crea la caja de texto para escribir la nota

#EFecha de naciemiento 
ttk.Label(frame_datospers, text="Fecha de nacimiento").grid(column=2, row=2,padx=2, pady=4)
ttk.Label(frame_datospers, text="dia").grid(column=3, row=2)
var_dianacimiento = tk.StringVar() #crea la variable que asignara el valor de la nota
f_dia = ttk.Entry(frame_datospers, width="10", textvariable=var_dianacimiento)
f_dia.grid(column=4, row=2,padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_datospers, text="mes").grid(column=5, row=2,padx=2, pady=4)
var_mes = tk.StringVar() #crea la variable que asignara el valor de la nota
f_mes = ttk.Entry(frame_datospers, width="10",text='mes', textvariable=var_mes)
f_mes.grid(column=6, row=2,padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_datospers, text="año").grid(column=7, row=2,padx=2, pady=4)
var_ano = tk.StringVar() #crea la variable que asignara el valor de la nota
f_ano = ttk.Entry(frame_datospers, width="10", textvariable=var_ano)
f_ano.grid(column=8, row=2,padx=2, pady=4) # crea la caja de texto para escribir la nota

# direccion y numero telefonico
ttk.Label(frame_datospers, text="Calle").grid(column=0, row=3,padx=2, pady=4)
var_calle = tk.StringVar()
calle = ttk.Entry(frame_datospers, width="20", textvariable=var_calle)
calle.grid(column=1, row=3,padx=2, pady=4)

ttk.Label(frame_datospers, text="Colonia").grid(column=2, row=3)
var_colonia = tk.StringVar()
colonia = ttk.Entry(frame_datospers, width="20", textvariable=var_colonia)
colonia.grid(column=3, row=3,padx=2, pady=4)

ttk.Label(frame_datospers, text="numero").grid(column=4, row=3)
var_numero = tk.StringVar()
numero = ttk.Entry(frame_datospers, width="20", textvariable=var_numero)
numero.grid(column=5, row=3,padx=2, pady=4)

ttk.Label(frame_datospers, text="codigo postal").grid(column=0, row=4)
var_postal = tk.StringVar()
postal = ttk.Entry(frame_datospers, width="20", textvariable=var_postal)
postal.grid(column=1, row=4,padx=2, pady=4)

ttk.Label(frame_datospers, text="Telefono").grid(column=2, row=4)
var_telefono = tk.StringVar()
telefono = ttk.Entry(frame_datospers, width="20", textvariable=var_telefono)
telefono.grid(column=3, row=4,padx=2, pady=4)

ttk.Label(frame_datospers,text='Seguro').grid(column=4, row=4, padx=2, pady=4)
combo_seguro = ttk.Combobox(
        frame_datospers,
        state="readonly",
        values= seguro,
    )
combo_seguro.grid(column=5, row=4, padx=2, pady=4)

ttk.Label(frame_datospers, text=fecha).grid(column=6, row=4)
#########################################
#Antecedentes personales patologicos
########################################

frame_patologicosp = ttk.LabelFrame(tab1, text="Antecedentes")# crea el frame para los datos patologicos
frame_patologicosp.grid(column=0, row=1, padx=2, pady=4)# asigna el espacio en el que aparecera el frame.

ttk.Label(frame_patologicosp, text="Alergias").grid(column=0, row=0, padx=2, pady=4)
var_alergias = tk.StringVar() #crea la variable que asignara el valor de la nota
alergia = ttk.Entry(frame_patologicosp, width="20", textvariable=var_alergias)
alergia.grid(column=1, row=0, padx=2, pady=4) # crea la caja de texto para escribir la nota
alergia.insert("end", t_alergia)
ttk.Label(frame_patologicosp, text="Enfermedades").grid(column=2, row=0, padx=2, pady=4)
var_enfermedades = tk.StringVar() #crea la variable que asignara el valor de la nota
enfermedades = ttk.Entry(frame_patologicosp, width="20", textvariable=var_enfermedades)
enfermedades.grid(column=3, row=0, padx=2, pady=4) # crea la caja de texto para escribir la nota
enfermedades.insert("end", t_enf)
ttk.Label(frame_patologicosp, text="Hospitalizaciones").grid(column=4, row=0, padx=2, pady=4)
var_hospitalizacion = tk.StringVar() #crea la variable que asignara el valor de la nota
hospitalizacion = ttk.Entry(frame_patologicosp, width="20", textvariable=var_hospitalizacion)
hospitalizacion.grid(column=5, row=0,padx=2, pady=4) # crea la caja de texto para escribir la nota
hospitalizacion.insert("end", t_hosp)
ttk.Label(frame_patologicosp, text="Cirugias").grid(column=0, row=1,padx=2, pady=4)
var_cirugias = tk.StringVar() #crea la variable que asignara el valor de la nota
cirugia = ttk.Entry(frame_patologicosp, width="20", textvariable=var_cirugias)
cirugia.grid(column=1, row=1,padx=2, pady=4) # crea la caja de texto para escribir la nota
cirugia.insert("end", t_cir)
ttk.Label(frame_patologicosp, text="Traumatismos").grid(column=2, row=1,padx=2, pady=4)
var_traumatismos = tk.StringVar() #crea la variable que asignara el valor de la nota
traumatismo = ttk.Entry(frame_patologicosp, width="20", textvariable=var_traumatismos)
traumatismo.grid(column=3, row=1,padx=2, pady=4) # crea la caja de texto para escribir la nota
traumatismo.insert("end", t_trauma)
ttk.Label(frame_patologicosp, text="Transfusiones").grid(column=4, row=1,padx=2, pady=4)
var_transfusiones = tk.StringVar() #crea la variable que asignara el valor de la nota
transfusion = ttk.Entry(frame_patologicosp, width="20", textvariable=var_transfusiones)
transfusion.grid(column=5, row=1,padx=2, pady=4) # crea la caja de texto para escribir la nota
transfusion.insert("end", t_trans)

#####################################
#Antecedentes personales patologicos
######################################
frame_patologicosp = ttk.LabelFrame(tab1, text="Antecedentes no patologicos")# crea el frame para los datos patologicos
frame_patologicosp.grid(column=0, row=2, padx=2, pady=4)# asigna el espacio en el que aparecera el frame.

ttk.Label(frame_patologicosp, text="Etilismo").grid(column=0, row=0,padx=2, pady=4)
var_etilismo = tk.StringVar() #crea la variable que asignara el valor de la nota
etilico = ttk.Entry(frame_patologicosp, width="20", textvariable=var_etilismo)
etilico.grid(column=1, row=0, padx=2, pady=4) # crea la caja de texto para escribir la nota
etilico.insert("end", t_etilismo)
ttk.Label(frame_patologicosp, text="Tabaquismo").grid(column=2, row=0)
var_tabaco = tk.StringVar() #crea la variable que asignara el valor de la nota
tabaco = ttk.Entry(frame_patologicosp, width="20", textvariable=var_tabaco)
tabaco.grid(column=3, row=0, padx=2, pady=4) # crea la caja de texto para escribir la nota
tabaco.insert("end", t_tabaquismo)
ttk.Label(frame_patologicosp, text="Toxicomanias").grid(column=4, row=0, padx=2, pady=4)
var_toxicomania = tk.StringVar() #crea la variable que asignara el valor de la nota
toxicomania = ttk.Entry(frame_patologicosp, width="20", textvariable=var_toxicomania)
toxicomania.grid(column=5, row=0, padx=2, pady=4) # crea la caja de texto para escribir la nota
toxicomania.insert("end", t_drogas)
ttk.Label(frame_patologicosp, text="Otros").grid(column=0, row=1, padx=2, pady=4)
var_otros = tk.StringVar() #crea la variable que asignara el valor de la nota
otros = ttk.Entry(frame_patologicosp, width="20", textvariable=var_otros)
otros.grid(column=1, row=1, padx=2, pady=4) # crea la caja de texto para escribir la nota

#####################
#Antecedentes gyo
####################

frame_gyo = ttk.LabelFrame(tab1, text="GyO")# crea el frame para los datos patologicos
frame_gyo.grid(column=0, row=3, padx=2, pady=4)# asigna el espacio en el que aparecera el frame.

ttk.Label(frame_gyo, text="Menarca").grid(column=0, row=0, padx=2, pady=4)
var_menarca = tk.StringVar() #crea la variable que asignara el valor de la nota
menarca = ttk.Entry(frame_gyo, width="20", textvariable=var_menarca)
menarca.grid(column=1, row=0, padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_gyo, text="IVSA").grid(column=2, row=0,padx=2, pady=4)
var_ivsa = tk.StringVar() #crea la variable que asignara el valor de la nota
ivsa = ttk.Entry(frame_gyo, width="20", textvariable=var_ivsa)
ivsa.grid(column=3, row=0,padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_gyo, text="NPSA").grid(column=4, row=0, padx=2, pady=4)
var_npsa = tk.StringVar() #crea la variable que asignara el valor de la nota
npsa = ttk.Entry(frame_gyo, width="20", textvariable=var_npsa)
npsa.grid(column=5, row=0, padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_gyo, text="Gestas").grid(column=2, row=1, padx=2, pady=4)
var_gesta = tk.StringVar() #crea la variable que asignara el valor de la nota
gesta = ttk.Entry(frame_gyo, width="20", textvariable=var_gesta)
gesta.grid(column=3, row=1, padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_gyo, text="Partos").grid(column=4, row=1, padx=2, pady=4)
var_parto = tk.StringVar() #crea la variable que asignara el valor de la nota
parto = ttk.Entry(frame_gyo, width="20", textvariable=var_parto)
parto.grid(column=5, row=1, padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_gyo, text="Cesareas").grid(column=0, row=2, padx=2, pady=4)
var_cesarea = tk.StringVar() #crea la variable que asignara el valor de la nota
cesarea = ttk.Entry(frame_gyo, width="20", textvariable=var_cesarea)
cesarea.grid(column=1, row=2, padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_gyo, text="Abortos").grid(column=2, row=2, padx=2, pady=4)
var_aborto = tk.StringVar() #crea la variable que asignara el valor de la nota
aborto = ttk.Entry(frame_gyo, width="20", textvariable=var_aborto)
aborto.grid(column=3, row=2, padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_gyo, text="Citologias").grid(column=4, row=2, padx=2, pady=4)
var_citologia = tk.StringVar() #crea la variable que asignara el valor de la nota
citologia = ttk.Entry(frame_gyo, width="20", textvariable=var_citologia)
citologia.grid(column=5, row=2, padx=2, pady=4) # crea la caja de texto para escribir la nota

# apartado para agregar los datos apra el calculo de fecha probable de parto asi como de semanas de gestacion.
ttk.Label(frame_gyo, text="Fecha de Ultima Menstruacion").grid(column=0, row=3, padx=2, pady=4)
ttk.Label(frame_gyo, text="Dia").grid(column=0, row=4, padx=2, pady=4)
dia_cb=ttk.Combobox(frame_gyo,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"] )
dia_cb.grid(column=1, row=4)
ttk.Label(frame_gyo, text="Mes").grid(column=2, row=4, padx=2, pady=4)
mes_cb=ttk.Combobox(frame_gyo,values=["1","2","3","4","5","6","7","8","9","10","11","12"] )
mes_cb.grid(column=3, row=4, padx=2, pady=4)
ttk.Label(frame_gyo, text="Ano").grid(column=4, row=4, padx=2, pady=4)
var_menstruacion = tk.StringVar() #crea la variable que asignara el valor de la nota
ano_cb = ttk.Entry(frame_gyo, width="20", textvariable=var_menstruacion)
ano_cb.grid(column=5, row=4)

#######################
#Antecedentes embarazo
#######################
frame_embarazo = ttk.LabelFrame(tab1, text="Embarazo")# crea el frame para los datos patologicos
frame_embarazo.grid(column=0, row=4, padx=2, pady=4)# asigna el espacio en el que aparecera el frame.

check_embarazo = tk.IntVar()
check = tk.Checkbutton(frame_embarazo, text="Positivo", variable=check_embarazo)
check.grid(column=0, row=0, padx=2, pady=4)

ttk.Label(frame_embarazo, text="Semanas de gestacion por FUM").grid(column=1, row=0, padx=2, pady=4)
var_sdg = tk.StringVar() #crea la variable que asignara el valor de la nota
sdg = ttk.Entry(frame_embarazo, width="20", textvariable=var_sdg)
sdg.grid(column=2, row=0, padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_embarazo, text="Semanas de gestacion por ultrasonido").grid(column=3, row=0, padx=2, pady=4)
var_usg = tk.StringVar() #crea la variable que asignara el valor de la nota
usg = ttk.Entry(frame_embarazo, width="20", textvariable=var_usg)
usg.grid(column=4, row=0, padx=2, pady=4) # crea la caja de texto para escribir la nota

frame_actual = ttk.LabelFrame(tab1, text="Padecimiento actual")# crea el frame para los datos patologicos
frame_actual.grid(column=0, row=5, padx=2, pady=4)

ttk.Label(frame_actual, text="Padecimiento actual").grid(column=0, row=0, padx=2, pady=4)
#var_actual = tk.StringVar() #crea la variable que asignara el valor de la nota
actual = ScrolledText(frame_actual, width="60", height=4)
actual.grid(column=1, row=0, padx=2, pady=4) # crea la caja de texto para escribir la nota

#####################
#Frame exploracion fisica
#####################
frame_signos = ttk.LabelFrame(tab2, text="Signos vitales")
frame_signos.grid(column=0, row=0, padx=2, pady=4)

#
#SIGNOS VITALES
#
ttk.Label(frame_signos, text="Peso").grid(column=0, row=0, padx=2, pady=4)
var_kg = tk.IntVar() #crea la variable que asignara el valor de la nota
kg = ttk.Entry(frame_signos, width="20", textvariable=var_kg)
kg.grid(column=1, row=0, padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_signos, text="Tension arterial").grid(column=2, row=0, padx=2, pady=4)
var_tension = tk.StringVar() #crea la variable que asignara el valor de la nota
svt = ttk.Entry(frame_signos, width="20", textvariable=var_tension)
svt.grid(column=3, row=0, padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_signos, text="Frecuencia cardiaca").grid(column=4, row=0, padx=2, pady=4)
var_fc = tk.StringVar() #crea la variable que asignara el valor de la nota
fc = ttk.Entry(frame_signos, width="20", textvariable=var_fc)
fc.grid(column=5, row=0, padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_signos, text="Frecuencia respiratoria").grid(column=0, row=1, padx=2, pady=4)
var_fr = tk.StringVar() #crea la variable que asignara el valor de la nota
fr = ttk.Entry(frame_signos, width="20", textvariable=var_fr)
fr.grid(column=1, row=1, padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_signos, text="Temperatura corporal").grid(column=2, row=1, padx=2, pady=4)
var_temp = tk.StringVar() #crea la variable que asignara el valor de la nota
tc = ttk.Entry(frame_signos, width="20", textvariable=var_temp)
tc.grid(column=3, row=1, padx=2, pady=4) # crea la caja de texto para escribir la nota

ttk.Label(frame_signos, text="Saturacion O2").grid(column=4, row=1, padx=2, pady=4)
var_sat = tk.StringVar() #crea la variable que asignara el valor de la nota
sat = ttk.Entry(frame_signos, width="20", textvariable=var_sat)
sat.grid(column=5, row=1, padx=2, pady=4) # crea la caja de texto para escribir la nota

#
#frame de seleccion o nueva enfermedad
#
frame_enfermedad = ttk.LabelFrame(tab2)
frame_enfermedad.grid(column=0, row=1, padx=2, pady=4)
ttk.Label(frame_enfermedad, text="Consulta").grid(column=0,row=0)

combo = ttk.Combobox(
        frame_enfermedad,
        state="readonly",
        values= dc
    )
combo.grid(column=0,row=1)

boton = ttk.Button(frame_enfermedad, text='seleccionar', command=seleccionar)
boton.grid(column=3,row=1)

ttk.Label(frame_enfermedad, text="Urgencias").grid(column=0,row=2)

combo2 = ttk.Combobox(
        frame_enfermedad,
        state="readonly",
        values= ux
    )
combo2.grid(column=0,row=3)

boton = ttk.Button(frame_enfermedad, text='seleccionar', command=seleccionar_u)
boton.grid(column=3,row=3)

########################################################
#APARTADO DE LA EXPLORACION
##########################################
frame_exploracion = ttk.LabelFrame(tab2, text="Exploracion Fisica")
frame_exploracion.grid(column=0, row=2, padx=2, pady=4)



ttk.Label(frame_exploracion, text="Neurologico").grid(column=0,row=0, padx=2, pady=4)
var_neuro = tk.StringVar()
txt_neuro = ScrolledText(frame_exploracion, height=4, width="60")
txt_neuro.grid(column=1, row=0, padx=2, pady=4)


ttk.Label(frame_exploracion, text="Piel y tegumentos").grid(column=0,row=1, padx=2, pady=4)
var_piel = tk.StringVar()
piel = ScrolledText(frame_exploracion, height=4, width="60")
piel.grid(column=1,row=1, padx=2, pady=4)


ttk.Label(frame_exploracion, text="Cabeza").grid(column=0,row=2, padx=2, pady=4)
var_cabeza = tk.StringVar()
cabeza = ScrolledText(frame_exploracion, height=4, width="60")
cabeza.grid(column=1,row=2, padx=2, pady=4)

ttk.Label(frame_exploracion, text="Cuello").grid(column=0,row=3, padx=2, pady=4)
var_cuello = tk.StringVar()
cuello = ScrolledText(frame_exploracion, height=4, width="60")
cuello.grid(column=1,row=3, padx=2, pady=4)


ttk.Label(frame_exploracion, text="Torax").grid(column=0,row=4, padx=2, pady=4)
var_torax = tk.StringVar()
torax = ScrolledText(frame_exploracion, height=4, width="60")
torax.grid(column=1,row=4, padx=2, pady=4)

ttk.Label(frame_exploracion, text="Abdomen").grid(column=0,row=5, padx=2, pady=4)
var_abdomen = tk.StringVar()
abdomen = ScrolledText(frame_exploracion, height=4, width="60")
abdomen.grid(column=1,row=5, padx=2, pady=4)


ttk.Label(frame_exploracion, text="Genitales").grid(column=0,row=6, padx=2, pady=4)
var_genitales = tk.StringVar()
genitales = ScrolledText(frame_exploracion, height=4, width="60")
genitales.grid(column=1,row=6, padx=2, pady=4)


ttk.Label(frame_exploracion, text="Extremidades").grid(column=0,row=7, padx=2, pady=4)
var_extremidades = tk.StringVar()
extremidades = ScrolledText(frame_exploracion, height=4, width="60")
extremidades.grid(column=1,row=7, padx=2, pady=4)


########################
#ANALISIS Y MANEJO
############################
frame_analisis = ttk.LabelFrame(tab4, text="Analisis")
frame_analisis.grid(column=0, row=0, padx=2, pady=4)

ttk.Label(frame_analisis, text="Analisis").grid(column=0, row=1, padx=2, pady=4)

var_analisis=tk.StringVar()
analisis = ttk.Entry(frame_analisis, width="60", textvariable=var_analisis)
analisis.grid(column=1, row=0, padx=2, pady=4)

frame_manejo = ttk.LabelFrame(tab4)
frame_manejo.grid(column=0, row=2, padx=2, pady=4)


ttk.Label(frame_manejo, text="Analisis").grid(column=0, row=0, padx=2, pady=4)
txt_analisis = ScrolledText(frame_manejo, height=7, width="60")
txt_analisis.grid(column=1, row=0, padx=2, pady=4)

ttk.Label(frame_manejo, text="Manejo").grid(column=0, row=1, padx=2, pady=4)
manejo = ScrolledText(frame_manejo, height=7, width="60")
manejo.grid(column=1, row=1, padx=2, pady=4)


frame_generar = ttk.LabelFrame(tab4, text="Diagnostico")
frame_generar.grid(column=0, row=3, padx=2, pady=4)

ttk.Label(frame_generar,text='Diagnostico').grid(column=0, row=0, padx=2, pady=4)
var_diagnostico=tk.StringVar()
diagnostico = ttk.Entry(frame_generar, width="60", textvariable=var_diagnostico)
diagnostico.grid(column=1, row=0, padx=2, pady=4)

#se crea el frame para agregar los medicamentos a la nota y receta
frame_med = ttk.LabelFrame(tab4, text="Medicamentos")
frame_med.grid(column=0, row=0, padx=2, pady=4)

#combobox para seleccionar medicamentos
ttk.Label(frame_med,text='Medicamento').grid(column=0, row=0, padx=2, pady=4)
combomed = ttk.Combobox(
        frame_med,
        state="readonly",
        values= sal,
    )
combomed.grid(column=1, row=0, padx=2, pady=4)

#Variables para agregar la presentacion del medicamento
ttk.Label(frame_med,text='Mg').grid(column=0, row=1, padx=2, pady=4)
var_medmg=tk.IntVar()
medmg = ttk.Entry(frame_med, width="5", textvariable=var_medmg)
medmg.grid(column=1, row=1, padx=2, pady=4)
ttk.Label(frame_med,text='/').grid(column=2, row=1, padx=2, pady=4)
ttk.Label(frame_med,text='Mg').grid(column=3, row=1, padx=2, pady=4)
var_medmg2=tk.IntVar()
medmg2 = ttk.Entry(frame_med, width="5", textvariable=var_medmg2)
medmg2.grid(column=4, row=1, padx=2, pady=4)
ttk.Label(frame_med,text='/').grid(column=5, row=1, padx=2, pady=4)
ttk.Label(frame_med,text='Ml').grid(column=6, row=1, padx=2, pady=4)
var_medml=tk.IntVar()
medml = ttk.Entry(frame_med, width="5", textvariable=var_medml)
medml.grid(column=7, row=1, padx=2, pady=4)

#Variables para agregar la dosis a calcular del medicamento.
ttk.Label(frame_med,text='Dosis').grid(column=0, row=2, padx=2, pady=4)
var_dosis=tk.IntVar()
dosis = ttk.Entry(frame_med, width="10", textvariable=var_dosis)
dosis.grid(column=1,row=2, padx=2, pady=4)

#Variables para agregar los horarios del medicamento.
ttk.Label(frame_med,text='Hrs').grid(column=0, row=3, padx=2, pady=4)
dia_med=ttk.Combobox(frame_med, width="5", values=[6,8,12,24] )
dia_med.grid(column=1, row=3, padx=2, pady=4)

ttk.Label(frame_med,text='Dias').grid(column=0, row=4, padx=2, pady=4)
var_media=tk.IntVar()
media = ttk.Entry(frame_med, width="10", textvariable=var_media)
media.grid(column=1, row=4, padx=2, pady=4)

check_med = tk.IntVar()
checkmed = tk.Checkbutton(frame_med, text="dosis", variable=check_med)
checkmed.grid(column=2, row=4, padx=2, pady=4)


#############################################
# BOTONES PARA GENERAR LAS NOTAS Y LIMPIEZA
###########################################
frame_nota = ttk.LabelFrame(tab5, text="Nota")
frame_nota.grid(column=0, row=0, pady=2, padx=2)

g_nota = ScrolledText(frame_nota, font=("Arial", 12),width="60", height="30")
g_nota.grid(column=0, row=0, padx=2)

ttk.Label(frame_nota,text='fechas').grid(column=1, row=0, padx=2, pady=4)
lista_fecha = tk.Listbox(
        frame_nota,
    )
lista_fecha.grid(column=2, row=0, padx=2, pady=4)
lista_fecha.bind('<<ListboxSelect>>', cargar_nota)

status=ttk.Label(frame_nota,text='Guardado', foreground='red')
status.grid(column=1, row=1, padx=2, pady=4)

frame_opciones = ttk.LabelFrame(tab5, text="Opciones")#Genera el frame para los botones de opciones para generar notas o almacenar en base de datos y formato de texto
frame_opciones.grid(column=0, row=1, padx=2)

generar_inicial = ttk.Button(frame_opciones, text="Generar historia clinica", command=gen_historia)
generar_inicial.grid(column=0, row=0, padx=2)

generar = ttk.Button(frame_opciones, text="Generar nota de consulta", command=evo)
generar.grid(column=1, row=0, padx=2)

guardar = ttk.Button(frame_opciones, text="Guardar archivo", command=nota_texto)
guardar.grid(column=1, row=1, padx=2)

nuevo = ttk.Button(frame_opciones, text="Limpiar", command=n_limpiar)
nuevo.grid(column=0, row=1, padx=2)

boton_receta = ttk.Button(frame_opciones, text="imprir receta", command=gen_receta)
boton_receta.grid(column=6, row=1, padx=2)

boton_suma= ttk.Button(frame_opciones, text="imprir receta", command=lambda:calculo.suma(var_kg.get(),5))
boton_suma.grid(column=6, row=2, padx=2)

add_med = ttk.Button(frame_med, text="Agregar medicamento", command=receta)
add_med.grid(column=0, row=6, padx=2)

cargar_medicina = ttk.Button(frame_med, text="cargar datos", command=cargar_med)
cargar_medicina.grid(column=2, row=0, padx=2)


#========================
#   INICIA LA VENTANA
#========================
ven.bind("<Control-g>",pres_a)
ven.mainloop()
