import tkinter as tk
from tkinter import VERTICAL, Y, DoubleVar, Scrollbar, ttk, scrolledtext, Menu
from tkinter import messagebox as msg
from tkinter.scrolledtext import ScrolledText
from tkinter import Menu
from decimal import *

ven = tk.Tk()
ven.title("pacientes")


def info():
    tk.messagebox.showinfo('Acerca de','Version: 29.04.23A\n Creador: R3MF Luna')
    
def evo():
    g_check = check_embarazo.get()
    g_check2 = check_roja.get()
    g_check3 = check_blanca.get()
    g_check4 = check_quimica.get()
    g_check5 = check_otro.get()

    g_serieroja = 'hemoglobina: ' + var_hemo.get() +', eritrocitos: ' + var_eritros.get() +', hematocrito: ' + var_hemato.get()+', vcm: ' +vcm.get() +', hcm: ' +var_hcm.get() +', chmg: ' + var_cmhg.get() +', plt: ' + var_plaqueta.get() 
    g_serieblanca ='Leucocitos: ' +var_leuco.get() +', neutrofilos: ' + var_neutro.get() +', linfocitos: ' +var_linfo.get() +', monocitos: ' + var_mono.get() +', eosinofilos: ' + var_eos.get() +', basofilos: ' + var_baso.get() +', neutrofilos#: ' +var_neutro2.get() +', linfocitos#: ' + var_linfo2.get() +', monocitos#: ' + var_mono2.get() +', eosinofilos#: ' + var_eos2.get() +', basofilos#: ' + var_baso2.get()
    g_quimica = 'glucosa: ' +var_gluc.get() +', urea: ' + var_urea.get() +'creatinina: ' + var_creatinina.get() +', bun: ' + var_nitro.get() +', colesterol total: ' + var_colesterol.get() +', ldl: ' + var_ldl.get() +', hdl: ' + var_hdl.get() +', vldl: ' + var_vldl.get() +', alt: ' + var_alt.get() +', ast: ' + var_ast.get() +', Bilirrubina total: ' + var_bt.get() +', Bilirrubina directa: ' + var_bd.get() +', bilirrubina indirecta: ' + var_bi.get() +', HbA1c: ' + var_hglu.get() +', Fosfatasa alcalina: ' + var_fa.get() +', ggt: ' + var_ggt.get() +', Na: ' + var_na.get() +', K: ' + var_k.get() +', Ca: ' + var_ca.get() +', Cl: ' + var_cl.get()
    g_otro = var_labotro.get()
   
    g_signos = "Tension arterial: " + var_tension.get() + ", Frecuencia cardiaca: " + var_fr.get() + ", Frecuencia respiratoria: " + var_fr.get() + ", Temperatura: " + var_temp.get() + ", Saturacion: " + var_sat.get()
    g_nombre = var_paterno.get() + " " + var_materno.get() +" "+ var_nombre.get()
    g_pp = var_alergias.get() + var_enfermedades.get() + var_hospitalizacion.get() + var_cirugias.get() + var_transfusiones.get() + var_traumatismos.get()
    g_np = var_etilismo.get() + var_tabaco.get() + var_toxicomania.get()
    g_gyo = "Menarca: "+ var_menarca.get() + ", Inicio de vida sexual activa: " + var_ivsa.get() + ", numero de parejas sexualmente activas: "+ var_npsa.get() + ", gestas: "+ var_gesta.get() + ", partos: "+ var_parto.get() + ", cesarea: "+ var_cesarea.get() + ", aborto: "+ var_aborto.get() + ", citologias: "+ var_citologia.get() + ", fecha de ultima menstruacion: "+ var_menstruacion.get()
    g_ef = var_neuro.get() + var_piel.get() + var_cabeza.get() + var_cuello.get() + var_torax.get() + var_abdomen.get() + var_genitales.get() + var_extremidades.get()
    g_actual = var_actual.get()
    g_diagnostico = var_diagnostico.get()
    g_manejo = "\n\nMedicamentos\n\n" +var_manejo.get()

    if sexo_eleccion.get() == "Femenino":
        if g_check == 1:
            if g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSemanas de gestacion por fum: " +var_sdg.get()+ ", semanas de gestacion por ultrasonido: "+ var_usg.get() + "\n\nAPNP: "+g_np+"\n\nSignos vitales: " + g_signos + ".\n\nExploracion fisica:"+g_ef+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+".\n\nManejo:" +g_manejo )
            elif g_check2 == 1 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSemanas de gestacion por fum: " +var_sdg.get()+ ", semanas de gestacion por ultrasonido: "+ var_usg.get() +"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieroja+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
            elif g_check2 == 0 and g_check3 == 1 and g_check4 == 0 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSemanas de gestacion por fum: " +var_sdg.get()+ ", semanas de gestacion por ultrasonido: "+ var_usg.get() +"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieblanca+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
            elif g_check2 == 0 and g_check3 == 0 and g_check4 == 1 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSemanas de gestacion por fum: " +var_sdg.get()+ ", semanas de gestacion por ultrasonido: "+ var_usg.get() +"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_quimica+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
            elif g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 1:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSemanas de gestacion por fum: " +var_sdg.get()+ ", semanas de gestacion por ultrasonido: "+ var_usg.get() +"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_otro+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
            elif g_check2 == 1 and g_check3 == 1 and g_check4 == 1 and g_check5 == 1:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSemanas de gestacion por fum: " +var_sdg.get()+ ", semanas de gestacion por ultrasonido: "+ var_usg.get() +"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieroja + g_serieblanca + g_quimica + g_otro +".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
        else:
            if g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+ "\n\nAPNP: "+g_np+"\n\nSignos vitales: " + g_signos + ".\n\nExploracion fisica:"+g_ef+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
            elif g_check2 == 1 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieroja+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
            elif g_check2 == 0 and g_check3 == 1 and g_check4 == 0 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieblanca+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
            elif g_check2 == 0 and g_check3 == 0 and g_check4 == 1 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_quimica+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
            elif g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 1:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_otro+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
            elif g_check2 == 1 and g_check3 == 1 and g_check4 == 1 and g_check5 == 1:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieroja + g_serieblanca + g_quimica + g_otro +".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
    else:
        if g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+ "\n\nAPNP: "+g_np+"\n\nSignos vitales: " + g_signos + ".\n\nExploracion fisica:"+g_ef+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
        elif g_check2 == 1 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieroja+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
        elif g_check2 == 0 and g_check3 == 1 and g_check4 == 0 and g_check5 == 0:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieblanca+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
        elif g_check2 == 0 and g_check3 == 0 and g_check4 == 1 and g_check5 == 0:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_quimica+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
        elif g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 1:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_otro+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )
        elif g_check2 == 1 and g_check3 == 1 and g_check4 == 1 and g_check5 == 1:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieroja + g_serieblanca + g_quimica + g_otro +".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico+ ".\n\nManejo:" +g_manejo )

