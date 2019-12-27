# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import base64

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

if module == "toBase64":
    img_ = GetParams('img_')
    var_ = GetParams('var_')

    with open(img_, "rb") as img_file:
        res_ = base64.b64encode(img_file.read())
        res_ = res_.decode()
    print(res_)

    SetVar(var_,res_)