def gen_historia():
    #Funcion para generar las notas del paciente, almacena los valores en variables y finalmente lo agrega al scrolledtext para su revision modificacion y copiado.
    g_check = check_embarazo.get()
    g_check2 = check_roja.get()
    g_check3 = check_blanca.get()
    g_check4 = check_quimica.get()
    g_check5 = check_otro.get()

    g_serieroja = 'hemoglobina: ' + var_hemo.get() +', eritrocitos: ' + var_eritros.get() +', hematocrito: ' + var_hemato.get()+', vcm: ' +vcm.get() +', hcm: ' +var_hcm.get() +', chmg: ' + var_cmhg.get() +', plt: ' + var_plaqueta.get() 
    g_serieblanca ='Leucocitos: ' +var_leuco.get() +', neutrofilos: ' + var_neutro.get() +', linfocitos: ' +var_linfo.get() +', monocitos: ' + var_mono.get() +', eosinofilos: ' + var_eos.get() +', basofilos: ' + var_baso.get() +', neutrofilos#: ' +var_neutro2.get() +', linfocitos#: ' + var_linfo2.get() +', monocitos#: ' + var_mono2.get() +', eosinofilos#: ' + var_eos2.get() +', basofilos#: ' + var_baso2.get()
    g_quimica = 'glucosa: ' +var_gluc.get() +', urea: ' + var_urea.get() +'creatinina: ' + var_creatinina.get() +', bun: ' + var_nitro.get() +', colesterol total: ' + var_colesterol.get() +', ldl: ' + var_ldl.get() +', hdl: ' + var_hdl.get() +', vldl: ' + var_vldl.get() +', alt: ' + var_alt.get() +', ast: ' + var_ast.get() +', Bilirrubina total: ' + var_bt.get() +', Bilirrubina directa: ' + var_bd.get() +', bilirrubina indirecta: ' + var_bi.get() +', HbA1c: ' + var_hglu.get() +', Fosfatasa alcalina: ' + var_fa.get() +', ggt: ' + var_ggt.get() +', Na: ' + var_na.get() +', K: ' + var_k.get() +', Ca: ' + var_ca.get() +', Cl: ' + var_cl.get()
    g_otro = var_labotro.get()

    g_signos = "Tension arterial: " + var_tension.get() + "Frecuencia cardiaca: " + var_fr.get() + ",Frecuencia respiratoria: " + var_fr.get() + ",Temperatura: " + var_temp.get() + ",Saturacion: " + var_sat.get()
    g_nombre = var_paterno.get() + " " + var_materno.get() +" "+ var_nombre.get()
    g_direccion = var_calle.get() + ", colonia: "+var_colonia.get() +", numero: " + var_numero.get() +", codigo postal: " + var_postal.get()
    g_pp = var_alergias.get() + var_enfermedades.get() + var_hospitalizacion.get() + var_cirugias.get() + var_transfusiones.get() + var_traumatismos.get()
    g_np = var_etilismo.get() + var_tabaco.get() + var_toxicomania.get()
    g_gyo = "Menarca: "+ var_menarca.get() + ", Inicio de vida sexual activa: " + var_ivsa.get() + ", numero de parejas sexualmente activas: "+ var_npsa.get() + ", gestas: "+ var_gesta.get() + ", partos: "+ var_parto.get() + ", cesarea: "+ var_cesarea.get() + ", aborto: "+ var_aborto.get() + ", citologias: "+ var_citologia.get() + ", fecha de ultima menstruacion: "+ var_menstruacion.get()
    g_ef = var_neuro.get() + var_piel.get() + var_cabeza.get() + var_cuello.get() + var_torax.get() + var_abdomen.get() + var_genitales.get() + var_extremidades.get()
    g_actual = var_actual.get()
    g_diagnostico = var_diagnostico.get()

    if sexo_eleccion.get() == "Femenino":
        if g_check == 1:
            if g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSemanas de gestacion por fum: " +var_sdg.get()+ ", semanas de gestacion por ultrasonido: "+ var_usg.get() + "\n\nAPNP: "+g_np+"\n\nSignos vitales: " + g_signos + ".\n\nExploracion fisica:"+g_ef+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
            elif g_check2 == 1 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSemanas de gestacion por fum: " +var_sdg.get()+ ", semanas de gestacion por ultrasonido: "+ var_usg.get() +"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieroja+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
            elif g_check2 == 0 and g_check3 == 1 and g_check4 == 0 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSemanas de gestacion por fum: " +var_sdg.get()+ ", semanas de gestacion por ultrasonido: "+ var_usg.get() +"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieblanca+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
            elif g_check2 == 0 and g_check3 == 0 and g_check4 == 1 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSemanas de gestacion por fum: " +var_sdg.get()+ ", semanas de gestacion por ultrasonido: "+ var_usg.get() +"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_quimica+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
            elif g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 1:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSemanas de gestacion por fum: " +var_sdg.get()+ ", semanas de gestacion por ultrasonido: "+ var_usg.get() +"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_otro+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
            elif g_check2 == 1 and g_check3 == 1 and g_check4 == 1 and g_check5 == 1:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSemanas de gestacion por fum: " +var_sdg.get()+ ", semanas de gestacion por ultrasonido: "+ var_usg.get() +"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieroja + g_serieblanca + g_quimica + g_otro +".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
        else:
            if g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+ "\n\nAPNP: "+g_np+"\n\nSignos vitales: " + g_signos + ".\n\nExploracion fisica:"+g_ef+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
            elif g_check2 == 1 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+ "\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieroja+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico +".\n\nManejo:" +var_manejo.get() )
            elif g_check2 == 0 and g_check3 == 1 and g_check4 == 0 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+ "\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieblanca+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
            elif g_check2 == 0 and g_check3 == 0 and g_check4 == 1 and g_check5 == 0:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+ "\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_quimica+".\n\nAnalisis:"+var_analisis.get()++ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
            elif g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 1:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_otro+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
            elif g_check2 == 1 and g_check3 == 1 and g_check4 == 1 and g_check5 == 1:
                g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nAntecedentes gineco-obstetricos: "+g_gyo+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieroja + g_serieblanca + g_quimica + g_otro +".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
    else:
        if g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+ "\n\nAPNP: "+g_np+"\n\nSignos vitales: " + g_signos + ".\n\nExploracion fisica:"+g_ef+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
        elif g_check2 == 1 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieroja+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
        elif g_check2 == 0 and g_check3 == 1 and g_check4 == 0 and g_check5 == 0:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieblanca+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
        elif g_check2 == 0 and g_check3 == 0 and g_check4 == 1 and g_check5 == 0:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_quimica+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico + ".\n\nManejo:" +var_manejo.get() )
        elif g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 1:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() + "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_otro+".\n\nAnalisis:"+var_analisis.get()+ "\n\nDiagnostico: "+g_diagnostico +".\n\nManejo:" +var_manejo.get() )
        elif g_check2 == 1 and g_check3 == 1 and g_check4 == 1 and g_check5 == 1:
            g_nota.insert("end","Nombre:" + g_nombre + "\nFecha de nacimiento: " + var_nacimiento.get() + "\nEdad: " + var_edad.get() + "\nDireccion: "+g_direccion+ "\nNumero de telefono: " + var_numero.get() +  "\n\nPadecimiento actual:" + g_actual +"\n\nAPP: " +g_pp+"\n\nSignos vitales: " + g_signos +  ".\n\nExploracion fisica:"+g_ef+ "\n\nLaboratorios: " + g_serieroja + g_serieblanca + g_quimica + g_otro +".\n\nAnalisis:"+var_analisis.get()+ ".\n\nManejo:" +var_manejo.get() )

def nota_texto():
    #GENERA LA NOTA EN UN ARCHIVO DE TEXTO
    g_check = check_embarazo.get()
    g_check2 = check_roja.get()
    g_check3 = check_blanca.get()
    g_check4 = check_quimica.get()
    g_check5 = check_otro.get()
    g_serieroja = 'hemoglobina: ' + var_hemo.get() +', eritrocitos: ' + var_eritros.get() +', hematocrito: ' + var_hemato.get()+', vcm: ' +vcm.get() +', hcm: ' +var_hcm.get() +', chmg: ' + var_cmhg.get() +', plt: ' + var_plaqueta.get() 
    g_serieblanca ='Leucocitos: ' +var_leuco.get() +', neutrofilos: ' + var_neutro.get() +', linfocitos: ' +var_linfo.get() +', monocitos: ' + var_mono.get() +', eosinofilos: ' + var_eos.get() +', basofilos: ' + var_baso.get() +', neutrofilos#: ' +var_neutro2.get() +', linfocitos#: ' + var_linfo2.get() +', monocitos#: ' + var_mono2.get() +', eosinofilos#: ' + var_eos2.get() +', basofilos#: ' + var_baso2.get()
    g_quimica = 'glucosa: ' +var_gluc.get() +', urea: ' + var_urea.get() +'creatinina: ' + var_creatinina.get() +', bun: ' + var_nitro.get() +', colesterol total: ' + var_colesterol.get() +', ldl: ' + var_ldl.get() +', hdl: ' + var_hdl.get() +', vldl: ' + var_vldl.get() +', alt: ' + var_alt.get() +', ast: ' + var_ast.get() +', Bilirrubina total: ' + var_bt.get() +', Bilirrubina directa: ' + var_bd.get() +', bilirrubina indirecta: ' + var_bi.get() +', HbA1c: ' + var_hglu.get() +', Fosfatasa alcalina: ' + var_fa.get() +', ggt: ' + var_ggt.get() +', Na: ' + var_na.get() +', K: ' + var_k.get() +', Ca: ' + var_ca.get() +', Cl: ' + var_cl.get()
    g_otro = var_labotro.get()
    g_pp = var_alergias.get() + var_enfermedades.get() + var_hospitalizacion.get() + var_cirugias.get() + var_transfusiones.get() + var_traumatismos.get()
    g_np = var_etilismo.get() + var_tabaco.get() + var_toxicomania.get()
    g_gyo = "Menarca: "+ var_menarca.get() + ", Inicio de vida sexual activa: " + var_ivsa.get() + ", numero de parejas sexualmente activas: "+ var_npsa.get() + ", Gestas: "+ var_gesta.get() + ", partos: "+ var_parto.get() + ", cesarea: "+ var_cesarea.get() + ", aborto: "+ var_aborto.get() + ", citologias: "+ var_citologia.get() + ", fecha de ultima menstruacion: "+ var_menstruacion.get()
    g_ef = var_neuro.get() + var_piel.get() + var_cabeza.get() + var_cuello.get() + var_torax.get() + var_abdomen.get() + var_genitales.get() + var_extremidades.get()
    g_actual = var_actual.get()
    g_signos = "Tensión arterial: " + var_tension.get() + "Frecuencia cardiaca: " + var_fr.get() + ",Frecuencia respiratoria: " + var_fr.get() + ",Temperatura: " + var_temp.get() + ",Saturacion: " + var_sat.get()
    g_ef = var_neuro.get() + var_piel.get() + var_cabeza.get() + var_cuello.get() + var_torax.get() + var_abdomen.get() + var_genitales.get() + var_extremidades.get()
    g_nombre = var_paterno.get() + " " + var_materno.get() +" "+ var_nombre.get()
    g_signos = "Tension arterial: " + var_tension.get() + ", Frecuencia cardiaca: " + var_fr.get() + ", Frecuencia respiratoria: " + var_fr.get() + ", Temperatura: " + var_temp.get() + ", Saturacion: " + var_sat.get()
    g_ef = var_neuro.get() + var_piel.get() + var_cabeza.get() + var_cuello.get() + var_torax.get() + var_abdomen.get() + var_genitales.get() + var_extremidades.get()
    g_nota = g_nombre + '\n\n' + g_actual + '\n\n' + g_pp + '\n\n' + g_np + '\n\n' + g_signos + '\n\n' + g_ef + '\n\n'
    g_notafem = g_nombre + '\n\n' + g_actual + '\n\n' + g_pp + '\n\n' + g_np + '\n\n' + '\n\n' + g_gyo + '\n\n' + g_signos + '\n\n' + g_ef + '\n\n'
    g_analisis = var_analisis.get()
    g_diagnostico = var_diagnostico.get()
    manejo = "\n\nMedicamentos\n\n" +var_manejo.get()
    f = open(g_nombre+".txt","x")
    
    if sexo_eleccion.get() == "Femenino":
        if g_check == 1:
            if g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
                word_nota = g_notafem +'\n' + g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
            elif g_check2 == 1 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
                word_nota = g_notafem+'Laboratorios:'+g_serieroja+'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
            elif g_check2 == 0 and g_check3 == 1 and g_check4 == 0 and g_check5 == 0:
                word_nota = g_notafem +'Laboratorios:'+g_serieblanca+'\n\n'+ g_analisis + '\n\n' + +g_diagnostico + '\n\n' + manejo
            elif g_check2 == 0 and g_check3 == 0 and g_check4 == 1 and g_check5 == 0:
                word_nota = g_notafem +'Laboratorios:'+g_quimica+'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
            elif g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 1:
                word_nota = g_notafem +'Laboratorios:'+g_otro+'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
            elif g_check2 == 1 and g_check3 == 1 and g_check4 == 1 and g_check5 == 1:
                word_nota = g_notafem +'Laboratorios:'+g_serieroja+g_serieblanca+g_quimica+g_otro+'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
        else:
            if g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
                word_nota = g_notafem +'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
            elif g_check2 == 1 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
                word_nota = g_notafem +'Laboratorios:'+g_serieroja+'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
            elif g_check2 == 0 and g_check3 == 1 and g_check4 == 0 and g_check5 == 0:
                word_nota = g_notafem +'Laboratorios:'+g_serieblanca+'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
            elif g_check2 == 0 and g_check3 == 0 and g_check4 == 1 and g_check5 == 0:
                word_nota = g_notafem +'Laboratorios:'+g_quimica+'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
            elif g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 1:
                word_nota = g_notafem +'Laboratorios:'+g_otro+'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
            elif g_check2 == 1 and g_check3 == 1 and g_check4 == 1 and g_check5 == 1:
                word_nota = g_notafem +'Laboratorios:'+g_serieroja+g_serieblanca+g_quimica+g_otro+'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
    else:
        if g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
            word_nota = g_nota + g_analisis + '\n\n' +g_diagnostico + '\n\n' + manejo
        elif g_check2 == 1 and g_check3 == 0 and g_check4 == 0 and g_check5 == 0:
            word_nota = g_nota +'Laboratorios:'+g_serieroja+'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
        elif g_check2 == 0 and g_check3 == 1 and g_check4 == 0 and g_check5 == 0:
            word_nota =g_nota +'Laboratorios:'+g_serieblanca+'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
        elif g_check2 == 0 and g_check3 == 0 and g_check4 == 1 and g_check5 == 0:
            word_nota = g_nota +'Laboratorios:'+g_quimica+'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
        elif g_check2 == 0 and g_check3 == 0 and g_check4 == 0 and g_check5 == 1:
            word_nota =g_nota +'Laboratorios:'+g_otro+'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
        elif g_check2 == 1 and g_check3 == 1 and g_check4 == 1 and g_check5 == 1:
            word_nota = g_nota +'Laboratorios:'+g_serieroja+g_serieblanca+g_quimica+g_otro+'\n\n'+ g_analisis + '\n\n' + g_diagnostico + '\n\n' + manejo
    f.write(word_nota)
    f.close()
    
def n_limpiar():
    #Realiza limpieza de los campos de texto para realizar nueva nota
    g_nota.delete("1.0", "end")    
    alergia.delete("0",'end')
    alergia.insert('end',t_alergia)
    paterno.delete("0",'end')
    materno.delete("0",'end')
    nombre.delete("0",'end')
    edad.delete("0",'end')
    nacimiento.delete("0",'end')
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
    actual.delete("0",'end')
    analisis.delete("0",'end')
    manejo.delete("0",'end')
    svt.delete('0','end')
    fc.delete('0','end')
    fr.delete('0','end')
    tc.delete('0','end')
    sat.delete('0','end')
    neuro.delete("0",'end')
    neuro.insert('end',t_neurologico)    
    piel.delete("0",'end')    
    piel.insert('end',t_piel)
    cabeza.delete("0",'end')   
    cabeza.insert('end',t_craneo)
    cuello.delete("0",'end')   
    cuello.insert('end',t_cuello)
    torax.delete("0",'end') 
    torax.insert('end',t_torax)   
    abdomen.delete("0",'end')   
    abdomen.insert('end',t_abdomen)
    genitales.delete("0",'end')
    genitales.insert('end',t_genitales)
    extremidades.delete("0",'end')    
    extremidades.insert('end',t_extremidades)
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
    diagnostico.delete("0","end")
    medname.delete("0","end")
    media.delete("0","end")
    medmg.delete("0","end")
    medml.delete("0","end")
    dosis.delete("0","end")
    dia_med.delete("0","end")

def calculo_fum():
    
    pass
def receta():
    nombre = var_medname.get()
    mg = var_medmg.get()
    ml = var_medml.get()
    hora = dia_med.get()
    dias = var_media.get()
    kg = var_kg.get()
    dosis = var_dosis.get()
    checkmed=check_med.get()
    
    if var1.get()==1:
        manejo.insert("end", nombre + "tomar " + str(dosis) +" cada " + str(hora) +" horas por " +str(dias) + " dias. " )
    elif var1.get()==0:
        if checkmed == 1:
            if hora == "6":
                calculos = ((kg * dosis * ml) / mg) / 4
                calculos=float(calculos)
                manejo.insert("end", nombre + str(mg) + "mg/" + str(ml) + " ml, " + "tomar" + str(calculos) +" ml cada " + str(hora) +" horas por " +str(dias) + " dias." )
            elif hora == "8":
                calculos = ((kg * dosis * ml) / mg) / 3
                calculos=float(calculos)
                manejo.insert("end", nombre + str(mg) + "mg/" + str(ml) + " ml, " + "tomar" + str(calculos) +" ml cada " + str(hora) +" horas por " +str(dias) + " dias." )
            elif hora == "12":
                calculos = ((kg * dosis * ml) / mg) / 2
                calculos=float(calculos)
                manejo.insert("end", nombre + str(mg) + "mg/" + str(ml) + " ml, " + "tomar" + str(calculos) +" ml cada " + str(hora) +" horas por " +str(dias) + " dias." )
        else:
            
            dosis = float(dosis) * kg
            dosis = dosis * ml
            dosis = dosis / mg
            manejo.insert("end", nombre + str(mg) + "mg/" + str(ml) + " ml, " + "tomar " + str(dosis) +" ml cada " + str(hora) +" horas por " +str(dias) + " dias. " )
def medidas():
    manejo.insert("end","Medidas generales: Datos de alarma. Cita abierta a urgencias en caso de presentar datos de alarma.")      


# ++++++++++++++++++++++++++++++++++++++
#   GENERA LOS TABS DE NAVEGACION
# ++++++++++++++++++++++++++++++++++++++

#barra de menu

menu_bar = Menu(ven)
ven.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Acerca de', command=info)
forms = Menu(menu_bar, tearoff=0)
forms.add_command(label="lumbalgia")

menu_bar.add_cascade(label="Archivo", menu=file_menu)
menu_bar.add_cascade(label="Formatos", menu=forms)




#tabs
tabs = ttk.Notebook(ven)
tab1 = ttk.Frame(tabs)
tabs.add(tab1, text='Datos personales')
tabs.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabs)
tabs.add(tab2, text='Exploración física')
tabs.pack(expand=1, fill='both')

tab3 = ttk.Frame(tabs)
tabs.add(tab3, text='Gabinete')
tabs.pack(expand=1, fill='both')

tab4 = ttk.Frame(tabs)
tabs.add(tab4, text='Analisis y manejo')
tabs.pack(expand=1, fill='both')

tab5 = ttk.Frame(tabs)
tabs.add(tab5, text='Nota final')
tabs.pack(expand=1, fill='both')

#texto que se insertara en las cajas de texo para explroacion fisica
var1 = tk.IntVar()
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

t_neurologico = 'Consciente, alerta, cooperador, ubicado en sus tres esferas,'
t_piel = 'adecuada hidratación de piel y tegumentos,'
t_craneo = 'cráneo normocéfalo, pupilas isocóricas normorreflécticas, narinas permeables, mucosa oral hidratada, sin presencia de exudados, '
t_cuello = 'cuello cilíndrico sin presencia de adenomegalias,'
t_torax = 'tórax simétrico, campos pulmonares ventilados, murmullo vesicular presente sin presencia de estertores ni sibilancias, ruidos cardiacos rítmicos de buena intensidad sin ruidos agregados,'
t_abdomen = 'abdomen asignológico,'
t_genitales = 'exploracion diferida, '
t_extremidades = 'extremidades integras, arcos de movimiento conservados, llenado capilar inmediato.\n'


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
ttk.Label(frame_datospers, text="Fecha de nacimiento").grid(column=2, row=2)
var_nacimiento = tk.StringVar() #crea la variable que asignara el valor de la nota
nacimiento = ttk.Entry(frame_datospers, width="10", textvariable=var_nacimiento)
nacimiento.grid(column=3, row=2,padx=2, pady=4) # crea la caja de texto para escribir la nota

# direccion y numero telefonico
ttk.Label(frame_datospers, text="Calle").grid(column=0, row=3)
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

#########################################
#Antecedentes personales patologicos
########################################

frame_patologicosp = ttk.LabelFrame(tab1, text="Antecedentes")# crea el frame para los datos patologicos
frame_patologicosp.grid(column=0, row=1, pady=2)# asigna el espacio en el que aparecera el frame.

ttk.Label(frame_patologicosp, text="Alergias").grid(column=0, row=0)
var_alergias = tk.StringVar() #crea la variable que asignara el valor de la nota
alergia = ttk.Entry(frame_patologicosp, width="20", textvariable=var_alergias)
alergia.grid(column=1, row=0) # crea la caja de texto para escribir la nota
alergia.insert("end", t_alergia)
ttk.Label(frame_patologicosp, text="Enfermedades").grid(column=2, row=0)
var_enfermedades = tk.StringVar() #crea la variable que asignara el valor de la nota
enfermedades = ttk.Entry(frame_patologicosp, width="20", textvariable=var_enfermedades)
enfermedades.grid(column=3, row=0) # crea la caja de texto para escribir la nota
enfermedades.insert("end", t_enf)
ttk.Label(frame_patologicosp, text="Hospitalizaciones").grid(column=4, row=0)
var_hospitalizacion = tk.StringVar() #crea la variable que asignara el valor de la nota
hospitalizacion = ttk.Entry(frame_patologicosp, width="20", textvariable=var_hospitalizacion)
hospitalizacion.grid(column=5, row=0) # crea la caja de texto para escribir la nota
hospitalizacion.insert("end", t_hosp)
ttk.Label(frame_patologicosp, text="Cirugias").grid(column=0, row=1)
var_cirugias = tk.StringVar() #crea la variable que asignara el valor de la nota
cirugia = ttk.Entry(frame_patologicosp, width="20", textvariable=var_cirugias)
cirugia.grid(column=1, row=1) # crea la caja de texto para escribir la nota
cirugia.insert("end", t_cir)
ttk.Label(frame_patologicosp, text="Traumatismos").grid(column=2, row=1)
var_traumatismos = tk.StringVar() #crea la variable que asignara el valor de la nota
traumatismo = ttk.Entry(frame_patologicosp, width="20", textvariable=var_traumatismos)
traumatismo.grid(column=3, row=1) # crea la caja de texto para escribir la nota
traumatismo.insert("end", t_trauma)
ttk.Label(frame_patologicosp, text="Transfusiones").grid(column=4, row=1)
var_transfusiones = tk.StringVar() #crea la variable que asignara el valor de la nota
transfusion = ttk.Entry(frame_patologicosp, width="20", textvariable=var_transfusiones)
transfusion.grid(column=5, row=1) # crea la caja de texto para escribir la nota
transfusion.insert("end", t_trans)

#####################################
#Antecedentes personales patologicos
######################################
frame_patologicosp = ttk.LabelFrame(tab1, text="Antecedentes no patologicos")# crea el frame para los datos patologicos
frame_patologicosp.grid(column=0, row=2, pady=2)# asigna el espacio en el que aparecera el frame.

ttk.Label(frame_patologicosp, text="Etilismo").grid(column=0, row=0)
var_etilismo = tk.StringVar() #crea la variable que asignara el valor de la nota
etilico = ttk.Entry(frame_patologicosp, width="20", textvariable=var_etilismo)
etilico.grid(column=1, row=0) # crea la caja de texto para escribir la nota
etilico.insert("end", t_etilismo)
ttk.Label(frame_patologicosp, text="Tabaquismo").grid(column=2, row=0)
var_tabaco = tk.StringVar() #crea la variable que asignara el valor de la nota
tabaco = ttk.Entry(frame_patologicosp, width="20", textvariable=var_tabaco)
tabaco.grid(column=3, row=0) # crea la caja de texto para escribir la nota
tabaco.insert("end", t_tabaquismo)
ttk.Label(frame_patologicosp, text="Toxicomanias").grid(column=4, row=0)
var_toxicomania = tk.StringVar() #crea la variable que asignara el valor de la nota
toxicomania = ttk.Entry(frame_patologicosp, width="20", textvariable=var_toxicomania)
toxicomania.grid(column=5, row=0) # crea la caja de texto para escribir la nota
toxicomania.insert("end", t_drogas)
ttk.Label(frame_patologicosp, text="Otros").grid(column=0, row=1)
var_otros = tk.StringVar() #crea la variable que asignara el valor de la nota
otros = ttk.Entry(frame_patologicosp, width="20", textvariable=var_otros)
otros.grid(column=1, row=1) # crea la caja de texto para escribir la nota

#####################
#Antecedentes gyo
####################

frame_gyo = ttk.LabelFrame(tab1, text="GyO")# crea el frame para los datos patologicos
frame_gyo.grid(column=0, row=3, pady=2)# asigna el espacio en el que aparecera el frame.

ttk.Label(frame_gyo, text="Menarca").grid(column=0, row=0)
var_menarca = tk.StringVar() #crea la variable que asignara el valor de la nota
menarca = ttk.Entry(frame_gyo, width="20", textvariable=var_menarca)
menarca.grid(column=1, row=0) # crea la caja de texto para escribir la nota

ttk.Label(frame_gyo, text="IVSA").grid(column=2, row=0)
var_ivsa = tk.StringVar() #crea la variable que asignara el valor de la nota
ivsa = ttk.Entry(frame_gyo, width="20", textvariable=var_ivsa)
ivsa.grid(column=3, row=0) # crea la caja de texto para escribir la nota

ttk.Label(frame_gyo, text="NPSA").grid(column=4, row=0)
var_npsa = tk.StringVar() #crea la variable que asignara el valor de la nota
npsa = ttk.Entry(frame_gyo, width="20", textvariable=var_npsa)
npsa.grid(column=5, row=0) # crea la caja de texto para escribir la nota

ttk.Label(frame_gyo, text="Gestas").grid(column=2, row=1)
var_gesta = tk.StringVar() #crea la variable que asignara el valor de la nota
gesta = ttk.Entry(frame_gyo, width="20", textvariable=var_gesta)
gesta.grid(column=3, row=1) # crea la caja de texto para escribir la nota

ttk.Label(frame_gyo, text="Partos").grid(column=4, row=1)
var_parto = tk.StringVar() #crea la variable que asignara el valor de la nota
parto = ttk.Entry(frame_gyo, width="20", textvariable=var_parto)
parto.grid(column=5, row=1) # crea la caja de texto para escribir la nota

ttk.Label(frame_gyo, text="Cesareas").grid(column=0, row=2)
var_cesarea = tk.StringVar() #crea la variable que asignara el valor de la nota
cesarea = ttk.Entry(frame_gyo, width="20", textvariable=var_cesarea)
cesarea.grid(column=1, row=2) # crea la caja de texto para escribir la nota

ttk.Label(frame_gyo, text="Abortos").grid(column=2, row=2)
var_aborto = tk.StringVar() #crea la variable que asignara el valor de la nota
aborto = ttk.Entry(frame_gyo, width="20", textvariable=var_aborto)
aborto.grid(column=3, row=2) # crea la caja de texto para escribir la nota

ttk.Label(frame_gyo, text="Citologias").grid(column=4, row=2)
var_citologia = tk.StringVar() #crea la variable que asignara el valor de la nota
citologia = ttk.Entry(frame_gyo, width="20", textvariable=var_citologia)
citologia.grid(column=5, row=2) # crea la caja de texto para escribir la nota

# apartado para agregar los datos apra el calculo de fecha probable de parto asi como de semanas de gestacion.
ttk.Label(frame_gyo, text="Fecha de Ultima Menstruacion").grid(column=0, row=3)
ttk.Label(frame_gyo, text="Dia").grid(column=0, row=4)
dia_cb=ttk.Combobox(frame_gyo,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"] )
dia_cb.grid(column=1, row=4)
ttk.Label(frame_gyo, text="Mes").grid(column=2, row=4)
mes_cb=ttk.Combobox(frame_gyo,values=["1","2","3","4","5","6","7","8","9","10","11","12"] )
mes_cb.grid(column=3, row=4)
ttk.Label(frame_gyo, text="Ano").grid(column=4, row=4)
var_menstruacion = tk.StringVar() #crea la variable que asignara el valor de la nota
ano_cb = ttk.Entry(frame_gyo, width="20", textvariable=var_menstruacion).grid(column=5, row=4)

#######################
#Antecedentes embarazo
#######################
frame_embarazo = ttk.LabelFrame(tab1, text="Embarazo")# crea el frame para los datos patologicos
frame_embarazo.grid(column=0, row=4, pady=2)# asigna el espacio en el que aparecera el frame.

check_embarazo = tk.IntVar()
check = tk.Checkbutton(frame_embarazo, text="Positivo", variable=check_embarazo)
check.grid(column=0, row=0)

ttk.Label(frame_embarazo, text="Semanas de gestacion por FUM").grid(column=1, row=0)
var_sdg = tk.StringVar() #crea la variable que asignara el valor de la nota
sdg = ttk.Entry(frame_embarazo, width="20", textvariable=var_sdg)
sdg.grid(column=2, row=0) # crea la caja de texto para escribir la nota

ttk.Label(frame_embarazo, text="Semanas de gestacion por ultrasonido").grid(column=3, row=0)
var_usg = tk.StringVar() #crea la variable que asignara el valor de la nota
usg = ttk.Entry(frame_embarazo, width="20", textvariable=var_usg)
usg.grid(column=4, row=0) # crea la caja de texto para escribir la nota

frame_actual = ttk.LabelFrame(tab1, text="Padecimiento actual")# crea el frame para los datos patologicos
frame_actual.grid(column=0, row=5, pady=2)

ttk.Label(frame_actual, text="Padecimiento actual").grid(column=0, row=0)
var_actual = tk.StringVar() #crea la variable que asignara el valor de la nota
actual = ttk.Entry(frame_actual, width="60", textvariable=var_actual)
actual.grid(column=1, row=0) # crea la caja de texto para escribir la nota

#####################
#Frame exploracion fisica
#####################
frame_signos = ttk.LabelFrame(tab2, text="Signos vitales")
frame_signos.grid(column=0, row=0, pady=2)

#
#SIGNOS VITALES
#
ttk.Label(frame_signos, text="Peso").grid(column=0, row=0)
var_kg = tk.IntVar() #crea la variable que asignara el valor de la nota
kg = ttk.Entry(frame_signos, width="20", textvariable=var_kg)
kg.grid(column=1, row=0) # crea la caja de texto para escribir la nota

ttk.Label(frame_signos, text="Tension arterial").grid(column=2, row=0)
var_tension = tk.StringVar() #crea la variable que asignara el valor de la nota
svt = ttk.Entry(frame_signos, width="20", textvariable=var_tension)
svt.grid(column=3, row=0) # crea la caja de texto para escribir la nota

ttk.Label(frame_signos, text="Frecuencia cardiaca").grid(column=4, row=0)
var_fc = tk.StringVar() #crea la variable que asignara el valor de la nota
fc = ttk.Entry(frame_signos, width="20", textvariable=var_fc)
fc.grid(column=5, row=0) # crea la caja de texto para escribir la nota

ttk.Label(frame_signos, text="Frecuencia respiratoria").grid(column=6, row=0)
var_fr = tk.StringVar() #crea la variable que asignara el valor de la nota
fr = ttk.Entry(frame_signos, width="20", textvariable=var_fr)
fr.grid(column=7, row=0) # crea la caja de texto para escribir la nota

ttk.Label(frame_signos, text="Temperatura corporal").grid(column=0, row=2)
var_temp = tk.StringVar() #crea la variable que asignara el valor de la nota
tc = ttk.Entry(frame_signos, width="20", textvariable=var_temp)
tc.grid(column=1, row=2) # crea la caja de texto para escribir la nota

ttk.Label(frame_signos, text="Saturacion O2").grid(column=2, row=2)
var_sat = tk.StringVar() #crea la variable que asignara el valor de la nota
sat = ttk.Entry(frame_signos, width="20", textvariable=var_sat)
sat.grid(column=3, row=2) # crea la caja de texto para escribir la nota


########################################################
#APARTADO DE LA EXPLORACION
##########################################
frame_exploracion = ttk.LabelFrame(tab2, text="Exploracion Fisica")
frame_exploracion.grid(column=0, row=1, pady=2)

ttk.Label(frame_exploracion, text="Neurologico").grid(column=0,row=0)
var_neuro = tk.StringVar()
neuro = ttk.Entry(frame_exploracion, width="90", textvariable=var_neuro)
neuro.grid(column=1,row=0)
neuro.insert("end", t_neurologico)

ttk.Label(frame_exploracion, text="Piel y tegumentos").grid(column=0,row=1)
var_piel = tk.StringVar()
piel = ttk.Entry(frame_exploracion, width="90", textvariable=var_piel)
piel.grid(column=1,row=1)
piel.insert("end", t_piel)

ttk.Label(frame_exploracion, text="Cabeza").grid(column=0,row=2)
var_cabeza = tk.StringVar()
cabeza = ttk.Entry(frame_exploracion, width="90", textvariable=var_cabeza)
cabeza.grid(column=1,row=2)
cabeza.insert("end", t_craneo)
ttk.Label(frame_exploracion, text="Cuello").grid(column=0,row=3)
var_cuello = tk.StringVar()
cuello = ttk.Entry(frame_exploracion, width="90", textvariable=var_cuello)
cuello.grid(column=1,row=3)
cuello.insert("end", t_cuello)

ttk.Label(frame_exploracion, text="Torax").grid(column=0,row=4)
var_torax = tk.StringVar()
torax = ttk.Entry(frame_exploracion, width="90", textvariable=var_torax)
torax.grid(column=1,row=4)
torax.insert("end", t_torax)
ttk.Label(frame_exploracion, text="Abdomen").grid(column=0,row=5)
var_abdomen = tk.StringVar()
abdomen = ttk.Entry(frame_exploracion, width="90", textvariable=var_abdomen)
abdomen.grid(column=1,row=5)
abdomen.insert("end", t_abdomen)

ttk.Label(frame_exploracion, text="Genitales").grid(column=0,row=6)
var_genitales = tk.StringVar()
genitales = ttk.Entry(frame_exploracion, width="90", textvariable=var_genitales)
genitales.grid(column=1,row=6)
genitales.insert("end", t_genitales)

ttk.Label(frame_exploracion, text="Extremidades").grid(column=0,row=7)
var_extremidades = tk.StringVar()
extremidades = ttk.Entry(frame_exploracion, width="90", textvariable=var_extremidades)
extremidades.grid(column=1,row=7)
extremidades.insert("end", t_extremidades)


######################
#laboratorio
###################
frame_laboratorio = ttk.LabelFrame(tab3, text="Laboratorios")
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


########################
#ANALISIS Y MANEJO
############################
frame_analisis = ttk.LabelFrame(tab4, text="Analisis")
frame_analisis.grid(column=0, row=0)

ttk.Label(frame_analisis, text="Analisis").grid(column=0, row=0)

var_analisis=tk.StringVar()
analisis = ttk.Entry(frame_analisis, width="60", textvariable=var_analisis)
analisis.grid(column=1, row=0)

frame_manejo = ttk.LabelFrame(tab4, text="Manejo")
frame_manejo.grid(column=0, row=1)

ttk.Label(frame_manejo, text="Manejo").grid(column=0, row=0)

var_manejo=tk.StringVar()
manejo = ttk.Entry(frame_manejo, width="60", textvariable=var_manejo)
manejo.grid(column=1, row=0)


frame_generar = ttk.LabelFrame(tab4, text="Diagnostico")
frame_generar.grid(column=0, row=3)

ttk.Label(frame_generar,text='Diagnostico').grid(column=0, row=0)
var_diagnostico=tk.StringVar()
diagnostico = ttk.Entry(frame_generar, width="60", textvariable=var_diagnostico)
diagnostico.grid(column=1, row=0)

#se crea el frame para agregar los medicamentos a la nota y receta
frame_med = ttk.LabelFrame(tab4, text="Medicamentos")
frame_med.grid(column=1, row=0)

#Variables para agregar la el nombre del medicamento
ttk.Label(frame_med,text='Medicamento').grid(column=0, row=0)
var_medname=tk.StringVar()
medname = ttk.Entry(frame_med, width="20", textvariable=var_medname)
medname.grid(column=1, row=0)

#Variables para agregar la presentacion del medicamento
ttk.Label(frame_med,text='Mg').grid(column=0, row=1)
var_medmg=tk.IntVar()
medmg = ttk.Entry(frame_med, width="5", textvariable=var_medmg)
medmg.grid(column=1, row=1)
ttk.Label(frame_med,text='/').grid(column=2, row=1)
ttk.Label(frame_med,text='Ml').grid(column=3, row=1)
var_medml=tk.IntVar()
medml = ttk.Entry(frame_med, width="5", textvariable=var_medml)
medml.grid(column=4, row=1)

#Variables para agregar la dosis a calcular del medicamento.
ttk.Label(frame_med,text='Dosis').grid(column=0, row=2)
var_dosis=tk.IntVar()
dosis = ttk.Entry(frame_med, width="10", textvariable=var_dosis)
dosis.grid(column=1,row=2)

#Variables para agregar los horarios del medicamento.
ttk.Label(frame_med,text='Hrs').grid(column=0, row=3)
dia_med=ttk.Combobox(frame_med, width="5", values=[6,8,12,24] )
dia_med.grid(column=1, row=3)

ttk.Label(frame_med,text='Dias').grid(column=0, row=4)
var_media=tk.IntVar()
media = ttk.Entry(frame_med, width="10", textvariable=var_media)
media.grid(column=1, row=4)

check_med = tk.IntVar()
checkmed = tk.Checkbutton(frame_med, text="dosis?", variable=check_med)
checkmed.grid(column=2, row=4)


manejo.insert("end", "Medicamentos: ")


#############################################
# BOTONES PARA GENERAR LAS NOTAS Y LIMPIEZA
###########################################
frame_nota = ttk.LabelFrame(tab5, text="Nota")
frame_nota.grid(column=0, row=0, pady=2)

g_nota = ScrolledText(frame_nota, font=("Arial", 12),width="60", height="30")
g_nota.grid(column=0, row=0)

frame_opciones = ttk.LabelFrame(tab5, text="Opciones")#Genera el frame para los botones de opciones para generar notas o almacenar en base de datos y formato de texto
frame_opciones.grid(column=1, row=0, pady=2)

generar_inicial = ttk.Button(frame_opciones, text="Generar historia clinica", command=gen_historia)
generar_inicial.grid(column=0, row=0)

generar = ttk.Button(frame_opciones, text="Generar nota de consulta", command=evo)
generar.grid(column=1, row=0)

guardar = ttk.Button(frame_opciones, text="Almacenar nota", command=nota_texto)
guardar.grid(column=0, row=1)


limpiar_nota = ttk.Button(frame_opciones, text="Limpiar nota", command=n_limpiar)
limpiar_nota.grid(column=1, row=1)

add_med = ttk.Button(frame_med, text="Agregar medicamento", command=receta)
add_med.grid(column=0, row=5)
add_med = ttk.Button(frame_med, text="Agregar medidas generales", command=medidas)
add_med.grid(column=1, row=5)


#========================
#   INICIA LA VENTANA
#========================
ven.mainloop()
